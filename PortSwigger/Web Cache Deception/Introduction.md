## Web Cache
A web cache is a system that sits between the origin server and the user. 
When a client requests a static resource, the request is first directed to the cache. If the cache doesn't contain a copy of the resource (known as a cache miss), the request is forwarded to the origin server, which processes and responds to the request.
The response is then sent to the cache before being sent to the user. The cache uses a preconfigured set of rules to determine whether to store the response.

<img width="1123" height="288" alt="image" src="https://github.com/user-attachments/assets/5fc4af2c-4df2-46f1-918c-30531a6b0f85" />

> [!INFO]
> Content Delivery Networks (CDNs) use caching, to store copies of content on distributed servers all over the world. CDNs speed up delivery by serving content from the server closest to the user, reducing load times by minimizing the distance data travels.
