{% extends 'flatpages/default.html' %}

{% block content %}

<form method="post" action="{% url 'login' %}">
{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="login">
    <input type="hidden" name="next" value="{{ next }}">
</form>

{% endblock %}