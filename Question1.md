1. Curling wetransfer.com

I open a terminal and type in `curl wetransfer.com`. Please describe in as much detail as you wish what happens between the time you press `Enter` and the time you see curl’s response.

Here we’re looking for an understanding of what happens on the shell and in the kernel, what internet protocols are involved and how they work. We prefer that you show evidence of your understanding with tools rather than internet research.

---

```
➜ curl wetransfer.com -v
*   Trying 52.213.142.26:80...
* Connected to wetransfer.com (52.213.142.26) port 80 (#0)
> GET / HTTP/1.1
> Host: wetransfer.com
> User-Agent: curl/7.79.1
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 301 Moved Permanently
< Date: Mon, 18 Jul 2022 11:56:35 GMT
< Content-Length: 0
< Connection: keep-alive
< location: https://wetransfer.com/
<
* Connection #0 to host wetransfer.com left intact
```

1. I type `curl wetransfer.com -v` into my terminal and press Enter. The `-v` was added for extra verbosity as the initial curl without this returned nothing and did not allow me to see the status code.
1. The DNS is checked to find an IP address associated with `wetransfer.com`, the IP was determined to be `52.213.142.26`.
1. As no port was specified, the default HTTP port (port 80) was used.
1. `curl` then ran a HTTP GET request against the IP.
1. The request was accepted and a response code of 301 was returned indicating that the resource was "Moved Permanently" and can be found at `https://wetransfer.com/`.
1. In order to follow the request to the endpoint the `-L` option can be added. `curl wetransfer.com -vL` hits the same destination but allows `curl` to follow the new location towards `52.213.142.26:443`. This endpoint returns a 200 "OK" and gives the html etc. for the `wetransfer.com` homepage as can be seen in a web browser.
1. This indicates that HTTP has been disabled for `wetransfer.com` and incoming HTTP requests should be directed to port 443 as HTTPS requests.
