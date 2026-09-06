Generally speaking, constructing a basic web cache deception attack involves the following steps:

1. Identify a target endpoint that returns a dynamic response containing sensitive information. Review responses in Burp, as some sensitive information may not be visible on the rendered page. Focus on endpoints that support the GET, HEAD, or OPTIONS methods as requests that alter the origin server's state are generally not cached.

2. Identify a discrepancy in how the cache and origin server parse the URL path. This could be a discrepancy in how they:

- Map URLs to resources.
- Process delimiter characters.
- Normalize paths.

3. Craft a malicious URL that uses the discrepancy to trick the cache into storing a dynamic response. When the victim accesses the URL, their response is stored in the cache. Using Burp, you can then send a request to the same URL to fetch the cached response containing the victim's data. Avoid doing this directly in the browser as some applications redirect users without a session or invalidate local data, which could hide a vulnerability.

## Using Cache Buster
While testing for discrepancies and crafting a web cache deception exploit, make sure that each request you send has a different cache key.
As both URL path and any query parameters are typically included in the cache key, you can change the key by adding a query string to the path and changing it each time you send a request.
Automate this process using the **Param Miner extension**. 
- To do this, once you've installed the extension, click on the top-level Param miner > Settings menu, then select Add dynamic cachebuster.
- Burp now adds a unique query string to every request that you make.
- You can view the added query strings in the Logger tab.

## Detecting Cached Response
It's crucial that you're able to identify cached responses. To do so, look at response headers and response times.
Various response headers may indicate that it is cached. For example:

The **X-Cache header** provides information about whether a response was served from the cache. Typical values include:
1. X-Cache: hit - The response was served from the cache.
2. X-Cache: miss - The cache did not contain a response for the request's key, so it was fetched from the origin server. In most cases, the response is then cached. To confirm this, send the request again to see whether the value updates to hit.
3. X-Cache: dynamic - The origin server dynamically generated the content. Generally this means the response is not suitable for caching.
4. X-Cache: refresh - The cached content was outdated and needed to be refreshed or revalidated.

The **Cache-Control header** may include a directive that indicates caching, like public with a max-age higher than 0. Note that this only suggests that the resource is cacheable. It isn't always indicative of caching, as the cache may sometimes override this header.

If you notice a big difference in response time for the same request, this may also indicate that the faster response is served from the cache.

## Exploiting Web Cache
### Static Extension Cache Rules
Cache rules often target static resources by matching common file extensions like .css or .js. This is the default behavior in most CDNs.

If there are discrepancies in how the cache and origin server map the URL path to resources or use delimiters, an attacker may be able to craft a request for a dynamic resource with a static extension that is ignored by the origin server but viewed by the cache.

### Path mapping discrepancies
URL path mapping is the process of associating URL paths with resources on a server, such as files, scripts, or command executions. There are a range of different mapping styles used by different frameworks and technologies. 
Two common styles are traditional URL mapping and RESTful URL mapping.

**Traditional URL mapping** represents a direct path to a resource located on the file system. Here's a typical example:

`http://example.com/path/in/filesystem/resource.html`

- `http://example.com` points to the server.
- `/path/in/filesystem/` represents the directory path in the server's file system.
- `resource.html` is the specific file being accessed.

**REST-style** URLs don't directly match the physical file structure. They abstract file paths into logical parts of the API:

`http://example.com/path/resource/param1/param2`

- `http://example.com` points to the server.
- `/path/resource/` is an endpoint representing a resource.
- `param1` and `param2` are path parameters used by the server to process the request.

### Example of Path mapping discrepancies
Discrepancies in how the cache and origin server map the URL path to resources can result in web cache deception vulnerabilities. Consider the following example:

`http://example.com/user/123/profile/wcd.css`

- An origin server using REST-style URL mapping may interpret this as a request for the `/user/123/profile` endpoint and returns the profile information for user `123`, ignoring `wcd.css` as a non-significant parameter.
- A cache that uses traditional URL mapping may view this as a request for a file named `wcd.css` located in the `/profile` directory under `/user/123`. It interprets the URL path as `/user/123/profile/wcd.css`. If the cache is configured to store responses for requests where the path ends in `.css`, it would cache and serve the profile information as if it were a CSS file.

## How to identify Path mapping discrepancies?
To test how the origin server maps the URL path to resources, add an arbitrary path segment to the URL of your target endpoint.
If the response still contains the same sensitive data as the base response, it indicates that the origin server abstracts the URL path and ignores the added segment. For example, this is the case if modifying `/api/orders/123` to `/api/orders/123/foo` still returns order information.

To test how the cache maps the URL path to resources, you'll need to modify the path to attempt to match a cache rule by adding a static extension. For example, update `/api/orders/123/foo` to `/api/orders/123/foo.js`. If the response is cached, this indicates:
- That the cache interprets the full URL path with the static extension.
- That there is a cache rule to store responses for requests ending in .js.

Caches may have rules based on specific static extensions. Try a range of extensions, including .css, .ico, and .exe.

> [!IMPORTANT]
> You can then craft a URL that returns a dynamic response that is stored in the cache. Note that this attack is limited to the specific endpoint that you tested, as the origin server often has different abstraction rules for different endpoints.

> [!NOTE]
> Burp Scanner automatically detects web cache deception vulnerabilities that are caused by path mapping discrepancies during audits. You can also use the **Web Cache Deception Scanner** BApp to detect misconfigured web caches.
