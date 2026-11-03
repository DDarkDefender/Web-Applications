# Table of contents

1. Introduction to SQLi
    - [Detecting SQLi](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Intro.md#how-to-detect-sql-injection-vulnerabilities)
    - [Reason for SQLi vulnerability](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Intro.md#how-does-sql-injection-arrise)
    - [Common commands to check for discovery](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Intro.md#common-sql-commands-to-check)
    - [Common functions affected by SQLi](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Intro.md#common-functions-to-check)

2. Examining Database
    - [Identifying database in use](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Examining%20Database.md#examining-the-database-in-sql-injection-attacks)
    - [Listing the contents of the database](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Database%20Contents.md#listing-the-contents-of-the-database)

3. SQLi union attacks
    - [Determining number of columns](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/UNION%20Attacks.md#determining-the-number-of-columns-required)
    - [Finding column with useful datatype](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/UNION%20Attacks.md#finding-columns-with-a-useful-data-type)
    - [SQLi union attack](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/UNION%20Attacks.md#using-a-sql-injection-union-attack-to-retrieve-interesting-data)
    - [Retrieving multiple data in a single column](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/UNION%20Attacks.md#retrieving-multiple-values-within-a-single-column) 

4. Blind SQLi
    - [Understanding exploitation](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Blind%20SQLi.md#exploiting-blind-sql-injection-by-triggering-conditional-responses)
    - [Exploitation queries](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Blind%20SQLi.md#queries-that-can-be-used-for-exploitation--)

5. Error-based SQLi
    - [Error-Based SQLi Queries](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Error-based%20SQLi.md#queries-that-can-be-used-for-exploitation--)
    - [Extracting sensitive data via verbose SQL error messages](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Error-based%20SQLi.md#extracting-sensitive-data-via-verbose-sql-error-messages)

6. SQLi with time-delays
    - [Exploiting blind SQL injection by triggering time delays](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/SQLi%20with%20time%20delays.md#exploiting-blind-sql-injection-by-triggering-time-delays)

7. Out-of-Band (OAST) SQLi
    - [Exploiting SQLi using OAST techniques](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Out-of-Band%20(OAST)%20SQLi.md#exploiting-blind-sql-injection-using-out-of-band-oast-techniques)
    - [Exflitrating data using OAST technique](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Out-of-Band%20(OAST)%20SQLi.md#exfiltrating-data-using-oast-technique)

8. [SQLi in different context](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/SQLi%20in%20different%20contexts.md#sql-injection-in-different-contexts)

9. [Second-Order SQLi](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Intro.md#second-order-sql-injection)

10. [SQLi Prevention](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/Intro.md#sqli-prevention)

> [!NOTE]
> Determine the database to use the correct query syntax. Refer to the [cheatsheet](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/Injection%20(SQL%20and%20NoSQL)/SQL/CheatSheet.md) to find the correct syntax as per identified database.

> [!TIP]
> Use quotes '' when retrieving any string data.
