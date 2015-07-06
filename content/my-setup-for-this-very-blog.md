Title: My setup for this very blog
Date: 22:22 Sat 20 Jun 2015
Tags: blog,misc
Category: web
Author: pdt
Summary: This blog's Pelican setup

Tonight is a quiet lonely night and I'm in the mood for writing something, anything really. Normally I would love to
talk a bit about politics or history, but I have this priviledge coming from a communist country
where these kinds of stuffs would get you into troubles. So I guess writing a bit on how I get this blog
up and running might not be a bit *less complicated*.

# How to get started
[As mentioned earlier]({filename}/my-first-post-ever.md), this very blog was setup using the Pelican
static blog engine. As Pelican is quite popular, especially among Python fans (albeit not as popular
as its eternal enemy jekyll), there's no lack of [great](http://nafiulis.me/making-a-static-blog-with-pelican.html)
[tutorials](http://terriyu.info/blog/posts/2013/07/pelican-setup/) out there helping you to get started.

Google it, you say? Well, obviously it might feel a bit overwhelming at first for those who do not have prior background in web dev.
But believe me once you're get your basic config up, you'll then get comfortable very quickly and everything
takes off from there.

For me, the most important thing with blogging with Pelican (or any static engine for that matters)
consists in finding a workflow that works for you. If you don't have one yet, well it's a great time
to pick one and learn!


Regardless of the workflow choice, it should enable you to at least do these following tasks:

* Preview the content of your posts and/or your site (*)
* Push the changes to the server (**)
* Customizing the feel and look of your blog (***)

I personally find the [post by nafiulis](http://nafiulis.me/making-a-static-blog-with-pelican.html)
very comprehensive. Go read it and follows his instructions if you have no clues, highly recommended!

# My own setup

How blogging with Pelican works again?
------------------------------------------
When working with Pelican, you write not in HTML directly but in some markup language like Markdown or
reStructuredText. Pelican will take care of compiling the content that you write into HTML, coupled with
the style defined in your chosen theme to render the fancy blog posts. It comes with a default one, so need
to get your hand dirty.

Previewing content
------------------------------------------
When you first install Peliacan, it typically gives you a choice between a makefile and a Fabric script
for automating all the repetitive tasks. Either one allows you to take a peek before the post goes out into the wild.
More technically, it launches a local web server allowing you to see your site with the newly added posts.
Sounds great, battery included!  Bad new is every time you make some changes to your liking, let it be customizing your
theme or update the post, the server will not be aware of this yet and you have to refresh the browser manually. So much hassle.

<!-- So there are several ways to solve this. For example one can use a text editor capable of automatically -->
<!-- render the post lik -->e
Obviously there are text editor our there that can help you do this automatically like [Atom]() which gives you the a of the result HTML.
The incovenience is that it may not be able to take into account the look and feel from your blog's current theme.

Like many other, my approach is to use an automate tool like [Gulp]() or [Grunt]() since I was already using one.
The learning curve is rather steep, but after you set them up, you'll never have to look back. The concecus now is apparently 
[Gulp](). So if you've never heard of either of them, it may be a great time to learn.

Pushing your posts to the server
------------------------------------
Fully disclose, I host this blog that no one reads without paying a dime at [Github Pages]().
If you have never heard of github (or git), again seriously man go learn
at least the basics of them Once you get the principle ideas already, now we are presented with
different strategies to deploy our posts.

We can render locally to HTML and push the changes to the distant server (by our friend at github
in my case). Or we can use the technique described [
here](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html).
You see, regardless of strategies, we still need to use git (or mercurial but no CVS, thanks) to
version-control our content. The later approach allows to leverage TravisCI and git-hooks to detect
every time we push the markup code to our github repo, then compile and push the rendered content
to the github page branch. Very nice and clean method.

Customizing the looks and feels
------------------------------------
This parts requires some basic knowledge of CSS and HTML, you just can expect to get around it
and be alive. Again, if you opt for the Grunt (Gulp) solution, you should be fine here
as Grunt/Gulp will capture any modifications you make to reflect on the theme and allow you
to preview before going live. I normally don't do CSS directly but use SASS instead, so an automation
tool is a must for me as no sane men compile them manually.

The most important part: writing
---------------------------------------
You gotta agree with me here, being able to update your site requires more time than setting it up.
This is the most important part in your workflow yet no tools could help you with!
