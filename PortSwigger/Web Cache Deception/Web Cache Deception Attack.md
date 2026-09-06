Generally speaking, constructing a basic web cache deception attack involves the following steps:

1. Identify a target endpoint that returns a dynamic response containing sensitive information. Review responses in Burp, as some sensitive information may not be visible on the rendered page. Focus on endpoints that support the GET, HEAD, or OPTIONS methods as requests that alter the origin server's state are generally not cached.
2. Identify a discrepancy in how the cache and origin server parse the URL path. This could be a discrepancy in how they:

- Map URLs to resources.
- Process delimiter characters.
- Normalize paths.
3. Craft a malicious URL that uses the discrepancy to trick the cache into storing a dynamic response. When the victim accesses the URL, their response is stored in the cache. Using Burp, you can then send a request to the same URL to fetch the cached response containing the victim's data. Avoid doing this directly in the browser as some applications redirect users without a session or invalidate local data, which could hide a vulnerability.
