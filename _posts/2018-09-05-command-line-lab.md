---
title: "Lab 1: Using the Command Line"
layout: lab
categories: assignment
published: true
due: 2018-09-10
permalink: /labs/1
---

As a student of computing, you're going to have to spend a lot of time
using computers. Computers have great interfaces these days, but
programmers still spend a surprising amount of time interacting with
text-based interfaces to their machines.

In this lab, I'd like you to play around with the command line a
bit. First, I'd like you to read [the following
guide](https://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything). Read
it up until (but not including) the section on "Looping Over a Set of
Files."

### Lab Assignment

- Open a web browser with an email addressed to me, titled `<your
  name>'s Lab 1`. Start filling out the questions as I ask you to do
  them.

- Start inside your home directory (if you are not there, type `cd ~`,
  the perhaps-confusing name `~` is an alias to your home directory).

- Create a directory `lab1` via `mkdir lab1`

- Navigate into that directory `cd lab1`

- The command `touch <filename>` "touches" a file. Every file has a
  "timestamp" showing when it was create, modified, etc.. Touching a
  file updates this timestamp. If the file does not yet exist, `touch
  <filename>` creates an empty file of the specified name.

- Run `touch hello`.

- Now run `stat hello`. This asks the computer to tell you some
  statistics about the file, including its size, when it was created,
  etc.. 

- Copy and paste the output of the command in your email to me.

- Google a little bit about how stat works. Figure out how to make it
  print the time the file was last modified.

- Now run `touch hello` again, followed by `stat hello`. What changed?
  And why?

- Open any editor on your computer and create a file named `text.txt`
  inside of the `lab1` folder. Put a few lines of text in the file,
  really anything you want. This can be any editor: GEdit if you're on
  linux, TextEdit if you're on mac, or `nano`, `emacs`, or `vim` if
  you're used to using one of those.

- Now type `cat text.txt`, which shows the contents of the file.

- Now type `cat text.txt text.txt`. `cat` accepts multiple arguments.

- Now type `cat >text.txt`. Be prepared: the command won't
  terminate. It will allow you to keep typing until you type the
  character to stop typing (Control-D on most machines) and kill the
  program, and will write that into the file.

- Type a few lines, and then hit Control-D.

- Now cat the file again.

- Copy the file `text.txt` to the parent directory: `cp text.txt ..`
  (equivalently, you could have done `cp text.txt ../text.txt`).

- Now--without changing the directory--use cat to print the file to
  the screen. Tell me what command you used to do that.

- Now change the directory to the parent directory: `cd ..`.

- This should be your home directory. Print the working directory by
  using the `pwd` command (print working directory).

- Now remove the folder and the file: `rm -r -i lab1`. Note that the
  `-r` option means "recursive" (i.e., delete directories, not just
  files), and the `-i` option means "interactive" (i.e., ask before
  deleting any files). If you want, you could have typed in `rm -ri
  lab1`. Often, when there are multiple flags you can pass to
  programs, you can pass multiple at once by simply putting them
  together (this is not always true, but it is for "core utilies" like
  `rm`).

- Now also remove the copied `text.txt` by doing `rm text.txt`.

- To complete your email to me, answer the following questions:
  - What scares you the most about using the command line?
  - Name the most interesting / useful thing you learned in this lab
  - Is there any situation in which you'd rather use the command line
    rather than a visual user-interface?

- Send your email to me and I'll put you down with a 100% within a
  week.
