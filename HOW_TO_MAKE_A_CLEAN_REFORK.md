# How to make a clean refork before proposing code

## Summary

You have forked a GitHub repository into your own GitHub account. But your fork is now too old and you should want to refork the master branch of this repository without destroying all the branches you have created.

## Example

For example, you have forked the _linuxmint/cinnamon-spices-applets_ repository (https://github.com/linuxmint/cinnamon-spices-applets).

This fork is at https://github.com/**your_github_id**/cinnamon-spices-applets.

Before to propose your code (or translation, or any kind of file) to the cinnamon-spices-applets team, you should have in your own repository the latest version of the master branch of linuxmint/cinnamon-spices-applets.

## Step by step

### Install git

Execute into a terminal:
  `apt update`
  `apt install git`

### Make a local clone

```
mkdir -p ~/git/csa
cd ~/git/csa
git clone -b master --single-branch https://github.com/YOUR_GITHUB_ID/cinnamon-spices-applets cinnamon-spices-applets
cd cinnamon-spices-applets
git config --global user.name "YOUR_GITHUB_ID"
git config --global user.email "YOUR@EMAIL"
git remote -v
```

The last command should return:

```
origin	https://github.com/claudiux/cinnamon-spices-applets.git (fetch)
origin	https://github.com/claudiux/cinnamon-spices-applets.git (push)
```

Now, add the linuxmint/cinnamon-spices-applets as upstream:

`git remote add upstream https://github.com/linuxmint/cinnamon-spices-applets.git`

The command `git remote -v` should return now:

```
origin	https://github.com/your_github_id/cinnamon-spices-applets.git (fetch)
origin	https://github.com/your_github_id/cinnamon-spices-applets.git (push)
upstream	https://github.com/linuxmint/cinnamon-spices-applets.git (fetch)
upstream	https://github.com/linuxmint/cinnamon-spices-applets.git (push)
```
### Refork now!

Execute the following commands (you can create a script named `refork-csa` containing them):

```
cd ~/git/csa/cinnamon-spices-applets
git fetch upstream
git pull upstream master
git push -f origin HEAD
```

You must enter your GitHub id, then your GitHub password.

Then, go to your own repository; the master branch is now up to date!

**Do not forget: Never work directly in ~/git/csa/cinnamon-spices-applets! You must never change this folder yourself!**

### Tips
I created a `bin` directory in my home directory to put my own scripts there.
```
mkdir -p ~/bin
```
I added (or uncommented) these lines in my `~/.profile` file:
```
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

```

To take these lines into account: `source ~/.profile`

I created the `~/bin/refork-csa` script, containing:
```
#!/bin/sh
cd ~/git/csa/cinnamon-spices-applets
git fetch upstream
git pull upstream master
git push -f origin HEAD
```
I set this script executable: `chmod +x ~/bin/refork-csa`

Whenever I want to update my fork, I run this script.


### Example of use: Offer code or translation

Supposing you want to propose the Dutch translation (for example) of the Spices Update applet messages.

On your computer, execute the command: 
`refork-csa`

Then, open in your browser: https://github.com/YOUR_GITHUB_ID/cinnamon-spices-applets

Create a branch from master named SpicesUpdate-nl. To do it, click on "master" (scrolling menu) and type "SpicesUpdate-nl", then validate. That's all.

On your computer:

```
cd ~/git/
git clone -b SpicesUpdate-nl --single-branch https://github.com/your_github_id/cinnamon-spices-applets SpicesUpdate-nl
```

A `SpicesUpdate-nl` subfolder is created in your folder `~/git`, containing your branch.

Open with nemo the folder `~/git/SpicesUpdate-nl/SpicesUpdate@claudiux/files/SpicesUpdate@claudiux/po`.

Open with poEdit the SpicesUpdate@claudiux.pot file. Create a new Dutch translation and save it in the nl.po file.

In a terminal:

```
cd ~/git/SpicesUpdate-nl/SpicesUpdate@claudiux/po
git status
git add nl.po
git status
git commit -m "SpicesUpdate@claudiux: Dutch translation. New nl.po file."
git push origin SpicesUpdate-nl
```

Open https://github.com/YOUR_GITHUB_ID/cinnamon-spices-applets.git and click on `Compare and pull request`. Comment and validate your pull request.

Some hours or days later, your pull request (PR) is accepted (merged) or rejected by the linuxmint/cinnamon-spices-applets team.

You can complete or modify your file(s) with `git add ...`, `git commit -m "..."` and `git push origin SpicesUpdate-nl` while your PR is not merged into the master branch of linuxmint/cinnamon-spices-applets.

Once merged, you can delete your SpicesUpdate-nl branch on GitHub and on your computer.
