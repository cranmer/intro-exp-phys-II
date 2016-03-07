# Intro to Exp Phys II

* Kyle Cranmer 


This is a GitHub repository to accompany Intro to Exp Phys II. Click on the notebooks.
Sometimes the math in the notebooks doesn't display well in GitHub... and it doesn't work on many mobile phones.
Instead you can look at it with [nbviewer](http://nbviewer.jupyter.org/). Here are some links for convenience:
   * http://nbviewer.jupyter.org/github/cranmer/intro-exp-phys-II/blob/master/change-of-variables.ipynb
   * http://nbviewer.jupyter.org/github/cranmer/intro-exp-phys-II/blob/master/change-of-variables.ipynb
   * http://nbviewer.jupyter.org/github/cranmer/intro-exp-phys-II/blob/master/lecture1-in-class-demo.ipynb

   
Run the notebooks from within your browser without installing anything thanks to [Binder](http://mybinder.org)

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/cranmer/intro-exp-phys-II)


## working with GitHub

1. Fork this repository by clicking on "Fork" button above
1. Clone your fork of the repository to your computer (find repository in your GitHub user profile, and clone it from there)

If there are updates that you want to get:
1. check if your repository is in a clean state with `git status`. 
1. If it is not, you will need to clean it up (more info below)
1. If it is, then make sure you are on your `master` branch with `git branch`. 
If you aren't you need to check it out with `git checkout master`
Now you are ready to update:
```
git fetch cranmer master
git merge cranmer/master
```

Now you should have the up-to-date repository.


1. On your computer you should make a new branch if you want to play aroud
```
git branch play
git checkout play
```
now you can make changes without conflicting with the `master` branch.
To save your changes 

Tutorials:

https://guides.github.com/activities/hello-world/

https://guides.github.com/introduction/flow

https://guides.github.com/activities/forking/
