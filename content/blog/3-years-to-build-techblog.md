---
date: '2025-01-06T20:58:59+01:00'
author: 'Daniil Roman'
keywords: 'hugo,github,simple analytics,giscus,tech blog'
draft: false
title: 'How it took me 3 years to setup a personal website'
cover:
  image: '3-year-personal-website/logo.png'
  width: 120
  height: 60
  responsiveImages: true
---
In this article, I'm going to tell the story of why this website even exists 😄.
I’ll share the tech stack I’ve chosen, covering CMS, domains, analytics, and even a comments integration. But trust me, I really tried to use dev.to and Medium.

Check this website project on [GitHub](https://github.com/DaniilRoman/personal-website) by the way

## How I Started / Background

Here are a few words about me and my background. I’m a backend developer who enjoys learning new things, building small personal pet projects, and sharing my experiences by turning them into tech articles like this one.

My first-ever blog post was a silly tutorial on how to build a personal dating app using only Redis as a datastore. It was a lot of fun building that MVP and writing about the experience. Back then, the choice of platform for publishing my first article was crystal clear to me.

I was in Russia at the time, and habr.com was the most popular platform there, with a huge and active community. It was never the most polite community, though, but over time, I realized that having an engaged and involved audience is incredibly valuable.

I posted the article, received a few comments and a few thousand views. I was actually very happy with that result and decided it was time to translate it into English to reach an even wider audience (ohh, that was so naive) 😁

## The Hard Time Switching to English-Speaking Platforms

When I first started writing in English, my language skills were pretty poor, and I didn’t have ChatGPT to help — but that didn’t stop me.

I had heard about Medium as a general platform for posting articles, and I knew about more tech-specific platforms like dev.to and dzone.com, but I didn’t really follow them (still don’t, to be honest). I just saw them in browser recommendations from time to time.

Anyway, I didn’t know many options. I didn’t even realize I could ask on Reddit or Twitter (not sure that would have helped, though). So, Medium seemed like the way to go since it was the most popular platform.

And… the response? Pure silence. 🫠

{{< linkpreview 
text="Designing an application with Redis as a data store. What? Why?"
url="https://medium.com/@daniil_roman/designing-an-application-with-redis-as-a-data-store-what-why-d02e685ee2b8"
>}}

On habr.ru, over time, my article received 17,000 views, 20 comments, and was bookmarked by 68 people.

![First habr article view](/3-year-personal-website/first-habr-article-view.png)

![Screenshot 2025-02-07 at 21.31.14.png](/3-year-personal-website/first-habr-article-reactions.png)

I thought, _okay, it won’t be the same on Medium, but…_

![Medium statistics from my first article](/3-year-personal-website/medium-stats.png)

I didn’t expect it to be that bad. 🫠 Basically, it was 100 times worse. 🤯

## The Rise and Fall of dev.to

But I gave it a second shot — this time with dev.to.

I wrote about a work-related topic on Elasticsearch.

{{< linkpreview 
text="How we built Elasticsearch index"
url="https://dev.to/daniilroman/how-we-built-elasticsearch-index-8hh"
>}}

When I posted it… well, it was better.

![dev.to first post reactions](/3-year-personal-website/devto-post-reactions.png)

But here’s the catch: I posted the same article on Habr and could compare the results.

![Corporate blog post statistics from habr.com](/3-year-personal-website/habr-corporate-post-views.png)

On dev.to, compared to habr.com, it performed 30 times worse. 👍

Still, that was _progress_ compared to Medium. And there was a tiny bit of hope — at least I got a few reactions on dev.to. Compared to the _complete silence_ on Medium, that was a win.

## Why I Didn’t Want a Personal Blog at First

A fair question might be: _“Why not just start your own blog?”_

But in the beginning, I didn’t think it would be easy for me to set up a personal website from a technical perspective. I didn’t want to spend time maintaining a website or dealing with bugs (yeah, I simply didn’t know the right tools).

More importantly, I wanted to benefit from existing communities, just like I did on Habr.

I wanted my articles to be recommended to the right audience on a platform. I wanted to at least have the chance to be seen — something that’s much harder on the open web.

Publishing on established platforms seemed like the reasonable choice.

## Why I Finally Switched to a Personal Blog

At the end of the day, it became obvious that these platforms didn’t work for me. My assumption is that they _could_ work if I posted more regularly and stuck to a single topic, like Java or Elasticsearch.

But honestly, I don’t think people use dev.to or Medium to follow recommendations or discover new authors. Instead, they just Google something like _“How to use Kafka in a Spring Boot application”_ — and those platforms show up at the top of search results thanks to good SEO. That’s it.

But I prefer writing more personal, author-driven content. I’d rather post rarely about something meaningful to me and my work than churn out artificial content just to fit a niche.

With my own website, I can focus on long-lived articles, continuously updating them as needed.

And honestly, setting up a personal website is criminally simple nowadays — especially if you have even basic web knowledge. 🤯

## Toolset 🛠️

First of all, I still didn’t want to write all the code from scratch and maintain it myself. I needed to choose a CMS and a few other tools so I could focus solely on my content.

Thankfully, there are plenty of static site generators out there. But still, I had to replace the essential features that platforms like Medium and dev.to provide for free — such as analytics, reactions, comments, and automated content deployment.

## Hugo ✅ → To Build the Website

Of course, the most important part was choosing a CMS tool to generate the website.

Hugo was a pretty obvious choice — Markdown-based and boasting **78k+ stars** on GitHub. And we all know GitHub stars never lie, right? 🙃

{{< linkpreview
text="4.5 Million (Suspected) Fake Stars in GitHub: A Growing Spiral of..."
url="https://arxiv.org/abs/2412.13459"
>}}

Nevertheless, so far, it’s been working really well. Hugo has a lot of templates, and I’m using one of them. Plus, it offers plenty of ways to extend the default settings and insert custom HTML blocks when needed.

I’ve already had to inject a custom one-liner JavaScript snippet into the HTML header for Simple Analytics, and it was super easy to figure out. And, of course, ChatGPT helped — because how else do you work with a new tool? Read the documentation? Definitely not. 🙅‍♂️

{{< linkpreview
text="The world’s fastest framework for building websites"
url="https://gohugo.io/"
>}}

## GitHub Pages ✅ → To Deploy

Alright, but I still needed a way to make it visible to my ~~mom~~ readers. 🤔

The next step was deployment. I needed a way to deliver the final website to a remote server where it would be hosted.

And these days, **GitHub Pages** is the easiest and most straightforward way to achieve that. Do we even have any other real options? Really?
{{< linkpreview
text="GitHub Pages documentation - GitHub Docs"
url="https://docs.github.com/en/pages"
>}}

![GitHub actions UI](/3-year-personal-website/github-actions.png)

## Cloudflare ✅ → To Manage Domains and Redirects

Cool! At this point, my website was up and running, but it was still hosted on GitHub's default domain. I wanted my own domain — [daniilroman.com](http://daniilroman.com/).

On top of that, I wanted to add a small trick: serving my personal projects under subdomains of my website, like this one — [substacktrends.daniilroman.com](https://substacktrends.daniilroman.com/). 🚀

{{< linkpreview
text="Connect, protect, and build everywhere | Cloudflare"
url="https://www.cloudflare.com/"
>}}

![Cloudflare UI with domains overview](/3-year-personal-website/cloudflare-ui.png)

It turned out to be pretty simple as well. Just a few **CNAME** records to configure, and voilà! 🎉

## Simple Analytics ✅ → To Track Visitors

The next essential feature I was missing, compared to platforms like Medium or dev.to, was **analytics**.

I could have used **Google Analytics**, which is the default choice for most projects, but… not if you're in Europe. 🫠

I didn’t need any fancy analytics. I just wanted to know how many times a URL was opened.

Platforms like Medium and dev.to offer much more detailed analytics, but replicating that for free is tricky.

{{< linkpreview
text="The privacy-first Google Analytics alternative - Simple Analytics"
url="https://www.simpleanalytics.com/"
>}}

![Simple Analytics dashboard with numbers for the last 30 days](/3-year-personal-website/analytics-dashboard.png)

Luckily, it wasn’t that hard. I found Simple Analytics, and it met my needs by providing simple page view tracking.

The only custom tweak I had to add was a single line of JavaScript.

```js
<script async src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
````

in `/layouts/partials/extend_footer.html`

## Comments Based on GitHub Discussions ✅ → To Leave Feedback

The final touch, the cherry on top, was adding comments and reactions.

While randomly browsing Hugo’s documentation, I discovered that I could integrate GitHub Discussions into my website completely for free.

{{< linkpreview
text="giscus"
url="https://giscus.app/"
>}}

You can see an example right at the end of this page. 👇👇👇

These days, building a website is easier than making a perfectly steamed egg. Then again, even cooking a simple egg feels like a challenge sometimes. 🤔

## Conclusion

My final toolset:\
**Hugo + GitHub Actions + GitHub Pages + Cloudflare + Simple Analytics + Giscus**

Overall, it was way easier than I expected. Modern tools make it super simple for anyone to create their own website nowadays.

**Keep crafting!** 🪩