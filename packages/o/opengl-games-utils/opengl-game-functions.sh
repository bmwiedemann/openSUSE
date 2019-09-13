# check if DRI is available, show an error and exit if it isn't
checkDriOK() {
  if ! glxinfo | grep -Fx "direct rendering: Yes" > /dev/null; then
    zenity --error --text="Your system currently is not capable of hardware \
accelerated 3D. Therefore $1 cannot run.

Usually the cause of this error is that there are no Free Software drivers \
for your graphics card, please contact your graphics card manufacturer and \
kindly ask them to provide Free Software support for your card."
    return 1
  fi
}
