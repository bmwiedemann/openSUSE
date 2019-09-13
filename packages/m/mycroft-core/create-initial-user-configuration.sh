#!/bin/sh

[[ -e ~/.mycroft/mycroft.conf ]] && exit 0

echo "Creating initial user configuration at ~/.mycroft/mycroft.conf ... "

[[ -d ~/.mycroft ]] || mkdir ~/.mycroft

cp /usr/share/mycroft-core/mycroft-user-template.conf ~/.mycroft/mycroft.conf

sed -i -e "s,HOME_MYCROFT_DIR,$HOME/.mycroft," ~/.mycroft/mycroft.conf
sed -i -e "s,HOME_SKILL_DIR,$HOME/.mycroft/skills," ~/.mycroft/mycroft.conf
sed -i -e "s,HOME_SKILLS_REPO_DIR,$HOME/.mycroft/.skills-repo," ~/.mycroft/mycroft.conf

echo "Installing the default skills ... "
mkdir -p ~/.mycroft/skills

# Load the default skills
msm default

echo "Done"
