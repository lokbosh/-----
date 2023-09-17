from django import template


register = template.Library()



censor_words = ['редиска','дурень','ишак']

@register.filter()
def censor(value):
    text = []
    text1 = value.split(" ")
    for i in text1:
        for i in censor_words:
            i = '****'
        text.append(i)
    return " ".join(text)
    