# Markov Learner

This script uses Markov chains to learn how to post. Using a user-specified board,
this script trains a Markov chain on all posts on all pages of said board and generates
post on command. Also includes a random image from the same board. This doesn't
actually post to 4chan.

This makes extensive use of 4chan's read-only JSON API.

# Dependencies

* Python 3
* PyMarkovChain
* urllib

# How to Use

0. Install the required dependencies if you don't already have them.
1. Run `./shitposter.py`.
2. Enter a board to train on - ex. /a/, /b/, /co/, /tv/, etc.
3. Once training is finished, hit enter to generate a post.

The command `train` will re-train the Markov chain on the same board.

The command `board <board>` will switch to the specified board.

The command `exit` will exit the script.

# Credits
* [ChangedNameTo](https://github.com/ChangedNameTo) - Image-grabbing
* [franzwr](https://github.com/franzwr) - Data pickling
* [Tim La Roche](https://github.com/timlaroche) - Python 3 support
