---
layout: default
---

## [Schedule](#schedule)


{% for semester in site.data.toc %}

---

### {{ semester.title }}

---

{% for week in semester.weeks %}

#### {{ week.title }}
{% for topic in week.topics %}
- [{{ topic.title }}](./topics/{{topic.title | slugify}}.html)
{% endfor %}
{% endfor %}
{% endfor %}

## [FAQs](#faqs)

{% for question in site.faqs %}

### [{{ question.title }}](#{{ question.slug }})

```plaintext
{{ question.content | strip_html}}
```

{% endfor %}

## [Assessment]({{ site.baseurl}}/assessment/)

## [Log](#blog)

([RRS feed]({{ site.baseurl }}/feed.xml))

{% for post in site.posts %}
- [{{post.date | date: '%Y-%m-%d'}}: {{ post.title }}](./{{ post.url }})
  {{ post.excerpt }}
{% endfor %}
