# Projects in Data Science (2025)

Mandatory Assignment



#### Overview

This is a template repository of the mandatory assignment of "Projects in Data Science". You should refer to this repository in your mid-term hand-in.

If using github.itu.dk, you need to download the repository and make your own. 

If you are using general Github, you can clone or fork the repository directly. If your usernames do not give sufficient hints as to who you are, you can tell the TAs how to match them. 

Your repository MUST be named 2025-FYP-groupXX where XX is your group number. 

Look at the slides of the previous two weeks for details of the hand-in. 



#### Python environment

Follow TA instructions when setting up the Python environment before running any code. Remember to export your Python library requirements by `pip freeze > requirements.txt` and attach it to the repo so we can evaluate your scripts.



#### File Hierarchy

The file hierarchy of your hand-in repo should be as follows:

```
2025-FYP/
├── data/
│   └── example.jpg
├── result/
│   ├── __init__.py
│   ├── img_util.py
│   └── inpaint.py
├── util/
├── main.py
└── README.md
```



**Notes:**

1. DO NOT upload your data (images) to Github.
2. When the same code block needs to be executed multiple times in the script, make it a custom function instead. All the custom functions and modules, such as image read and write, should be grouped into different files under the *"util"* subfolder, based on the task they are designed for. Do not put everything in a single Python file or copy-paste the same code block across the script.
3. The "dataset.csv" lists all the image files along with a group ID, you should be only using the files assigned to your group. Your code must load the entire dataset and then filter the files based on your group ID. Ask TAs for help if you don't know how to do that.







