## Understanding the HTML tree

```html
<html>
  <body>
    <div>
      <p> Hello World! </p>
      <p> Thanks for watching! </p>
    </div>
    <p> Hope you have enjoyed the video! </p>
  </body>
</html>
```

## HTML Tags and Attributes
* Easier way to find elements! 

```html
<tag-name attrib-name="attrib info">
  ...element contents...
</tag-name>

```
* The attribute name is followed by = followed by information assigned to that attribute, usually quoted text.

## Let's "div"vy up the tag

```html
<div id="unique-id" class="some class">
  ..div element contents
<div>
```
* id attribute should be unique
* class attribute doesn't need to be unique


## "a" be linkin'
```html
<a href="https://www.datacamo.com">
  This text links to DataCamp!
</a>
* a tags are for hyperlinks
* href attribute tells what link to go to 


```

## Class
```html
<html>
  <head>
    <title>Website Title</title>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="class1" id="div1">
      <p class="class2">
        Visit <a href="http://datacamp.com/">DataCamp</a>!
      </p>
    </div>
    <div class="class1 class3" id="div2">
      <p class="class2">
        Or search for it on <a href="http://www.google.com">Google</a>!
      </p>
    </div>
  </body>
</html>
```

## Slasher
```html
xpath = '/html/body/div[2]'
```
* tag-names between slashes give dirextion to which element(s).
* '[ ]' is to specify which div we need. The example has shown that we are searching for the second div.


## Double slasher
```html
xpath = '//table'
```
* Direct to all the table elements. 

Or:
```html
xpath = '/html/body/div[2]//table'
```
* Direct to all table elements which are descendants of 2nd div child of the body element.










