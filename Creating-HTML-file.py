# Creating the HTML file
file_html = open("/var/www/html/index.html", "w")
# Adding the input data to the HTML file
file_html.write('''<html>
<head>
<title>HTML File</title>
</head> 
<body>
<h1>Welcome To Apache2 Webserver</h1>           
<p>This HTML Files was generated from a Python script</p> 
</body>
</html>''')
# Saving the data into the HTML file
file_html.close()
