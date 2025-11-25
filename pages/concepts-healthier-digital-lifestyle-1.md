---
layout: default
title: "Screen Nutrition: Part I"
original_url: "/concepts/healthier-digital-lifestyle-1"
permalink: /concepts/healthier-digital-lifestyle-1/
---

### An Information Void

At Screen Nutrition, it is our belief that most people will make good decisions when empowered with timely and relevant information. Regrettably, when it comes to the type and magnitude of online content one should consume, such information is almost entirely absent.

Like the absence of clocks or natural light in a casino, the absence of this information is no accident. Social media platforms and even some content creators aim to maximize the amount of time a user spends entrapped on their site/content, which leads them to either directly/indirectly encourage users to develop harmful habits like doomscrolling and powerful addictions to the platform/content through cheap dopamine. The machine learning powered, carefully curated visuals, notifications, and misinformation mesmerize and entice users into acting irrationally and against their own best interests.

### What Information is Needed?

The question now becomes about what kinds of information would help someone make a good, informed decision about what they view or how much time they spend.

It comes down to two parts: knowing something about the content you are about to consume, and knowing something about yourself.

Through the development of Digital Nutrition Labels and the Screen Nutrition Connect platform, we are addressing the first half of the problem. With the concept of Digital Metabolism Index (DMI), as a digital twin of the Basal Metabolism Index (BMI), we are addressing the second part of the puzzle. In this article, we’ll present an overview of each of the above, including the criteria for a successful design as well as a proposal on what such a design could be.

## The Digital Nutrition Label

The goal of a digital nutrition label is to inform a user about the amounts of *digital nutrients* expected to be present in a given piece of content.

It is useful to draw a parallel with a typical food nutrition facts label. The four main nutrient categories for food are carbohydrates, fats, proteins and vitamins & minerals. There is further subclassification within some of these macro categories. For example, micronutrients, which are different kinds of vitamins & minerals. There is also a notion of a recommended *daily value* and a percent of said value that the *serving size* meets. The advantage of drawing inspiration from the nutrition facts label is that these labels are familiar to and typically well understood by the consumer, and any transfer learning we could take advantage of would heavily simplify the task of learning a foreign concept.

What are the corresponding digital twins of these concepts?

Before we dive into the answer to this question, let’s lay out some broader guidelines for what makes a good digital nutrition label.

### Label Design Guiding Principles

**Content-specific**: Just like the food nutrition label, we want the digital nutrition label to depend solely on the content being labeled. In other words, the label is not something personalized to each user. The initial separation of information into something about the content (label) and something about the user (personalization), helps with maintaining this discipline. This guideline allows labels to be crowd-sourced (via the Screen Nutrition Connect Platform), along the lines of Common Sense Media, and also allows for a comparatively large amount of effort to be invested in the creation of the label, for example, using a machine learning labeling algorithm, because a label once created can be reused across users.

**Automatable**: Unlike food items, the number of digital content pieces might be 4-8 orders of magnitude greater. As such, labeling the universe of content manually is infeasible. Though manual labeling as a means of getting started and allowing research into the efficacy of the ideas of digital nutrition may be useful, eventually we envision the large majority of labels to be auto-generated, with perhaps a human in the loop remediation process.

**Intelligible**: The components of the nutrition label need to make intuitive sense to the user, enabling them to reason about balance, nutrition and good habits on the basis of such labels. The bar here isn't just about classifying content into “nutrition groups” but also to ensuring that the nutritional information is easily digestible and not overwhelming due to the label's numerous dimensions.

**Machine-friendly**: We also want to take the opportunity to ensure that the labels we apply to content can be easily discovered, identified, parsed, and processed by computers. We envision the screen equivalent of a calorie counter — perhaps a tool that helps users accumulate the amount of each digital nutrient they have consumed during a given interval.

**Starting simple**: Finally, one point of departure from the food nutrition label. We need to start simple. The food nutrition label has evolved over several decades to get to its current form, with dozens of nutrients and micronutrients listed with daily values and other details. To some extent, the label has co-evolved with its users. For the digital label, it is important to start simple and create an idea that spreads, due to its simplicity and utility. Trading off simplicity for enhanced utility isn’t advisable during the initial phases of adoption of such labels. We expect over time, with the benefit of primary research, user feedback, and technology evolution, we will co-evolve the label alongside its user population.

### The Digital Nutrients

Armed with the guiding principles above, we are now ready to explore the answer to the question we posed before:

What are the corresponding digital twins of nutrients in a nutrition label?

For our first foray, we conducted a limited set of user inquiries — essentially Screen Nutrition volunteers, friends and family. Here is what seems to ring true with this limited user set. At the risk of oversimplification, we propose just three digital nutrient groups: carbohydrates, protein and vitamins. In addition, for each piece of content we provide an aggregate “digital calories” value.

#### Digital Calories

The most prominent information on a nutrition label is the overall calorific value of a serving. For digital labels, we do away with the notion of a serving; and instead the label represents the nutritional values of the entirety of the content being labeled.

We believe that the most natural equivalent of calories in the digital world is simply the amount of expected time it would take a user to consume the content. Video content already comes labeled with length. Many content portals (for example medium.com) also already label their content with the anticipated amount of time an average user would take to consume it (e.g. “5 min read”).

Identifying the time required to consume an image can be challenging. We expect a simple treatment of this, perhaps based on complexity of the image or presence of text within the image. For instance, many instagram posts appear to carry text within the images.

#### Digital Carbohydrates

We believe that content that can be broadly classified as entertainment, closely fits the notion of a carbohydrate. In the food world, carbohydrates are often tasty, easy to consume, easy to over consume, have short term energy benefits, could be an impediment to health, and contribute to obesity if routinely over consumed. These attributes transfer readily to entertainment content in the digital domain.

Note that it is not to say that carbohydrates or entertainment serve no useful value. On the contrary, a digital diet devoid of entertainment may not be considered balanced either. A healthy mind needs some level of entertainment and stimulation, just as a healthy body needs carbohydrates. However, balance and moderation are key, and discipline and awareness are needed to avoid falling prey to overconsumption.

What kind of activities would we consider entertainment? Broadly speaking, this category contains things like watching movies, TV shows, streaming media, short-form videos, gaming, entertainment through podcasts and audio content and visual graphics and text content.

#### Digital Proteins

Next, let's look at content that could qualify as proteins. One again, in the food world, proteins are responsible for strong musculature, growth, definition and maintenance of the body. What would be responsible for a strong mind, mental growth, and maintenance of acuity? We believe the answer here is content that helps us learn and grow. Additionally, we can also include content that helps us satiate our natural curiosity, since curiosity is a precursor to learning and growth.

Just like with proteins, it is possible to over consume the digital proteins - learning and growth content as well. And the keyword is balance, once again.

What kind of activities would fall into this category? For starters: khanacademy, self-training/how-to videos, documentaries, nonfiction reading, remote school/lectures and so on.

#### Digital Vitamins

Finally, the third nutrient of our digital diet is what we call vitamins. In the food world, vitamins are micronutrients. We don’t require a large quantity of them — often just a few milligrams or grams — but they have a profound impact on our health.

The youth population is currently in the midst of a mental health crisis of epidemic proportions. Fortunately, there is very effective mindfulness content now available in mobile apps and websites, that is making a positive difference in this fight. We believe that just like vitamins, mindfulness and self-help or self-improvement content can go a long way in improving mental health, even when practiced or consumed sparingly in the digital diet.

#### Emotional Intensity

As countless studies have established, the content we consume has a deep emotional impact. A digital nutrition label will be remiss without capturing some notion of the emotional intensity and direction of the content it labels. Being able to look ahead of time, what sort of emotional impact we can expect from consuming a piece of content, can be a critical discriminant in seeking or avoiding certain emotions in our digital diet.

Fortunately, such emotion analysis is within the reach of modern day machine learning algorithms. [reference]. At Screen Nutrition, we have been further researching automated ways of identifying not just what emotional impact the content might have, but also to identify what emotions are absent from a given content. This latter analysis is crucial to being able to actively weed out detrimental/intense emotions such as hate speech and hopelessness.

#### What about everything else?

We have erred on the side of keeping the initial digital nutrition label drastically simple. A consequence of this is that there will be some nuances that are lost. Is all entertainment created equal? For example, is there a difference between a user watching a violent movie vs. a movie with positive social messages? Is there a difference between compulsive behaviors such as doom scrolling or mindless chasing of notifications and likes, vs deliberate behavior? There are certainly differences in these examples. We debated introducing a fourth category, “digital fats”, to capture at least some of the differences, and relegate some of the more self-sabotaging behaviors to the category of digital fats. However, we felt that the distinction can easily be subjective, and could be tantamount to imposing one sense of morality and values on everyone, which runs counter to our beliefs.

#### Putting it all together

Now that we have the digital nutrients identified, how does a digital nutrient label look? And what does a user do with it?

A sample digital nutrition label, incorporating the four dimensions of nutrients is shown in the figure. In this first rendition, the label is modeled after a typical food nutrition label, and supports adding more detail within each nutrient category (some examples are shown).

1. For each nutrient category, we label a percentage, as opposed to an absolute quantity. This percentage represents the proportion of the content that can be attributed to this nutrient class.

2. We expect a piece of content, in general, to contain ingredients in more than one nutrient class. For instance, a given video could be educational as well as entertaining.

3. The three macronutrients should to add up to 100%. We remain open to the possibility of unclassified or unclassifiable portions of the content, and don’t require the label proportions to add up to 100%.

#### Digital Nutrition Tags

While the detailed nutrition label, patterned after the food label, is useful to understand the full detail of information available, it is not reasonable for the user to spend considerable time studying the nutrition label. This is especially true now, where the average duration of consumption of digital content is decreasing, with the rise of short-form content: tweets, messages, notifications, TikTok, Instagram reels, YouTube shorts, and so on.

What we also need is nutrition information that can be consumed at a glance. To that end, we propose a simple tag cloud style rendering of the key nutrients of the digital label. It could look something like this.

#### Calorie Counters: Automated Accumulators

A typical user may consume hundreds to thousands of digital content items in a single day. We envision a calorie counter that will aggregate the consumption so far, and let the user gain a better understanding of their consumption habits as well as their digital nutritional balance. We’ll talk in greater detail about the notion of daily balance in the 2nd part of this article.
