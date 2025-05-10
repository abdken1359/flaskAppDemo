Sure! Here's a **full beginner-friendly tutorial** on **Jinja2 Filters** in Flask. Jinja filters allow you to modify variables in your templates before displaying them in the browser.

---

## Jinja2 Filters in Flask

### **What are Jinja Filters?**

Filters in Jinja allow you to modify the output of variables in your templates. For example, you can:

* Change the case of a string
* Format a date
* Truncate a string
* Apply custom transformations to your data

### **Basic Syntax for Filters**

Filters are applied to variables using the **pipe (`|`) symbol**. The syntax is as follows:

```html
{{ variable | filter_name }}
```

For example:

```html
{{ name | upper }}
```

This will take the value of `name` and convert it to uppercase.

---

### **Commonly Used Filters**

#### 1. **`escape`** – Escape HTML characters

Escapes HTML characters to prevent them from being rendered as HTML (e.g., `<`, `>`, `&` will be escaped as `&lt;`, `&gt;`, and `&amp;` respectively).

```html
{{ "<h1>Hello</h1>" | escape }}
```

Output:

```
&lt;h1&gt;Hello&lt;/h1&gt;
```

#### 2. **`lower`** – Convert to lowercase

Converts a string to lowercase.

```html
{{ "HELLO" | lower }}
```

Output:

```
hello
```

#### 3. **`upper`** – Convert to uppercase

Converts a string to uppercase.

```html
{{ "hello" | upper }}
```

Output:

```
HELLO
```

#### 4. **`length`** – Get the length of a list or string

Returns the length of an object, like a string, list, or dictionary.

```html
{{ "Hello" | length }}
```

Output:

```
5
```

#### 5. **`default`** – Set a default value if a variable is undefined or empty

If a variable is not defined or is empty, you can provide a fallback/default value.

```html
{{ name | default("Anonymous") }}
```

If `name` is undefined, it will show "Anonymous".

#### 6. **`replace`** – Replace part of a string

Replaces occurrences of a substring in a string.

```html
{{ "Hello, world!" | replace("world", "Flask") }}
```

Output:

```
Hello, Flask!
```

#### 7. **`join`** – Join items in a list into a string

Joins a list into a single string, separated by a specified separator.

```html
{{ ["apple", "banana", "cherry"] | join(", ") }}
```

Output:

```
apple, banana, cherry
```

#### 8. **`truncate`** – Truncate a string to a specified length

Truncates a string if it's longer than the specified length and adds an ellipsis (`...`).

```html
{{ "This is a long sentence" | truncate(10) }}
```

Output:

```
This is a...
```

#### 9. **`int` / `float`** – Convert to an integer or float

Convert a string to an integer or a float.

```html
{{ "123.45" | float }}
```

Output:

```
123.45
```

#### 10. **`date`** – Format dates

You can format a `datetime` object using this filter.

```html
{{ some_date | date("Y-m-d") }}
```

If `some_date` is a `datetime` object, this will format it as `2025-05-10`.

#### 11. **`time`** – Format time

Like `date`, but for `time` objects.

```html
{{ some_time | time("H:i:s") }}
```

Formats the time as `15:45:30` (hours\:minutes\:seconds).

#### 12. **`safe`** – Mark a string as safe HTML

Prevents a string from being escaped in the template (be careful when using this to prevent XSS attacks).

```html
{{ "<h1>Hello</h1>" | safe }}
```

Output:

```html
<h1>Hello</h1>
```

---

### **Using Filters in Flask Templates**

You can use Jinja filters directly in your Flask HTML templates. Here’s an example:

#### **Flask App Code (`app.py`)**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="John Doe", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec venenatis.")

if __name__ == "__main__":
    app.run(debug=True)
```

#### **Template Code (`index.html`)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jinja Filters Example</title>
</head>
<body>

    <h1>Welcome, {{ name | upper }}!</h1>
    
    <p>Your description: {{ description | truncate(30) }}</p>
    
    <p>Length of name: {{ name | length }}</p>

    <p>Your description in uppercase: {{ description | upper }}</p>
    
    <p>Safe HTML: {{ "<strong>This is important!</strong>" | safe }}</p>

</body>
</html>
```

### **What Happens in the Template:**

* The `{{ name | upper }}` will display `JOHN DOE` because it's converted to uppercase.
* `{{ description | truncate(30) }}` will show a truncated version of the `description` with a length of 30 characters, adding an ellipsis (`...`) if necessary.
* `{{ name | length }}` will show the length of the string `John Doe`, which is `8`.
* `{{ description | upper }}` will display the `description` in all uppercase.
* `{{ "<strong>This is important!</strong>" | safe }}` will display the HTML `<strong>This is important!</strong>` as actual HTML, making the text bold.

---

### **Custom Filters in Flask**

You can create your **own custom Jinja2 filters** if the built-in ones don’t meet your needs. Here’s how:

1. Define a custom filter function.
2. Register the filter in the Flask app.

#### **Example: Custom `reverse` Filter**

#### **Flask App Code (`app.py`)**

```python
from flask import Flask, render_template

app = Flask(__name__)

# Define the custom filter
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route("/")
def home():
    return render_template("index.html", name="Flask")

if __name__ == "__main__":
    app.run(debug=True)
```

#### **Template Code (`index.html`)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jinja Custom Filter</title>
</head>
<body>

    <h1>{{ name | reverse }}</h1>

</body>
</html>
```

#### **What Happens:**

* The custom `reverse` filter reverses the string `Flask` and prints `ksalF`.

### **Registering Custom Filters:**

In this example, we used the `@app.template_filter('reverse')` decorator to register a custom filter. You can register as many filters as you need, and use them in your templates with the pipe (`|`) syntax.

---

### **Conclusion**

Jinja filters are a powerful way to transform data in your templates. Here's a summary:

* **Basic Filters**: `lower`, `upper`, `length`, `date`, `default`, `truncate`, etc.
* **Safe HTML**: Use `safe` to display HTML tags.
* **Custom Filters**: You can create your own custom filters in Flask by defining a function and registering it.

This should be enough to get you started with filters in Flask and Jinja2. Experiment with them to see how they can clean and enhance the display of your data. Let me know if you'd like a challenge or any additional clarifications!
