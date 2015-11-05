Title: Biggest professional mistake
Date: 06:10 Thu 05 Nov 2015
Tags: dev, engineering, mistake, learning
Category: dev, misc
Author: pdt
This is about a time when I interviewed and the interviewer asked me about
my biggest professional mistake to date.

At that time it was not very clear to me what he meant by "professional mistake", so I asked him
whether it was like some illegal thing or the like. Yeah, it was kind of silly, I agree but you have to understand
I was during an interview and I was quite tense.

Like everyone else, I've made tons of mistakes. Some are more painful than others. I typically take failure
very very hard, but it helps in the long term avoiding some of these previous ones. So after thinking for a bit,
I went with the time during my last-term internship. I remember it affecting me quite a lot, but I don't think my answer
was really great, which is a sad because I really really like the position.
The thing is there are some lessons we learned the hard way that completely changed the way we work
and thus we took them a bit for granted. After getting out of the company, I was thinking deeply about this,
leading to a note, which subsequently becomes this post.

Know your priorities
--------------------------

First, the mistake that I told the interviewer was where I had serialize and send data to the front-end where they are displayed
using some js visualization libraries. Now it does not seem like too much, but I was not a front-end/js guy (far from it),
so what I did was write some python wrappers for the visualization libraries since
that what my old team taught me (even though it was java and not python but the idea still holds).
The "solution" was ugly, complex and nasty. But the most important part is that it's very buggy,
so it took me a lot of time debugging and ironing out the errors, missing out on all the
`priorities`. Yes, `priority` is the key word here. I was tasked to help display the data, to solve a particular problem,
not to write wrappers! So I ended up end up doing tons and tons of extra time yet  without much success.
It was quite painful: the inertia, reverting to one's old shell without thinking. From that time one, everytime
I spent much more time on the design part before diving right in like crazy. Some are much better than me at this,
they do it intuitively but not me, I've learned my lesson.


Copy-paste is EVIL
----------------------------
What else? Yesterday I was teaching a course and see somebody was copying/pasting code from stackoverflow
and had trouble getting the right answer. The code was correct  but there's a twist: it's not quite
the same interface / precondition so one has to adapt a bit. I'm not at all against using stackoverflow/gg but
at least we have to understand the solution and the problem we're solving.
So I asked him why he's struggling and walked him through the problem and the solution and it turned out very nice.
What he did actually reminds me a lot of myself.

So back when i started I used to put a focus on the whole problem solving and not much on implementation and
I did a lot of copy-pasty from the net, especially when dealing with languages/frameworks that I was not familiar with.
It helps accomplish the task much faster, at least at the beginning. Therefore, when the problem arises again,
I just went ahead and took the old piece of code or searching, adapt a bitand put it there.

Then there's this one co-worker who saw me doing this all over the place so he taught me about the
`DRY principle`. I did not quite get him until I had to deal with compilation errors when I change my mind but forget to
modify the code at all places.

Moreover, one day it just hits me that I already visited the same stackoverflow page multiple times,
which means I had not learned anything about this particular problem. Now I always always try to retype the whole thing first.


Always write unit tests
-----------------------------------------------------
But I still think the biggest mistake I committed is not writing unittest properly also during an internship. At my school,
I actually don't remember we put a focus on this aspect. So in order to move faster, I completely ignore the whole
testing thing and hoped to get away with it.

For me at that time, it works if the majority if for some cases it give the right behavior. Well, now
most of seasoned/experienced engineers know it's 100\% stupid and I agree with them. Because I had to take feedback from
the final client so the specs change constantly and boys the headache it gave me debugging/dealing with broken things.


I learned this lesson so hard now I'm not even comfortable without unit tests. I just don't feel safe. I just have
to write some tests to sleep better at night. There's someone like the guy in the first chapter of "Coders at work"
who just knows that his code works but not me, not again.


Final
----------------------------------------------------
Since many have now become a part of your workflow, incorporated with your workstyle you don't think much
about it anymore,  but if I got asked that question again, this would be my answer. 

