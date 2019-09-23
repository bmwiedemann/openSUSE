#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT(khunphan, 0.55)
AC_CONFIG_SRCDIR([config.h.in])
AC_CONFIG_HEADER([config.h])
AM_INIT_AUTOMAKE(foreign)

AC_CANONICAL_BUILD

# Checks for programs.
AC_PROG_CXX
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_RANLIB

# Checks for libraries.
AC_CHECK_LIB([GL], [main])
AC_CHECK_LIB([GLU], [main])
AC_CHECK_LIB([glut], [main])
AC_CHECK_LIB([png], [main])
AC_CHECK_LIB([pthread], [main])
AC_CHECK_LIB([xml2], [main])

AC_PATH_XTRA

dnl Check for SDL 
SDL_VERSION=1.2.0
AM_PATH_SDL($SDL_VERSION, 
         :,
         AC_MSG_ERROR([*** SDL version $SDL_VERSION not found!]) 
) 
dnl Check for SDL_mixer
AC_CHECK_LIB(SDL_mixer, 
       main, 
       LIBS="$LIBS -lSDL_mixer", 
       AC_MSG_ERROR([*** SDL_mixer library not found!]) 
)
 
CXXFLAGS="$CXXFLAGS $SDL_CFLAGS" 
LIBS="$LIBS $SDL_LIBS"

# Checks for header files.
AC_HEADER_DIRENT
AC_HEADER_STDC
AC_CHECK_HEADERS([limits.h stdlib.h string.h strings.h sys/time.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_C_CONST
AC_C_INLINE
AC_TYPE_SIZE_T
AC_HEADER_TIME

# Checks for library functions.
AC_FUNC_CLOSEDIR_VOID
AC_TYPE_SIGNAL
AC_FUNC_STAT
AC_FUNC_VPRINTF
AC_CHECK_FUNCS([atexit gettimeofday memset mkdir rmdir sqrt strtol strtoul])

AC_CONFIG_FILES([Makefile
                 admin/Makefile
                 khunphan/Makefile
                 khunphan/Music/Makefile
                 khunphan/Sounds/Makefile
                 khunphan/Sounds/bubbles/Makefile
                 khunphan/Sounds/marble/Makefile
                 khunphan/Sounds/metal/Makefile
                 khunphan/Sounds/painting/Makefile
                 khunphan/Sounds/rock/Makefile
                 khunphan/Sounds/smily/Makefile
                 khunphan/Textures/Makefile
                 khunphan/Textures/bubbles/Makefile
                 khunphan/Textures/marble/Makefile
                 khunphan/Textures/metal/Makefile
                 khunphan/Textures/painting/Makefile
                 khunphan/Textures/rock/Makefile
                 khunphan/Textures/smily/Makefile
                 khunphan/Textures/wood/Makefile
                 khunphan/docs/Makefile
                 khunphan/docs/en/Makefile
                 khunphan/locale/Makefile])
AC_OUTPUT
