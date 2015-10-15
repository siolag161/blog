Title: Markov Chain for Text Generation
Date: 17:43 Sun 26 Jul 2015
Tags: nlp, dev, model, markov
Category: dev
Author: pdt
Summary: Simple yet fun

Yesterday, I stumbled upon [this post](https://www.reddit.com/r/nba/comments/3ei3i7/theres_a_bot_that_comments_as_you_based_on_your/)
while browsing reddit on the NBA sub (I'm a NBA follower).
In brief, it was about a reddit post that generate gibberish comments based on your
own activity history.

For those who are not familiar with these kind of bots. Basically, they're some program
that systematically scan new posts in certain subreddits (sub-forums kind-of) and
then trigger some actions based on some pre-defined rules. For example, a bot
would periodically visit the `soccer` subreddit and everytime it see a youtube video posted,
it would try to download this video and upload to another video services (since youtube is famous, understandably,
for being very aggressive in video deletion)

In this case, if we type a username and then the bot's name, the bot would then scan
the user's comment history and generate some funny nonsense comment. It was an instant hit
due to some gems like

> This comment is so terrible that it might just use him as the primary ball handler
> off the top 5 mid-range shooter in the future.
> Anthony Davis 43 pts / 10 reb / 3 blk. He won't be a hall of famer.


or, you know, because it's the NBA offseason.

How can they do it? Actually it's the same way people build [chatbot](https://en.wikipedia.org/wiki/Mark_V._Shaney) back in the day.
I think today it's getting much more complicated, but maybe they just got more data?
Either case, the engine's behind the scene is something called ["Markov chain"](https://en.wikipedia.org/wiki/Markov_chain).

# Markov model for English text
First, we have to understand the way text/document are models. I'm definitely not going into details
here but roughly speaking, a text can be thought as a sequence of words (actually `shingles`, but more on that later),
based on some loosely defined rules. What do I mean by `loosely defined`? Let's consider this sentence

> I found myself wishing Berg focused more on Brower's investigations.

Now, we can think it as a sequence of [`I`, `found`, `myself`, `wishing`, `Berg`, `focused`, `more`,
`on`, `Brower's`, `investigations`]. So if I were a child and that's the first time I heard an English
sentence, since no ones taught me grammar yet, I would think that well, based on my own observation,
a sentence probably starts always with an `I`, and then follows by `found`, then `myself` and so on.
Which means here we ignore virtually everything about the grammar (tenses, positions, etc...).

Then maybe after that, I see and hear more and more then probably I would get that sometime there're more verbs
then `found`. Probably there's a `he` or `she` which acts as the subject also. More precisely,
let's say I heard another sentence:

> I found him to be quite ignorant.

now, `found` is not **always** followed by `myself` but there's a 50% chance it's a **him**.

What we just described is called 2-order Markov chain model for text generation. Indeed, the `1-order` part
refers to the fact we only use a sequences of pair of consecutive words to form a sentence.
We look at ('I', 'found'), then ('found', 'him') or ('found', 'myself') and so on.

So now, it's my turn to talk back. I would construct a sentence by `chaining` the 'pairs' together until I hit
something that marks the end (like `.` or '!'). More technically correct, after building the model,
we would obtain a random graph, and in order to generate the text, we perform simply a random walk in this graph.

Such pair is often called 'bigram', [more on that here for the general case](https://en.wikipedia.org/wiki/N-gram).
People find that an order between `2` and `5` would get the job done in most cases.

# How to learn the model?
You may say that it looks quite simplist but it works pretty well in practice. It's also quite easy
to write the code to train the model. We have to split the document into consecutive `n-gram` (or shingles)
and then update the Markov chain's parameters, which consist only of the shingle's occurrences. Actually,
we learn the matrix of transition but it's not that important.

The simplicity is partially due to the way English word separation works. Indeed, in English (or French and many other languages),
what separates 2 sepaxrate words is either a space or some punctuation (`,`, '.', '!', ...). In some other language like
Vietnamese, it'd get much more complicated so obtain n-gram since there are composite words, like "to quoc" is just a word.
Actually in English there also "composite words" like this, the idea stills hold, we have to take into account the context somehow.

You can find much more information on the model on the internet, espcially on the theorical side. It's probably the most
basic model yet gives an important more general idea of how statistical learning approach works in natural langague processing.

# NBA comment bot's and other applications
Applications of such bot are vast. They used to power botchat. The way botchat works are that they already have a trained model,
it would generate the reply back to you using your sentence as `context`. For example,

You may say:
> Let's talk about Bush

then it would use [`talk`, `let's`, 'Bush'] as seeds for the next reply:

> Bush is no longer in the office, Obama is. (using Bush)
> Let's talk about Kim Kardashian instead (using let's)

and then use your text to update the model. I've heard some model that's trained for decades, wondering around
in many chat channels, talking with generations of innocent souls!

With NBA bot (or twitterbot), the same ideas apply. But if you cross multiple contexts and text, for example
comment history with something serious such as the Bible, probably it'd generate some rather amusing result (or offensive, it depends!)

It's also used to generate random fake comments (for example: `I heard that this product is pretty great`)
but I think we should heavily tweak the model in order to bypass the filter.

# Example:
[Here's a yet another Markov model I coded in Python ](https://github.com/siolag161/markov_generator) which use the book of Tao as input,
generating:

```bash
[1]: Is it not because it could not hurt men.

[2]: The softest thing in the Tao, the more implements to add to his own person last, and do not know it.

[3]: The excellence of a reward for the things which I call it The Great.

[4]: There are few in the world delight to exalt him and do not know it.

[5]: Therefore when one knows that the ancients prized this Tao, the more.
```

it trains the model only in memory. If you want to train the model for years like those chatbots, you should have a database.
Probably just a lightweight one suffices.
