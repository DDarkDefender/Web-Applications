## Web Cache
A web cache is a system that sits between the origin server and the user. 
When a client requests a static resource, the request is first directed to the cache. If the cache doesn't contain a copy of the resource (known as a cache miss), the request is forwarded to the origin server, which processes and responds to the request.
The response is then sent to the cache before being sent to the user. The cache uses a preconfigured set of rules to determine whether to store the response.

<img width="1123" height="288" alt="image" src="https://github.com/user-attachments/assets/5fc4af2c-4df2-46f1-918c-30531a6b0f85" />

> [!NOTE]
> Content Delivery Networks (CDNs) use caching, to store copies of content on distributed servers all over the world. CDNs speed up delivery by serving content from the server closest to the user, reducing load times by minimizing the distance data travels.

### Cache Keys
When the cache receives an HTTP request, it must decide whether there is a cached response that it can serve directly, or whether it has to forward the request to the origin server. The cache makes this decision by generating a 'cache key' from elements of the HTTP request. Typically, this includes the URL path and query parameters, but it can also include a variety of other elements like headers and content type.

If the incoming request's cache key matches that of a previous request, the cache considers them to be equivalent and serves a copy of the cached response.

### Cache Rules
Cache rules determine what can be cached and for how long. Cache rules are often set up to store static resources, which generally don't change frequently and are reused across multiple pages. Dynamic content is not cached as it's more likely to contain sensitive information, ensuring users get the latest data directly from the server.

Web cache deception attacks exploit how cache rules are applied, so it's important to know about some different types of rules, particularly those based on defined strings in the URL path of the request.
- Static file extension rules - These rules match the file extension of the requested resource, for example .css for stylesheets or .js for JavaScript files.
- Static directory rules - These rules match all URL paths that start with a specific prefix. These are often used to target specific directories that contain only static resources, for example /static or /assets.
- File name rules - These rules match specific file names to target files that are universally required for web operations and change rarely, such as robots.txt and favicon.ico.

Caches may also implement custom rules based on other criteria, such as URL parameters or dynamic analysis.
