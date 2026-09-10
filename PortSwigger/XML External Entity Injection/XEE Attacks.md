# Types of XXE attacks
1. [Exploiting XXE to retrieve files](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XEE%20Attacks.md#exploiting-xxe-to-retrieve-files), where an external entity is defined containing the contents of a file, and returned in the application's response.
2. [Exploiting XXE to perform SSRF attacks](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XEE%20Attacks.md#exploiting-xxe-to-perform-ssrf-attacks), where an external entity is defined based on a URL to a back-end system.
3. [Exploiting blind XXE exfiltrate data out-of-band](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XEE%20Attacks.md#exploiting-blind-xxe-exfiltrate-data-out-of-band), where sensitive data is transmitted from the application server to a system that the attacker controls.
4. [Exploiting blind XXE to retrieve data via error messages](https://github.com/DDarkDefender/Web-Applications/blob/main/PortSwigger/XML%20External%20Entity%20Injection/XEE%20Attacks.md#exploiting-blind-xxe-to-retrieve-data-via-error-messages), where the attacker can trigger a parsing error message containing sensitive data.

## Exploiting XXE to retrieve files
To perform an XXE injection attack that retrieves an arbitrary file from the server's filesystem, you need to modify the submitted XML in two ways:
  - Introduce (or edit) a DOCTYPE element that defines an external entity containing the path to the file.
  - Edit a data value in the XML that is returned in the application's response, to make use of the defined external entity.

<u>**Example:**</u>
Suppose a shopping application checks for the stock level of a product by submitting the following XML to the server:
```
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>381</productId></stockCheck>
```
The application performs no particular defenses against XXE attacks, so you can exploit the XXE vulnerability to retrieve the /etc/passwd file by submitting the following XXE payload:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```
This XXE payload defines an external entity &xxe; whose value is the contents of the `/etc/passwd` file and uses the entity within the `productId` value. This causes the application's response to include the contents of the file:
```
Invalid product ID: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...
```

> [!NOTE]
> With real-world XXE vulnerabilities, there will often be a large number of data values within the submitted XML, any one of which might be used within the application's response. To test systematically for XXE vulnerabilities, you will generally need to test each data node in the XML individually, by making use of your defined entity and seeing whether it appears within the response.

## Exploiting XXE to perform SSRF attacks
Aside from retrieval of sensitive data, the other main impact of XXE attacks is that they can be used to perform server-side request forgery (SSRF). This is a potentially serious vulnerability in which the server-side application can be induced to make HTTP requests to any URL that the server can access.

To exploit an XXE vulnerability to perform an SSRF attack, you need to define an external XML entity using the URL that you want to target, and use the defined entity within a data value. If you can use the defined entity within a data value that is returned in the application's response, then you will be able to view the response from the URL within the application's response, and so gain two-way interaction with the back-end system. If not, then you will only be able to perform blind SSRF attacks (which can still have critical consequences).

In the following XXE example, the external entity will cause the server to make a back-end HTTP request to an internal system within the organization's infrastructure:
```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://internal.vulnerable-website.com/"> ]>
```

## Exploiting blind XXE exfiltrate data out-of-band

## Exploiting blind XXE to retrieve data via error messages
