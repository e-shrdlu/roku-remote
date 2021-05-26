# roku remote for mobile
This is an "app" that allows you to control your roku from your phone!
(yeah I know, theres already an app for that)

## how to use

to use, simply copy and paste the contents of `app.txt` into your phones url bar (on IOS you must use safari, on android.. idk i havent tested it). then, scroll to the bottom and enter you roku's local IP adress (which is under `settings > network > about` on your roku), and youre ready to go! if you want, you can even change the default IP adress by changing the last few characters in the URL (it should look somthing like `."IP"%20value="192.168.50.152"/></body></html>`)

## why did I make this?
well, it all started out when I stumbled across the fact that rokus have a remote control API and thought it'd be cool to do something with it. first, I made a [python tool](https://github.com/rainbowkitty227/roku-remote), but how often do you have your computer with you while watching TV? so next I made new local website on the raspberry pi that [controls my LED lights](https://github.com/rainbowkitty227/LED-controller), which executed anything in a text box (yeah, security vulnerability, I know), including commands for my python roku remote thing. But, then somehow I broke the raspberry pi, in that it can accept incoming connections (you can go to the page), but wont make outgoing connections (so when you try to connect to the roku, it doesnt work).\
So, I needed to find another option. I could do the same thing but on my laptop, but Id need to leave it on all the time, and I was more worried about security holes in the regular computer than pi.\
So I started looking for a way to do it on my phone (aside from like, just downloading the app). I thought maybe the built-in shortcuts app might be the way to go, but there was no options for what I needed. Oh that reminds me, I should mention why it wouldnt work.

okay so when you connect to a website, your computer is like "yo, google.com, gimme your webpage", and googles like "sure, here you go". thats called a GET request -- your computer is GETing the page. theres also something called a POST request, which is when your computer is like "hey, twitter.com, I got this cool new tweet, here you go", and twitters like "thanks bro, Ill put it up".\
To use the roku api to send a keypress, say, the home button, you need to send a POST request to `<roku-ip>:8060/keypress/home`, but you cant just do that by typing that into the url bar, because that will send a GET request, and the roku will ignore it. the easiest way to send a POST request would be to run something like `curl -X POST <roku-ip>:8060/keypress/home`, but since apple doesnt want their users to be able to *do* anything, you cant do that on youre phone.

then today, I was messing around and I discovered the safari app (but none of the other browsers for some reason) allows top level data urls!

what the heck is that? see below


## how does it work?
Im assuming you dont know what a data url is, so Ill explain:\
say youre making a website, and youve got a page with a whole bunch of users, and each one has a profile picture. maybe you dont want to send a request back to youre server for each picture, so you can use data urls!\
for example, normally to embed a picture, you would do something like `<img src="http://example.com/images/profilepicture001.jpg">`. with data urls, youd do something like ```<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAZABkDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDkE019UuzAJVjCKGJYcdfSrqaNPp1lIzyJMAwXK8bferlhGVQ74UO/kE9WH+f50txLstZkMYV5nB4P8I7kf56Vo7uszdKKoXOZ1a3e4WJUGcEk1mf2VP8A3f1rq4EQsxPb1qzmL+6Kxr1nGbSHSppwTK3jKe7tr22u7YPHDsaEK0eB1zjB/wA8VD4OPmPeXWoP5gkaOMK3cAnOPpkVt/ET/kD23/XwP/QWrL8Pf8i8f98/zrWK1M5X2NvVNIWyzPbbmjJwyk/d9PwrJ+b+6Pzrrr7/AI8Lj/rmP5VyVZVYKcrs1g+VWR//2Q==">```\
a much longer url, but that holds the *entire* image. no internet connection needed. you can try it out too, just copy paste everything inside the quotes into the url bar.

anyways, I found out that you can run javascript on your iphone with something like `data:text/html,<script>console.log('hello, world')</script>`. now that we have a way to execute code on an iphone, we can accomplish the goal of controlling the roku with `data:text/html,<script>fetch('http://[roku_ip]:8060/keypress/home',{method:'POST'})</script>`. from there, I just made a simple page, converted the whole thing to a data url so I could just paste it in and I wouldnt need a server to run it (since you just open local files in the web browser either. thanks apple)

aand thats about it
