## API Building Styles

### Representational State Transfer (REST)
It uses a **`client-server`** model where clients make requests to resources on a server using standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`). 
`RESTful` APIs are **`stateless`**, meaning each request contains all necessary information for the server to process it, and responses are typically serialized as JSON or XML.

### Simple Object Access Protocol (SOAP)
SOAP APIs use **`XML`** for message exchange between systems.
They are highly standardized and offer comprehensive features for security, transactions, and error handling, but they are generally more complex to implement and use than `RESTful` APIs.

### GraphQL
An alternative style that provides a more **`flexible and efficient way to fetch and update data`**.
GraphQL allows clients to specify exactly what data they need, reducing over-fetching and under-fetching of data. They use a single endpoint and a **`strongly-typed query language`** to retrieve data.

### gRPC
A newer style that uses [Protocol Buffers](https://protobuf.dev/) for **`message serialization`**, providing a high-performance, efficient way to communicate between systems.
They are particularly useful for microservices and distributed systems.
