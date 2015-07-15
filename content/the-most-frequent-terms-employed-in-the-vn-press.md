Title: The most frequent terms employed in the VN press
Date: 15:14 Tue 14 Jul 2015
Tags: dev, stats
Category: dev, stats
Author: pdt
Status: draft
Summary: What are the most used words or terms in the VN press
This is the content of my super blog post.

A bit like in China, private-held media are not (officially) allowed in Vietnam.
[Recent study (quoted from BBC, realized by Gallup) ](http://www.bbg.gov/blog/2015/05/26/media-use-in-vietnam/)
found that most VietnameseN trust bloggers more than official news agency! That tells alot, IMHO.

Plus, <!-- at least according to my own experience and the people I know -->
 it's no secret that the  general
 quality of the media has deteriorated to the point of unbearibality. Every time I visit
 a newspaper site, on the front page news on celeb's private life, showbiz's scandals,
 clickbait headlines are all over the place. I sometimes do wonder if anyone has studied how bad
 it is.

# How to address the press quality
But then again, `bad` is quite subjective, it's not obvious to quantify the quality of the press. I believe
we cannot have a definite answer either. However, if we go to the quatitative route, I think if we can
perform some sort of statisical analysis to obtain the general focus of the press, we can somehow infer the quality.
For example, we can perform a [topic modeling](https://en.wikipedia.org/wiki/Topic_model) to see if
`attack on corruption` is an important part. As I do not have much experience in natural language processing,
my take is that this task is very interesting but also very difficult. 

As I don't have the ambition to perform the full-scale analysis, I only want to do a baby step which is to find the
most frequently used terms in the press, after removing all the [stop words](https://en.wikipedia.org/wiki/Stop_words).
This seems to be an easy task but it turns out to be quite the contrary.

# Word segmentation
The difficulty of our task lies in the problem of extracts the words from a sentence. In a language like English,
where  words are delimited by space and punctiations, it's very easy. However, Vietnamese is an interesting language
where most of the words maycontain more two or more syllables. These syllables come together to form a form but they
are delimited by a space. For example, "kitten" in vietnamese is "meo con", which also a disyllabic word. There's
some studies on this but I have no idea where the state of the are is at the moment. 



