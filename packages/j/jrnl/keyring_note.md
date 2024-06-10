#### Using jrnl with encryption and keyring
If your reading this, your likely running osc on your system and seeing the following error `AttributeError: '_PasswordRetriever' object has no attribute 'encode'`

This is an upstream issue with `python3{ver}-keyring-keyutils` with an upstream report <sup>Ref 3</sup> created in September 2022 with no action at this time.

Please use either of the following workarounds.

#### Workaround 1
Drop into the python3 interpretor by running `python3` and run;
```bash
import keyring
journal_name = "default" # Should match name in  `jrnl --list`
password = "mypassword" # Change to your journal's password
keyring.set_password("jrnl", journal_name, password)

exit()
```
#### Workaround 2
Uninstall python3{ver}-keyring-keyutils, create your password in the keyring for jrnl, then re-install python3{ver}-keyring-keyutils.

---
Ref 1: [openSUSE Bug Report (boo#1223003)](https://bugzilla.suse.com/show_bug.cgi?id=1223003)

Ref 2: [Upstream Bug (gh#jrnl-org/jrnl#1883)](https://github.com/jrnl-org/jrnl/issues/1883)

Ref 3: [python-keyring-keyutils (gh#marcus-h/python-keyring-keyutils#1)](
https://github.com/marcus-h/python-keyring-keyutils/issues/1)

---