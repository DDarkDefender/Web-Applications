# XML external entity injection (XEE Injection)
XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data.
It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access.

> [!INFO]
> In some situations, an attacker can escalate an XXE attack to compromise the underlying server or other back-end infrastructure to perform server-side request forgery (SSRF) attacks.

## How do XXE vulnerabilities arise?
Some applications use the XML format to transmit data between the browser and the server. Applications that do this virtually always use a standard library or platform API to process the XML data on the server. 
XXE vulnerabilities arise because the XML specification contains various potentially dangerous features, and standard parsers support these features even if they are not normally used by the application.

Refer to [XML Entities](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XML%20Entities.md) for basic understanding of XML.

## Types of XXE attacks
1. [Exploiting XXE to retrieve files](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XXE%20Attacks.md#exploiting-xxe-to-retrieve-files), where an external entity is defined containing the contents of a file, and returned in the application's response.
2. [Exploiting XXE to perform SSRF attacks](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XXE%20Attacks.md#exploiting-xxe-to-perform-ssrf-attacks), where an external entity is defined based on a URL to a back-end system.
3. [Exploiting blind XXE exfiltrate data out-of-band](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XXE%20Attacks.md#exploiting-blind-xxe-exfiltrate-data-out-of-band), where sensitive data is transmitted from the application server to a system that the attacker controls.
4. [Exploiting blind XXE to retrieve data via error messages](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XXE%20Attacks.md#exploiting-blind-xxe-to-retrieve-data-via-error-messages), where the attacker can trigger a parsing error message containing sensitive data.
5. [Exploiting blind XXE by repurposing a local DTD](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XXE%20Attacks.md#exploiting-blind-xxe-by-repurposing-a-local-dtd), where an internal DTD that is fully specified within the DOCTYPE element.
6. [Finding hidden attack surface for XXE injection](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XXE%20Attacks.md#finding-hidden-attack-surface-for-xxe-injection)

## How to find and test for XXE vulnerabilities
The vast majority of XXE vulnerabilities can be found quickly and reliably using Burp Suite's web vulnerability scanner.

Manually testing for XXE vulnerabilities generally involves:

- Testing for file retrieval by defining an external entity based on a well-known operating system file and using that entity in data that is returned in the application's response.
- Testing for blind XXE vulnerabilities by defining an external entity based on a URL to a system that you control, and monitoring for interactions with that system. Burp Collaborator is perfect for this purpose.
- Testing for vulnerable inclusion of user-supplied non-XML data within a server-side XML document by using an XInclude attack to try to retrieve a well-known operating system file.

> [!NOTE] Keep in mind that XML is just a data transfer format. Make sure you also test any XML-based functionality for other vulnerabilities like XSS and SQL injection. You may need to encode your payload using XML escape sequences to avoid breaking the syntax, but you may also be able to use this to obfuscate your attack in order to bypass weak defences.

## How to prevent XXE vulnerabilities
Virtually all XXE vulnerabilities arise because the application's XML parsing library supports potentially dangerous XML features that the application does not need or intend to use. The easiest and most effective way to prevent XXE attacks is to disable those features.

Generally, it is sufficient to disable resolution of external entities and disable support for XInclude. This can usually be done via configuration options or by programmatically overriding default behavior. Consult the documentation for your XML parsing library or API for details about how to disable unnecessary capabilities.
