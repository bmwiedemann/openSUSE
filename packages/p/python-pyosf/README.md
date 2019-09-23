`pyosf` is a pure Python library for simple file sync with Open Science Framework

This package is for simple synchronisation of files from the local file space to the Open Science Framework (OSF). There is a more complex fully-featured sync package by the Center for Open Science,
who created OSF, called [osf-sync](https://github.com/CenterForOpenScience/osf-sync)

The OSF official package is designed for continuous automated synchronisation of many projects (a la Dropbox). We needed something simpler (for combination with PsychoPy). `pyosf` package aims to perform basic search/login/sync operations with single projects on OSF but only when instructed to do so (no continuous sync).

In implementation `pyosf` differs from osf-sync in the following ways:
	* fewer dependencies
	* support for Python2.x
	* no GUI included (yet)
	* local database of files saved as flat json format (no database)
	* simpler handling of sync resolution rules(?)

It can be distributed freely under the MIT license.

[![Build Status](https://travis-ci.org/psychopy/pyosf.svg?branch=master)](https://travis-ci.org/psychopy/pyosf)
[![codecov.io](https://codecov.io/github/psychopy/pyosf/coverage.svg?branch=master)](https://codecov.io/github/psychopy/pyosf?branch=master)

Installation
-------------------

`pyosf` is compatible with Linux, OS X and Windows, and with Python 2.7 and Python 3.4 (upwards)

Install it with::

	pip install pyosf

Usage
---------

When you first create a `Project`, or to perform searches for projects, you need to create a `Session`::

    import pyosf
    session = pyosf.Session(username="name@gmail.com", password="xxyxyayxy")

The `Session` allows you to conduct searches::

```python
users = session.find_users("Peirce")  # a list of user ids
print users
jon_id = users[0]['id']  # we're just using the first one
projs = session.find_user_projects(user_id=jon_id)  # id=None to find your own projects
for proj in projs:
    print("{}: {}".format(proj.id, proj.title))

osf_proj = session.open_project(proj_id)  # or this if you know the project id
```

Then you can create a `Project` object to track the remote and local files. To do this you need:
    - project_file: a location to store project info
    - root_path:
    - osf: an OSF project object from a `Session`
    OR
    - simply a project file location, on subsequent repeats

```python
proj = pyosf.Project(project_file="/Home/myUserName/pyosfProjects/first.proj",
                       root_path="/Home/myUserName/experiments/firstExperiment",
                       osf=osf_proj)
changes = proj.analyze()  #so you can inspect them if needed
changes.apply()  #do the sync
proj.save()
```

The project file saves your username (but not password) and, if the username has previously been used to authenticate a `Session` with OSF then an authentication token will have been saved to `~/.pyosf/tokens.json` and that will allow the project to create a new session. i.e. on subseqent logins you can do just

```python
import pyosf
# no need to create a session second time around
proj = pyosf.Project(project_file="/Home/myUserName/pyosfProjects/first.proj")
changes = proj.analyze()
changes.apply()
```

Security and passwords
---------------------------

When you first create a `Session` you need to provide a username (email address) and your OSF password. These will be sent securely (over https) and an auth token will be retrieved. That auth token will be stored in readable text in the current user space of your computer (in ~/.pyosf/tokens.json). When a `Session` is subsequently created the username is used to check for a previous auth token and if one is found a password will not be needed.

The second step is from the `Project`. The `Project` stores in its .proj file (json format) the username that was being used for this sync (as supplied on first access). That username will be used to create a `Session` which will then fetch the appropriate token as described above.
