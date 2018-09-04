---
layout: mainpage
---

## Upcoming deadlines

<ul class="due-list">
{% for post in site.posts %}
    {% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}
    {% capture duetime %}{{post.due | date: '%s'}}{% endcapture %}
    {% if post.categories contains 'assignment' and duetime > nowunix %}
    <li>
       <span><span class="post-meta"><b>(Due <span itemprop="date">{{ post.due | date: "%b %-d, %Y" }}</span>)</b></span><a class="mainpage-asn-link" href="{{ post.url | absolute_url }}">{{ post.title }}</a></span></li>
   {% endif %}
{% endfor %}
</ul>

## Information

<div class="infomatter">
<table class="infotablestyle">
<tr><td>Course Number</td>
    <td>CMSC 107 (Fall 2018) at <a href="https://www.haverford.edu/computer-science/">Haverford College</a></td>
</tr>
<tr><td>Instructor</td>
    <td><a href="http://kmicinski.com">Kristopher Micinski</a></td>
</tr>
<tr>
    <td>Times</td>
    <td>Tu/Thur 11:30-13:00 <i>Lecture</i>  W 11:30 / 12:30 <i>Labs</i></td>
</tr>
<tr>
    <td>Office Hours</td>
    <td>Tu/Thur after class and by appointment</td>
</tr>
</table>
<img class="krispic" src="/assets/img/krisbw.jpg">
</div>
    
## Introduction 

This course is an accelerated introduction to computer science,
covering the same material as both CS105 and CS106 at [Haverford
College](https://www.haverford.edu/computer-science/). We have two
broad goals. The first is to become thoughtful programmers who can
articulate the methodology behind the design of our code. The second
is to use those principles to help us understand the core
data-structures that underlie the design of robust, efficient
systems. We will do both of these by writing a good amount of code,
but also thinking hard about how we can be sure we got it right.

Code is the vocabulary through which we articulate computation. We
need to learn how to write it well. This takes a lot of time, a lot of
getting it wrong, and a lot of figuring out what we can do
better. We'll spend the fist half of the semester learning Python,
learning the core features and building up to some ambitious projects
along the way.

Along with the basic vocabulary given to us by the programming
language (e.g., the syntax), designing *good* programs requires
utilizing robust, efficient abstractions for the data on which these
programs operate. For example, think about how we might represent a
phone book. We might implement the phone book as a large unordered
list of pairs (of names and numbers). But that wouldn't be very
efficient: searching for a phone number would require combing through
the list person-by-person. Instead, we might use a dictionary: an
efficient way of representing keys (names, in this case) and their
corresponding values (phone numbers). Of course, there are a variety
of different ways we could envision implementing a dictionary. In
practice, we probably won't be writing this implementation ourselves
(since someone's likely done that for us), but we need to understand
the implementation trade-offs to pick an implementation that best
suits the system *we* want to build.

So rather than just gain superficial knowledge of different data
structures, we're going to implement them ourselves. We do this for a
few reasons. First, implementing data-structures correctly is hard and
error-prone, and will hopefully force you into so much frustration
that you have to sit back and think hard about how the pieces fit
together. When you get it right, you'll understand the essence of
programming: tackling a conceptual problem and articulating a solution
as an algorithm implemented in code. Second, you're going to need to
write a *lot* of code to become a good programmer. This course isn't
going to be enough to do that, but our goal is to get you on a path so
that you can continue in subsequent courses, internships, and your own
projects.

Last, we want to write *good* code. We don't want to hack something
together, tinkering with it until it appears to work. We want to
present a principled argument behind why our code is correct. So
first, we're going to write a ton of tests (we'll study in the course
what makes a *good* test). Next, we're going to learn how to use
formal reasoning to talk precisely about our code. But beyond these
technical things, we're going to talk to each other about our
code---and have some frank discussions about what we should be doing
better.

I hope you're excited for the course as I am!

## Course Structure

Please read the [Syllabus]({{ "/syllabus" | absolute_url }}) for course information.
