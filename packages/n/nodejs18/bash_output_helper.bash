#
# Node can break stdin/stdout/stderr by setting them O_NONBLOCK
# and then not resetting it back to blocking mode on exit
# This function redirects stdio descriptors via new logging pipe
#


function decoupled_cmd
{
   mkfifo _log
   ($@) < /dev/null > _log 2>_log &
   cat _log
   rm _log
   wait $!
}

