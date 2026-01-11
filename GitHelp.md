# Github Commands

## To get help   
>git help config
>man git-restore  
>git restore --help  

## To set the name and email in git configuration
>git config --global user.name myName  
>git config --global user.email myEmail

## To check the name, email (any specific key) in git configuration
>git config --global user.name   
>git config --global user.email

## To check more config details
>git config --list

## To set default code editor for git
>git config --global code.editor "path to the executable of editor"

## To set default branch name during git init
>git config --global init.defaultBranch newName

## To open Vs code using git 
>code .

## To initialize an empty git repository 
> git init

## To see the hidden folders 
> ls -lart

## To see if file's status and stages 
> git status
Stages of file - [Untracked(??), Unmodified, Modified(M), Staged(A)]

## To see compactly (symbols with filenames) 
> git status -s  
### initial 2 symbols represents 2 columns
left col : staging area  
right col : working directory   

<code>M- f1.py // modified and staged     </code>  
<code>-M f2.py // modified but not staged  </code>  
<code>MM f3.py // modified, staged & again modified but not staged </code>    
<code>A- f4.py // staged  </code>  
<code>?? f5.py // untracked file</code>

## To track / stage a file 
> git add filename.extension
## To track / stage all files at once 
> git add -A

## To commit a file and write commit message 
> git commit
   #### vim editor : To write into the file -> press i & write the commit message
   #### vim editor : To exit the editor -> press Esc & write :wq and then enter

## Short hand to commit file with message 
> git commit -m "Commit message"

## To see all the commits 
>  git log

## To see few commits 
> git log -p -3          [enter q to exit log]

## Compare working tree/directory with staging area (difference) 
> git diff  

show content that is changed but not staged

## Compare staging area with last commit 
> git diff --staged   

OR  
> git diff --cached      

show content that is modified after last commit

## To create a blank file 
> touch filename.extension

## To create a new branch 
> git branch feature1
## To see the current branch 
> git branch
## To enter a branch 
> git checkout feature1
## To merge a branch into master branch 
> git merge master

## To remove a file from directory and staging area both 
> git rm file.extension
## To remove a file from staging area only (untrack again)
> git rm --cached file.extension  
> 
Note - If git keyword is not used, fill will be removed but deletion is not staged so deleted file has to be staged exclusively

---
## To push public local repository from computer to github repository :-
>### create a origin url of repo :
     >> git remote add origin http....Repo.git  
>### to know the origin :
     >> git remote
>#### to see the url link of repo linked :
     >> git remote -v
>### to push the local directory to github :
     >> git push origin master
>### to push the local directory to github :
     >> git push -u origin master
>### to change the origin url :
     >> git remote set-url origin https...
>### to push a branch :
     >> git push origin branch_name


## To push private local repository from computer to github repository :-
#### create a repo and change it's url to ssh on github

>### create origin url of repo in git 
>> git remote origin ssh...link
>### to see the origin 
>> git remote
>### to see the url 
>> git remote -v
>### to push the master branch to remote repo 
>> git push origin master
     ## Error - Private repository : Take access to computer for read & write
>### goto ssh & gpg keys at repo setting on github
>### generate a ssh key 
>> ssh-keygen -t ed25519 -C 'your_email@example.com'
>### get the agent process id 
>> eval $(ssh-agent -s)
>### link the ssh key 
>>  ssh-add ~/.ssh/id_ed25519
>### get the ssh key on bash 
>> cat ~/.ssh/id_ed25519.pub
>### copy the key and paste it on github ssh key to add the key to github acc
>### Now you can push the master to origin 
>> git push origin master

  ## To clone a repository 
  > git clone repository.link...
  
## To prevent file from getting tracked, create .gitignore file and put the name of files in .gitignore file  (pattern matching is allowed)

> cat .gitignore

> *.bin              
Note - ignores file ending with .bin

## To rename a file in git 
> git mv fileFrom fileTo


## UNDO the actions -
### To modify last commit, make changes and run 
> git commit --amend 

### To unstage a staged file 
> git reset HEAD filename

OR after v2.23           
> git restore --staged filename

### To undo a modification file (discard changed in working directory) 
> git restore filename
