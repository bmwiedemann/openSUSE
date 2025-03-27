# After installation you need enable and start timekpr.service:
```
sudo systemctl enable timekpr.service
sudo systemctl start timekpr.service
```
- If you whant to be able control timekpr-nExT without superuser privileges, add your account to the timekpr group:
```
sudo gpasswd -a $USER timekpr
```
and re-login to session.

- If you are using a GNOME Shell, please ***do not forget*** to install ["AppIndicator and KStatusNotifierItem Support"](https://extensions.gnome.org/extension/615/appindicator-support/) GNOME extension manually for every controlled users, otherwise icon will be hidden!