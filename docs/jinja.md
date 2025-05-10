Absolutely — if you're learning Flask, Jinja2 is your best friend. It’s how Flask dynamically generates HTML from Python data.

Here’s a **beginner-friendly Jinja2 tutorial**, focused **only on HTML templating**, with **no JavaScript** involved.

---

## 🧠 What is Jinja2?

Jinja2 is a **template engine**. It lets you:

* Insert dynamic content into HTML
* Use logic like loops and conditionals
* Keep your templates clean and reusable

---

## 🗂️ Basic Setup

Assume your Flask app uses a folder called `templates/` and a file like `index.html` inside it.

Your Flask route might look like this:

```python
@app.route("/")
def home():
    return render_template("index.html", name="Alex")
```

---

## 🔤 1. Insert Variables

Inside `templates/index.html`:

```html
<h1>Hello, {{ name }}!</h1>
```

Double curly braces `{{ }}` are used to **print** Python values passed from Flask.

---

## 🔁 2. Loops

Pass a list from Flask:

```python
@app.route("/numbers")
def numbers():
    return render_template("numbers.html", items=[1, 2, 3, 4, 5])
```

In `numbers.html`:

```html
<ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

* `{% ... %}` = **logic block**
* `{{ ... }}` = **output**

---

## 🔀 3. Conditionals

```html
{% if items %}
  <p>We have {{ items|length }} items.</p>
{% else %}
  <p>No items found.</p>
{% endif %}
```

You can also use filters like `|length`, `|lower`, `|capitalize`.

---

## 📂 4. Template Inheritance

Let’s make a `base.html`:

```html
<!DOCTYPE html>
<html>
<head><title>{% block title %}My Site{% endblock %}</title></head>
<body>
  <header><h1>My Website</h1></header>
  <main>
    {% block content %}{% endblock %}
  </main>
</body>
</html>
```

Then, in `index.html`:

```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
  <p>Welcome to the homepage!</p>
{% endblock %}
```

✅ **This keeps your HTML DRY and organized.**

---

## 🧪 5. Escaping & Safety

If your data comes from users, Jinja auto-escapes it for security:

```html
<p>{{ user_input }}</p>
```

If you *want* to include raw HTML (rarely needed), use `|safe`:

```html
<p>{{ user_input|safe }}</p>
```

---

## ✅ Summary of Key Syntax

| Purpose        | Syntax                      |             |
| -------------- | --------------------------- | ----------- |
| Output         | `{{ variable }}`            |             |
| If statement   | `{% if condition %}`        |             |
| Loop           | `{% for item in list %}`    |             |
| Template block | `{% block name %}`          |             |
| Inheritance    | `{% extends "base.html" %}` |             |
| Filter         | \`{{ value                  | filter }}\` |

---

Would you like a mini project idea using Flask + Jinja2 with no JavaScript — like a blog, calculator, or todo list?
