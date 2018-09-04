# Hidden Message

The challenge presents us with `nc 202.120.7.211 8719`, the name in the title is the hint. 

When we netcat into the server, it gives us long segments of text describing the TCP/IP protocol. When searching this, it turns out that it's almost completetely identicial to the [Wikipedia page of TCP/IP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)

I saved both the output of the netcat and Wikipedia to text file and compared the two using diff. The flag was the difference in characters.


Despite how simple this challenge was in the end, it was my first individual flag playing CTF :)


