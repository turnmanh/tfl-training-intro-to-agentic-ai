---
title: "Markdown slides:"
subtitle: Examples of using the<br/> appliedAI Institute template
tag: Some examples and features
mdc: true
---

**Jane Doe**
jane.doe@appliedai-institute.de

---
layout: Section
---

<div class="absolute top-50% left-5%">

  <!-- Section title -->
  <div style="text-align: left; font-size: 3rem;">
    Section Title &#x1F680;
  </div>

  <!-- Section description -->
  <div style="text-align: left; font-size: 1.2rem; margin-top: 2rem;">
    This is a section description that can be used to introduce the content of the section.
  </div>

</div>


---
title: Default slide
subtitle: Text alignment (default)
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
title: Default slide
subtitle: Text alignment (center)
align: center
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
title: Default slide
subtitle: Text alignment (end)
align: end
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
title: Default slide
subtitle: Text justification (default)
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
title: Default slide
subtitle: Text justification (center)
justify: center
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
title: Default slide
subtitle: Text justification (right)
justify: right
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
title: Default slide
subtitle: Typography
---

# Heading 1

## Heading 2

### Heading

Body text

**Bold text**

*Italic text*

`monospace text`


---
title: Default slide
subtitle: Decoration
lines: true
---

---
title: Default slide
subtitle: Text size (xs)
text: xs
---

# Extra small text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec faucibus velit. Donec sollicitudin est sit amet elit molestie bibendum. In mattis tincidunt dui, quis suscipit odio tristique vel. Nunc faucibus maximus ex, sed mollis dui commodo nec. Proin elementum nunc vel ligula eleifend, vel ornare tellus suscipit. In mattis nulla eu neque auctor, sed mattis nibh feugiat. Nulla facilisi. Sed fringilla tincidunt varius.

---
title: Default slide
subtitle: Text size (sm)
text: sm
---

# Small text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec faucibus velit. Donec sollicitudin est sit amet elit molestie bibendum. In mattis tincidunt dui, quis suscipit odio tristique vel. Nunc faucibus maximus ex, sed mollis dui commodo nec. Proin elementum nunc vel ligula eleifend, vel ornare tellus suscipit. In mattis nulla eu neque auctor, sed mattis nibh feugiat. Nulla facilisi. Sed fringilla tincidunt varius.

---
title: Default slide
subtitle: Text size (md)
text: md
---

# Medium text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec faucibus velit. Donec sollicitudin est sit amet elit molestie bibendum. In mattis tincidunt dui, quis suscipit odio tristique vel. Nunc faucibus maximus ex, sed mollis dui commodo nec. Proin elementum nunc vel ligula eleifend, vel ornare tellus suscipit. In mattis nulla eu neque auctor, sed mattis nibh feugiat. Nulla facilisi. Sed fringilla tincidunt varius.


---
title: Default slide
subtitle: Text size (lg)
text: lg
---

# Large text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec faucibus velit. Donec sollicitudin est sit amet elit molestie bibendum. In mattis tincidunt dui, quis suscipit odio tristique vel. Nunc faucibus maximus ex, sed mollis dui commodo nec. Proin elementum nunc vel ligula eleifend, vel ornare tellus suscipit. In mattis nulla eu neque auctor, sed mattis nibh feugiat. Nulla facilisi. Sed fringilla tincidunt varius.



---
title: Default slide
subtitle: Code blocks
align: center
---

```python
def say_hello(name: str) -> None:
    print f"Hello, {name}"

hello("Jan Willem")
```

:vspace{size=sm}

**💡 hint:** toggle light/dark mode

---
title: Default slide
subtitle: Scrollable code blocks (with maximal height)
align: center
---

```python{*}{maxHeight:'40%'}
def fibonacci(n: int) -> list:
    """Generate a Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

# Example usage
fib_sequence = fibonacci(10)
print(fib_sequence)
```

---
layout: twocols
title: Two column slide
subtitle: Span (default, 6)
---

::left::

### Left column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

::right::

### Right column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
layout: twocols
title: Two column slide
subtitle: Span (8)
span: 8
---

::left::

### Left column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

::right::

### Right column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
layout: twocols
title: Two column slide
subtitle: Text alignment (center)
align: center
---

::left::

### Left column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

::right::

### Right column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
layout: twocols
title: Two column slide
subtitle: Text alignment (top, center)
align: [top, center]
---

::left::

### Left column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

::right::

### Right column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
layout: twocols
title: Two column slide
subtitle: Text justification (center)
justify: center
---

::left::

### Left column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

::right::

### Right column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
layout: twocols
title: Two column slide
subtitle: Text justification (left, right)
justify: [left, right]
---

::left::

### Left column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

::right::

### Right column:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.


---
title: Grid system
subtitle: Boxes (colors)
align: center
---

::grid{columns=4}
:::box{color=white height=25 text=sm}
**White box:**

Content in the white box
:::

:::box{color=grey text=sm}
**Grey box:**

Content in the grey box
:::

:::box{color=blue text=sm}
**Blue box:**

Content in the blue box
:::

:::box{color=dark-blue text=sm}
**Dark blue box:**

Content in the dark blue box
:::
::


---
title: Grid system
subtitle: Boxes (text alignment & justification)
align: center
---

::grid{columns=3 width=80}
:::box{height=30}
Top left
:::

:::box{align=center justify=center}
Center
:::

:::box{align=end justify=right}
Bottom right
:::
::


---
title: Grid system
subtitle: Boxes (text size)
align: center
---

::grid{columns=3 width=80}
:::box{height=30 align=center justify=center text=sm}
Small text
:::

:::box{align=center justify=center text=md}
Medium text
:::

:::box{align=center justify=center text=lg}
Large text
:::
::

---
title: Grid system
subtitle: Boxes (vertical stacks)
align: center
---

::grid{columns=1}
:::box{color=white text=sm justify=center}
Row 1
:::

:::box{color=grey text=sm justify=center}
Row 2
:::

:::box{color=blue text=sm justify=center}
Row 3
:::

:::box{color=dark-blue text=sm justify=center}
Row 4
:::
::


---
title: Grid system
subtitle: Spacing (small)
align: center
---

::grid{columns=4 gap=sm}
:::box{color=white height=25 text=sm}
**White box:**

Content in the white box
:::

:::box{color=grey text=sm}
**Grey box:**

Content in the grey box
:::

:::box{color=blue text=sm}
**Blue box:**

Content in the blue box
:::

:::box{color=dark-blue text=sm}
**Dark blue box:**

Content in the dark blue box
:::
::


---
title: Grid system
subtitle: Spacing (medium)
align: center
---

::grid{columns=4 gap=md}
:::box{color=white height=25 text=sm}
**White box:**

Content in the white box
:::

:::box{color=grey text=sm}
**Grey box:**

Content in the grey box
:::

:::box{color=blue text=sm}
**Blue box:**

Content in the blue box
:::

:::box{color=dark-blue text=sm}
**Dark blue box:**

Content in the dark blue box
:::
::


---
title: Grid system
subtitle: Spacing (large)
align: center
---

::grid{columns=4 gap=lg}
:::box{color=white height=25 text=sm}
**White box:**

Content in the white box
:::

:::box{color=grey text=sm}
**Grey box:**

Content in the grey box
:::

:::box{color=blue text=sm}
**Blue box:**

Content in the blue box
:::

:::box{color=dark-blue text=sm}
**Dark blue box:**

Content in the dark blue box
:::
::


---
title: Grid system
subtitle: Width (70%)
align: center
---

::grid{columns=3 width=70}
:::box{height=30 align=center justify=center text=sm}
Small text
:::

:::box{align=center justify=center text=md}
Medium text
:::

:::box{align=center justify=center text=lg}
Large text
:::
::


---
title: Grid system
subtitle: Width (80%)
align: center
---

::grid{columns=3 width=80}
:::box{height=30 align=center justify=center text=sm}
Small text
:::

:::box{align=center justify=center text=md}
Medium text
:::

:::box{align=center justify=center text=lg}
Large text
:::
::


---
title: Grid system
subtitle: Width (90%)
align: center
---

::grid{columns=3 width=90}
:::box{height=30 align=center justify=center text=sm}
Small text
:::

:::box{align=center justify=center text=md}
Medium text
:::

:::box{align=center justify=center text=lg}
Large text
:::
::


---
title: Grid system
subtitle: Column spanning (1-3-2)
align: center
---

::grid{columns=6}
:::box{height=25 span=1 align=center justify=center}
Small box
:::

:::box{span=3 align=center justify=center}
Large box
:::

:::box{span=2 align=center justify=center}
Medium box
:::

::


---
title: Grid system
subtitle: Layouts
align: center
---

::grid{columns=3 width=80}
:::box{height=20 span=3 align=center justify=center color=dark-blue}
Large box
:::

:::box{height=25 span=1 align=center justify=center color=grey}
Small box
:::

:::box{span=2 align=center justify=center}
Medium box
:::
::



---
title: Images
subtitle: Image only side
align: center
---

::imgx{src=./src/shared_images/example_title_image.png width=30}
Image caption
::

---
title: Images
subtitle: Absolutely positioned
---

<div class="absolute top-30% left-5%">

<img src="./src/shared_images/example_title_image.png"  width="30%">

</div>


---
layout: twocols
span: 8
title: Images
subtitle: In the right column
align: [top, center]
---

::left::

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

::right::

::imgx{src=./src/shared_images/example_title_image.png width=80}
Image caption
::


---
title: Images
subtitle: In the grid
align: center
---

::grid{columns=9 width=80 gap=lg}
:::field{align=end span=2}
::::imgx{src=./src/shared_images/example_title_image.png}
Image caption
::::
:::

:::field{align=end span=3}
::::imgx{src=./src/shared_images/example_title_image.png}
Image caption
::::
:::

:::field{align=center span=4}
::::imgx{src=./src/shared_images/example_title_image.png}
Image caption
::::
:::
::


---
layout: image
image: "./src/shared_images/example_background.jpg"
---

<!-- PLEASE DELETE WHEN COPYING -->
<div style="position:absolute; top:0; left:0; width:100%; height:100%; display:flex; justify-content:center; align-items:center; color:black; font-size:3rem; font-weight:bold;">
  FULL SLIDE IMAGE
</div>


---
title: Quote
align: center
justify: center
---

<!-- Quote Box -->
<div style="
    background: white;
    padding: 2rem 2.5rem;
    border-radius: 1rem;
    max-width: 800px;
    font-size: 1.6rem;
    line-height: 1.6;
    font-style: italic;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(0,0,0,0.06);
    text-align: left;
    position: relative;
">
This is an inspiring quotation that delivers impact and clarity while fitting in a clean, modern card layout.
It has more than one sentence.

<!-- Decorative Quote Marks -->
<span style="
    position: absolute;
    top: -20px;
    left: -5px;
    font-size: 4rem;
    color: rgba(0,0,0,0.1);
">
“
</span>
<span style="
    position: absolute;
    bottom: -50px;
    right: 10px;
    font-size: 4rem;
    color: rgba(0,0,0,0.1);
">
”
</span>
</div>

<!-- Quote Source -->
<div style="margin-top: 1rem; margin-left: 1rem; font-size: 1.25rem; color: rgba(0,0,0,0.6);">
— Author Name, <em>Publication</em>, 2025
</div>

---
title: Definition
---

:::box{color=white text=lg}

**Prompt Engineering**

<hr
style="
height: 3px;
background-color: #d6dde0ff;
margin-top: 0.5rem;
margin-bottom: 1rem;
">

The craft of writing instructions that clearly tell the model how to respond — focusing on phrasing, style, and structure of the request itself.

:::




---
title: ChatGPT Prompt Component
subtitle: Example
align: center
---

::prompt{tool=search size=lg w=[70%]}
    Create a Slidev component for illustrating prompts in ChatGPT.

    Role: You are a senior front-end developer specialized in Vue.js

    Instructions:
    - Split the components in sub-compents
    - Add options for tool selection (e.g., `agent`, `research`)
    - Copy the prompt to the clipboard when clicking the submit button
::