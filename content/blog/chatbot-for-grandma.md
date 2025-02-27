---
date: '2025-01-06T20:58:59+01:00'
author: 'Daniil Roman'
keywords: 'chatbot,chat-bot,yandex alisa,яндекс алиса,no code,no-code'
draft: false
title: 'Chatbot for Grandma'
cover:
  image: 'chatbot-for-grandma/cropped-logo.png'
  width: 120
  height: 60
  responsiveImages: true
---
Hey everyone 👋

Have you ever wondered how to keep in contact with your elderly grandma who lives in another country? What if she's never used any messaging apps and doesn't even have a smartphone?

Well, in this article, I'm going to share my story about overcoming this challenge 😁 and why I even ended up writing some code for it.

By the end of the article, you'll understand why smart assistants, messengers, and chatbots come into play here.

## Idea
I didn't begin with creating anything too complex, of course. Firstly, I simply handed her my old smartphone, where I removed all the icons except for Telegram, which is my primary messaging app. I increased the Telegram icon as much as possible and centered it on the screen. I even opened the dialog with myself there so that she could easily call me with just two clicks.

And... that's it. I'm glad you took the time to read this. I put a lot of effort into this article, so thank you all, and see you next time!👋

But, of course, that wasn't everything I did. In fact, it was just 20% of the work that yielded 80% of the results. But let's delve into the other 80%.

Around that time, I introduced her to a home assistant ([Yandex's smart assistant](https://yandex.ru/alice) - Alisa), and all of a sudden, she started using it quite extensively. This got me thinking, "What if I could chat with my grandma through this device in some way?"

I personally prefer texting; sending a simple message is 10 times easier and faster than making a call. Plus, I might not always be available when my grandma wants to call, but I can respond to her messages within minutes whenever I have the time.

In conclusion, this idea led me to connect the home assistant (Alisa) with Telegram

## System design
Why did I even think it was feasible to implement this in a timely manner? Well, I had no intention of starting from scratch using any programming language and APIs.

No, no, no... "no-code" is my go-to solution in this case.
![gif 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/35ie24l9eo7ei90wd6nn.gif)
(low code actually, but who cares)

At that time, I worked at a company where we were developing a low-code platform for chat-bots, and this problem presented itself as the perfect use case to put my skills to the test.

So, after a few iterations, I came up with this “design”.

![high level system design](/chatbot-for-grandma/final-arch.png)
Each Alisa icon and Telegram icon represents a separate chat-bot.

I opted to use two different chat-bots for Alisa to ensure that I don't have any NLP logic embedded within my chat-bot scenario. Instead, I've dedicated the NLP logic to the higher level within the Alisa framework, rather than incorporating it directly into the chat-bot.

But what does this mean? If I had included NLP logic within my chat-bot, let's call it an app, I would receive plain text messages from my grandma and then route her questions or requests to the appropriate state, handler, or section of my chat-bot's code.

![monolith chat-bot](/chatbot-for-grandma/option-1.png)
Instead, I rely on Alisa's built-in NLP capability, and when my chat-bot is activated, it signifies that the correct request from my grandma has been successfully recognized. In other words, the right chat-bot wouldn't even be triggered otherwise.


![separated chat-bots](/chatbot-for-grandma/option-2.png)
I use Google Sheets as a simple message queue (chosen mainly for its technical convenience). The Telegram bot writes to Google Sheets, and the `Alisa reading bot` retrieves messages from there.

The `Alisa writing bot` can communicate directly with the Telegram bot through the platform.

The happy path is quite straightforward, actually.

Here's how it goes: My grandma calls the Alisa chat-bot to send me a message. I received the message in Telegram and responded to her. My response is sent to Google Sheets. Then, my grandma can occasionally call the other Alisa chat-bot to read from Google Sheets. If there are any messages for her, they'll be voiced and then removed from Google Sheets.

Pretty clear, isn't it?
![gif 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q37g9i93qdk1h90z7lzh.gif)
> The most exciting thing is that I managed to implement this idea in just one weekend.

The only minor disappointment was that I couldn't add a notification feature in Alisa (home assistant) to alert my grandma when she received a response from me. It seemed there was no way to send such notifications to the home assistant.

## JAICP intro
Let's delve a bit deeper, and here's a brief introduction to the platform I built upon.

[JAICP](https://app.jaicp.com/) is a cloud-based, low-code platform where you can create your chat-bot using a custom DSL mixed with JavaScript code. The DSL defines the structure of the chat-bots, while JavaScript empowers your bots with intelligence.

If you're interested, you can find more information in the [documentation](https://help.just-ai.com/docs/en/). There's tons of useful information covering all the functionalities the platform offers.

What's particularly great in our case is that hosting costs us practically nothing. We'll have exactly one user for each chat-bot, and with such minimal traffic, it won't cost any expenses.

## Implementation
We're going to dive deep into the codebase with detailed line-by-line explanations. If this isn't your cup of tea, feel free to skip this part.

Of course, you can find all the code on [GitHub](https://github.com/DaniilRoman/babushka-chat-bot).

> Naturally, we have to create our bots on the Telegram and Alisa side first in order to get tokens. I won't cover how to configure everything, instead, I will focus only on chat-bots coding part

Let’s have a closer look at Alisa’s bots as they’re more finely-grained compared to the Telegram bot.

Below you’ll find all the code for the `writing Alisa bot` and yes, it's just 14 lines of code.

```js
theme: /

    state: BabushkaSay
        q!: $regex</start>
        a: What would you like to text to Daniil?

    state: NoMatch
        event!: noMatch
        script:
            var toSendRightNowTime = "2022-07-02T10:00:00";
            $pushgate.createEvent(toSendRightNowTime, "SetBabushkaData", 
                    {"sayData": $request.query}, 
                    "telegram",
                    $secrets.get("TLGRM_BOT_ID"),
                    $secrets.get("TLGRM_USER_ID"));
        a: Message was sent 
```


As I mentioned earlier, I don't include any NLP logic within my chat-bots. This means that when my grandma says, "Alisa, text a message to Daniil," Alisa is responsible for recognition. I only receive the `start command` on the 4th line and respond with `What would you like to text to Daniil?` on the next line.

To retrieve all the text my grandma said, I make use of the system variable **`$request.query`**.

Additionally, **`$pushgate.createEvent`** comes in handy here, allowing us to send the event directly to the Telegram chat-bot. You can find more information about this method in the **[docs](https://help.just-ai.com/docs/en/JS_API/built_in_services/pushgate/createEvent)**.

> There is some configuration happening behind the scenes, but in general, there are only 14 lines of code that handle the task quite effectively.

It's almost the same for the `reading Alisa's bot`.

```js
theme: /

    state: BabushkaSay
        q!: $regex</start>
        script:
            var danilAnswers = $integration.googleSheets.readDataFromCells(
                $secrets.get("INTEGRATION_ID"),
                $secrets.get("SPREADSHEET_ID"),
                "List1",
                ["A1"]
            );
        
            if (danilAnswers.length === 0) {
                $reactions.answer("Danil haven't had time to respond yet");
            } else {
                $reactions.answer("Danil is talking");
                var answers = danilAnswers[0]["value"];
                $reactions.answer(answers)

								$integration.googleSheets.writeDataToCells(
		                $secrets.get("INTEGRATION_ID"),
		                $secrets.get("SPREADSHEET_ID"),
		                "List1",
		                [{value s: [""], cell: "A1"}]
		            );
            }
        

    state: GoogleSheetError
        a: Couldn't get the data, call to Danil
```

1. We read from Google Sheets
2. If there's anything in Google Sheets, we send a response to Alisa to speak.
3. Clear the data in Google Sheets

`$integration.googleSheets` provides functionality to read and write to Google Sheets (probably it’s quite obvious)

And `$reactions.answer` is used to send a message to the connected channel, which in our case is Alisa.

Here, we do have a few more lines of code, but everything remains at a high level and is quite readable, which is great.

## Feedback
So, what happened next you might ask?
Let's recall that my granny was already a “strong” Telegram user at that point. I was excited to introduce her to my project, but before anything else, I had to sell her on the idea, to convince her to give it a try.
I spent just one weekend to implement that and all my emotions were absolutely fresh.

On the day "X", I traveled from another city to visit her. I talked to my grandma about Telegram and the Alisa home assistant to know her thoughts about new stuff. And then, I presented her with this chat-bot and the new way to chat with me anytime.

When I showed my grandma what I had created, I was bursting with pride and eagerly anticipated how she would use it. However, reality hit hard – she refused to use it because she found it too difficult.

The end.

![the end picture](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/919bv91sqf6pdy503uq9.jpg)
There were two main reasons actually:

1. The chat-bot cold start
   The platform functions much like any other lambda or serverless function, and it experiences a cold start like any other.
   While this might not be a significant issue with a high volume of users who use the chat-bot frequently (as it would always be cached), or if it were a text-based chat-bot like the ones on Telegram. However, it presented a challenge in our case.
   With only one user and a voice-based chat-bot, there were occasions when the chat-bot took too long to start for my grandma. She became confused when she didn't receive any responses from Alisa and eventually gave up. There were even times when the bot responded with a timeout error, which was a frustrating experience for her. She doesn’t have the mindset that if something didn't work initially, it could be retried or restarted. From her perspective, if something didn't work, it was broken beyond repair.

2. The Alisa’s bots voice UX
   To activate an Alisa bot, you have to say something like "Alisa, enable bot XXX." Then, you have to wait for a moment to receive a response from the chat-bot itself (this is where the chat-bot's cold start occurs). In my case, the chat-bot responds with "What do you want to send to Daniil?" as a welcome phrase. Only after this, my grandma can send the message to me.
   This process involved several steps for her, and it was a longer and more complicated journey compared to simply making a phone call.

## What could be next steps for this chat-bot system?

So, in the end, we received feedback from customers, and it appears there's no real demand for this product 😅
Or, to put it another way, my grandma simply said she's not going to use this darn thing 🙃

**But what could we potentially do to improve the situation if our MVP was to be successful?**

Resolving the cold start issue is a fairly manageable task. It would, of course, require writing more code to integrate everything and creating and deploying my own service, which would need to be available 24/7 (perhaps even a very lightweight lambda function in the cloud could suffice). However, the outcome would be a straightforward service where I could store everything, possibly even locally, and seamlessly route messages between Alisa and Telegram, ensuring a smoother user experience.

The second issue is a bit trickier. We have to react to the `/start` event in any case, even if we don't respond with anything, and only then we can receive the text to send to Telegram.

This means we cannot eliminate the first step entirely and be ready to receive the text as soon as my grandma begins speaking.

We could make an assumption that as soon as the skill is enabled, we are ready to accept text to send because there's almost no cold start. This would eliminate the need to send any response for the **`/start`** event to notify my grandma. However, it's important to note that this can only be an assumption and not a strict rule. By making this assumption, there's a potential risk of losing some data.

Nevertheless, there are ways to address this problem and make this idea accessible even for my elderly grandmother.

## What actually happened next, you may wonder?
The idea of chatting with grandma through chat-bots faded away, and we went back to good old voice calls via Telegram. However, that wasn't the end of the story 🙃

All of a sudden, she was able to call me, but for some reason, she couldn't answer my calls.
So, here's the latest chapter about how I communicate with grandma over the Internet.

As you might recall, I only have two options: 1 - Telegram and 2 - Alisa home assistant. If Telegram didn't work out, it was time to explore all available options to work with the home assistant, excluding a custom chat-bot.

And there was one option that came to light. I discovered that I could call the home assistant directly through a special messenger designed specifically for this home assistant. You can't call anyone through the home assistant, but you can answer a call and talk through the home assistant, which was quite remarkable. It was something I couldn't even have imagined before.

> A quick reminder: The options available to you are, of course, strictly dependent on the ecosystem you are using.

## Conclusion
So, in the end, we didn't end up using those chat-bots; we simply call each other. She calls through Telegram, and I call her back through the special messenger, and she answers the call by using the home assistant. This setup still works perfectly for us 😄

Even though the chat-bot idea didn't work out as expected, it was an incredibly interesting and educational journey. I gained hands-on experience in creating and validating a quick MVP. I highly recommend this to everyone, especially software developers. Finding your own ideas, creating, and validating end-to-end MVPs can give you tons of insights about product development in general.

In my case, I understood how crucial UX (User Experience) is and how a cold start can vanish all your efforts.

So, as a final word, I’d like to remind you of a simple and hopefully well-known thought: All aspects of software development are equally important!

And don’t forget to call your grandma 😄