# URL-splitter
A Python script to create multiple URL feeds

## Introduction
For context, [Nitter](https://github.com/zedeus/nitter) is an alternative, lightweight frontend for X/Twitter that is focused on privacy. In the years since its introduction, there hasn't really been a concrete way to use Nitter as a replacement for browsing X/Twitter. There is a feature within Nitter that allows users to browse multiple X/Twitter accounts at once, but its reliance on X/Twitter's own search functions means that attempting to combine too many handles will go over the character limit and prevent the page from loading.

This is where URL-splitter comes in. Using Python, I've created a script that, when provided with a list of handles, will automatically create a set of URLs that can be browsed individually without fear of the page failing to load due to an overabundance of characters. The only requirement is that the user must provide a plaintext list of all the handles they wish to keep track of themselves.

Unfortunately, the volatile state of X/Twitter's API and general website design means that browsing feeds through Nitter is not guaranteed to work on every instance which hosts it. The [list of instances](https://github.com/zedeus/nitter/wiki/Instances) on Nitter's GitHub wiki can be used to locate up-to-date instances that nitter-splitter can be used in conjunction with.

## Usage
All of the code used to create the list of URL feeds is located within the `URL_splitter` function. It is recommended that you edit the function call within the `main` function to tailor the script to your preference:
- Replace `handles.txt` with the filepath of the plaintext file in which the handles are located.
- Replace `\n` with the delimiter that will split the handles into a list. By default, the script will split the handles based on newlines.
- Replace `20` with the number of handles that each URL will contain. The page will fail to load if there are too many handles in one URL, so it may be necessary to run the script with different numbers to receive a list of URLs that all work correctly.
- Replace `,` with the delimiter that will separate the handles in the URLs once they are created. It is recommended that you leave this as-is, since handles in Nitter multis are split by commas.

After it runs, the script will print a list of URLs based on the preferences provided in the function call.
