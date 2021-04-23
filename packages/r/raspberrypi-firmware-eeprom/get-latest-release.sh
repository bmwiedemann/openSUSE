#!/bin/bash
# set -x
# Gets the latest rpi-eeprom release and updates the relevant package files
# Dependencies: git, curl, jq and bsdtar

LATEST_RELEASE="https://api.github.com/repos/raspberrypi/rpi-eeprom/releases/latest"

current_version=$(cat raspberrypi-firmware-eeprom.spec | grep Version: | cut -d":" -f2 | xargs)
current_archive_version=$(cat raspberrypi-firmware-eeprom.spec | grep " archive_version " | cut -d" " -f11 | xargs)
version=$(curl --silent $LATEST_RELEASE | jq -r ".tag_name" | sed "s/\-/\./" | cut -c2-)
archive_version=$(curl --silent $LATEST_RELEASE | jq -r ".name" | sed -n -e 's/^rpi-boot-eeprom-recovery-//p')
# Compare current version with latest release version
if [[ $1 != "-f" && $version == $current_version ]]; then
	echo Current version is up to date: $current_version
	exit 0
fi

# Get latest release package URL
url=$(curl --silent $LATEST_RELEASE | jq -r ".assets[0].browser_download_url")
if [[ $url == "null" ]]; then
	echo Failed to get latest release url
	exit 1
fi

# Download latest release .zip and repackage it into .tar.xz
osc rm -f rpi-boot-eeprom-recovery-$current_archive_version.zip || true
echo Getting version $version from: $url
curl --silent --output rpi-boot-eeprom-recovery-$archive_version.zip -L $url
osc add rpi-boot-eeprom-recovery-$archive_version.zip

# Replace version in spec file and update changes file
sed -i "s/\(Version:\)\(.*\)/\1        ${version}/" raspberrypi-firmware-eeprom.spec
sed -i "s/\(%define         archive_version \)\(.*\)/\1${archive_version}/" raspberrypi-firmware-eeprom.spec
osc vc raspberrypi-firmware-eeprom -m "Update to $version"

echo All good!
exit 0
