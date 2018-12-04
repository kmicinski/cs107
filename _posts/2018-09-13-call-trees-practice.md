---
title: "Call Trees Practice"
layout: post
categories: lecture
published: true
due: 2018-09-10
permalink: /lectures/call-trees-practice
---

Consider the following Python functions

```
def foo(x):
    if (x == 1 or x == 2):
        return x
    else:
        return x * foo(x/2)

def slice(l,start,end):
    return l[start:end]

def f(x):
    if (len(x) == 1) return x[0]
    elif (len (x) % 2 == 1): return f(slice(l, len(l)/2, len(l)))
    else: return f(slice(l,0,len(l)/2))
```

Draw call trees for the following calls:

- `foo(1)`
- `foo(10)`
- `f([1,2,3,4,5,6])`


