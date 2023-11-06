---
layout: default
---

## Class notes

A collection of all my personal notes for class.

**Note: These are not designed to be
student facing.**

I make them available with the intent of making it easier to plan and/or take
notes from class.

Student facing resources for each topic are all available at [vknight.org/cfm]({{site.baseurl}}/).

{% for notes in site.class-notes %}

- [{{ notes.title }}]({{notes.title | slugify}}.html)

{% endfor %}
