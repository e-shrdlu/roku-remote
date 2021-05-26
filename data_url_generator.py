import urllib.parse, base64

with open('main.html', 'r') as f:
    htmlFile = f.read()

# remove /* */ comments
comment_start = None
for i in range(len(htmlFile)):
    if not comment_start: # when comment not detected, look for one
        if htmlFile[i:i+2]=='/*':
            comment_start = i
    if comment_start: # when comment is detected, look for end
        if htmlFile[i:i+2]=='*/':
            htmlFile = htmlFile[:comment_start] + htmlFile[i+2:] # htmlfile = htmlfile before comment + htmlfile after comment
            comment_start = None

# remove // comments
# disabled because it also broke urls (removed everything after "http://")
"""for i in range(len(htmlFile)):
    if not comment_start: # when comment not detected, look for one
        if htmlFile[i:i+2]=='//':
            comment_start = i
    if comment_start: # when comment is detected, look for end
        if htmlFile[i]=='\n':
            htmlFile = htmlFile[:comment_start] + htmlFile[i+2:] # htmlfile = htmlfile before comment + htmlfile after comment
            comment_start = None"""

htmlFile = htmlFile.replace('\n','').replace('    ','').replace('\t','') # remove newlines and indentation (probably breaks something if you have more than 3 spaces in a string or something, but I dont so I dont care)

dataUrl = urllib.parse.quote(htmlFile, safe="()[]{}<>=+-_/")
dataUrl = 'data:text/html,' + dataUrl
with open('app.txt','w') as f:
    f.write(dataUrl)

# removed because only 91 characters were being saved
"""
base64DataUrl = base64.b64encode(htmlFile.encode()).decode()
base64DataUrl = 'data:text/html;base64,'+base64DataUrl
with open('base64.txt','w') as f:
    f.write(base64DataUrl)
"""
