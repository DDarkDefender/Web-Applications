Enables users to specify exactly what data they want in response, helping to avoid the large response objects and multiple calls that can be sometimes seen in REST APIs.

GraphQL is platform agnostic and can be implemented with a wide range of programming languages.

### Working
GraphQL schemas define the structure of the service's data, listing the available objects (known as types), fields, and relationships.

The data described by a GraphQL schema can be manipulated using three types of operation:

- **Queries** - Fetch data.
- **Mutations** - Add, Change, or Remove data.
- **Subscriptions** - Similar to Queries, but set up a permanent connection by which a server can proactively push data to a client in the specified format.

All GraphQL operations use the same endpoint, and are generally sent as a POST request.

### Schema

Most of the types defined are object types, which define the objects available and the fields and arguments they have. Each field has its own type, which can either be another object or a scalar, enum, union, interface, or custom type.

The example below shows a simple schema definition for a Product type. The `!` operator indicates that the field is non-nullable when called (that is, mandatory).

```
#Example schema definition 

type Product { 
id: ID! 
name: 
String! description: String! 
price: Int 
}
```

### Queries
- A `query` operation type. This is technically optional but encouraged, as it explicitly tells the server that the incoming request is a query.
- A query name. This can be anything you want. The query name is optional, but encouraged as it can help with debugging.
- A data structure. This is the data that the query should return.
- Optionally, one or more arguments. These are used to create queries that return details of a specific object (for example "give me the name and description of the product that has the ID 123").

### Components
- **Fields** - All GraphQL types contain items of queryable data called fields. When you send a query or mutation, you specify which of the fields you want the API to return. The response mirrors the content specified in the request.

- **Arguments** - Arguments are values that are provided for specific fields. The arguments that can be accepted for a type are defined in the schema. 
```
#Example query with arguments 

query myGetEmployeeQuery { 
	getEmployees(id:1) { 
		name { 
			firstname 
			lastname 
		} 
	}
}
```

- **Variables** - Variables enable you to pass dynamic arguments, rather than having arguments directly within the query itself. Variable-based queries use the same structure as queries using inline arguments, but certain aspects of the query are taken from a separate JSON-based variables dictionary.
```
#Example query with variable 

query getEmployeeWithVariable($id: ID!) { 
	getEmployees(id:$id) { 
		name { 
			firstname 
			lastname 
		}
	} 
} 

Variables: { 
	"id": 1 
}
```

- **Aliases** - GraphQL objects can't contain multiple properties with the same name. Aliases enable you to bypass this restriction by explicitly naming the properties you want the API to return. You can use aliases to return multiple instances of the same type of object in one request. This helps to reduce the number of API calls needed.

```
#Valid query using aliases 

query getProductDetails { 
	product1: getProduct(id: "1") { 
		id 
		name 
	} 
	product2: getProduct(id: "2") { 
		id 
		name 
	} 
}
```

- **Fragments** - Fragments are reusable parts of queries or mutations. They contain a subset of the fields belonging to the associated type. Once defined, they can be included in queries or mutations. If they are subsequently changed, the change is included in every query or mutation that calls the fragment.
```
`#Example fragment fragment 

productInfo on Product { 
	id 
	name 
	listed 
} 

query { 
	getProduct(id: 1) { 
	...productInfo 
	stock 
	} 
}
```

## Introspection

Introspection is a built-in GraphQL function that enables you to query a server for information about the schema. It is commonly used by applications such as GraphQL IDEs and documentation generation tools. 
Introspection can represent a serious information disclosure risk, as it can be used to access potentially sensitive information (such as field descriptions) and help an attacker to learn how they can interact with the API. It is best practice for introspection to be disabled in production environments.
