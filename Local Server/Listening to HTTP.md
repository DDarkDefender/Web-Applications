## Why you might need a local server?
When you're testing in an environment with no Internet access, the Burp Suite collaborator will not work you can use an internal OOB interaction server instead.

### Key Requirement
The target system must be able to reach a server you control, and that server must record the interaction.

 If the system you're testing can reach your machine over the local network, a small Python HTTP server can act as a basic substitute for Collaborator for HTTP-based OOB detection.
 
 1. Initiate a server using command:
    `python3 -m http.server 8000 --bind 0.0.0.0`
 2. Then determine your machine's LAN address, using either of the following command based on your OS:
    `ipconfig` or `ifconfig`
 3. The test system needs to make a request to:
    `http://<IP>:8000/`

**--bind** tells the Python server which network interface/address to listen on.
**--bind 0.0.0.0** says Listen on port 8000 on all network interfaces available on this machine.

> [!NOTE]
> 0.0.0.0 is not an address you normally connect to. It's a special "all IPv4 interfaces" listen address

A basic Python HTTP server is **not equivalent to Collaborator**.
For testing something like blind SSRF, HTTP is often enough. But if you need to detect DNS callbacks, you'd want a [DNS listener](https://github.com/DDarkDefender/Web-Applications/blob/main/Local%20Server/HTTP%20and%20DNS/Info.md) as well.
