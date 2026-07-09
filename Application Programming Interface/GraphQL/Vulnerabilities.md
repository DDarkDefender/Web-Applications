
## Finding GraphQL endpoints

#### Universal queries
If you send `query{__typename}` to any GraphQL endpoint, it will include the string `{"data": {"__typename": "query"}}` somewhere in its response.
Ex. /api?query=query%7b__typename%7d

The query works because every GraphQL endpoint has a reserved field called `__typename` that returns the queried object's type as a string.

#### Common endpoints
- `/graphql`
- `/api`
- `/api/graphql`
- `/graphql/api`
- `/graphql/graphql
 `
If these common endpoints don't return a GraphQL response, you could also try appending `/v1` to the path.

#### Request methods
It is best practice for production GraphQL endpoints to only accept POST requests that have a content-type of `application/json`, as this helps to protect against CSRF vulnerabilities.

 However, some endpoints may accept alternative methods, such as GET requests or POST requests that use a content-type of `x-www-form-urlencoded`.
 Try resending the universal query using alternative HTTP methods.

## Exploring unsanitised arguments

If the API uses arguments to access objects directly, it may be vulnerable to access control vulnerabilities. 
A user could potentially access information simply by supplying an argument that corresponds to that information. This is sometimes known as an insecure direct object reference (IDOR).

## Discovering schema information

The best way to do this is to use introspection queries. Introspection is a built-in GraphQL function that enables you to query a server for information about the schema.

1. Probe for introspection
```
#Introspection probe request 

{ "query": "{__schema{queryType{name}}}" }
```
2. Running a full introspection query
```
#Full introspection query 

query IntrospectionQuery { __schema { queryType { name } mutationType { name } subscriptionType { name } types { ...FullType } directives { name description args { ...InputValue } 
onOperation #Often needs to be deleted to run query 
onFragment #Often needs to be deleted to run query 
onField #Often needs to be deleted to run query 
} } } fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } } fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue } fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name } } } }
```

## Bypassing Introspection Detection

Try inserting a special character after the `__schema` keyword. Developers may have used regex to exclude the `__schema` keywords in query. 
You should try characters like spaces, new lines and commas, as they are ignored by GraphQL but not by flawed regex.

- As such, if the developer has only excluded `__schema{`, then the below introspection query would not be excluded.
```
#Introspection query with newline 

{ "query": "query{__schema 
	{queryType{name}}}" 
}
```
- Try running the probe over an alternative request method, as introspection may only be disabled over POST. Try a GET request, or a POST request with a content-type of `x-www-form-urlencoded`.
```
# Introspection probe as GET request 

GET /graphql?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D
```

## GraphQL CSRF

Cross-site request forgery (CSRF) vulnerabilities enable an attacker to induce users to perform actions that they do not intend to perform. This is done by creating a malicious website that forges a cross-domain request to the vulnerable application.

CSRF vulnerabilities can arise where a GraphQL endpoint does not validate the content type of the requests sent to it and no CSRF tokens are implemented.

POST requests that use a content type of `application/json` are secure against forgery as long as the content type is validated. In this case, an attacker wouldn't be able to make the victim's browser send this request even if the victim were to visit a malicious site.

However, alternative methods such as GET, or any request that has a content type of `x-www-form-urlencoded`, can be sent by a browser and so may leave users vulnerable to attack if the endpoint accepts these requests. Where this is the case, attackers may be able to craft exploits to send malicious requests to the API.
