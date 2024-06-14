# check if DRI is available, true if it is, false otherwise

hasDri ()
{
  if [ "`glxinfo | grep "direct rendering: " | head -n 1 | cut -d " " -f 3`" != Yes ] ||
     glxinfo | grep -qE "OpenGL renderer string: Software Rasterizer|OpenGL renderer string: Gallium .* on llvmpipe"; then
    return 1
  else
    return 0
  fi 
}

# check if DRI is available, show an error and exit if it isn't

checkDriOK ()
{
  if ! hasDri; then
    zenity --error --text="Your system currently is not capable of hardware \
accelerated 3D. Therefore $1 cannot run.

Usually the cause of this error is that there are no Free Software drivers \
for your graphics card, please contact your graphics card manufacturer and \
kindly ask them to provide Free Software support for your card."
    exit 1;
  fi
}
