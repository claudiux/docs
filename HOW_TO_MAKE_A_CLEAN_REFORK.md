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

  `apt install git`

### Make a local clone

```
mkdir -p ~/git/csa
cd ~/git/csa
git clone -b master --single-branch https://github.com/your_github_id/cinnamon-spices-applets master
cd master
git config --global user.name "your_github_id"
git config --global user.email "your@email"
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

Execute the following commands (you can create a script named `refork-csa.sh` containing them):

```
cd ~/git/csa/master
git fetch upstream
git pull upstream master
git push -f origin HEAD
```

You must enter your GitHub id, then your GitHub password.

Then, go to your own repository; the master branch is now up to date!

**Do not forget: Never work directly in ~/git/csa/master! You must never change this folder yourself!**

### To propose code or translation

Supposing you want to propose the Dutch translation (for example) of the Spices Update applet messages.

Open https://github.com/your_github_id/cinnamon-spices-applets.

Create a branch from master named SpicesUpdate-nl.

On your computer:

```
cd ~/git/
git clone -b SpicesUpdate-nl --single-branch https://github.com/your_github_id/cinnamon-spices-applets SpicesUpdate-nl
```

A `SpicesUpdate-nl` folder is created, containing your branch.

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

Open https://github.com/your_github_id/cinnamon-spices-applets.git and click on `Compare and pull request`. Comment and validate your pull request.

Some hours or days later, your pull request (PR) is accepted (merged) or rejected by the linuxmint/cinnamon-spices-applets team.

You can complete or modify your file(s) with `git add ...`, `git commit -m "..."` and `git push ...` while your PR is not merged into the master branch of linuxmint/cinnamon-spices-applets.

Once merged, you can delete your own SpicesUpdate-nl branch on GitHub.
