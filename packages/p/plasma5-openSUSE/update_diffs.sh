#!/bin/bash
if [ "$(whoami)" != "root" ]; then
    echo "This has to be run as root, it syncs the sddm theme components with the look-and-feel"
    exit 1
fi

# Sync sddm theme components with look-and-feel
rsync -av --delete /usr/share/plasma/look-and-feel/org.openSUSE.desktop/contents/components/ /usr/share/sddm/themes/breeze-openSUSE/components/ >/dev/null
ln -sf ../../../../../wallpapers/openSUSEdefault/contents/images/1920x1080.jpg /usr/share/sddm/themes/breeze-openSUSE/components/artwork/1920x1080.jpg

# Update lookandfeel.diff
# We need to ignore files in the .tar, so copy everything into /tmp and delete them
cp -R /usr/share/plasma/look-and-feel/org.{kde.breeze,openSUSE}.desktop /tmp
for i in $(tar -tf plasma5-openSUSE*.tar* | sed "s#plasma5-openSUSE/config-files/usr/share/plasma/look-and-feel#/tmp#" | grep /tmp); do
    rm -f -- "$i" "$(printf %s "$i" | sed "s/org.openSUSE.desktop/org.kde.breeze.desktop/")" 2>/dev/null
done;
# Part of layout.diff
rm /tmp/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js

(cd /tmp; git diff --no-index org.{kde.breeze,openSUSE}.desktop) > lookandfeel.diff

rm -rf /tmp/org.{kde.breeze,openSUSE}.desktop

# Check for added binary files, those need to be added to the tar
grep -E "^Binary files /dev/null and " lookandfeel.diff
[ $? -eq 1 ] || echo "New binary files, please add them to the tar."

# Update layout.diff
git diff --no-index /usr/share/plasma/shells/org.kde.plasma.desktop/contents/layout.js /usr/share/plasma/look-and-feel/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js > layout.diff

# Update panel.diff
(cd /usr/share/plasma/layout-templates/; git diff --no-index org.{kde.plasma,opensuse}.desktop.defaultPanel) > panel.diff

# Update sddmtheme.diff
(cd /usr/share/sddm/themes/; git diff --no-index breeze{,-openSUSE}) > sddmtheme.diff
