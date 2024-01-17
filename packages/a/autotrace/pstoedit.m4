# a macro to get the libs/cflags for libpstoedit
# Copyed from gdk-pixbuf.m4

dnl AM_PATH_PSTOEDIT([MINIMUM-VERSION, [ACTION-IF-FOUND [, ACTION-IF-NOT-FOUND]])
dnl Test to see if libpstoedit is installed, and define PSTOEDIT_CFLAGS, LIBS
dnl
AC_DEFUN(AM_PATH_PSTOEDIT,
[dnl
dnl Get the cflags and libraries from the pstoedit-config script
dnl
AC_ARG_WITH(pstoedit-prefix,[  --with-pstoedit-prefix=PFX   Prefix where Pstoedit is installed (optional)],
            pstoedit_prefix="$withval", pstoedit_prefix="")
AC_ARG_WITH(pstoedit-exec-prefix,[  --with-pstoedit-exec-prefix=PFX Exec prefix where Pstoedit is installed (optional)],
            pstoedit_exec_prefix="$withval", pstoedit_exec_prefix="")
AC_ARG_ENABLE(pstoedittest, [  --disable-pstoedittest       Do not try to compile and run a test Pstoedit program],
		    , enable_pstoedittest=yes)

  if test x$pstoedit_exec_prefix != x ; then
     pstoedit_args="$pstoedit_args --exec_prefix=$pstoedit_exec_prefix"
     if test x${PSTOEDIT_CONFIG+set} != xset ; then
        PSTOEDIT_CONFIG=$pstoedit_exec_prefix/bin/pstoedit-config
     fi
  fi
  if test x$pstoedit_prefix != x ; then
     pstoedit_args="$pstoedit_args --prefix=$pstoedit_prefix"
     if test x${PSTOEDIT_CONFIG+set} != xset ; then
        PSTOEDIT_CONFIG=$pstoedit_prefix/bin/pstoedit-config
     fi
  fi

  AC_PATH_PROG(PSTOEDIT_CONFIG, pstoedit-config, no)
  min_pstoedit_version=ifelse([$1], ,3.32.0,$1)
  AC_MSG_CHECKING(for PSTOEDIT - version >= $min_pstoedit_version)
  no_pstoedit=""
  if test "$PSTOEDIT_CONFIG" = "no" ; then
    no_pstoedit=yes
  else
    PSTOEDIT_CFLAGS=`$PSTOEDIT_CONFIG $pstoedit_args --cflags`
    PSTOEDIT_LIBS=`$PSTOEDIT_CONFIG $pstoedit_args --libs`

    pstoedit_major_version=`$PSTOEDIT_CONFIG $pstoedit_args --version | \
           sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\1/'`
    pstoedit_minor_version=`$PSTOEDIT_CONFIG $pstoedit_args --version | \
           sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\2/'`
    pstoedit_micro_version=`$PSTOEDIT_CONFIG $pstoedit_args --version | \
           sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\3/'`
    if test "x$enable_pstoedittest" = "xyes" ; then
      ac_save_CFLAGS="$CFLAGS"
      ac_save_LIBS="$LIBS"
      CFLAGS="$CFLAGS $PSTOEDIT_CFLAGS"
      LIBS="$PSTOEDIT_LIBS $LIBS"
dnl
dnl Now check if the installed PSTOEDIT is sufficiently new. (Also sanity
dnl checks the results of pstoedit-config to some extent
dnl
      rm -f conf.pstoedittest
      AC_TRY_RUN([
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pstoedit/pstoedit.h>

char*
my_strdup (char *str)
{
  char *new_str;
  
  if (str)
    {
      new_str = malloc ((strlen (str) + 1) * sizeof(char));
      strcpy (new_str, str);
    }
  else
    new_str = NULL;
  
  return new_str;
}

int main ()
{
  int major, minor, micro;
  char *tmp_version;

  system ("touch conf.pstoedittest");

  /* HP/UX 9 (%@#!) writes to sscanf strings */
  tmp_version = my_strdup("$min_pstoedit_version");
  if (sscanf(tmp_version, "%d.%d.%d", &major, &minor, &micro) != 3) {
     printf("%s, bad version string\n", "$min_pstoedit_version");
     exit(1);
   }

   if (($pstoedit_major_version > major) ||
      (($pstoedit_major_version == major) && ($pstoedit_minor_version > minor)) ||
      (($pstoedit_major_version == major) && ($pstoedit_minor_version == minor) && ($pstoedit_micro_version >= micro)))
    {
      return 0;
    }
  else
    {
      printf("\n*** 'pstoedit-config --version' returned %d.%d.%d, but the minimum version\n", $pstoedit_major_version, $pstoedit_minor_version, $pstoedit_micro_version);
      printf("*** of PSTOEDIT required is %d.%d.%d. If pstoedit-config is correct, then it is\n", major, minor, micro);
      printf("*** best to upgrade to the required version.\n");
      printf("*** If pstoedit-config was wrong, set the environment variable PSTOEDIT_CONFIG\n");
      printf("*** to point to the correct copy of pstoedit-config, and remove the file\n");
      printf("*** config.cache before re-running configure\n");
      return 1;
    }
}
],, no_pstoedit=yes,[echo $ac_n "cross compiling; assumed OK... $ac_c"])
       CFLAGS="$ac_save_CFLAGS"
       LIBS="$ac_save_LIBS"
     fi
  fi
  if test "x$no_pstoedit" = x ; then
     AC_MSG_RESULT(yes)
     ifelse([$2], , :, [$2])     
  else
     AC_MSG_RESULT(no)
     if test "$PSTOEDIT_CONFIG" = "no" ; then
       echo "*** The pstoedit-config script installed by PSTOEDIT could not be found"
       echo "*** If PSTOEDIT was installed in PREFIX, make sure PREFIX/bin is in"
       echo "*** your path, or set the PSTOEDIT_CONFIG environment variable to the"
       echo "*** full path to pstoedit-config."
     else
       if test -f conf.pstoedittest ; then
        :
       else
          echo "*** Could not run PSTOEDIT test program, checking why..."
          CFLAGS="$CFLAGS $PSTOEDIT_CFLAGS"
          LIBS="$LIBS $PSTOEDIT_LIBS"
          AC_TRY_LINK([
#include <stdio.h>
#include <pstoedit/pstoedit.h>
],      [ return 0; ],
        [ echo "*** The test program compiled, but did not run. This usually means"
          echo "*** that the run-time linker is not finding PSTOEDIT or finding the wrong"
          echo "*** version of PSTOEDIT. If it is not finding PSTOEDIT, you'll need to set your"
          echo "*** LD_LIBRARY_PATH environment variable, or edit /etc/ld.so.conf to point"
          echo "*** to the installed location  Also, make sure you have run ldconfig if that"
          echo "*** is required on your system"
	  echo "***"
          echo "*** If you have an old version installed, it is best to remove it, although"
          echo "*** you may also be able to get things to work by modifying LD_LIBRARY_PATH"],
        [ echo "*** The test program failed to compile or link. See the file config.log for the"
          echo "*** exact error that occured. This usually means PSTOEDIT was incorrectly installed"
          echo "*** or that you have moved PSTOEDIT since it was installed. In the latter case, you"
          echo "*** may want to edit the pstoedit-config script: $PSTOEDIT_CONFIG" ])
          CFLAGS="$ac_save_CFLAGS"
          LIBS="$ac_save_LIBS"
       fi
     fi
     PSTOEDIT_CFLAGS=""
     PSTOEDIT_LIBS=""
     ifelse([$3], , :, [$3])
  fi
  AC_SUBST(PSTOEDIT_CFLAGS)
  AC_SUBST(PSTOEDIT_LIBS)
  rm -f conf.pstoedittest
])
