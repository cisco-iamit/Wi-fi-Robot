# Web Controller Activity

In this activity, you will be making a remote control guide for the robot and
it looks like this:


To do this, we will be writing HTML, CSS and JavaScript

## Files to edit and seeing your site

For the purposes of this tutorial, you will be editing these files:

```shell
webserver/index.html # HTML
webserver/static/css/style.css # CSS
webserver/static/js/controls.js # JavaScript
```

To see the results, run this:

```shell
cd webserver
python3 server.py
```

Then navigate to `192.168.4.1:8000` on a webbrowser to see the page

## Intro to HTML

HTML stands for _Hyper Text Markup Language_, it simply tells the browser
the structure of the webpage.

### Introductory tags

The `<head> </head>` is where you put any imports and meta data about the
webpage, but inside the `<body> </body>` tags is where we will put our
controls!

```html
<html>
  <head>
  </head>
  <body>
  </body>
</html>
```

You'll see that the `<head></head>` tags already been filled in for you!
So let's add some code to the `<body></body>`

### Tags

HTML tags e.g `<body>` or `<head>` are written with `<` and `>`, these aren't
shown on the page, but just tell the browser that it's a marker for something
special and to render the contents inside the tags different.

For example, the `<h1>` tag is the tag for headlines so anything marked with
`<h1> Title </h1>` will be displayed in a large bold, headline like font.

Let's add in a title that says "Robot Control" (or whatever you like!)

So you should get something like this:

```html
<body>
  <div class="root-container">
    <h1> Robot Driver</h1>
  </div>
</body>
```

(don't worry about the `div` tags! - ask one of the mentors if you are curious!)

You should get something like this on the webbrowser:

### Adding sensor icons

To add sensor icons, we will make use of the FontAwesome library. This has
already been provided and you can simply use the icons out of the box:

Simply add `<i class='fas proximity proximity-left fa-wifi'></i>`: inbetween
the `<div class='top-row'></div>`

```html
<div class="proximity-container">
    <div class="top-row">
        <i class="fas proximity proximity-left fa-wifi"></i>
        <i class="fas proximity proximity-front fa-wifi"></i>
        <i class="fas proximity proximity-right fa-wifi"></i>
    </div>
</div>
```

You'll now see this:

This is great, but we want to differentiate between all three sensors. We
can do this using some _CSS_.

CSS stands for _Cascading StyleSheet_, we simply use it to tell the browser
how the things should look.

Let's rotate the sensor symbols to show that they should be left or right.

Edit the `webserver/static/css/style.css` file and use this transform to rotate
the icon:

```css
.proximity-left {
    transform: rotate(-45deg);
}
```

Work out what you need to do for the right sensor!

```css
.proximity-right {

}
```

If you've done it correctly, you'll now something that looks like this

### Adding control arrows

Let's now add all the control arrows! You'll need to add these icons:

```html
<div class="top-row">
    <i class="fas fa-arrow-up"></i>
</div>

<div class="bottom-row">
    <i class="fas fa-arrow-left"></i>
    <i class="fas fa-arrow-down"></i>
    <i class="fas fa-arrow-right"></i>
</div>
```

You should get something like this:

### Label the sections

Just like with `h1` we can also use other headings e.g `h2`, `h3`. `h3` can be
used to give a heading smaller than `h1`.

Add a tag `h3` to label the icons!

You should get something like this: (if you get stuck, you can ask a mentor!)

You'll have something that looks like this:


Now that we have the visuals sorted, we can move on to the interactive elements

## JavaScript
