# roku remote
This allows you to control a roku on your local network through any web browser using a data URI to display a webpage without requiring a server

## how to use

to use, simply copy and paste the contents of `app.txt` into your phones url bar (on IOS you must use safari). then, scroll to the bottom and enter you roku's local IP adress (under `settings > network > about` on your roku), and youre ready to go! if you want, you can even change the default IP adress by changing the last few characters in the URL allowing the page to keep the same IP address upon refresh (it should look somthing like `."IP"%20value="192.168.1.152"/></body></html>`).

If you don't have access to the Roku remote to find the IP, the following command will scan your network in an attempt to find it:
`nmap -p 8060 -v -T4 --open 192.168.0-1.0-255`
this will check for any device in the range 192.168.0.0--192.168.1.255 (may need to adjust based on your network) with the port 8060 open (the port Roku uses for it's remote control API).

## Why does this exist?
That's a fantastic question. Some projects exist to accomplish some functional purpose, or to make daily interactions with technology more convenient. This is neither. All Rokus ship with a remote, and even if you insist on using your phone or computer instead, there are far better apps than this.\
No, this project exists for another purpose: Simply to see if I could. I discovered Roku's API and wanted to see if I could get something to work on my iphone.\
The iphone, at least as far as I knew at the time, didn't allow for a way to execute commands like those required to make the POST requests. I could write an html document that would run JavaScript to do what I wanted, but I didn't believe there would be a way to open it on an iphone without hosting it somewhere. Finally, when I stumbled across the idea of a data URI, I realized I could abuse them to open my html file straight inside my web browser.\
I almost gave up hope, because like any good script kiddie, I had about 5 browsers on my phone at the time, and all the ones I used didn't handle top level data URIs, but fourtunatly the built in safari browser worked.

## how does it work?
A data URI is a way of encoding something that would normally be loaded via url directly into an html page.\
For example, normally to embed a picture, you would do something like `<img src="http://example.com/images/profilepicture001.jpg">`. with data urls, youd do something like

```
<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAZABkDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDkE019UuzAJVjCKGJYcdfSrqaNPp1lIzyJMAwXK8bferlhGVQ74UO/kE9WH+f50txLstZkMYV5nB4P8I7kf56Vo7uszdKKoXOZ1a3e4WJUGcEk1mf2VP8A3f1rq4EQsxPb1qzmL+6Kxr1nGbSHSppwTK3jKe7tr22u7YPHDsaEK0eB1zjB/wA8VD4OPmPeXWoP5gkaOMK3cAnOPpkVt/ET/kD23/XwP/QWrL8Pf8i8f98/zrWK1M5X2NvVNIWyzPbbmjJwyk/d9PwrJ+b+6Pzrrr7/AI8Lj/rmP5VyVZVYKcrs1g+VWR//2Q==">
```

a much longer url, but that holds the *entire* image. no internet connection needed. you can try it out too, just copy/paste everything inside the quotes into the url bar.

## what about the same-origin policy?
someone familiar with web security might ask how a website can send requests and control a device on the local network -- the same-origin policy should protect against this.\
Well, it does. Sort of. If you open the browser console while my little app is running, you'll see it flooded with complaints and warnings about how this violates the policy. But, the way the same-origin policy works is it only blocks the *response* from a disallowed request, I can send as many requests to whoever I want, I just can't read the results to any of them.\
So theoretically, any website would be able to rick-roll all the Rokus in your house just by loading the page, the only issue being the website wouldn't know the IP address of your Roku, but if we assume most home networks are set up with an IP range of 192.168.0.X or 192.168.1.X, then we only have 512 requests to send, which is certainly doable as long as the user is on the page long enough
