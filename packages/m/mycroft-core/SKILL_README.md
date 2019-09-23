## Installing a skill

Installing a skill using this folder is very simple. You just need to find the skill you want on Github (our [skills repository](https://github.com/MycroftAI/mycroft-skills) is a good source for this) and then clone it into
this folder, and then follow any additional installation steps it may have. This may be things like installing new python packages via pip, installing new Linux packages, etc.

For example, if you wanted to install the mp3 demo skill, you just need to do the following:
```
cd /opt/mycroft/skills
git clone https://github.com/ethanaward/demo_skill
```

If the repo has a requirements file, you will need to install the requirements into the mycroft virtualenv by doing the following:
```
cd /opt/mycroft/skills
git clone https://github.com/example_user/example_skill
cd example_skill
workon mycroft
pip install -r requirements.txt
```

Other skills may have more complicated requiremnts. Read each skill's README for more specific instructions.
