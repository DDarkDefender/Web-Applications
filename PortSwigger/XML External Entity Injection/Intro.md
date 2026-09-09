## XML external entity injection (XEE Injection)
XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data.
It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access.

> [!INFO]
> In some situations, an attacker can escalate an XXE attack to compromise the underlying server or other back-end infrastructure to perform server-side request forgery (SSRF) attacks.

### How do XXE vulnerabilities arise?
Some applications use the XML format to transmit data between the browser and the server. Applications that do this virtually always use a standard library or platform API to process the XML data on the server. 
XXE vulnerabilities arise because the XML specification contains various potentially dangerous features, and standard parsers support these features even if they are not normally used by the application.

Refer to [XML Entities]() for basic understanding of XML.
