A few years ago I made a bet with a friend that by 2040 there will be full-feature AI generated movies with quality on par with human-made ones. While I remain confident that at the current rate of progress I will easily win the bet by 2040, I think many principal components for building such an application are already in place and it could be accomplished much sooner. Also it's just a fascinating and challenging thing to build so why not try.


The motivation behind AI movie generation is that it would allow for hyperpersonalized content generation. It has been a childhood dream of mine to be able to see my dream as a movie, and AI movie generation could make it possible. It can also obviously greatly reduce the cost of movie production from where it is now (millions of dollars to make a movie).

There are two downsides to this idea. First (and more immediate one) is that it will put a lot of people out of job and automate yet another artistic pursuit. It especially feels quite important on the backdrop of the current writers strike. I believe AI movies will not completely replace human-made movies, and the latter will retain higher value and a different niche, similar to how handmade goods exists next to mass manufacture, or arthouse movies exist next to blockbuster hollywood. Ultimately, just like with any other technology that increases human productivity, humanity will adapt, new jobs will appear, and the immediate human impact can be mitigated with careful transition measures.

Second concern is a possibility of creating a hedonistic loop, where humans would just plug into a never ending stream of automatically generated tailored entertainment and get completely detached from reality. This one, while less immediate, feels more scary, since movies are already addictive as they are and making them more accessible and more personalized can have a negative impact at society at large. I have no idea what to do with this or how to prevent technology into developing into this, and I think a technology powerful enough to become addictive is still a long time away. So for now, let's rememver about this problem and just build.

Why now? General idea is that many "ingridients" for making an AI-generated movies are already in place. AI can already generate creative stories (chatgpt) and to some degree it is also already possible to generate video content automatically (runway ML).

Building an end-to-end text to movie generation as one model seems to be impossible at this point, however it might be possible to achieve with a pipeline (generate idea -> generate script -> generate detailed scene description -> generate each shot description -> generate shots with runwayml).

okay two things:

first, runway ML is good but as many other models does not do well with complex commands/spacial understanding, so might struggle with generating the scene precisely as instucted

second: script generation. how can we make AI generate fun, interesting scripts?
gonna work on second as my Language Generation research