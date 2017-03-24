# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > `pwd` - show current directory path  
> > `mkdir` - create a directory  
> > `rmdir` - delete a directory  
> > `touch filename.extension` - create empty file "filename"  
> > `rm` - delete a file  
> > `mv newname oldname` - moving a file effectively renaming it  
> > `ls` - list files  
> > `cp` - copy a file  
> > `find . -name '*.txt' -print` - find all files ending in .txt change extension or * content to search for specific files  
> > `cat filename.txt` - creates a text file and allows for instant editing from command line - q to exit  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` - list files  
> > `ls -a` - list all files  
> > `ls -l` - list files long format  
> > `ls -lh` list files long format human readable  
> > `ls -lah` list all files long format human readable  
> > `ls -t` list files sorted by time  
> > `ls -Glp` list files long format, no grouping, and indicator appended to directories   

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -c` - lists with timestamp  
> > `ls -rt` - displays files in reverse order by time stamp  
> > `ls -R` - displays subdirectories  
> > `ls -1` - displays one entry on each lines  
> > `ls -u` - displays files by access time
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` constructs a command in the command line from standard input.  
> > This allows more control over the output by using "xargs -p" to prompt  
> > to see if they want to continue executing the file, "xargs -d\n" to  
> > read the text literally including all line breaks, "xargs -n ##" to  
> > control how many characters appear per line in a list. Simply typing  
> > "xargs" with create an input space, left by pressing ctrl + d which  
> > results in echo-ing of entered text. xargs can be combined with other  
> > commands such as find to search over/in files and then perform some  
> > action on those files that fit the criteria  
> >  
> > For example: `$ find . -name "*.txt" | xargs rm -rf` will remove all  
> > text files from the current directory.

 

