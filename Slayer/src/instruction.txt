

The execution of the tool is divided in three parts. Clustering, Training and Test phase.
Clustering and Training need to be executed only once. Test can be executed on the files that the user want to be classified by the tool.

FIRST RUN

Here are the steps that you first have to do when using this software. This can be executed only once and directly replace the "clustering" and "classifier" folders with the ones inside the "premade" one.

You have to own a number of malicious and benign files. Then, you have to put them in the "malicious" and "benign" folder respectively (NOT in other folders).
After that, launch:

python slayer.py cluster

and wait for the process to be finished. A file called "keyword" should have been generated in the "clustering" folder. Then:

python slayer.py train

and wait for the process to be finished. A file called "classifier.p" should have been generated in the "classifier" folder.


TEST PHASE (NORMAL USAGE)

In order to test PDF files, just put them in the "test folder" and run:

python slayer.py test

Or you can also use another folder with the command:

python slayer -f [YOURFOLDER] test

OTHER OPTIONS

You can also enable debug mode with the flag -d True.