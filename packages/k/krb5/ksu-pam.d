#%PAM-1.0
auth     sufficient     pam_rootok.so
auth     include        common-auth
account  sufficient     pam_rootok.so
account  include        common-account
password include        common-password
session  optional       pam_keyinit.so force revoke
session  include        common-session
session  optional       pam_xauth.so
