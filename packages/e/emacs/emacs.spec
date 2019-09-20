#
# spec file for package emacs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_without  autoconf
%if 0%{?suse_version} >= 1550
%bcond_without  mailutils
%else
%bcond_with     mailutils
%endif
# Experimental, not for production (see https://www.gnu.org/software/emacs/news/NEWS.25.2)
%bcond_with     cairo

Name:           emacs
BuildRequires:  ImageMagick
BuildRequires:  ImageMagick-devel
%if %{with autoconf}
BuildRequires:  autoconf
BuildRequires:  automake
%endif
BuildRequires:  alsa-devel
%if %{with cairo}
BuildRequires:  cairo-devel
%endif
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  fonts-config
BuildRequires:  freetype2-devel
BuildRequires:  giflib-devel
BuildRequires:  gpm-devel
BuildRequires:  gtk3-devel
# Used for installtion of info pages as well as to
# detect if the page info.info is part of that package
BuildRequires:  info
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libotf-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtiff-devel
BuildRequires:  libudev-devel
BuildRequires:  libxml2-devel
BuildRequires:  m17n-lib-devel
%if %{with mailutils}
BuildRequires:  mailutils
BuildRequires:  mailutils-devel
%endif
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  system-user-games
%endif
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-alternatives
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(ice)
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libacl)
%else
BuildRequires:  libacl-devel
%endif
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.12
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xaw3d)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xxf86vm)
Url:            http://www.gnu.org/software/emacs/
Version:        26.3
Release:        0
Summary:        GNU Emacs Base Package
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
Provides:       nxml-mode = 20041004
Obsoletes:      nxml-mode < 20041004
Provides:       epg = 1.0.0
Obsoletes:      epg < 1.0.0
Requires:       emacs-info = %{version}
Requires:       emacs_program = %{version}-%{release}
Requires:       etags
%if %{with mailutils}
Requires:       mailutils
%endif
Requires(pre):  fileutils
%if 0%{?suse_version} >= 1500
Requires(pre):  group(games)
Requires(pre):  user(games)
%endif
Source:         ftp://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.xz
Source1:        app-defaults.Emacs
Source2:        site-lisp.tar.bz2
Source3:        dot.gnu-emacs
Source4:        emacs-rpmlintrc
Source5:        emacs.sh
Patch:          emacs-26.2.dif
# PATCH-FIX-UPSTREAM Adjust to GnuPG 2.1 key listing change
Patch2:         emacs-24.4-glibc.patch
Patch4:         emacs-24.3-asian-print.patch
Patch5:         emacs-24.4-ps-bdf.patch
Patch7:         emacs-24.1-ps-mule.patch
Patch8:         emacs-24.4-nonvoid.patch
Patch11:        emacs-24.4-xim.patch
Patch12:        emacs-24.3-x11r7.patch
Patch15:        emacs-24.3-iconic.patch
Patch16:        emacs-24.4-flyspell.patch
Patch23:        emacs-25.1-custom-fonts.patch
# this patch works with both ImageMagick-6 and ImageMagick-7 for us,
# but that is because we ship /usr/include/ImageMagick-7/wand compat
# symlink
Patch24:        emacs-25.2-ImageMagick7.patch
Patch25:        emacs-26.1-xft4x11.patch
Patch26:        xwidget.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global include_info %(test -s /usr/share/info/info.info* && echo 0 || echo 1)}
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%define _x11lib     %{_exec_prefix}/%{_lib}
%define _x11data    %{_exec_prefix}/lib/X11
%define _libx11     %{_x11data}
%define _x11inc     %{_exec_prefix}/include
%define appDefaultsDir %{_x11data}/app-defaults
%define appDefaultsFile %{appDefaultsDir}/Emacs
%else
%define _x11lib     %{_libdir}
%define _x11data    %{_datadir}/X11
%define _libx11     %{_exec_prefix}/lib/X11
%define _x11inc     %{_includedir}
%define appDefaultsDir %{_x11data}/app-defaults
%define appDefaultsFile %{appDefaultsDir}/Emacs
%endif
%define info_files emacs eintr elisp ada-mode auth autotype bovine calc ccmode cl dbus dired-x ebrowse ede ediff edt eieio emacs-mime epa erc ert eshell eudc efaq eww flymake forms gnus emacs-gnutls htmlfontify idlwave ido info.info mairix-el message mh-e newsticker nxml-mode octave-mode org pcl-cvs pgg rcirc remember reftex sasl sc semantic ses sieve smtpmail speedbar srecode todo-mode tramp url vhdl-mode vip viper widget wisent woman

%description
Basic package for the GNU Emacs editor. Requires emacs-x11 or
emacs-nox.

%package     -n emacs-nox
Requires(post): fileutils
Requires:       emacs = %{version}-%{release}
Provides:       emacs_program = %{version}-%{release}
Summary:        GNU Emacs-nox: An Emacs Binary without X Window System Support
Group:          Productivity/Text/Editors

%description -n emacs-nox
Eight Megabytes And Constantly Swapping. Call it

emacs-nox

Love it or leave it.

%package     -n emacs-x11
Requires(post): fileutils
Requires:       emacs = %{version}-%{release}
Provides:       emacs_program = %{version}-%{release}
Requires:       efont-unicode
Requires:       ifnteuro
Requires:       xorg-x11-fonts
Requires:       xorg-x11-fonts-core
Enhances:       libX11-6
Summary:        GNU Emacs: Emacs binary with X Window System Support
Group:          Productivity/Text/Editors

%description -n emacs-x11
Call it

Emacs

Love it or leave it. This is the Emacs binary with X Window System
Support.

%package     -n emacs-el
Requires:       emacs = %{version}-%{release}
Summary:        Several Lisp Files for GNU Emacs
Group:          Productivity/Text/Editors
BuildArch:      noarch

%description -n emacs-el
Several Lisp files not needed for running GNU Emacs. Most of these
files are pre-byte compiled and therefore not necessary.

%package     -n emacs-info
Summary:        Info files for GNU Emacs
Group:          Productivity/Text/Editors
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
BuildArch:      noarch

%description -n emacs-info
This package contains all the Info files for GNU Emacs. These files can
be read online with GNU Emacs. They describe Emacs and some of its
modes.

%package     -n etags
Summary:        Generate Tag Files for Use with Emacs
Group:          Development/Tools/Navigators
Requires(post): coreutils update-alternatives
Requires(preun): coreutils update-alternatives
Provides:       ctags:/usr/bin/etags

%description -n etags
ETags generates tag files from source code in Pascal, Cobol, Ada, Perl,
LaTeX, Scheme, Emacs Lisp/Common Lisp, Postscript, Erlang, Python, Prolog,
and most assembler-like syntaxes.

%prep
%setup -q -b 2
%patch2  -p0 -b .glibc
%patch4  -p0 -b .print
%patch5  -p0 -b .psbdf
%patch7  -p0 -b .psmu
%patch8  -p0 -b .nvoid
%patch11 -p0 -b .xim
%patch12 -p0 -b .x11r7
%patch15 -p0 -b .iconic
%patch16 -p0 -b .flyspell
%patch23 -p0 -b .custfnt
%patch24 -p1 -b .imag
%patch25 -p0 -b .xft
%patch26 -p1 -b .xwd
%patch   -p0 -b .0

%build
%if %{without autoconf}
# We don't want to run autoconf
if test configure.ac -nt aclocal.m4 -o m4/gnulib-comp.m4 -nt aclocal.m4 ; then
    sleep 1
    touch aclocal.m4
fi
if test configure.ac -nt configure -o aclocal.m4 -nt configure ; then
    sleep 1
    touch configure
fi
if test configure.ac -nt src/stamp-h.in -o aclocal.m4 -nt src/stamp-h.in ; then
    sleep 1
    touch src/stamp-h.in
fi
if test aclocal.m4 -nt lib/Makefile.in -o lib/Makefile.am -nt lib/Makefile.in -o lib/gnulib.mk -nt lib/Makefile.in ; then
    sleep 1
    touch lib/Makefile.in
fi
if test -s autogen.sh ; then
    mv autogen.sh autogen.sh.no
    ln -sf /bin/true autogen.sh
fi
%else
autoreconf -fiv -I $PWD -I $PWD/m4
%endif

# make sure that the binaries work (pagesize on build must be the same as on target, bnc#726769)
%ifarch ppc ppc64 ia64
%if %(getconf PAGESIZE) != 65536
%error "Error: wrong build host, PAGESIZE must be 65536"
exit 1
%endif
%endif
  exec_shield=0
  if test -e /proc/sys/kernel/exec-shield; then
      read -t 1 exec_shield < /proc/sys/kernel/exec-shield
  fi
  if test $exec_shield -ne 0 ; then
      echo Sorry, Execution Shield exists and is enabled 1>&2
      exit 1
  fi

  cflags ()
  {
      local flag=$1; shift
      local var=$1; shift
      test -n "${flag}" -a -n "${var}" || return
      case "${!var}" in
      *${flag}*) return
      esac
      case "$flag" in
      -Wl,*)
	  set -o noclobber
	  echo 'int main () { return 0; }' > ldtest.c
	  if ${CC:-gcc} -Werror $flag -o /dev/null -xc ldtest.c > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
	  set +o noclobber
	  rm -f ldtest.c
	  ;;
      *)
	  if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
	  if ${CXX:-g++} -Werror $flag -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
      esac
  }

  # remove reference to win32 info page
  info_found="$((sed -rn '\@^info:@{ s@.*/@@;s/\.info//p; }' doc/emacs/Makefile.in doc/lispintro/Makefile.in doc/lispref/Makefile.in ; sed -rn '\@^INFO_COMMON@,\@^$@{ s@.*=@@; s@[[:blank:]]+@ @g; :join; /\\$/{N; s/\s*\\\n//; b join;}; p}' ./doc/misc/Makefile.in)|xargs|sed -e 's,efaq-w32 ,,')"
  if test "$info_found" != "%info_files"
  then
      echo Please update info_files >&2
      exit 1
  fi
VERSION=%{version}
%ifarch noarch
    SYS="--build=%{_build_cpu}-suse-%{_build_os}
"
%else
    SYS="--build=%{_target_cpu}-suse-%{_build_os}
"
%endif
 CFLAGS="${RPM_OPT_FLAGS} -D_GNU_SOURCE -DGDK_DISABLE_DEPRECATION_WARNINGS -DGLIB_DISABLE_DEPRECATION_WARNINGS"
LDFLAGS=
  cflags -Wl,-no-pie             LDFLAGS
  cflags -pipe                   CFLAGS
  cflags -Wno-pointer-sign       CFLAGS
  cflags -Wno-unused-variable    CFLAGS
  cflags -Wno-unused-label       CFLAGS
  cflags -fno-optimize-sibling-calls CFLAGS
  cflags -fno-PIE                CFLAGS
  cflags -Wl,-O2		 LDFLAGS
%ifarch ia64
 CFLAGS=$(echo "${CFLAGS}"|sed -r 's/-O[0-9]?/-O1/g')
%endif
  SMALL="-DSYSTEM_PURESIZE_EXTRA=25000 \
	 -DSITELOAD_PURESIZE_EXTRA=10000 \
"
  LARGE="-DSYSTEM_PURESIZE_EXTRA=55000 \
	 -DSITELOAD_PURESIZE_EXTRA=10000 \
"
   LANG=POSIX; LC_CTYPE=en_US.UTF-8
export CC CFLAGS LANG LC_CTYPE LDFLAGS
 PREFIX="--prefix=%{_prefix} \
	 --mandir=%{_mandir} \
	 --infodir=%{_infodir} \
	 --datadir=%{_datadir} \
	 --localstatedir=%{_localstatedir} \
	 --sharedstatedir=%{_localstatedir}/lib \
	 --libexecdir=%{_prefix}/lib \
	 --enable-locallisppath=%{_datadir}/emacs/%{version}/site-lisp:%{_datadir}/emacs/site-lisp
"
DESKTOP="--with-x \
	 --with-xim \
	 --with-sound \
	 --with-xpm \
	 --with-jpeg \
	 --with-tiff \
	 --with-gif \
	 --with-png \
	 --with-rsvg \
	 --with-dbus \
	 --with-xft \
	 --without-gpm \
"
    GTK="${DESKTOP} \
	 --with-x-toolkit=gtk3 \
	 --with-toolkit-scroll-bars \
	 --x-includes=%{_x11inc} \
	 --x-libraries=%{_x11lib} \
	 --with-libotf \
	 --with-m17n-flt \
%if %{with cairo}
	 --with-cairo \
%endif
	 --with-xwidgets \
"
    X11="${DESKTOP} \
	 --with-x-toolkit=lucid \
	 --with-toolkit-scroll-bars \
	 --x-includes=%{_x11inc} \
	 --x-libraries=%{_x11lib}:%{_x11data} \
	 --without-libotf \
	 --without-m17n-flt \
"
  NOX11="--with-gpm \
	 --without-x \
	 --without-xim \
	 --without-sound \
	 --without-xpm \
	 --without-jpeg \
	 --without-tiff \
	 --without-gif \
	 --without-png \
	 --without-rsvg \
	 --without-dbus \
	 --without-xft \
	 --without-libotf \
	 --without-m17n-flt \
"
   COMP="--disable-build-details \
%if %{with mailutils}
	 --without-pop
	 --with-mailutils
%else
	 --with-pop \
%endif
	 --without-hesiod \
	 --with-gameuser=:games \
	 --with-kerberos \
	 --with-kerberos5 \
	 --with-file-notification=inotify \
	 --with-modules \
	 --enable-autodepend \
"
if (($(getconf LONG_BIT) < 62))
then
    COMP="${COMP} --with-wide-int"
fi

##OIFS="$IFS"; IFS=.
##set -- $(gcc -dumpversion 2>/dev/null)
##(($1 > 4 || ($1 == 4 && $2 > 4))) && COMP="$COMP --enable-link-time-optimization"
##IFS="$OIFS"

make_mchkoff ()
{
    local OMC=$MALLOC_CHECK_
    unset MALLOC_CHECK_
    if test -n "${1}" ; then
	setarch $(uname -m) -R make ${1+"$@"}
	set -- $(src/emacs -batch --eval "(print pure-space-overflow)")
	test "$1" = "nil" || exit 1
    fi
    make -C src/ versionclean
    setarch $(uname -m) -R make
    set -- $(src/emacs -batch --eval "(print pure-space-overflow)")
    test "$1" = "nil" || exit 1
    if test -n "$OMC" ; then
	MALLOC_CHECK_=$OMC
	export MALLOC_CHECK_
    fi
}

# new giflib5 does not have this function and it is unused anyway...
ac_cv_lib_gif_EGifPutExtensionLast=yes
export ac_cv_lib_gif_EGifPutExtensionLast

CFLAGS="$CFLAGS $SMALL" ./configure ${COMP} ${PREFIX} ${NOX11} ${SYS}
make_mchkoff bootstrap
make -C lisp updates compile
for i in `find site-lisp/ -name '*.el'`; do
    src/emacs -batch -q --no-site -f batch-byte-compile $i; \
done
cp src/emacs emacs-nox
make distclean
#
CFLAGS="$CFLAGS $LARGE" ./configure ${COMP} ${PREFIX} ${GTK} ${SYS}
make_mchkoff
cp src/emacs emacs-gtk
make distclean
#
CFLAGS="$CFLAGS $LARGE" ./configure ${COMP} ${PREFIX} ${X11} ${SYS}
make_mchkoff
cp src/emacs emacs-x11
#
cd ../site-lisp/
../emacs-%{version}/src/emacs -batch -q --no-site -f batch-byte-compile *.el
rm -vf site-start.elc
rm -vf site-start.el.orig

%install
#
PATH=/sbin:$PATH
##
VERSION=%{version}
mkdir -p %{buildroot}/usr/bin
install -m 0755 emacs-nox %{buildroot}/usr/bin/
install -m 0755 emacs-gtk %{buildroot}/usr/bin/
install -m 0755 emacs-x11 %{buildroot}/usr/bin/
make install DESTDIR=%{buildroot} systemdunitdir=%{_userunitdir}
rm -vf %{buildroot}/usr/bin/emacs
install -p %{S:5} %{buildroot}/usr/bin/emacs
chmod 0755        %{buildroot}/usr/bin/emacs
tar cf - `find site-lisp/ -name '*.el'  -o -name '*.elc'` | \
tar -x -f - -C %{buildroot}%{_datadir}/emacs/%{version}/
mkdir -p %{buildroot}%{_docdir}/emacs
ln -sf %{_datadir}/emacs/%{version}/etc %{buildroot}%{_docdir}/emacs/doc
find %{buildroot}%{_datadir}/emacs/%{version}/ -name '*,v' -o -name '*.orig' | xargs -r rm -f
for f in %{buildroot}%{_infodir}/* ; do
    case "$f" in
	*.gz)			;;
	*/dir)	rm -f ${f}	;;
	*)	test -e  ${f}.gz && rm ${f}.gz
		gzip -9f ${f}
    esac
done
#
mkdir -p %{buildroot}%(dirname %{appDefaultsFile})
cp -p %{S:1} %{buildroot}%{appDefaultsFile}
pushd ../
mkdir -p %{buildroot}/etc/skel
install -m 0644 %{S:3} %{buildroot}/etc/skel/.gnu-emacs
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/site-start.d
tar cf - site-lisp/ | tar xvvf - -C %{buildroot}%{_datadir}/emacs/
chmod -R a+r %{buildroot}%{_datadir}/emacs/site-lisp/
popd
(cd %{buildroot}
 find usr/share/emacs/site-lisp/ -type f	\
      \( -name site-start.el -printf "%%%%config " , \
	 -printf "/%%p\n" \)
) | sort > site-lisp.lst
#
# cleanup
#
unelc ()
{
    local elc=$1
    local elz=${elc%%.elc}.el.gz
    rm -vf $elc
    if test -n "$elz" -a -e "$elz" ; then
	gunzip "$elz"
    fi
}
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/dired.el.dired
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/loaddefs.el.psbdf
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/ps-bdf.el.psbdf
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/ps-mule.el.print
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/ps-mule.el.mule
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/startup.el.iconic
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/textmodes/ispell.el.mule
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/term.el.term
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/etc/ETAGS.EBNF
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/etc/ETAGS.README
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/elc.tar.gz
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/mail/sendmail.el.snd
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/ldefs-boot.el.psbdf
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/ps-mule.el.psmu
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/textmodes/ispell.el.psmu
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/files.el.CVE20075795
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/fast-lock.el.flc
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/obsolete/fast-lock.el.flc
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/loaddefs.el.flc
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/progmodes/python.el.python
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/textmodes/flyspell.el.flyspell
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/obsolete/spell.el.obsolate
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/cmuscheme.el.0
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/international/mule-cmds.el.0
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/net/ange-ftp.el.0
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/site-load.el.0
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/speedbar.el.0
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/textmodes/ispell.el.0
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/epg.el.gnupg
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/mouse.el.prime
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/dynamic-setting.el.custfnt
unelc  %{buildroot}%{_datadir}/emacs/%{version}/lisp/bindings.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/lisp/cus-start.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/lisp/generic-x.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/lisp/site-load.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/lisp/skeleton.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/lisp/term/xterm.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/site-lisp/subdirs.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/site-lisp/term/func-keys.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/site-lisp/term/gnome.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/site-lisp/term/kvt.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/site-lisp/term/linux.elc
unelc  %{buildroot}%{_datadir}/emacs/%{version}/site-lisp/term/locale.elc
unelc  %{buildroot}%{_datadir}/emacs/site-lisp/site-start.elc
unelc  %{buildroot}%{_datadir}/emacs/site-lisp/subdirs.elc
find %{buildroot}%{_datadir}/emacs/%{version}/etc/ -name '*[a-z].[16]' | \
    xargs gzip -9f
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/COPYING
ln -sf ../etc/COPYING \
       %{buildroot}%{_datadir}/emacs/%{version}/lisp/COPYING
# 
fdupes -q -r -1 %{buildroot}%{_datadir}/emacs/%{version}/etc/images/icons/ %{buildroot}%{_datadir}/icons/ |\
xargs -n 2 | while read first second; do
    case "${first}" in
    *emacs/%{version}/etc/*)
	target=$second
	file=$first
	;;
    *)  target=$first
	file=$second
    esac
    ln -sf ${file#%{buildroot}} ${target}
done
# install desktop file
test -e etc/emacs.desktop || exit 1
echo 'X-KDE-StartupNotify=false' >> etc/emacs.desktop
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/etc/emacs.desktop
cp etc/images/icons/hicolor/32x32/apps/emacs.png $RPM_SOURCE_DIR/emacs.png
%suse_update_desktop_file -r -i emacs TextEditor Utility
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/ctags		%{buildroot}%{_bindir}/ctags
ln -sf %{_sysconfdir}/alternatives/ctags.1%{ext_man}	%{buildroot}%{_mandir}/man1/ctags.1%{ext_man}
ln -sf %{_bindir}/gnuctags				%{buildroot}%{_sysconfdir}/alternatives/ctags
ln -sf %{_mandir}/man1/gnuctags.1%{ext_man}		%{buildroot}%{_sysconfdir}/alternatives/ctags.1%{ext_man}

%pre
test -L usr/bin/emacs && rm -f usr/bin/emacs || true

%post -n emacs-nox
if test -e usr/share/emacs/site-lisp/auctex/font-latex.elc ; then
  owd=$(pwd)
  cd usr/share/emacs/site-lisp/auctex || exit 1
  emacs -batch -no-site-file -no-init-file --eval '(setq load-path (cons "." load-path) 
    byte-compile-warnings nil
    TeX-lisp-directory "<none>"
    TeX-auto-global "<none>")' -f batch-byte-compile font-latex.el > /dev/null 2>&1
  cd $owd
fi

%post -n emacs-x11
if test -e usr/share/emacs/site-lisp/auctex/font-latex.elc ; then
  owd=$(pwd)
  cd usr/share/emacs/site-lisp/auctex || exit 1
  emacs -batch -no-site-file -no-init-file --eval '(setq load-path (cons "." load-path) 
    byte-compile-warnings nil
    TeX-lisp-directory "<none>"
    TeX-auto-global "<none>")' -f batch-byte-compile font-latex.el > /dev/null 2>&1
  cd $owd
fi

%post info
for f in %info_files; do
  test "$f" = "info.info" && continue
  test -e "$f" || f="${f}.info"
  %install_info --info-dir=%{_infodir} "%{_infodir}/$f.gz"
done

%preun info
for f in %info_files; do
  test "$f" = "info.info" && continue
  test -e "$f" || f="${f}.info"
  %install_info_delete --info-dir=%{_infodir} "%{_infodir}/$f.gz"
done

%post -n etags
test -L %{_bindir}/ctags || rm -f %{_bindir}/ctags
%{_sbindir}/update-alternatives --quiet --force --install \
	  %{_bindir}/ctags			ctags	%{_bindir}/gnuctags 10 \
  --slave %{_mandir}/man1/ctags.1%{ext_man}	ctags.1	%{_mandir}/man1/gnuctags.1%{ext_man}
%{_sbindir}/update-alternatives --auto ctags

%preun -n etags
if test $1 -eq 0 ; then
    %{_sbindir}/update-alternatives --quiet --remove ctags %{_bindir}/gnuctags
fi

%files -f site-lisp.lst -n emacs
%defattr(-, root, root)
%config /etc/skel/.gnu-emacs
%{_bindir}/ebrowse
%{_bindir}/emacs
%{_bindir}/emacsclient
%dir %{_prefix}/lib/emacs/
%dir %{_prefix}/lib/emacs/%{version}/
%dir %{_prefix}/lib/emacs/%{version}/*-suse-linux*/
%{_prefix}/lib/emacs/%{version}/*-suse-linux*/hexl
%if %{without mailutils}
%{_prefix}/lib/emacs/%{version}/*-suse-linux*/movemail
%endif
%{_prefix}/lib/emacs/%{version}/*-suse-linux*/profile
%{_prefix}/lib/emacs/%{version}/*-suse-linux*/rcs2log
%if 0
%attr(04755,games,games) %{_prefix}/lib/emacs/%{version}/*-suse-linux*/update-game-score
%else
%{_prefix}/lib/emacs/%{version}/*-suse-linux*/update-game-score
%endif
%{_userunitdir}/emacs.service
%dir %{_datadir}/doc/packages/emacs/
%{_datadir}/doc/packages/emacs/doc
%dir %{_datadir}/emacs/
%dir %{_datadir}/emacs/%{version}/
%dir %{_datadir}/emacs/%{version}/etc/
%doc %{_datadir}/emacs/%{version}/etc/AUTHORS
%doc %{_datadir}/emacs/%{version}/etc/CALC-NEWS
%doc %{_datadir}/emacs/%{version}/etc/CENSORSHIP
%doc %{_datadir}/emacs/%{version}/etc/COPYING
%doc %{_datadir}/emacs/%{version}/etc/DEBUG
%doc %{_datadir}/emacs/%{version}/etc/DEVEL.HUMOR
%doc %{_datadir}/emacs/%{version}/etc/DISTRIB
%{_datadir}/emacs/%{version}/etc/DOC
%doc %{_datadir}/emacs/%{version}/etc/ERC-NEWS
%doc %{_datadir}/emacs/%{version}/etc/FTP
%doc %{_datadir}/emacs/%{version}/etc/GNU
%doc %{_datadir}/emacs/%{version}/etc/GNUS-NEWS
%doc %{_datadir}/emacs/%{version}/etc/HELLO
%doc %{_datadir}/emacs/%{version}/etc/HISTORY
%doc %{_datadir}/emacs/%{version}/etc/JOKES
%doc %{_datadir}/emacs/%{version}/etc/LINUX-GNU
%doc %{_datadir}/emacs/%{version}/etc/MACHINES
%doc %{_datadir}/emacs/%{version}/etc/MH-E-NEWS
%doc %{_datadir}/emacs/%{version}/etc/MORE.STUFF
%{_datadir}/emacs/%{version}/etc/NEWS
%doc %{_datadir}/emacs/%{version}/etc/NEWS.1-17
%doc %{_datadir}/emacs/%{version}/etc/NEWS.18
%doc %{_datadir}/emacs/%{version}/etc/NEWS.19
%doc %{_datadir}/emacs/%{version}/etc/NEWS.20
%doc %{_datadir}/emacs/%{version}/etc/NEWS.21
%doc %{_datadir}/emacs/%{version}/etc/NEWS.22
%doc %{_datadir}/emacs/%{version}/etc/NEWS.23
%doc %{_datadir}/emacs/%{version}/etc/NEWS.24
%doc %{_datadir}/emacs/%{version}/etc/NEWS.25
%doc %{_datadir}/emacs/%{version}/etc/NEXTSTEP
%doc %{_datadir}/emacs/%{version}/etc/NXML-NEWS
%doc %{_datadir}/emacs/%{version}/etc/ORDERS
%doc %{_datadir}/emacs/%{version}/etc/ORG-NEWS
%doc %{_datadir}/emacs/%{version}/etc/PROBLEMS
%doc %{_datadir}/emacs/%{version}/etc/README
%doc %{_datadir}/emacs/%{version}/etc/TERMS
%doc %{_datadir}/emacs/%{version}/etc/THE-GNU-PROJECT
%doc %{_datadir}/emacs/%{version}/etc/TODO
%doc %{_datadir}/emacs/%{version}/etc/WHY-FREE
%dir %{_datadir}/emacs/%{version}/etc/charsets/
%{_datadir}/emacs/%{version}/etc/charsets/8859-10.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-11.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-13.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-14.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-15.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-16.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-2.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-3.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-4.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-5.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-6.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-7.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-8.map
%{_datadir}/emacs/%{version}/etc/charsets/8859-9.map
%{_datadir}/emacs/%{version}/etc/charsets/ALTERNATIVNYJ.map
%{_datadir}/emacs/%{version}/etc/charsets/BIG5-1.map
%{_datadir}/emacs/%{version}/etc/charsets/BIG5-2.map
%{_datadir}/emacs/%{version}/etc/charsets/BIG5-HKSCS.map
%{_datadir}/emacs/%{version}/etc/charsets/BIG5.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-1.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-2.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-3.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-4.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-5.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-6.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-7.map
%{_datadir}/emacs/%{version}/etc/charsets/CNS-F.map
%{_datadir}/emacs/%{version}/etc/charsets/CP10007.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1125.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1250.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1251.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1252.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1253.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1254.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1255.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1256.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1257.map
%{_datadir}/emacs/%{version}/etc/charsets/CP1258.map
%{_datadir}/emacs/%{version}/etc/charsets/CP720.map
%{_datadir}/emacs/%{version}/etc/charsets/CP737.map
%{_datadir}/emacs/%{version}/etc/charsets/CP775.map
%{_datadir}/emacs/%{version}/etc/charsets/CP858.map
%{_datadir}/emacs/%{version}/etc/charsets/CP932-2BYTE.map
%{_datadir}/emacs/%{version}/etc/charsets/CP949-2BYTE.map
%{_datadir}/emacs/%{version}/etc/charsets/EBCDICUK.map
%{_datadir}/emacs/%{version}/etc/charsets/EBCDICUS.map
%{_datadir}/emacs/%{version}/etc/charsets/GB180302.map
%{_datadir}/emacs/%{version}/etc/charsets/GB180304.map
%{_datadir}/emacs/%{version}/etc/charsets/GB2312.map
%{_datadir}/emacs/%{version}/etc/charsets/GBK.map
%{_datadir}/emacs/%{version}/etc/charsets/HP-ROMAN8.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM037.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM038.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM1004.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM1026.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM1047.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM256.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM273.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM274.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM275.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM277.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM278.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM280.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM281.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM284.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM285.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM290.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM297.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM420.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM423.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM424.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM437.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM500.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM850.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM851.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM852.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM855.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM856.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM857.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM860.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM861.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM862.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM863.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM864.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM865.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM866.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM868.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM869.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM870.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM871.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM874.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM875.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM880.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM891.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM903.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM904.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM905.map
%{_datadir}/emacs/%{version}/etc/charsets/IBM918.map
%{_datadir}/emacs/%{version}/etc/charsets/JISC6226.map
%{_datadir}/emacs/%{version}/etc/charsets/JISX0201.map
%{_datadir}/emacs/%{version}/etc/charsets/JISX0208.map
%{_datadir}/emacs/%{version}/etc/charsets/JISX0212.map
%{_datadir}/emacs/%{version}/etc/charsets/JISX2131.map
%{_datadir}/emacs/%{version}/etc/charsets/JISX2132.map
%{_datadir}/emacs/%{version}/etc/charsets/JISX213A.map
%{_datadir}/emacs/%{version}/etc/charsets/JOHAB.map
%{_datadir}/emacs/%{version}/etc/charsets/KA-ACADEMY.map
%{_datadir}/emacs/%{version}/etc/charsets/KA-PS.map
%{_datadir}/emacs/%{version}/etc/charsets/KOI-8.map
%{_datadir}/emacs/%{version}/etc/charsets/KOI8-R.map
%{_datadir}/emacs/%{version}/etc/charsets/KOI8-T.map
%{_datadir}/emacs/%{version}/etc/charsets/KOI8-U.map
%{_datadir}/emacs/%{version}/etc/charsets/KSC5601.map
%{_datadir}/emacs/%{version}/etc/charsets/KSC5636.map
%{_datadir}/emacs/%{version}/etc/charsets/MACINTOSH.map
%{_datadir}/emacs/%{version}/etc/charsets/MIK.map
%{_datadir}/emacs/%{version}/etc/charsets/MULE-ethiopic.map
%{_datadir}/emacs/%{version}/etc/charsets/MULE-ipa.map
%{_datadir}/emacs/%{version}/etc/charsets/MULE-is13194.map
%{_datadir}/emacs/%{version}/etc/charsets/MULE-lviscii.map
%{_datadir}/emacs/%{version}/etc/charsets/MULE-sisheng.map
%{_datadir}/emacs/%{version}/etc/charsets/MULE-tibetan.map
%{_datadir}/emacs/%{version}/etc/charsets/MULE-uviscii.map
%{_datadir}/emacs/%{version}/etc/charsets/NEXTSTEP.map
%{_datadir}/emacs/%{version}/etc/charsets/PTCP154.map
%doc %{_datadir}/emacs/%{version}/etc/charsets/README
%{_datadir}/emacs/%{version}/etc/charsets/TIS-620.map
%{_datadir}/emacs/%{version}/etc/charsets/VISCII.map
%{_datadir}/emacs/%{version}/etc/charsets/VSCII-2.map
%{_datadir}/emacs/%{version}/etc/charsets/VSCII.map
%{_datadir}/emacs/%{version}/etc/charsets/stdenc.map
%{_datadir}/emacs/%{version}/etc/charsets/symbol.map
%{_datadir}/emacs/%{version}/etc/compilation.txt
%dir %{_datadir}/emacs/%{version}/etc/e/
%doc %{_datadir}/emacs/%{version}/etc/e/README
%{_datadir}/emacs/%{version}/etc/e/eterm-color
%{_datadir}/emacs/%{version}/etc/e/eterm-color.ti
%{_datadir}/emacs/%{version}/etc/edt-user.el
%{_datadir}/emacs/%{version}/etc/emacs-buffer.gdb
%{_datadir}/emacs/%{version}/etc/emacs.appdata.xml
%{_datadir}/emacs/%{version}/etc/emacs.icon
%{_datadir}/emacs/%{version}/etc/emacs.service
%{_datadir}/emacs/%{version}/etc/enriched.txt
%dir %{_datadir}/emacs/%{version}/etc/forms/
%doc %{_datadir}/emacs/%{version}/etc/forms/README
%{_datadir}/emacs/%{version}/etc/forms/forms-d2.dat
%{_datadir}/emacs/%{version}/etc/forms/forms-d2.el
%{_datadir}/emacs/%{version}/etc/forms/forms-pass.el
%{_datadir}/emacs/%{version}/etc/future-bug
%{_datadir}/emacs/%{version}/etc/gnus-tut.txt
%dir %{_datadir}/emacs/%{version}/etc/gnus/
%{_datadir}/emacs/%{version}/etc/gnus/gnus-setup.ast
%{_datadir}/emacs/%{version}/etc/gnus/news-server.ast
%{_datadir}/emacs/%{version}/etc/grep.txt
%dir %{_datadir}/emacs/%{version}/etc/images/
%doc %{_datadir}/emacs/%{version}/etc/images/README
%{_datadir}/emacs/%{version}/etc/images/attach.pbm
%{_datadir}/emacs/%{version}/etc/images/attach.xpm
%{_datadir}/emacs/%{version}/etc/images/back-arrow.pbm
%{_datadir}/emacs/%{version}/etc/images/back-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/bookmark_add.pbm
%{_datadir}/emacs/%{version}/etc/images/bookmark_add.xpm
%{_datadir}/emacs/%{version}/etc/images/cancel.pbm
%{_datadir}/emacs/%{version}/etc/images/cancel.xpm
%{_datadir}/emacs/%{version}/etc/images/checked.xpm
%{_datadir}/emacs/%{version}/etc/images/close.pbm
%{_datadir}/emacs/%{version}/etc/images/close.xpm
%{_datadir}/emacs/%{version}/etc/images/connect.pbm
%{_datadir}/emacs/%{version}/etc/images/connect.xpm
%{_datadir}/emacs/%{version}/etc/images/contact.pbm
%{_datadir}/emacs/%{version}/etc/images/contact.xpm
%{_datadir}/emacs/%{version}/etc/images/copy.pbm
%{_datadir}/emacs/%{version}/etc/images/copy.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/custom/
%doc %{_datadir}/emacs/%{version}/etc/images/custom/README
%{_datadir}/emacs/%{version}/etc/images/custom/down-pushed.pbm
%{_datadir}/emacs/%{version}/etc/images/custom/down-pushed.xpm
%{_datadir}/emacs/%{version}/etc/images/custom/down.pbm
%{_datadir}/emacs/%{version}/etc/images/custom/down.xpm
%{_datadir}/emacs/%{version}/etc/images/custom/right-pushed.pbm
%{_datadir}/emacs/%{version}/etc/images/custom/right-pushed.xpm
%{_datadir}/emacs/%{version}/etc/images/custom/right.pbm
%{_datadir}/emacs/%{version}/etc/images/custom/right.xpm
%{_datadir}/emacs/%{version}/etc/images/cut.pbm
%{_datadir}/emacs/%{version}/etc/images/cut.xpm
%{_datadir}/emacs/%{version}/etc/images/data-save.pbm
%{_datadir}/emacs/%{version}/etc/images/data-save.xpm
%{_datadir}/emacs/%{version}/etc/images/delete.pbm
%{_datadir}/emacs/%{version}/etc/images/delete.xpm
%{_datadir}/emacs/%{version}/etc/images/describe.pbm
%{_datadir}/emacs/%{version}/etc/images/describe.xpm
%{_datadir}/emacs/%{version}/etc/images/diropen.pbm
%{_datadir}/emacs/%{version}/etc/images/diropen.xpm
%{_datadir}/emacs/%{version}/etc/images/disconnect.pbm
%{_datadir}/emacs/%{version}/etc/images/disconnect.xpm
%{_datadir}/emacs/%{version}/etc/images/exit.pbm
%{_datadir}/emacs/%{version}/etc/images/exit.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/ezimage/
%doc %{_datadir}/emacs/%{version}/etc/images/ezimage/README
%{_datadir}/emacs/%{version}/etc/images/ezimage/bits.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/bits.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/bitsbang.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/bitsbang.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/box-minus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/box-minus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/box-plus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/box-plus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/box.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/box.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/checkmark.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/checkmark.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/dir-minus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/dir-minus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/dir-plus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/dir-plus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/dir.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/dir.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/doc-minus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/doc-minus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/doc-plus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/doc-plus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/doc.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/doc.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/info.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/info.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/key.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/key.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/label.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/label.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/lock.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/lock.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/mail.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/mail.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/page-minus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/page-minus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/page-plus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/page-plus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/page.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/page.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-gt.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-gt.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-minus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-minus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-plus.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-plus.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-type.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-type.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-v.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag-v.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/tag.xpm
%{_datadir}/emacs/%{version}/etc/images/ezimage/unlock.pbm
%{_datadir}/emacs/%{version}/etc/images/ezimage/unlock.xpm
%{_datadir}/emacs/%{version}/etc/images/fwd-arrow.pbm
%{_datadir}/emacs/%{version}/etc/images/fwd-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus.pbm
%dir %{_datadir}/emacs/%{version}/etc/images/gnus/
%doc %{_datadir}/emacs/%{version}/etc/images/gnus/README
%{_datadir}/emacs/%{version}/etc/images/gnus/catchup.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/catchup.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/cu-exit.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/cu-exit.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/describe-group.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/describe-group.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/exit-gnus.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/exit-gnus.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/exit-summ.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/exit-summ.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/followup.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/followup.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/fuwo.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/fuwo.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/get-news.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/get-news.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/gnntg.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/gnntg.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/gnus-pointer.xbm
%{_datadir}/emacs/%{version}/etc/images/gnus/gnus-pointer.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/gnus.png
%{_datadir}/emacs/%{version}/etc/images/gnus/gnus.svg
%{_datadir}/emacs/%{version}/etc/images/gnus/gnus.xbm
%{_datadir}/emacs/%{version}/etc/images/gnus/gnus.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/important.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/important.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/kill-group.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/kill-group.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/mail-reply.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/mail-reply.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/mail-send.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/mail-send.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/next-ur.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/next-ur.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/post.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/post.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/prev-ur.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/prev-ur.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/preview.xbm
%{_datadir}/emacs/%{version}/etc/images/gnus/preview.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/receipt.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/receipt.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/reply-wo.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/reply-wo.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/reply.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/reply.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/rot13.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/rot13.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/save-aif.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/save-aif.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/save-art.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/save-art.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/subscribe.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/subscribe.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/toggle-subscription.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/toggle-subscription.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/unimportant.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/unimportant.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/unsubscribe.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/unsubscribe.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/uu-decode.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/uu-decode.xpm
%{_datadir}/emacs/%{version}/etc/images/gnus/uu-post.pbm
%{_datadir}/emacs/%{version}/etc/images/gnus/uu-post.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/gud/
%doc %{_datadir}/emacs/%{version}/etc/images/gud/README
%{_datadir}/emacs/%{version}/etc/images/gud/all.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/all.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/break.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/break.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/cont.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/cont.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/down.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/down.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/finish.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/finish.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/go.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/go.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/next.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/next.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/nexti.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/nexti.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/pp.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/pp.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/print.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/print.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/pstar.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/pstar.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/rcont.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/rcont.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/recstart.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/recstart.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/recstop.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/recstop.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/remove.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/remove.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/rfinish.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/rfinish.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/rnext.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/rnext.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/rnexti.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/rnexti.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/rstep.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/rstep.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/rstepi.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/rstepi.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/run.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/run.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/step.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/step.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/stepi.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/stepi.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/stop.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/stop.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/thread.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/thread.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/until.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/until.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/up.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/up.xpm
%{_datadir}/emacs/%{version}/etc/images/gud/watch.pbm
%{_datadir}/emacs/%{version}/etc/images/gud/watch.xpm
%{_datadir}/emacs/%{version}/etc/images/help.pbm
%{_datadir}/emacs/%{version}/etc/images/help.xpm
%{_datadir}/emacs/%{version}/etc/images/home.pbm
%{_datadir}/emacs/%{version}/etc/images/home.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/icons/
%doc %{_datadir}/emacs/%{version}/etc/images/icons/README
%dir %{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/closed.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/closed.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/empty.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/empty.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/end-connector.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/end-connector.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/extender-connector.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/extender-connector.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/leaf.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/leaf.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/locked-encrypted.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/locked-encrypted.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/mid-connector.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/mid-connector.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/opened.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/opened.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/skip-descender.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/skip-descender.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/through-descender.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/through-descender.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/unlocked-encrypted.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/dark-bg/unlocked-encrypted.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/closed.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/closed.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/empty.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/empty.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/end-connector.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/end-connector.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/extender-connector.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/extender-connector.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/leaf.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/leaf.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/locked-encrypted.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/locked-encrypted.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/mid-connector.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/mid-connector.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/opened.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/opened.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/skip-descender.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/skip-descender.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/through-descender.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/through-descender.xpm
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/unlocked-encrypted.png
%{_datadir}/emacs/%{version}/etc/images/icons/allout-widgets/light-bg/unlocked-encrypted.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/128x128/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/128x128/apps/
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/128x128/apps/emacs.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/128x128/apps/emacs23.png
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/16x16/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/16x16/apps/
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/16x16/apps/emacs.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/16x16/apps/emacs22.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/16x16/apps/emacs23.png
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/24x24/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/24x24/apps/
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/24x24/apps/emacs.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/24x24/apps/emacs22.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/24x24/apps/emacs23.png
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/32x32/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/32x32/apps/
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/32x32/apps/emacs.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/32x32/apps/emacs22.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/32x32/apps/emacs23.png
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/48x48/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/48x48/apps/
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/48x48/apps/emacs.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/48x48/apps/emacs22.png
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/48x48/apps/emacs23.png
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/apps/
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/apps/emacs.svg
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/apps/emacs23.svg
%dir %{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/mimetypes/
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/mimetypes/emacs-document.svg
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/mimetypes/emacs-document23.svg
%{_datadir}/emacs/%{version}/etc/images/index.pbm
%{_datadir}/emacs/%{version}/etc/images/index.xpm
%{_datadir}/emacs/%{version}/etc/images/info.pbm
%{_datadir}/emacs/%{version}/etc/images/info.xpm
%{_datadir}/emacs/%{version}/etc/images/jump-to.pbm
%{_datadir}/emacs/%{version}/etc/images/jump-to.xpm
%{_datadir}/emacs/%{version}/etc/images/left-arrow.pbm
%{_datadir}/emacs/%{version}/etc/images/left-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/letter.pbm
%{_datadir}/emacs/%{version}/etc/images/letter.xpm
%{_datadir}/emacs/%{version}/etc/images/lock-broken.pbm
%{_datadir}/emacs/%{version}/etc/images/lock-broken.xpm
%{_datadir}/emacs/%{version}/etc/images/lock-ok.pbm
%{_datadir}/emacs/%{version}/etc/images/lock-ok.xpm
%{_datadir}/emacs/%{version}/etc/images/lock.pbm
%{_datadir}/emacs/%{version}/etc/images/lock.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/low-color/
%doc %{_datadir}/emacs/%{version}/etc/images/low-color/README
%{_datadir}/emacs/%{version}/etc/images/low-color/back-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/copy.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/cut.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/fwd-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/help.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/home.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/index.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/jump-to.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/left-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/new.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/next-node.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/open.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/paste.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/preferences.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/prev-node.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/print.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/right-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/save.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/saveas.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/search.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/spell.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/undo.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/up-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/low-color/up-node.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/mail/
%doc %{_datadir}/emacs/%{version}/etc/images/mail/README
%{_datadir}/emacs/%{version}/etc/images/mail/compose.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/compose.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/copy.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/copy.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/flag-for-followup.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/flag-for-followup.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/forward.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/forward.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/inbox.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/inbox.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/move.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/move.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/not-spam.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/not-spam.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/outbox.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/outbox.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/preview.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/preview.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/repack.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/repack.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/reply-all.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/reply-all.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/reply-from.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/reply-from.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/reply-to.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/reply-to.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/reply.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/reply.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/save-draft.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/save-draft.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/save.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/send.pbm
%{_datadir}/emacs/%{version}/etc/images/mail/send.xpm
%{_datadir}/emacs/%{version}/etc/images/mail/spam.xpm
%{_datadir}/emacs/%{version}/etc/images/mh-logo.pbm
%{_datadir}/emacs/%{version}/etc/images/mh-logo.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/mpc/
%doc %{_datadir}/emacs/%{version}/etc/images/mpc/README
%{_datadir}/emacs/%{version}/etc/images/mpc/add.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/add.xpm
%{_datadir}/emacs/%{version}/etc/images/mpc/ffwd.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/ffwd.xpm
%{_datadir}/emacs/%{version}/etc/images/mpc/next.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/next.xpm
%{_datadir}/emacs/%{version}/etc/images/mpc/pause.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/pause.xpm
%{_datadir}/emacs/%{version}/etc/images/mpc/play.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/play.xpm
%{_datadir}/emacs/%{version}/etc/images/mpc/prev.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/prev.xpm
%{_datadir}/emacs/%{version}/etc/images/mpc/rewind.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/rewind.xpm
%{_datadir}/emacs/%{version}/etc/images/mpc/stop.pbm
%{_datadir}/emacs/%{version}/etc/images/mpc/stop.xpm
%{_datadir}/emacs/%{version}/etc/images/new.pbm
%{_datadir}/emacs/%{version}/etc/images/new.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/newsticker/
%doc %{_datadir}/emacs/%{version}/etc/images/newsticker/README
%{_datadir}/emacs/%{version}/etc/images/newsticker/browse-url.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/get-all.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/mark-immortal.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/mark-read.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/narrow.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/next-feed.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/next-item.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/prev-feed.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/prev-item.xpm
%{_datadir}/emacs/%{version}/etc/images/newsticker/rss-feed.png
%{_datadir}/emacs/%{version}/etc/images/newsticker/rss-feed.svg
%{_datadir}/emacs/%{version}/etc/images/newsticker/update.xpm
%{_datadir}/emacs/%{version}/etc/images/next-node.pbm
%{_datadir}/emacs/%{version}/etc/images/next-node.xpm
%{_datadir}/emacs/%{version}/etc/images/next-page.pbm
%{_datadir}/emacs/%{version}/etc/images/next-page.xpm
%{_datadir}/emacs/%{version}/etc/images/open.pbm
%{_datadir}/emacs/%{version}/etc/images/open.xpm
%{_datadir}/emacs/%{version}/etc/images/paste.pbm
%{_datadir}/emacs/%{version}/etc/images/paste.xpm
%{_datadir}/emacs/%{version}/etc/images/preferences.pbm
%{_datadir}/emacs/%{version}/etc/images/preferences.xpm
%{_datadir}/emacs/%{version}/etc/images/prev-node.pbm
%{_datadir}/emacs/%{version}/etc/images/prev-node.xpm
%{_datadir}/emacs/%{version}/etc/images/print.pbm
%{_datadir}/emacs/%{version}/etc/images/print.xpm
%{_datadir}/emacs/%{version}/etc/images/redo.pbm
%{_datadir}/emacs/%{version}/etc/images/redo.xpm
%{_datadir}/emacs/%{version}/etc/images/refresh.pbm
%{_datadir}/emacs/%{version}/etc/images/refresh.xpm
%{_datadir}/emacs/%{version}/etc/images/right-arrow.pbm
%{_datadir}/emacs/%{version}/etc/images/right-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/save.pbm
%{_datadir}/emacs/%{version}/etc/images/save.xpm
%{_datadir}/emacs/%{version}/etc/images/saveas.pbm
%{_datadir}/emacs/%{version}/etc/images/saveas.xpm
%{_datadir}/emacs/%{version}/etc/images/search-replace.pbm
%{_datadir}/emacs/%{version}/etc/images/search-replace.xpm
%{_datadir}/emacs/%{version}/etc/images/search.pbm
%{_datadir}/emacs/%{version}/etc/images/search.xpm
%{_datadir}/emacs/%{version}/etc/images/separator.pbm
%{_datadir}/emacs/%{version}/etc/images/separator.xpm
%{_datadir}/emacs/%{version}/etc/images/show.pbm
%{_datadir}/emacs/%{version}/etc/images/show.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/smilies/
%doc %{_datadir}/emacs/%{version}/etc/images/smilies/README
%{_datadir}/emacs/%{version}/etc/images/smilies/blink.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/blink.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/braindamaged.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/braindamaged.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/cry.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/cry.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/dead.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/dead.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/evil.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/evil.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/forced.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/forced.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/frown.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/frown.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/
%doc %{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/README
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/blink.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/braindamaged.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/cry.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/dead.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/evil.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/forced.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/frown.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/grin.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/indifferent.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/reverse-smile.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/sad.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/smile.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grayscale/wry.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/grin.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/grin.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/indifferent.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/indifferent.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/smilies/medium/
%doc %{_datadir}/emacs/%{version}/etc/images/smilies/medium/README
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/blink.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/braindamaged.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/cry.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/dead.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/evil.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/forced.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/frown.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/grin.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/indifferent.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/reverse-smile.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/sad.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/smile.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/medium/wry.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/sad.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/sad.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/smile.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/smile.xpm
%{_datadir}/emacs/%{version}/etc/images/smilies/wry.pbm
%{_datadir}/emacs/%{version}/etc/images/smilies/wry.xpm
%{_datadir}/emacs/%{version}/etc/images/sort-ascending.pbm
%{_datadir}/emacs/%{version}/etc/images/sort-ascending.xpm
%{_datadir}/emacs/%{version}/etc/images/sort-column-ascending.pbm
%{_datadir}/emacs/%{version}/etc/images/sort-column-ascending.xpm
%{_datadir}/emacs/%{version}/etc/images/sort-criteria.pbm
%{_datadir}/emacs/%{version}/etc/images/sort-criteria.xpm
%{_datadir}/emacs/%{version}/etc/images/sort-descending.pbm
%{_datadir}/emacs/%{version}/etc/images/sort-descending.xpm
%{_datadir}/emacs/%{version}/etc/images/sort-row-ascending.pbm
%{_datadir}/emacs/%{version}/etc/images/sort-row-ascending.xpm
%{_datadir}/emacs/%{version}/etc/images/spell.pbm
%{_datadir}/emacs/%{version}/etc/images/spell.xpm
%{_datadir}/emacs/%{version}/etc/images/splash.pbm
%{_datadir}/emacs/%{version}/etc/images/splash.png
%{_datadir}/emacs/%{version}/etc/images/splash.svg
%{_datadir}/emacs/%{version}/etc/images/splash.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/tree-widget/
%dir %{_datadir}/emacs/%{version}/etc/images/tree-widget/default/
%doc %{_datadir}/emacs/%{version}/etc/images/tree-widget/default/README
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/close.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/close.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/empty.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/empty.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/end-guide.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/end-guide.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/guide.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/guide.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/handle.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/handle.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/leaf.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/leaf.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/no-guide.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/no-guide.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/no-handle.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/no-handle.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/open.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/default/open.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/
%doc %{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/README
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/close.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/close.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/empty.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/empty.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/end-guide.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/end-guide.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/guide.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/guide.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/handle.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/handle.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/leaf.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/leaf.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/no-guide.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/no-guide.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/no-handle.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/no-handle.xpm
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/open.png
%{_datadir}/emacs/%{version}/etc/images/tree-widget/folder/open.xpm
%{_datadir}/emacs/%{version}/etc/images/unchecked.pbm
%{_datadir}/emacs/%{version}/etc/images/unchecked.xpm
%{_datadir}/emacs/%{version}/etc/images/undo.pbm
%{_datadir}/emacs/%{version}/etc/images/undo.xpm
%{_datadir}/emacs/%{version}/etc/images/up-arrow.pbm
%{_datadir}/emacs/%{version}/etc/images/up-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/up-node.pbm
%{_datadir}/emacs/%{version}/etc/images/up-node.xpm
%{_datadir}/emacs/%{version}/etc/images/zoom-in.pbm
%{_datadir}/emacs/%{version}/etc/images/zoom-in.xpm
%{_datadir}/emacs/%{version}/etc/images/zoom-out.pbm
%{_datadir}/emacs/%{version}/etc/images/zoom-out.xpm
%dir %{_datadir}/emacs/%{version}/etc/nxml/
%doc %{_datadir}/emacs/%{version}/etc/nxml/README
%{_datadir}/emacs/%{version}/etc/nxml/test-invalid.xml
%{_datadir}/emacs/%{version}/etc/nxml/test-valid.xml
%dir %{_datadir}/emacs/%{version}/etc/org/
%{_datadir}/emacs/%{version}/etc/org/OrgOdtContentTemplate.xml
%{_datadir}/emacs/%{version}/etc/org/OrgOdtStyles.xml
%doc %{_datadir}/emacs/%{version}/etc/org/README
%{_datadir}/emacs/%{version}/etc/package-keyring.gpg
%{_datadir}/emacs/%{version}/etc/ps-prin0.ps
%{_datadir}/emacs/%{version}/etc/ps-prin1.ps
%{_datadir}/emacs/%{version}/etc/publicsuffix.txt.gz
%dir %{_datadir}/emacs/%{version}/etc/refcards/
%{_datadir}/emacs/%{version}/etc/refcards/Makefile
%doc %{_datadir}/emacs/%{version}/etc/refcards/README
%doc %{_datadir}/emacs/%{version}/etc/refcards/calccard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/calccard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/cs-dired-ref.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/cs-dired-ref.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/cs-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/cs-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/cs-survival.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/cs-survival.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/de-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/de-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/dired-ref.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/dired-ref.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/emacsver.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/fr-dired-ref.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/fr-dired-ref.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/fr-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/fr-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/fr-survival.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/fr-survival.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/gnus-booklet.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/gnus-logo.eps
%doc %{_datadir}/emacs/%{version}/etc/refcards/gnus-logo.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/gnus-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/gnus-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/orgcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/orgcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/pdflayout.sty
%doc %{_datadir}/emacs/%{version}/etc/refcards/pl-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/pl-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/pt-br-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/pt-br-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/ru-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/ru-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/sk-dired-ref.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/sk-dired-ref.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/sk-refcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/sk-refcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/sk-survival.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/sk-survival.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/survival.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/survival.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/vipcard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/vipcard.tex
%doc %{_datadir}/emacs/%{version}/etc/refcards/viperCard.pdf
%doc %{_datadir}/emacs/%{version}/etc/refcards/viperCard.tex
%{_datadir}/emacs/%{version}/etc/rgb.txt
%dir %{_datadir}/emacs/%{version}/etc/schema/
%doc %{_datadir}/emacs/%{version}/etc/schema/README
%{_datadir}/emacs/%{version}/etc/schema/calstbl.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbcalstbl.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbhier.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbnotn.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbpool.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbstart.rnc
%{_datadir}/emacs/%{version}/etc/schema/docbook.rnc
%{_datadir}/emacs/%{version}/etc/schema/locate.rnc
%{_datadir}/emacs/%{version}/etc/schema/od-manifest-schema-v1.2-os.rnc
%{_datadir}/emacs/%{version}/etc/schema/od-schema-v1.2-os.rnc
%{_datadir}/emacs/%{version}/etc/schema/rdfxml.rnc
%{_datadir}/emacs/%{version}/etc/schema/relaxng.rnc
%{_datadir}/emacs/%{version}/etc/schema/schemas.xml
%{_datadir}/emacs/%{version}/etc/schema/xhtml-applet.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-attribs.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-base.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-bdo.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-bform.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-btable.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-csismap.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-datatypes.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-edit.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-events.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-form.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-frames.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-hypertext.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-iframe.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-image.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-inlstyle.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-legacy.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-link.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-lst.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-meta.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-nameident.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-object.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-param.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-pres.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-ruby.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-script.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-ssismap.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-struct.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-table.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-text.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-tgt.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml-xstyle.rnc
%{_datadir}/emacs/%{version}/etc/schema/xhtml.rnc
%{_datadir}/emacs/%{version}/etc/schema/xslt.rnc
%{_datadir}/emacs/%{version}/etc/ses-example.ses
%{_datadir}/emacs/%{version}/etc/spook.lines
%dir %{_datadir}/emacs/%{version}/etc/srecode/
%{_datadir}/emacs/%{version}/etc/srecode/c.srt
%{_datadir}/emacs/%{version}/etc/srecode/cpp.srt
%{_datadir}/emacs/%{version}/etc/srecode/default.srt
%{_datadir}/emacs/%{version}/etc/srecode/doc-cpp.srt
%{_datadir}/emacs/%{version}/etc/srecode/doc-default.srt
%{_datadir}/emacs/%{version}/etc/srecode/doc-java.srt
%{_datadir}/emacs/%{version}/etc/srecode/ede-autoconf.srt
%{_datadir}/emacs/%{version}/etc/srecode/ede-make.srt
%{_datadir}/emacs/%{version}/etc/srecode/el.srt
%{_datadir}/emacs/%{version}/etc/srecode/getset-cpp.srt
%{_datadir}/emacs/%{version}/etc/srecode/java.srt
%{_datadir}/emacs/%{version}/etc/srecode/make.srt
%{_datadir}/emacs/%{version}/etc/srecode/template.srt
%{_datadir}/emacs/%{version}/etc/srecode/test.srt
%{_datadir}/emacs/%{version}/etc/srecode/texi.srt
%{_datadir}/emacs/%{version}/etc/srecode/wisent.srt
%dir %{_datadir}/emacs/%{version}/etc/themes/
%{_datadir}/emacs/%{version}/etc/themes/adwaita-theme.el
%{_datadir}/emacs/%{version}/etc/themes/deeper-blue-theme.el
%{_datadir}/emacs/%{version}/etc/themes/dichromacy-theme.el
%{_datadir}/emacs/%{version}/etc/themes/leuven-theme.el
%{_datadir}/emacs/%{version}/etc/themes/light-blue-theme.el
%{_datadir}/emacs/%{version}/etc/themes/manoj-dark-theme.el
%{_datadir}/emacs/%{version}/etc/themes/misterioso-theme.el
%{_datadir}/emacs/%{version}/etc/themes/tango-dark-theme.el
%{_datadir}/emacs/%{version}/etc/themes/tango-theme.el
%{_datadir}/emacs/%{version}/etc/themes/tsdh-dark-theme.el
%{_datadir}/emacs/%{version}/etc/themes/tsdh-light-theme.el
%{_datadir}/emacs/%{version}/etc/themes/wheatgrass-theme.el
%{_datadir}/emacs/%{version}/etc/themes/whiteboard-theme.el
%{_datadir}/emacs/%{version}/etc/themes/wombat-theme.el
%dir %{_datadir}/emacs/%{version}/etc/tutorials/
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.bg
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.cn
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.cs
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.de
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.eo
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.es
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.fr
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.he
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.it
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.ja
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.ko
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.nl
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.pl
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.pt_BR
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.ro
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.ru
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.sk
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.sl
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.sv
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.th
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.translators
%{_datadir}/emacs/%{version}/etc/tutorials/TUTORIAL.zh
%{_datadir}/emacs/%{version}/etc/yow.lines
%dir %{_datadir}/emacs/%{version}/lisp/
%{_datadir}/emacs/%{version}/lisp/COPYING
%doc %{_datadir}/emacs/%{version}/lisp/README
%{_datadir}/emacs/%{version}/lisp/abbrev.elc
%{_datadir}/emacs/%{version}/lisp/align.elc
%{_datadir}/emacs/%{version}/lisp/allout-widgets.elc
%{_datadir}/emacs/%{version}/lisp/allout.elc
%{_datadir}/emacs/%{version}/lisp/ansi-color.elc
%{_datadir}/emacs/%{version}/lisp/apropos.elc
%{_datadir}/emacs/%{version}/lisp/arc-mode.elc
%{_datadir}/emacs/%{version}/lisp/array.elc
%{_datadir}/emacs/%{version}/lisp/auth-source-pass.elc
%{_datadir}/emacs/%{version}/lisp/auth-source.elc
%{_datadir}/emacs/%{version}/lisp/autoarg.elc
%{_datadir}/emacs/%{version}/lisp/autoinsert.elc
%{_datadir}/emacs/%{version}/lisp/autorevert.elc
%{_datadir}/emacs/%{version}/lisp/avoid.elc
%{_datadir}/emacs/%{version}/lisp/battery.elc
%{_datadir}/emacs/%{version}/lisp/bindings.el
%{_datadir}/emacs/%{version}/lisp/bookmark.elc
%{_datadir}/emacs/%{version}/lisp/bs.elc
%{_datadir}/emacs/%{version}/lisp/buff-menu.elc
%{_datadir}/emacs/%{version}/lisp/button.elc
%dir %{_datadir}/emacs/%{version}/lisp/calc/
%{_datadir}/emacs/%{version}/lisp/calc/calc-aent.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-alg.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-arith.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-bin.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-comb.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-cplx.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-embed.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-ext.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-fin.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-forms.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-frac.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-funcs.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-graph.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-help.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-incom.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-keypd.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-lang.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/calc/calc-macs.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-map.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-math.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-menu.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-misc.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-mode.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-mtx.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-nlfit.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-poly.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-prog.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-rewr.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-rules.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-sel.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-stat.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-store.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-stuff.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-trail.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-undo.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-units.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-vec.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc-yank.elc
%{_datadir}/emacs/%{version}/lisp/calc/calc.elc
%{_datadir}/emacs/%{version}/lisp/calc/calcalg2.elc
%{_datadir}/emacs/%{version}/lisp/calc/calcalg3.elc
%{_datadir}/emacs/%{version}/lisp/calc/calccomp.elc
%{_datadir}/emacs/%{version}/lisp/calc/calcsel2.elc
%{_datadir}/emacs/%{version}/lisp/calculator.elc
%dir %{_datadir}/emacs/%{version}/lisp/calendar/
%{_datadir}/emacs/%{version}/lisp/calendar/appt.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-bahai.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-china.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-coptic.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-dst.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-french.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-hebrew.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-html.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-islam.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-iso.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-julian.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/calendar/cal-mayan.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-menu.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-move.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-persia.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-tex.elc
%{_datadir}/emacs/%{version}/lisp/calendar/cal-x.elc
%{_datadir}/emacs/%{version}/lisp/calendar/calendar.elc
%{_datadir}/emacs/%{version}/lisp/calendar/diary-lib.elc
%{_datadir}/emacs/%{version}/lisp/calendar/diary-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/calendar/hol-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/calendar/holidays.elc
%{_datadir}/emacs/%{version}/lisp/calendar/icalendar.elc
%{_datadir}/emacs/%{version}/lisp/calendar/lunar.elc
%{_datadir}/emacs/%{version}/lisp/calendar/parse-time.elc
%{_datadir}/emacs/%{version}/lisp/calendar/solar.elc
%{_datadir}/emacs/%{version}/lisp/calendar/time-date.elc
%{_datadir}/emacs/%{version}/lisp/calendar/timeclock.elc
%{_datadir}/emacs/%{version}/lisp/calendar/todo-mode.elc
%{_datadir}/emacs/%{version}/lisp/case-table.elc
%{_datadir}/emacs/%{version}/lisp/cdl.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-cscope.elc
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-files.elc
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-global.elc
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-idutils.elc
%{_datadir}/emacs/%{version}/lisp/cedet/cedet.elc
%{_datadir}/emacs/%{version}/lisp/cedet/data-debug.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/ede/
%{_datadir}/emacs/%{version}/lisp/cedet/ede/auto.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/autoconf-edit.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/base.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/config.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/cpp-root.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/custom.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/detect.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/dired.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/emacs.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/files.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/generic.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/linux.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/loaddefs.el
%{_datadir}/emacs/%{version}/lisp/cedet/ede/locate.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/make.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/makefile-edit.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/pconf.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/pmake.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-archive.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-aux.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-comp.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-elisp.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-info.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-misc.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-obj.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-prog.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-scheme.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-shared.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/project-am.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/shell.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/simple.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/source.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/speedbar.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/srecode.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/system.elc
%{_datadir}/emacs/%{version}/lisp/cedet/ede/util.elc
%{_datadir}/emacs/%{version}/lisp/cedet/inversion.elc
%{_datadir}/emacs/%{version}/lisp/cedet/mode-local.elc
%{_datadir}/emacs/%{version}/lisp/cedet/pulse.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/semantic/
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/complete.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/debug.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/fcn.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/refs.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/c-by.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/c.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/debug.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/el.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/gcc.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/grammar.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/make-by.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/make.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/scm-by.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/scm.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/chart.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/complete.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ctxt.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-debug.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-ebrowse.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-el.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-file.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-find.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-global.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-javascript.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-mode.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-ref.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-typecache.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/debug.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate/
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate/include.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate/mode.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/dep.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/doc.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ede-grammar.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/edit.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/find.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/format.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/fw.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grammar-wy.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grammar.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/html.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ia-sb.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ia.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/idle.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/imenu.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/java.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/lex-spp.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/lex.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/loaddefs.el
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/mru-bookmark.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/sb.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/scope.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/senator.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/sort.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/cscope.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/filter.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/global.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/grep.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/idutils.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/list.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-file.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-ls.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-write.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/texi.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/util-modes.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/util.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/comp.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/grammar.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/java-tags.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/javascript.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/javat-wy.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/js-wy.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/python-wy.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/python.elc
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/wisent.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/srecode/
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/args.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/compile.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/cpp.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/ctxt.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/dictionary.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/document.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/el.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/expandproto.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/extract.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/fields.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/filters.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/find.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/getset.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/insert.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/java.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/loaddefs.el
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/map.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/mode.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/semantic.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt-mode.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt-wy.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/table.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/template.elc
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/texi.elc
%{_datadir}/emacs/%{version}/lisp/char-fold.elc
%{_datadir}/emacs/%{version}/lisp/chistory.elc
%{_datadir}/emacs/%{version}/lisp/cmuscheme.elc
%{_datadir}/emacs/%{version}/lisp/color.elc
%{_datadir}/emacs/%{version}/lisp/comint.elc
%{_datadir}/emacs/%{version}/lisp/completion.elc
%{_datadir}/emacs/%{version}/lisp/composite.elc
%{_datadir}/emacs/%{version}/lisp/cus-dep.elc
%{_datadir}/emacs/%{version}/lisp/cus-edit.elc
%{_datadir}/emacs/%{version}/lisp/cus-face.elc
%{_datadir}/emacs/%{version}/lisp/cus-load.el
%{_datadir}/emacs/%{version}/lisp/cus-start.el
%{_datadir}/emacs/%{version}/lisp/cus-theme.elc
%{_datadir}/emacs/%{version}/lisp/custom.elc
%{_datadir}/emacs/%{version}/lisp/dabbrev.elc
%{_datadir}/emacs/%{version}/lisp/delim-col.elc
%{_datadir}/emacs/%{version}/lisp/delsel.elc
%{_datadir}/emacs/%{version}/lisp/descr-text.elc
%{_datadir}/emacs/%{version}/lisp/desktop.elc
%{_datadir}/emacs/%{version}/lisp/dframe.elc
%{_datadir}/emacs/%{version}/lisp/dired-aux.elc
%{_datadir}/emacs/%{version}/lisp/dired-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/dired-x.elc
%{_datadir}/emacs/%{version}/lisp/dired.elc
%{_datadir}/emacs/%{version}/lisp/dirtrack.elc
%{_datadir}/emacs/%{version}/lisp/display-line-numbers.elc
%{_datadir}/emacs/%{version}/lisp/disp-table.elc
%{_datadir}/emacs/%{version}/lisp/dnd.elc
%{_datadir}/emacs/%{version}/lisp/doc-view.elc
%{_datadir}/emacs/%{version}/lisp/dom.elc
%{_datadir}/emacs/%{version}/lisp/dos-fns.elc
%{_datadir}/emacs/%{version}/lisp/dos-vars.elc
%{_datadir}/emacs/%{version}/lisp/dos-w32.elc
%{_datadir}/emacs/%{version}/lisp/double.elc
%{_datadir}/emacs/%{version}/lisp/dynamic-setting.elc
%{_datadir}/emacs/%{version}/lisp/ebuff-menu.elc
%{_datadir}/emacs/%{version}/lisp/echistory.elc
%{_datadir}/emacs/%{version}/lisp/ecomplete.elc
%{_datadir}/emacs/%{version}/lisp/edmacro.elc
%{_datadir}/emacs/%{version}/lisp/ehelp.elc
%{_datadir}/emacs/%{version}/lisp/elec-pair.elc
%{_datadir}/emacs/%{version}/lisp/electric.elc
%{_datadir}/emacs/%{version}/lisp/elide-head.elc
%dir %{_datadir}/emacs/%{version}/lisp/emacs-lisp/
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/advice.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/autoload.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/avl-tree.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/backquote.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/benchmark.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/bindat.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/byte-opt.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/byte-run.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/bytecomp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cconv.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/chart.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/check-declare.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/checkdoc.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-extra.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-generic.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-indent.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-lib.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-macs.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-preloaded.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-print.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-seq.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/copyright.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/crm.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cursor-sensor.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/debug.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/derived.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/disass.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/easy-mmode.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/easymenu.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/edebug.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-base.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-compat.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-core.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-custom.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-datadebug.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-opt.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-speedbar.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eldoc.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/elint.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/elp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ert-x.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ert.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ewoc.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/find-func.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/float-sup.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generator.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generic.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/gv.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/helper.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/inline.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/let-alist.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mnt.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mode.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/macroexp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map-ynp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/nadvice.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/package-x.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/package.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/pcase.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/pp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/radix-tree.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/re-builder.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/regexp-opt.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/regi.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ring.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/rmc.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/rx.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/seq.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/shadow.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/smie.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/subr-x.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/syntax.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tabulated-list.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tcover-ses.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tcover-unsafep.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/testcover.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/thunk.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/timer.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/timer-list.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tq.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/trace.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/unsafep.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/warnings.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lock.elc
%dir %{_datadir}/emacs/%{version}/lisp/emulation/
%{_datadir}/emacs/%{version}/lisp/emulation/cua-base.elc
%{_datadir}/emacs/%{version}/lisp/emulation/cua-gmrk.elc
%{_datadir}/emacs/%{version}/lisp/emulation/cua-rect.elc
%{_datadir}/emacs/%{version}/lisp/emulation/edt-lk201.elc
%{_datadir}/emacs/%{version}/lisp/emulation/edt-mapper.elc
%{_datadir}/emacs/%{version}/lisp/emulation/edt-pc.elc
%{_datadir}/emacs/%{version}/lisp/emulation/edt-vt100.elc
%{_datadir}/emacs/%{version}/lisp/emulation/edt.elc
%{_datadir}/emacs/%{version}/lisp/emulation/keypad.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper-cmd.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper-ex.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper-init.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper-keym.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper-macs.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper-mous.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper-util.elc
%{_datadir}/emacs/%{version}/lisp/emulation/viper.elc
%{_datadir}/emacs/%{version}/lisp/env.elc
%{_datadir}/emacs/%{version}/lisp/epa-dired.elc
%{_datadir}/emacs/%{version}/lisp/epa-file.elc
%{_datadir}/emacs/%{version}/lisp/epa-hook.elc
%{_datadir}/emacs/%{version}/lisp/epa-mail.elc
%{_datadir}/emacs/%{version}/lisp/epa.elc
%{_datadir}/emacs/%{version}/lisp/epg-config.elc
%{_datadir}/emacs/%{version}/lisp/epg.elc
%dir %{_datadir}/emacs/%{version}/lisp/erc/
%{_datadir}/emacs/%{version}/lisp/erc/erc-autoaway.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-backend.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-button.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-capab.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-compat.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-dcc.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-desktop-notifications.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-ezbounce.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-fill.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-goodies.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-ibuffer.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-identd.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-imenu.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-join.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-lang.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-list.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-log.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-match.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-menu.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-netsplit.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-networks.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-notify.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-page.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-pcomplete.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-replace.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-ring.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-services.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-sound.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-speedbar.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-spelling.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-stamp.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-track.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-truncate.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc-xdcc.elc
%{_datadir}/emacs/%{version}/lisp/erc/erc.elc
%dir %{_datadir}/emacs/%{version}/lisp/eshell/
%{_datadir}/emacs/%{version}/lisp/eshell/em-alias.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-banner.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-basic.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-cmpl.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-dirs.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-glob.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-hist.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-ls.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-pred.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-prompt.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-rebind.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-script.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-smart.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-term.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-tramp.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-unix.elc
%{_datadir}/emacs/%{version}/lisp/eshell/em-xtra.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-arg.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-cmd.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-ext.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-groups.el
%{_datadir}/emacs/%{version}/lisp/eshell/esh-io.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-mode.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-module.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-opt.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-proc.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-util.elc
%{_datadir}/emacs/%{version}/lisp/eshell/esh-var.elc
%{_datadir}/emacs/%{version}/lisp/eshell/eshell.elc
%{_datadir}/emacs/%{version}/lisp/expand.elc
%{_datadir}/emacs/%{version}/lisp/ezimage.elc
%{_datadir}/emacs/%{version}/lisp/face-remap.elc
%{_datadir}/emacs/%{version}/lisp/facemenu.elc
%{_datadir}/emacs/%{version}/lisp/faces.elc
%{_datadir}/emacs/%{version}/lisp/ffap.elc
%{_datadir}/emacs/%{version}/lisp/filecache.elc
%{_datadir}/emacs/%{version}/lisp/filenotify.elc
%{_datadir}/emacs/%{version}/lisp/files-x.elc
%{_datadir}/emacs/%{version}/lisp/files.elc
%{_datadir}/emacs/%{version}/lisp/filesets.elc
%{_datadir}/emacs/%{version}/lisp/find-cmd.elc
%{_datadir}/emacs/%{version}/lisp/find-dired.elc
%{_datadir}/emacs/%{version}/lisp/find-file.elc
%{_datadir}/emacs/%{version}/lisp/find-lisp.elc
%{_datadir}/emacs/%{version}/lisp/finder-inf.el
%{_datadir}/emacs/%{version}/lisp/finder.elc
%{_datadir}/emacs/%{version}/lisp/flow-ctrl.elc
%{_datadir}/emacs/%{version}/lisp/foldout.elc
%{_datadir}/emacs/%{version}/lisp/follow.elc
%{_datadir}/emacs/%{version}/lisp/font-core.elc
%{_datadir}/emacs/%{version}/lisp/font-lock.elc
%{_datadir}/emacs/%{version}/lisp/format-spec.elc
%{_datadir}/emacs/%{version}/lisp/format.elc
%{_datadir}/emacs/%{version}/lisp/forms.elc
%{_datadir}/emacs/%{version}/lisp/frame.elc
%{_datadir}/emacs/%{version}/lisp/frameset.elc
%{_datadir}/emacs/%{version}/lisp/fringe.elc
%{_datadir}/emacs/%{version}/lisp/generic-x.el
%dir %{_datadir}/emacs/%{version}/lisp/gnus/
%{_datadir}/emacs/%{version}/lisp/gnus/.dir-locals.el
%{_datadir}/emacs/%{version}/lisp/gnus/canlock.elc
%{_datadir}/emacs/%{version}/lisp/gnus/deuglify.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gmm-utils.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-agent.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-art.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-async.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-bcklg.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-bookmark.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cache.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cite.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cloud.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cus.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-delay.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-demon.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-diary.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dired.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-draft.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dup.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-eform.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-fun.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-gravatar.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-group.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-html.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-icalendar.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-int.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-kill.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-logic.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-mh.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-ml.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-mlspl.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-msg.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-notifications.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-picon.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-range.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-registry.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-rfc1843.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-salt.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-score.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-sieve.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-spec.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-srvr.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-start.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-sum.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-topic.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-undo.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-util.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-uu.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-vm.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-win.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gnus.elc
%{_datadir}/emacs/%{version}/lisp/gnus/gssapi.elc
%{_datadir}/emacs/%{version}/lisp/gnus/legacy-gnus-agent.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mail-source.elc
%{_datadir}/emacs/%{version}/lisp/gnus/message.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-archive.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-bodies.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-decode.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-encode.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-extern.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-partial.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-url.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-util.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-uu.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mm-view.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mml-sec.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mml-smime.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mml.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mml1991.elc
%{_datadir}/emacs/%{version}/lisp/gnus/mml2015.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnagent.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnbabyl.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nndiary.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nndir.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nndoc.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nndraft.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nneething.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnfolder.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nngateway.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnheader.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnimap.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnir.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnmail.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnmaildir.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnmairix.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnmbox.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnmh.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnml.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnnil.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnoo.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnregistry.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnrss.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnspool.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nntp.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnvirtual.elc
%{_datadir}/emacs/%{version}/lisp/gnus/nnweb.elc
%{_datadir}/emacs/%{version}/lisp/gnus/score-mode.elc
%{_datadir}/emacs/%{version}/lisp/gnus/smiley.elc
%{_datadir}/emacs/%{version}/lisp/gnus/smime.elc
%{_datadir}/emacs/%{version}/lisp/gnus/spam-report.elc
%{_datadir}/emacs/%{version}/lisp/gnus/spam-stat.elc
%{_datadir}/emacs/%{version}/lisp/gnus/spam-wash.elc
%{_datadir}/emacs/%{version}/lisp/gnus/spam.elc
%{_datadir}/emacs/%{version}/lisp/help-at-pt.elc
%{_datadir}/emacs/%{version}/lisp/help-fns.elc
%{_datadir}/emacs/%{version}/lisp/help-macro.elc
%{_datadir}/emacs/%{version}/lisp/help-mode.elc
%{_datadir}/emacs/%{version}/lisp/help.elc
%{_datadir}/emacs/%{version}/lisp/hex-util.elc
%{_datadir}/emacs/%{version}/lisp/hexl.elc
%{_datadir}/emacs/%{version}/lisp/hfy-cmap.elc
%{_datadir}/emacs/%{version}/lisp/hi-lock.elc
%{_datadir}/emacs/%{version}/lisp/hilit-chg.elc
%{_datadir}/emacs/%{version}/lisp/hippie-exp.elc
%{_datadir}/emacs/%{version}/lisp/hl-line.elc
%{_datadir}/emacs/%{version}/lisp/htmlfontify.elc
%{_datadir}/emacs/%{version}/lisp/ibuf-ext.elc
%{_datadir}/emacs/%{version}/lisp/ibuf-macs.elc
%{_datadir}/emacs/%{version}/lisp/ibuffer.elc
%{_datadir}/emacs/%{version}/lisp/ibuffer-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/icomplete.elc
%{_datadir}/emacs/%{version}/lisp/ido.elc
%{_datadir}/emacs/%{version}/lisp/ielm.elc
%{_datadir}/emacs/%{version}/lisp/iimage.elc
%{_datadir}/emacs/%{version}/lisp/image-dired.elc
%{_datadir}/emacs/%{version}/lisp/image-file.elc
%{_datadir}/emacs/%{version}/lisp/image-mode.elc
%{_datadir}/emacs/%{version}/lisp/image.elc
%{_datadir}/emacs/%{version}/lisp/imenu.elc
%dir %{_datadir}/emacs/%{version}/lisp/image/
%{_datadir}/emacs/%{version}/lisp/image/compface.elc
%{_datadir}/emacs/%{version}/lisp/image/gravatar.elc
%{_datadir}/emacs/%{version}/lisp/indent.elc
%{_datadir}/emacs/%{version}/lisp/info-look.elc
%{_datadir}/emacs/%{version}/lisp/info-xref.elc
%{_datadir}/emacs/%{version}/lisp/info.elc
%{_datadir}/emacs/%{version}/lisp/informat.elc
%dir %{_datadir}/emacs/%{version}/lisp/international/
%{_datadir}/emacs/%{version}/lisp/international/ccl.elc
%{_datadir}/emacs/%{version}/lisp/international/characters.elc
%{_datadir}/emacs/%{version}/lisp/international/charprop.el
%{_datadir}/emacs/%{version}/lisp/international/charscript.elc
%{_datadir}/emacs/%{version}/lisp/international/cp51932.elc
%{_datadir}/emacs/%{version}/lisp/international/eucjp-ms.elc
%{_datadir}/emacs/%{version}/lisp/international/fontset.elc
%{_datadir}/emacs/%{version}/lisp/international/isearch-x.elc
%{_datadir}/emacs/%{version}/lisp/international/iso-ascii.elc
%{_datadir}/emacs/%{version}/lisp/international/iso-cvt.elc
%{_datadir}/emacs/%{version}/lisp/international/iso-transl.elc
%{_datadir}/emacs/%{version}/lisp/international/ja-dic-cnv.elc
%{_datadir}/emacs/%{version}/lisp/international/ja-dic-utl.elc
%{_datadir}/emacs/%{version}/lisp/international/kinsoku.elc
%{_datadir}/emacs/%{version}/lisp/international/kkc.elc
%{_datadir}/emacs/%{version}/lisp/international/latexenc.elc
%{_datadir}/emacs/%{version}/lisp/international/latin1-disp.elc
%{_datadir}/emacs/%{version}/lisp/international/mule-cmds.elc
%{_datadir}/emacs/%{version}/lisp/international/mule-conf.elc
%{_datadir}/emacs/%{version}/lisp/international/mule-diag.elc
%{_datadir}/emacs/%{version}/lisp/international/mule-util.elc
%{_datadir}/emacs/%{version}/lisp/international/mule.elc
%{_datadir}/emacs/%{version}/lisp/international/ogonek.elc
%{_datadir}/emacs/%{version}/lisp/international/quail.elc
%{_datadir}/emacs/%{version}/lisp/international/rfc1843.elc
%{_datadir}/emacs/%{version}/lisp/international/robin.elc
%{_datadir}/emacs/%{version}/lisp/international/titdic-cnv.elc
%{_datadir}/emacs/%{version}/lisp/international/ucs-normalize.elc
%{_datadir}/emacs/%{version}/lisp/international/uni-bidi.el
%{_datadir}/emacs/%{version}/lisp/international/uni-brackets.el
%{_datadir}/emacs/%{version}/lisp/international/uni-category.el
%{_datadir}/emacs/%{version}/lisp/international/uni-combining.el
%{_datadir}/emacs/%{version}/lisp/international/uni-comment.el
%{_datadir}/emacs/%{version}/lisp/international/uni-decimal.el
%{_datadir}/emacs/%{version}/lisp/international/uni-decomposition.el
%{_datadir}/emacs/%{version}/lisp/international/uni-digit.el
%{_datadir}/emacs/%{version}/lisp/international/uni-lowercase.el
%{_datadir}/emacs/%{version}/lisp/international/uni-mirrored.el
%{_datadir}/emacs/%{version}/lisp/international/uni-name.el
%{_datadir}/emacs/%{version}/lisp/international/uni-numeric.el
%{_datadir}/emacs/%{version}/lisp/international/uni-old-name.el
%{_datadir}/emacs/%{version}/lisp/international/uni-special-lowercase.el
%{_datadir}/emacs/%{version}/lisp/international/uni-special-titlecase.el
%{_datadir}/emacs/%{version}/lisp/international/uni-special-uppercase.el
%{_datadir}/emacs/%{version}/lisp/international/uni-titlecase.el
%{_datadir}/emacs/%{version}/lisp/international/uni-uppercase.el
%{_datadir}/emacs/%{version}/lisp/international/utf7.elc
%{_datadir}/emacs/%{version}/lisp/international/utf-7.elc
%{_datadir}/emacs/%{version}/lisp/isearch.elc
%{_datadir}/emacs/%{version}/lisp/isearchb.elc
%{_datadir}/emacs/%{version}/lisp/jit-lock.elc
%{_datadir}/emacs/%{version}/lisp/jka-cmpr-hook.elc
%{_datadir}/emacs/%{version}/lisp/jka-compr.elc
%{_datadir}/emacs/%{version}/lisp/json.elc
%{_datadir}/emacs/%{version}/lisp/htmlfontify-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/kermit.elc
%{_datadir}/emacs/%{version}/lisp/kmacro.elc
%dir %{_datadir}/emacs/%{version}/lisp/language/
%{_datadir}/emacs/%{version}/lisp/language/burmese.elc
%{_datadir}/emacs/%{version}/lisp/language/cham.elc
%{_datadir}/emacs/%{version}/lisp/language/china-util.elc
%{_datadir}/emacs/%{version}/lisp/language/chinese.elc
%{_datadir}/emacs/%{version}/lisp/language/cyril-util.elc
%{_datadir}/emacs/%{version}/lisp/language/cyrillic.elc
%{_datadir}/emacs/%{version}/lisp/language/czech.elc
%{_datadir}/emacs/%{version}/lisp/language/english.elc
%{_datadir}/emacs/%{version}/lisp/language/ethio-util.elc
%{_datadir}/emacs/%{version}/lisp/language/ethiopic.elc
%{_datadir}/emacs/%{version}/lisp/language/european.elc
%{_datadir}/emacs/%{version}/lisp/language/georgian.elc
%{_datadir}/emacs/%{version}/lisp/language/greek.elc
%{_datadir}/emacs/%{version}/lisp/language/hanja-util.elc
%{_datadir}/emacs/%{version}/lisp/language/hebrew.elc
%{_datadir}/emacs/%{version}/lisp/language/ind-util.elc
%{_datadir}/emacs/%{version}/lisp/language/indian.elc
%{_datadir}/emacs/%{version}/lisp/language/japan-util.elc
%{_datadir}/emacs/%{version}/lisp/language/japanese.elc
%{_datadir}/emacs/%{version}/lisp/language/khmer.elc
%{_datadir}/emacs/%{version}/lisp/language/korea-util.elc
%{_datadir}/emacs/%{version}/lisp/language/korean.elc
%{_datadir}/emacs/%{version}/lisp/language/lao-util.elc
%{_datadir}/emacs/%{version}/lisp/language/lao.elc
%{_datadir}/emacs/%{version}/lisp/language/misc-lang.elc
%{_datadir}/emacs/%{version}/lisp/language/romanian.elc
%{_datadir}/emacs/%{version}/lisp/language/sinhala.elc
%{_datadir}/emacs/%{version}/lisp/language/slovak.elc
%{_datadir}/emacs/%{version}/lisp/language/tai-viet.elc
%{_datadir}/emacs/%{version}/lisp/language/thai-util.elc
%{_datadir}/emacs/%{version}/lisp/language/thai-word.elc
%{_datadir}/emacs/%{version}/lisp/language/thai.elc
%{_datadir}/emacs/%{version}/lisp/language/tibet-util.elc
%{_datadir}/emacs/%{version}/lisp/language/tibetan.elc
%{_datadir}/emacs/%{version}/lisp/language/tv-util.elc
%{_datadir}/emacs/%{version}/lisp/language/utf-8-lang.elc
%{_datadir}/emacs/%{version}/lisp/language/viet-util.elc
%{_datadir}/emacs/%{version}/lisp/language/vietnamese.elc
%{_datadir}/emacs/%{version}/lisp/ldefs-boot.el
%dir %{_datadir}/emacs/%{version}/lisp/leim/
%dir %{_datadir}/emacs/%{version}/lisp/leim/ja-dic/
%{_datadir}/emacs/%{version}/lisp/leim/ja-dic/ja-dic.elc
%{_datadir}/emacs/%{version}/lisp/leim/leim-list.el
%dir %{_datadir}/emacs/%{version}/lisp/leim/quail/
%{_datadir}/emacs/%{version}/lisp/leim/quail/4Corner.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ARRAY30.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/CCDOSPY.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/CTLau-b5.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/CTLau.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ECDICT.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ETZY.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/PY-b5.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/PY.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/Punct-b5.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/Punct.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/QJ-b5.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/QJ.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/SW.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/TONEPY.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ZIRANMA.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ZOZY.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/arabic.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/croatian.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/cyril-jis.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/cyrillic.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/czech.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ethiopic.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/georgian.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/greek.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/hangul.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja-jis.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja3.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/hebrew.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/indian.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ipa-praat.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/ipa.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/japanese.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/lao.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-alt.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-ltx.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-post.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-pre.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/lrt.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/persian.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/programmer-dvorak.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/py-punct.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/pypunct-b5.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/quick-b5.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/quick-cns.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/rfc1345.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/sgml-input.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/sisheng.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/slovak.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/symbol-ksc.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/tamil-dvorak.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/thai.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/tibetan.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/tsang-b5.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/tsang-cns.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/uni-input.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/viqr.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/vntelex.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/vnvni.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/welsh.elc
%{_datadir}/emacs/%{version}/lisp/linum.elc
%{_datadir}/emacs/%{version}/lisp/loaddefs.el
%{_datadir}/emacs/%{version}/lisp/loadhist.elc
%{_datadir}/emacs/%{version}/lisp/loadup.el
%{_datadir}/emacs/%{version}/lisp/locate.elc
%{_datadir}/emacs/%{version}/lisp/lpr.elc
%{_datadir}/emacs/%{version}/lisp/ls-lisp.elc
%{_datadir}/emacs/%{version}/lisp/macros.elc
%dir %{_datadir}/emacs/%{version}/lisp/mail/
%{_datadir}/emacs/%{version}/lisp/mail/binhex.elc
%{_datadir}/emacs/%{version}/lisp/mail/blessmail.el
%{_datadir}/emacs/%{version}/lisp/mail/emacsbug.elc
%{_datadir}/emacs/%{version}/lisp/mail/feedmail.elc
%{_datadir}/emacs/%{version}/lisp/mail/flow-fill.elc
%{_datadir}/emacs/%{version}/lisp/mail/footnote.elc
%{_datadir}/emacs/%{version}/lisp/mail/hashcash.elc
%{_datadir}/emacs/%{version}/lisp/mail/ietf-drums.elc
%{_datadir}/emacs/%{version}/lisp/mail/mail-extr.elc
%{_datadir}/emacs/%{version}/lisp/mail/mail-hist.elc
%{_datadir}/emacs/%{version}/lisp/mail/mail-parse.elc
%{_datadir}/emacs/%{version}/lisp/mail/mail-prsvr.elc
%{_datadir}/emacs/%{version}/lisp/mail/mail-utils.elc
%{_datadir}/emacs/%{version}/lisp/mail/mailabbrev.elc
%{_datadir}/emacs/%{version}/lisp/mail/mailalias.elc
%{_datadir}/emacs/%{version}/lisp/mail/mailclient.elc
%{_datadir}/emacs/%{version}/lisp/mail/mailheader.elc
%{_datadir}/emacs/%{version}/lisp/mail/metamail.elc
%{_datadir}/emacs/%{version}/lisp/mail/mspools.elc
%{_datadir}/emacs/%{version}/lisp/mail/qp.elc
%{_datadir}/emacs/%{version}/lisp/mail/reporter.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc2045.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc2047.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc2231.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc2368.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc822.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmail-spam-filter.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmail.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmailedit.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmailkwd.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmailmm.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmailmsc.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmailout.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmailsort.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmailsum.elc
%{_datadir}/emacs/%{version}/lisp/mail/rmail-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/mail/sendmail.elc
%{_datadir}/emacs/%{version}/lisp/mail/smtpmail.elc
%{_datadir}/emacs/%{version}/lisp/mail/supercite.elc
%{_datadir}/emacs/%{version}/lisp/mail/uce.elc
%{_datadir}/emacs/%{version}/lisp/mail/undigest.elc
%{_datadir}/emacs/%{version}/lisp/mail/unrmail.elc
%{_datadir}/emacs/%{version}/lisp/mail/uudecode.elc
%{_datadir}/emacs/%{version}/lisp/mail/yenc.elc
%{_datadir}/emacs/%{version}/lisp/makesum.elc
%{_datadir}/emacs/%{version}/lisp/man.elc
%{_datadir}/emacs/%{version}/lisp/master.elc
%{_datadir}/emacs/%{version}/lisp/mb-depth.elc
%{_datadir}/emacs/%{version}/lisp/md4.elc
%{_datadir}/emacs/%{version}/lisp/menu-bar.elc
%dir %{_datadir}/emacs/%{version}/lisp/mh-e/
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-acros.el
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-alias.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-buffers.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-comp.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-compat.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-e.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-folder.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-funcs.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-gnus.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-identity.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-inc.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-junk.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-letter.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-limit.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-mime.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-print.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-scan.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-search.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-seq.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-show.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-speed.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-thread.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-tool-bar.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-utils.elc
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-xface.elc
%{_datadir}/emacs/%{version}/lisp/midnight.elc
%{_datadir}/emacs/%{version}/lisp/minibuf-eldef.elc
%{_datadir}/emacs/%{version}/lisp/minibuffer.elc
%{_datadir}/emacs/%{version}/lisp/misc.elc
%{_datadir}/emacs/%{version}/lisp/misearch.elc
%{_datadir}/emacs/%{version}/lisp/mouse-copy.elc
%{_datadir}/emacs/%{version}/lisp/mouse-drag.elc
%{_datadir}/emacs/%{version}/lisp/mouse.elc
%{_datadir}/emacs/%{version}/lisp/mpc.elc
%{_datadir}/emacs/%{version}/lisp/msb.elc
%{_datadir}/emacs/%{version}/lisp/mwheel.elc
%dir %{_datadir}/emacs/%{version}/lisp/net/
%{_datadir}/emacs/%{version}/lisp/net/ange-ftp.elc
%{_datadir}/emacs/%{version}/lisp/net/browse-url.elc
%{_datadir}/emacs/%{version}/lisp/net/dbus.elc
%{_datadir}/emacs/%{version}/lisp/net/dig.elc
%{_datadir}/emacs/%{version}/lisp/net/dns.elc
%{_datadir}/emacs/%{version}/lisp/net/eudc-bob.elc
%{_datadir}/emacs/%{version}/lisp/net/eudc-export.elc
%{_datadir}/emacs/%{version}/lisp/net/eudc-hotlist.elc
%{_datadir}/emacs/%{version}/lisp/net/eudc-vars.elc
%{_datadir}/emacs/%{version}/lisp/net/eudc.elc
%{_datadir}/emacs/%{version}/lisp/net/eudcb-bbdb.elc
%{_datadir}/emacs/%{version}/lisp/net/eudcb-ldap.elc
%{_datadir}/emacs/%{version}/lisp/net/eudcb-mab.elc
%{_datadir}/emacs/%{version}/lisp/net/eww.elc
%{_datadir}/emacs/%{version}/lisp/net/gnutls.elc
%{_datadir}/emacs/%{version}/lisp/net/goto-addr.elc
%{_datadir}/emacs/%{version}/lisp/net/hmac-def.elc
%{_datadir}/emacs/%{version}/lisp/net/hmac-md5.elc
%{_datadir}/emacs/%{version}/lisp/net/imap.elc
%{_datadir}/emacs/%{version}/lisp/net/ldap.elc
%{_datadir}/emacs/%{version}/lisp/net/mailcap.elc
%{_datadir}/emacs/%{version}/lisp/net/mairix.elc
%{_datadir}/emacs/%{version}/lisp/net/net-utils.elc
%{_datadir}/emacs/%{version}/lisp/net/netrc.elc
%{_datadir}/emacs/%{version}/lisp/net/network-stream.elc
%{_datadir}/emacs/%{version}/lisp/net/newst-backend.elc
%{_datadir}/emacs/%{version}/lisp/net/newst-plainview.elc
%{_datadir}/emacs/%{version}/lisp/net/newst-reader.elc
%{_datadir}/emacs/%{version}/lisp/net/newst-ticker.elc
%{_datadir}/emacs/%{version}/lisp/net/newst-treeview.elc
%{_datadir}/emacs/%{version}/lisp/net/newsticker.elc
%{_datadir}/emacs/%{version}/lisp/net/nsm.elc
%{_datadir}/emacs/%{version}/lisp/net/ntlm.elc
%{_datadir}/emacs/%{version}/lisp/net/pop3.elc
%{_datadir}/emacs/%{version}/lisp/net/puny.elc
%{_datadir}/emacs/%{version}/lisp/net/quickurl.elc
%{_datadir}/emacs/%{version}/lisp/net/rcirc.elc
%{_datadir}/emacs/%{version}/lisp/net/rfc2104.elc
%{_datadir}/emacs/%{version}/lisp/net/rlogin.elc
%{_datadir}/emacs/%{version}/lisp/net/sasl-cram.elc
%{_datadir}/emacs/%{version}/lisp/net/sasl-digest.elc
%{_datadir}/emacs/%{version}/lisp/net/sasl-ntlm.elc
%{_datadir}/emacs/%{version}/lisp/net/sasl-scram-rfc.elc
%{_datadir}/emacs/%{version}/lisp/net/sasl.elc
%{_datadir}/emacs/%{version}/lisp/net/secrets.elc
%{_datadir}/emacs/%{version}/lisp/net/sieve-manage.elc
%{_datadir}/emacs/%{version}/lisp/net/sieve-mode.elc
%{_datadir}/emacs/%{version}/lisp/net/sieve.elc
%{_datadir}/emacs/%{version}/lisp/net/shr-color.elc
%{_datadir}/emacs/%{version}/lisp/net/shr.elc
%{_datadir}/emacs/%{version}/lisp/net/snmp-mode.elc
%{_datadir}/emacs/%{version}/lisp/net/soap-client.elc
%{_datadir}/emacs/%{version}/lisp/net/soap-inspect.elc
%{_datadir}/emacs/%{version}/lisp/net/socks.elc
%{_datadir}/emacs/%{version}/lisp/net/starttls.elc
%{_datadir}/emacs/%{version}/lisp/net/telnet.elc
%{_datadir}/emacs/%{version}/lisp/net/tls.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-adb.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-cache.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-cmds.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-compat.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-ftp.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-gvfs.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/net/tramp-sh.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-smb.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-uu.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp.elc
%{_datadir}/emacs/%{version}/lisp/net/trampver.elc
%{_datadir}/emacs/%{version}/lisp/net/webjump.elc
%{_datadir}/emacs/%{version}/lisp/net/zeroconf.elc
%{_datadir}/emacs/%{version}/lisp/newcomment.elc
%{_datadir}/emacs/%{version}/lisp/notifications.elc
%{_datadir}/emacs/%{version}/lisp/novice.elc
%dir %{_datadir}/emacs/%{version}/lisp/nxml/
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-enc.elc
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-maint.elc
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-mode.elc
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-ns.elc
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-outln.elc
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-parse.elc
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-rap.elc
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-util.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-cmpct.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-dt.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-loc.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-maint.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-match.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-nxml.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-parse.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-pttrn.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-uri.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-util.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-valid.elc
%{_datadir}/emacs/%{version}/lisp/nxml/rng-xsd.elc
%{_datadir}/emacs/%{version}/lisp/nxml/xmltok.elc
%{_datadir}/emacs/%{version}/lisp/nxml/xsd-regexp.elc
%{_datadir}/emacs/%{version}/lisp/obarray.elc
%dir %{_datadir}/emacs/%{version}/lisp/obsolete/
%{_datadir}/emacs/%{version}/lisp/obsolete/abbrevlist.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/assoc.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/bruce.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/cc-compat.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/cl-compat.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/complete.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/crisp.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/cust-print.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/erc-hecomplete.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/eudcb-ph.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/fast-lock.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/gs.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/gulp.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/html2text.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/iswitchb.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/landmark.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/lazy-lock.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/ledit.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/levents.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/lmenu.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/longlines.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/lucid.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/mailpost.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/meese.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/messcompat.el
%{_datadir}/emacs/%{version}/lisp/obsolete/mouse-sel.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/old-emacs-lock.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/old-whitespace.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/options.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/otodo-mode.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/patcomp.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pc-mode.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pc-select.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-def.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-gpg.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-parse.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-pgp.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-pgp5.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/rcompile.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/s-region.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/sregex.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/sup-mouse.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/terminal.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-edt.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-extras.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-mapper.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/vc-arch.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/vi.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/vip.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/ws-mode.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/xesam.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/yow.elc
%dir %{_datadir}/emacs/%{version}/lisp/org/
%{_datadir}/emacs/%{version}/lisp/org/ob-C.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-J.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-R.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-abc.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-asymptote.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-awk.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-calc.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-clojure.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-comint.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-coq.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-core.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-css.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ditaa.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-dot.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ebnf.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-emacs-lisp.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-eval.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-exp.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-forth.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-fortran.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-gnuplot.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-groovy.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-haskell.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-hledger.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-io.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-java.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-js.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-keys.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-latex.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ledger.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lilypond.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lisp.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lob.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lua.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-makefile.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-matlab.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-maxima.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-mscgen.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ocaml.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-octave.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-org.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-perl.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-picolisp.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-plantuml.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-processing.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-python.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ref.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ruby.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sass.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-scheme.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-screen.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sed.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-shen.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-shell.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sql.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sqlite.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-stan.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-table.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-tangle.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-vala.elc
%{_datadir}/emacs/%{version}/lisp/org/ob.elc
%{_datadir}/emacs/%{version}/lisp/org/org-agenda.elc
%{_datadir}/emacs/%{version}/lisp/org/org-archive.elc
%{_datadir}/emacs/%{version}/lisp/org/org-attach.elc
%{_datadir}/emacs/%{version}/lisp/org/org-bbdb.elc
%{_datadir}/emacs/%{version}/lisp/org/org-bibtex.elc
%{_datadir}/emacs/%{version}/lisp/org/org-capture.elc
%{_datadir}/emacs/%{version}/lisp/org/org-clock.elc
%{_datadir}/emacs/%{version}/lisp/org/org-colview.elc
%{_datadir}/emacs/%{version}/lisp/org/org-compat.elc
%{_datadir}/emacs/%{version}/lisp/org/org-crypt.elc
%{_datadir}/emacs/%{version}/lisp/org/org-ctags.elc
%{_datadir}/emacs/%{version}/lisp/org/org-datetree.elc
%{_datadir}/emacs/%{version}/lisp/org/org-docview.elc
%{_datadir}/emacs/%{version}/lisp/org/org-duration.elc
%{_datadir}/emacs/%{version}/lisp/org/org-element.elc
%{_datadir}/emacs/%{version}/lisp/org/org-entities.elc
%{_datadir}/emacs/%{version}/lisp/org/org-eshell.elc
%{_datadir}/emacs/%{version}/lisp/org/org-eww.elc
%{_datadir}/emacs/%{version}/lisp/org/org-faces.elc
%{_datadir}/emacs/%{version}/lisp/org/org-feed.elc
%{_datadir}/emacs/%{version}/lisp/org/org-footnote.elc
%{_datadir}/emacs/%{version}/lisp/org/org-gnus.elc
%{_datadir}/emacs/%{version}/lisp/org/org-habit.elc
%{_datadir}/emacs/%{version}/lisp/org/org-id.elc
%{_datadir}/emacs/%{version}/lisp/org/org-indent.elc
%{_datadir}/emacs/%{version}/lisp/org/org-info.elc
%{_datadir}/emacs/%{version}/lisp/org/org-inlinetask.elc
%{_datadir}/emacs/%{version}/lisp/org/org-install.el
%{_datadir}/emacs/%{version}/lisp/org/org-irc.elc
%{_datadir}/emacs/%{version}/lisp/org/org-lint.elc
%{_datadir}/emacs/%{version}/lisp/org/org-list.elc
%{_datadir}/emacs/%{version}/lisp/org/org-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/org/org-macro.elc
%{_datadir}/emacs/%{version}/lisp/org/org-macs.elc
%{_datadir}/emacs/%{version}/lisp/org/org-mhe.elc
%{_datadir}/emacs/%{version}/lisp/org/org-mobile.elc
%{_datadir}/emacs/%{version}/lisp/org/org-mouse.elc
%{_datadir}/emacs/%{version}/lisp/org/org-pcomplete.elc
%{_datadir}/emacs/%{version}/lisp/org/org-plot.elc
%{_datadir}/emacs/%{version}/lisp/org/org-protocol.elc
%{_datadir}/emacs/%{version}/lisp/org/org-rmail.elc
%{_datadir}/emacs/%{version}/lisp/org/org-src.elc
%{_datadir}/emacs/%{version}/lisp/org/org-table.elc
%{_datadir}/emacs/%{version}/lisp/org/org-timer.elc
%{_datadir}/emacs/%{version}/lisp/org/org-version.el
%{_datadir}/emacs/%{version}/lisp/org/org-w3m.elc
%{_datadir}/emacs/%{version}/lisp/org/org.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-ascii.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-beamer.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-html.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-icalendar.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-latex.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-man.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-md.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-odt.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-org.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-publish.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-texinfo.elc
%{_datadir}/emacs/%{version}/lisp/org/ox.elc
%{_datadir}/emacs/%{version}/lisp/outline.elc
%{_datadir}/emacs/%{version}/lisp/paren.elc
%{_datadir}/emacs/%{version}/lisp/password-cache.elc
%{_datadir}/emacs/%{version}/lisp/pcmpl-cvs.elc
%{_datadir}/emacs/%{version}/lisp/pcmpl-gnu.elc
%{_datadir}/emacs/%{version}/lisp/pcmpl-linux.elc
%{_datadir}/emacs/%{version}/lisp/pcmpl-rpm.elc
%{_datadir}/emacs/%{version}/lisp/pcmpl-unix.elc
%{_datadir}/emacs/%{version}/lisp/pcmpl-x.elc
%{_datadir}/emacs/%{version}/lisp/pcomplete.elc
%{_datadir}/emacs/%{version}/lisp/pixel-scroll.elc
%dir %{_datadir}/emacs/%{version}/lisp/play/
%{_datadir}/emacs/%{version}/lisp/play/5x5.elc
%{_datadir}/emacs/%{version}/lisp/play/animate.elc
%{_datadir}/emacs/%{version}/lisp/play/blackbox.elc
%{_datadir}/emacs/%{version}/lisp/play/bubbles.elc
%{_datadir}/emacs/%{version}/lisp/play/cookie1.elc
%{_datadir}/emacs/%{version}/lisp/play/decipher.elc
%{_datadir}/emacs/%{version}/lisp/play/dissociate.elc
%{_datadir}/emacs/%{version}/lisp/play/doctor.elc
%{_datadir}/emacs/%{version}/lisp/play/dunnet.elc
%{_datadir}/emacs/%{version}/lisp/play/fortune.elc
%{_datadir}/emacs/%{version}/lisp/play/gamegrid.elc
%{_datadir}/emacs/%{version}/lisp/play/gametree.elc
%{_datadir}/emacs/%{version}/lisp/play/gomoku.elc
%{_datadir}/emacs/%{version}/lisp/play/handwrite.elc
%{_datadir}/emacs/%{version}/lisp/play/hanoi.elc
%{_datadir}/emacs/%{version}/lisp/play/life.elc
%{_datadir}/emacs/%{version}/lisp/play/morse.elc
%{_datadir}/emacs/%{version}/lisp/play/mpuz.elc
%{_datadir}/emacs/%{version}/lisp/play/pong.elc
%{_datadir}/emacs/%{version}/lisp/play/snake.elc
%{_datadir}/emacs/%{version}/lisp/play/solitaire.elc
%{_datadir}/emacs/%{version}/lisp/play/spook.elc
%{_datadir}/emacs/%{version}/lisp/play/studly.elc
%{_datadir}/emacs/%{version}/lisp/play/tetris.elc
%{_datadir}/emacs/%{version}/lisp/play/zone.elc
%{_datadir}/emacs/%{version}/lisp/plstore.elc
%{_datadir}/emacs/%{version}/lisp/printing.elc
%{_datadir}/emacs/%{version}/lisp/proced.elc
%{_datadir}/emacs/%{version}/lisp/profiler.elc
%dir %{_datadir}/emacs/%{version}/lisp/progmodes/
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-prj.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-stmt.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-xref.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/antlr-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/asm-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/autoconf.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/bat-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/bug-reference.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-align.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-awk.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-bytecomp.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-cmds.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-defs.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-engine.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-fonts.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-guess.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-langs.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-menus.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-styles.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-vars.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cfengine.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cmacexp.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/compile.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cperl-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cpp.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/cwarn.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/dcl-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-abn.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-bnf.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-dtd.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-ebx.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-iso.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-otz.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-yac.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf2ps.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ebrowse.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/elisp-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/etags.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/executable.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/f90.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake-proc.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/fortran.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/gdb-mi.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/glasses.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/grep.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/gud.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/hideif.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/hideshow.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/icon.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-complete-structtag.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-help.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-shell.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-toolbar.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/idlwave.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/inf-lisp.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/js.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ld-script.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/m4-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/make-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/mantemp.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/meta-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/mixal-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/modula2.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/octave.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/opascal.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/pascal.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/perl-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/prog-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/project.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/prolog.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ps-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/python.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/ruby-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/scheme.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/sh-script.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/simula.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/sql.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/subword.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/tcl.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/vera-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/verilog-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/vhdl-mode.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/which-func.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/xref.elc
%{_datadir}/emacs/%{version}/lisp/progmodes/xscheme.elc
%{_datadir}/emacs/%{version}/lisp/ps-bdf.elc
%{_datadir}/emacs/%{version}/lisp/ps-def.elc
%{_datadir}/emacs/%{version}/lisp/ps-mule.elc
%{_datadir}/emacs/%{version}/lisp/ps-print.elc
%{_datadir}/emacs/%{version}/lisp/ps-print-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/ps-samp.elc
%{_datadir}/emacs/%{version}/lisp/recentf.elc
%{_datadir}/emacs/%{version}/lisp/rect.elc
%{_datadir}/emacs/%{version}/lisp/register.elc
%{_datadir}/emacs/%{version}/lisp/registry.elc
%{_datadir}/emacs/%{version}/lisp/repeat.elc
%{_datadir}/emacs/%{version}/lisp/replace.elc
%{_datadir}/emacs/%{version}/lisp/reposition.elc
%{_datadir}/emacs/%{version}/lisp/reveal.elc
%{_datadir}/emacs/%{version}/lisp/rfn-eshadow.elc
%{_datadir}/emacs/%{version}/lisp/rot13.elc
%{_datadir}/emacs/%{version}/lisp/rtree.elc
%{_datadir}/emacs/%{version}/lisp/ruler-mode.elc
%{_datadir}/emacs/%{version}/lisp/savehist.elc
%{_datadir}/emacs/%{version}/lisp/saveplace.elc
%{_datadir}/emacs/%{version}/lisp/sb-image.elc
%{_datadir}/emacs/%{version}/lisp/scroll-all.elc
%{_datadir}/emacs/%{version}/lisp/scroll-bar.elc
%{_datadir}/emacs/%{version}/lisp/scroll-lock.elc
%{_datadir}/emacs/%{version}/lisp/select.elc
%{_datadir}/emacs/%{version}/lisp/server.elc
%{_datadir}/emacs/%{version}/lisp/ses.elc
%{_datadir}/emacs/%{version}/lisp/shadowfile.elc
%{_datadir}/emacs/%{version}/lisp/shell.elc
%{_datadir}/emacs/%{version}/lisp/simple.elc
%{_datadir}/emacs/%{version}/lisp/site-load.el
%{_datadir}/emacs/%{version}/lisp/skeleton.el
%{_datadir}/emacs/%{version}/lisp/sort.elc
%{_datadir}/emacs/%{version}/lisp/soundex.elc
%{_datadir}/emacs/%{version}/lisp/speedbar.elc
%{_datadir}/emacs/%{version}/lisp/startup.elc
%{_datadir}/emacs/%{version}/lisp/strokes.elc
%{_datadir}/emacs/%{version}/lisp/subdirs.el
%{_datadir}/emacs/%{version}/lisp/subr.elc
%{_datadir}/emacs/%{version}/lisp/svg.elc
%{_datadir}/emacs/%{version}/lisp/t-mouse.elc
%{_datadir}/emacs/%{version}/lisp/tabify.elc
%{_datadir}/emacs/%{version}/lisp/talk.elc
%{_datadir}/emacs/%{version}/lisp/tar-mode.elc
%{_datadir}/emacs/%{version}/lisp/tempo.elc
%{_datadir}/emacs/%{version}/lisp/term.elc
%dir %{_datadir}/emacs/%{version}/lisp/term/
%{_datadir}/emacs/%{version}/lisp/term/AT386.elc
%doc %{_datadir}/emacs/%{version}/lisp/term/README
%{_datadir}/emacs/%{version}/lisp/term/bobcat.elc
%{_datadir}/emacs/%{version}/lisp/term/common-win.elc
%{_datadir}/emacs/%{version}/lisp/term/cygwin.elc
%{_datadir}/emacs/%{version}/lisp/term/internal.elc
%{_datadir}/emacs/%{version}/lisp/term/iris-ansi.elc
%{_datadir}/emacs/%{version}/lisp/term/konsole.elc
%{_datadir}/emacs/%{version}/lisp/term/linux.elc
%{_datadir}/emacs/%{version}/lisp/term/lk201.elc
%{_datadir}/emacs/%{version}/lisp/term/news.elc
%{_datadir}/emacs/%{version}/lisp/term/ns-win.elc
%{_datadir}/emacs/%{version}/lisp/term/pc-win.elc
%{_datadir}/emacs/%{version}/lisp/term/rxvt.elc
%{_datadir}/emacs/%{version}/lisp/term/screen.elc
%{_datadir}/emacs/%{version}/lisp/term/sun.elc
%{_datadir}/emacs/%{version}/lisp/term/tmux.elc
%{_datadir}/emacs/%{version}/lisp/term/tty-colors.elc
%{_datadir}/emacs/%{version}/lisp/term/tvi970.elc
%{_datadir}/emacs/%{version}/lisp/term/vt100.elc
%{_datadir}/emacs/%{version}/lisp/term/vt200.elc
%{_datadir}/emacs/%{version}/lisp/term/w32-win.elc
%{_datadir}/emacs/%{version}/lisp/term/w32console.elc
%{_datadir}/emacs/%{version}/lisp/term/wyse50.elc
%{_datadir}/emacs/%{version}/lisp/term/x-win.elc
%{_datadir}/emacs/%{version}/lisp/term/xterm.el
%dir %{_datadir}/emacs/%{version}/lisp/textmodes/
%{_datadir}/emacs/%{version}/lisp/textmodes/artist.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/bib-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/bibtex-style.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/bibtex.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/conf-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/css-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/dns-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/enriched.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/fill.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/flyspell.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/ispell.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/less-css-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/makeinfo.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/mhtml-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/nroff-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/page-ext.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/page.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/paragraphs.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/picture.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/po.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/refbib.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/refer.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/refill.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-auc.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-cite.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-dcr.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-global.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-index.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-parse.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-ref.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-sel.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-toc.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-vars.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/remember.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/rst.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/sgml-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/table.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/tex-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/texinfmt.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/texinfo.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/texnfo-upd.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/text-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/tildify.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/two-column.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/underline.elc
%{_datadir}/emacs/%{version}/lisp/thingatpt.elc
%{_datadir}/emacs/%{version}/lisp/thumbs.elc
%{_datadir}/emacs/%{version}/lisp/time-stamp.elc
%{_datadir}/emacs/%{version}/lisp/time.elc
%{_datadir}/emacs/%{version}/lisp/timezone.elc
%{_datadir}/emacs/%{version}/lisp/tmm.elc
%{_datadir}/emacs/%{version}/lisp/tool-bar.elc
%{_datadir}/emacs/%{version}/lisp/tooltip.elc
%{_datadir}/emacs/%{version}/lisp/tree-widget.elc
%{_datadir}/emacs/%{version}/lisp/tutorial.elc
%{_datadir}/emacs/%{version}/lisp/type-break.elc
%{_datadir}/emacs/%{version}/lisp/uniquify.elc
%dir %{_datadir}/emacs/%{version}/lisp/url/
%{_datadir}/emacs/%{version}/lisp/url/url-about.elc
%{_datadir}/emacs/%{version}/lisp/url/url-auth.elc
%{_datadir}/emacs/%{version}/lisp/url/url-cache.elc
%{_datadir}/emacs/%{version}/lisp/url/url-cid.elc
%{_datadir}/emacs/%{version}/lisp/url/url-cookie.elc
%{_datadir}/emacs/%{version}/lisp/url/url-dav.elc
%{_datadir}/emacs/%{version}/lisp/url/url-dired.elc
%{_datadir}/emacs/%{version}/lisp/url/url-domsuf.elc
%{_datadir}/emacs/%{version}/lisp/url/url-expand.elc
%{_datadir}/emacs/%{version}/lisp/url/url-file.elc
%{_datadir}/emacs/%{version}/lisp/url/url-ftp.elc
%{_datadir}/emacs/%{version}/lisp/url/url-future.elc
%{_datadir}/emacs/%{version}/lisp/url/url-gw.elc
%{_datadir}/emacs/%{version}/lisp/url/url-handlers.elc
%{_datadir}/emacs/%{version}/lisp/url/url-history.elc
%{_datadir}/emacs/%{version}/lisp/url/url-http.elc
%{_datadir}/emacs/%{version}/lisp/url/url-imap.elc
%{_datadir}/emacs/%{version}/lisp/url/url-irc.elc
%{_datadir}/emacs/%{version}/lisp/url/url-ldap.elc
%{_datadir}/emacs/%{version}/lisp/url/url-mailto.elc
%{_datadir}/emacs/%{version}/lisp/url/url-methods.elc
%{_datadir}/emacs/%{version}/lisp/url/url-misc.elc
%{_datadir}/emacs/%{version}/lisp/url/url-news.elc
%{_datadir}/emacs/%{version}/lisp/url/url-nfs.elc
%{_datadir}/emacs/%{version}/lisp/url/url-ns.elc
%{_datadir}/emacs/%{version}/lisp/url/url-parse.elc
%{_datadir}/emacs/%{version}/lisp/url/url-privacy.elc
%{_datadir}/emacs/%{version}/lisp/url/url-proxy.elc
%{_datadir}/emacs/%{version}/lisp/url/url-queue.elc
%{_datadir}/emacs/%{version}/lisp/url/url-tramp.elc
%{_datadir}/emacs/%{version}/lisp/url/url-util.elc
%{_datadir}/emacs/%{version}/lisp/url/url-vars.elc
%{_datadir}/emacs/%{version}/lisp/url/url.elc
%{_datadir}/emacs/%{version}/lisp/userlock.elc
%dir %{_datadir}/emacs/%{version}/lisp/vc/
%{_datadir}/emacs/%{version}/lisp/vc/add-log.elc
%{_datadir}/emacs/%{version}/lisp/vc/compare-w.elc
%{_datadir}/emacs/%{version}/lisp/vc/cvs-status.elc
%{_datadir}/emacs/%{version}/lisp/vc/diff-mode.elc
%{_datadir}/emacs/%{version}/lisp/vc/diff.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-diff.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-help.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-hook.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-init.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-merg.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-mult.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-ptch.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-util.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-vers.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff-wind.elc
%{_datadir}/emacs/%{version}/lisp/vc/ediff.elc
%{_datadir}/emacs/%{version}/lisp/vc/emerge.elc
%{_datadir}/emacs/%{version}/lisp/vc/log-edit.elc
%{_datadir}/emacs/%{version}/lisp/vc/log-view.elc
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-defs.elc
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-info.elc
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-parse.elc
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-util.elc
%{_datadir}/emacs/%{version}/lisp/vc/pcvs.elc
%{_datadir}/emacs/%{version}/lisp/vc/smerge-mode.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-annotate.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-bzr.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-cvs.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-dav.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-dir.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-dispatcher.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-filewise.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-git.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-hg.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-hooks.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-mtn.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-rcs.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-sccs.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-src.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc-svn.elc
%{_datadir}/emacs/%{version}/lisp/vc/vc.elc
%{_datadir}/emacs/%{version}/lisp/vcursor.elc
%{_datadir}/emacs/%{version}/lisp/version.elc
%{_datadir}/emacs/%{version}/lisp/view.elc
%{_datadir}/emacs/%{version}/lisp/vt-control.elc
%{_datadir}/emacs/%{version}/lisp/vt100-led.elc
%{_datadir}/emacs/%{version}/lisp/w32-fns.elc
%{_datadir}/emacs/%{version}/lisp/w32-vars.elc
%{_datadir}/emacs/%{version}/lisp/wdired.elc
%{_datadir}/emacs/%{version}/lisp/whitespace.elc
%{_datadir}/emacs/%{version}/lisp/wid-browse.elc
%{_datadir}/emacs/%{version}/lisp/wid-edit.elc
%{_datadir}/emacs/%{version}/lisp/widget.elc
%{_datadir}/emacs/%{version}/lisp/windmove.elc
%{_datadir}/emacs/%{version}/lisp/window.elc
%{_datadir}/emacs/%{version}/lisp/winner.elc
%{_datadir}/emacs/%{version}/lisp/woman.elc
%{_datadir}/emacs/%{version}/lisp/xdg.elc
%{_datadir}/emacs/%{version}/lisp/x-dnd.elc
%{_datadir}/emacs/%{version}/lisp/xml.elc
%{_datadir}/emacs/%{version}/lisp/xt-mouse.elc
%{_datadir}/emacs/%{version}/lisp/xwidget.elc
%dir %{_datadir}/emacs/%{version}/site-lisp/
%{_datadir}/emacs/%{version}/site-lisp/subdirs.el
%dir %{_datadir}/emacs/%{version}/site-lisp/term/
%{_datadir}/emacs/%{version}/site-lisp/term/func-keys.el
%{_datadir}/emacs/%{version}/site-lisp/term/gnome.el
%{_datadir}/emacs/%{version}/site-lisp/term/kvt.el
%{_datadir}/emacs/%{version}/site-lisp/term/linux.el
%{_datadir}/emacs/%{version}/site-lisp/term/locale.el
%dir %{_datadir}/emacs/site-lisp/
%dir %{_datadir}/emacs/site-lisp/site-start.d/
%{_mandir}/man1/*.1%{ext_man}
%exclude %{_mandir}/man1/*tags.1%{ext_man}
%dir %attr(770,games,games) %{_localstatedir}/games/emacs
%attr(660,games,games) %{_localstatedir}/games/emacs/snake-scores
%attr(660,games,games) %{_localstatedir}/games/emacs/tetris-scores

%files       -n emacs-nox
%defattr(-, root, root)
%{_bindir}/emacs-nox

%files       -n emacs-x11
%defattr(-, root, root)
%{_bindir}/emacs-x11
%{_bindir}/emacs-gtk
%dir %{appDefaultsDir}
%{appDefaultsFile}
%{_datadir}/applications/emacs.desktop
%{_datadir}/icons/hicolor/128x128/apps/emacs.png
%{_datadir}/icons/hicolor/16x16/apps/emacs.png
%{_datadir}/icons/hicolor/24x24/apps/emacs.png
%{_datadir}/icons/hicolor/32x32/apps/emacs.png
%{_datadir}/icons/hicolor/48x48/apps/emacs.png
%{_datadir}/icons/hicolor/scalable/apps/emacs.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document23.svg
%if 0%{?suse_version} <= 1315
%dir %{_datadir}/metainfo/
%endif
%{_datadir}/metainfo/emacs.appdata.xml
%{_datadir}/pixmaps/emacs.png

%files       -n emacs-info
%defattr(-, root, root)
%doc %{_infodir}/*.gz
%if 0%{?include_info} == 0
%exclude %{_infodir}/info.info.gz
%endif

%files       -n emacs-el
%defattr(-, root, root)
%{_x11inc}/emacs-module.h
%{_datadir}/emacs/%{version}/lisp/abbrev.el.gz
%{_datadir}/emacs/%{version}/lisp/align.el.gz
%{_datadir}/emacs/%{version}/lisp/allout-widgets.el.gz
%{_datadir}/emacs/%{version}/lisp/allout.el.gz
%{_datadir}/emacs/%{version}/lisp/ansi-color.el.gz
%{_datadir}/emacs/%{version}/lisp/apropos.el.gz
%{_datadir}/emacs/%{version}/lisp/arc-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/array.el.gz
%{_datadir}/emacs/%{version}/lisp/auth-source-pass.el.gz
%{_datadir}/emacs/%{version}/lisp/auth-source.el.gz
%{_datadir}/emacs/%{version}/lisp/autoarg.el.gz
%{_datadir}/emacs/%{version}/lisp/autoinsert.el.gz
%{_datadir}/emacs/%{version}/lisp/autorevert.el.gz
%{_datadir}/emacs/%{version}/lisp/avoid.el.gz
%{_datadir}/emacs/%{version}/lisp/battery.el.gz
%{_datadir}/emacs/%{version}/lisp/bookmark.el.gz
%{_datadir}/emacs/%{version}/lisp/bs.el.gz
%{_datadir}/emacs/%{version}/lisp/buff-menu.el.gz
%{_datadir}/emacs/%{version}/lisp/button.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-aent.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-alg.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-arith.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-bin.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-comb.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-cplx.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-embed.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-ext.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-fin.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-forms.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-frac.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-funcs.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-graph.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-help.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-incom.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-keypd.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-lang.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-macs.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-map.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-math.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-menu.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-misc.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-mtx.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-nlfit.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-poly.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-prog.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-rewr.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-rules.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-sel.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-stat.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-store.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-stuff.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-trail.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-undo.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-units.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-vec.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc-yank.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calc.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calcalg2.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calcalg3.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calccomp.el.gz
%{_datadir}/emacs/%{version}/lisp/calc/calcsel2.el.gz
%{_datadir}/emacs/%{version}/lisp/calculator.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/appt.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-bahai.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-china.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-coptic.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-dst.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-french.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-hebrew.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-html.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-islam.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-iso.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-julian.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-mayan.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-menu.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-move.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-persia.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-tex.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/cal-x.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/calendar.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/diary-lib.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/holidays.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/icalendar.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/lunar.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/parse-time.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/solar.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/time-date.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/timeclock.el.gz
%{_datadir}/emacs/%{version}/lisp/calendar/todo-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/case-table.el.gz
%{_datadir}/emacs/%{version}/lisp/cdl.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-cscope.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-files.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-global.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-idutils.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/cedet.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/data-debug.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/auto.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/autoconf-edit.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/base.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/config.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/cpp-root.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/custom.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/detect.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/dired.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/emacs.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/files.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/generic.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/linux.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/locate.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/make.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/makefile-edit.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/pconf.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/pmake.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-archive.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-aux.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-comp.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-elisp.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-info.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-misc.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-obj.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-prog.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-scheme.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-shared.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/project-am.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/shell.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/simple.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/source.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/speedbar.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/srecode.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/system.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/ede/util.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/inversion.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/mode-local.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/pulse.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/complete.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/debug.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/fcn.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/refs.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/c-by.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/c.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/debug.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/el.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/gcc.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/grammar.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/make-by.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/make.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/scm-by.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/scm.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/chart.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/complete.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ctxt.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-debug.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-ebrowse.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-el.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-file.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-find.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-global.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-javascript.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-ref.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-typecache.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/debug.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate/include.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate/mode.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/dep.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/doc.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ede-grammar.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/edit.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/find.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/format.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/fw.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grammar-wy.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grammar.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/html.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ia-sb.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ia.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/idle.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/imenu.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/java.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/lex-spp.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/lex.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/mru-bookmark.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/sb.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/scope.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/senator.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/sort.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/cscope.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/filter.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/global.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/grep.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/idutils.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/list.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-file.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-ls.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-write.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/texi.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/util-modes.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/util.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/comp.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/grammar.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/java-tags.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/javascript.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/javat-wy.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/js-wy.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/python-wy.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/python.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/wisent.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/args.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/compile.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/cpp.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/ctxt.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/dictionary.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/document.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/el.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/expandproto.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/extract.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/fields.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/filters.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/find.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/getset.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/insert.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/java.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/map.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/mode.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/semantic.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt-wy.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/table.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/template.el.gz
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/texi.el.gz
%{_datadir}/emacs/%{version}/lisp/char-fold.el.gz
%{_datadir}/emacs/%{version}/lisp/chistory.el.gz
%{_datadir}/emacs/%{version}/lisp/cmuscheme.el.gz
%{_datadir}/emacs/%{version}/lisp/color.el.gz
%{_datadir}/emacs/%{version}/lisp/comint.el.gz
%{_datadir}/emacs/%{version}/lisp/completion.el.gz
%{_datadir}/emacs/%{version}/lisp/composite.el.gz
%{_datadir}/emacs/%{version}/lisp/cus-dep.el.gz
%{_datadir}/emacs/%{version}/lisp/cus-edit.el.gz
%{_datadir}/emacs/%{version}/lisp/cus-face.el.gz
%{_datadir}/emacs/%{version}/lisp/cus-theme.el.gz
%{_datadir}/emacs/%{version}/lisp/custom.el.gz
%{_datadir}/emacs/%{version}/lisp/dabbrev.el.gz
%{_datadir}/emacs/%{version}/lisp/delim-col.el.gz
%{_datadir}/emacs/%{version}/lisp/delsel.el.gz
%{_datadir}/emacs/%{version}/lisp/descr-text.el.gz
%{_datadir}/emacs/%{version}/lisp/desktop.el.gz
%{_datadir}/emacs/%{version}/lisp/dframe.el.gz
%{_datadir}/emacs/%{version}/lisp/dired-aux.el.gz
%{_datadir}/emacs/%{version}/lisp/dired-x.el.gz
%{_datadir}/emacs/%{version}/lisp/dired.el.gz
%{_datadir}/emacs/%{version}/lisp/dirtrack.el.gz
%{_datadir}/emacs/%{version}/lisp/disp-table.el.gz
%{_datadir}/emacs/%{version}/lisp/display-line-numbers.el.gz
%{_datadir}/emacs/%{version}/lisp/dnd.el.gz
%{_datadir}/emacs/%{version}/lisp/doc-view.el.gz
%{_datadir}/emacs/%{version}/lisp/dom.el.gz
%{_datadir}/emacs/%{version}/lisp/dos-fns.el.gz
%{_datadir}/emacs/%{version}/lisp/dos-vars.el.gz
%{_datadir}/emacs/%{version}/lisp/dos-w32.el.gz
%{_datadir}/emacs/%{version}/lisp/double.el.gz
%{_datadir}/emacs/%{version}/lisp/dynamic-setting.el.gz
%{_datadir}/emacs/%{version}/lisp/ebuff-menu.el.gz
%{_datadir}/emacs/%{version}/lisp/echistory.el.gz
%{_datadir}/emacs/%{version}/lisp/ecomplete.el.gz
%{_datadir}/emacs/%{version}/lisp/edmacro.el.gz
%{_datadir}/emacs/%{version}/lisp/ehelp.el.gz
%{_datadir}/emacs/%{version}/lisp/elec-pair.el.gz
%{_datadir}/emacs/%{version}/lisp/electric.el.gz
%{_datadir}/emacs/%{version}/lisp/elide-head.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/advice.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/autoload.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/avl-tree.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/backquote.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/benchmark.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/bindat.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/byte-opt.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/byte-run.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/bytecomp.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cconv.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/chart.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/check-declare.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/checkdoc.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-extra.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-generic.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-indent.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-lib.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-macs.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-preloaded.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-print.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-seq.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/copyright.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/crm.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cursor-sensor.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/debug.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/derived.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/disass.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/easy-mmode.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/easymenu.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/edebug.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-base.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-compat.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-core.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-custom.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-datadebug.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-opt.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-speedbar.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eldoc.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/elint.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/elp.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ert-x.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ert.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ewoc.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/find-func.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/float-sup.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generator.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generic.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/gv.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/helper.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/inline.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/let-alist.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mnt.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/macroexp.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map-ynp.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/nadvice.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/package-x.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/package.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/pcase.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/pp.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/re-builder.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/regexp-opt.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/regi.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ring.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/rx.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/seq.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/shadow.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/smie.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/subr-x.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/syntax.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/radix-tree.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/rmc.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tabulated-list.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tcover-ses.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tcover-unsafep.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/testcover.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/thunk.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/timer.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/timer-list.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tq.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/trace.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/unsafep.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/warnings.el.gz
%{_datadir}/emacs/%{version}/lisp/emacs-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/cua-base.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/cua-gmrk.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/cua-rect.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/edt-lk201.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/edt-mapper.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/edt-pc.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/edt-vt100.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/edt.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/keypad.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper-cmd.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper-ex.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper-init.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper-keym.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper-macs.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper-mous.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper-util.el.gz
%{_datadir}/emacs/%{version}/lisp/emulation/viper.el.gz
%{_datadir}/emacs/%{version}/lisp/env.el.gz
%{_datadir}/emacs/%{version}/lisp/epa-dired.el.gz
%{_datadir}/emacs/%{version}/lisp/epa-file.el.gz
%{_datadir}/emacs/%{version}/lisp/epa-hook.el.gz
%{_datadir}/emacs/%{version}/lisp/epa-mail.el.gz
%{_datadir}/emacs/%{version}/lisp/epa.el.gz
%{_datadir}/emacs/%{version}/lisp/epg-config.el.gz
%{_datadir}/emacs/%{version}/lisp/epg.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-autoaway.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-backend.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-button.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-capab.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-compat.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-dcc.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-desktop-notifications.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-ezbounce.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-fill.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-goodies.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-ibuffer.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-identd.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-imenu.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-join.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-lang.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-list.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-log.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-match.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-menu.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-netsplit.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-networks.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-notify.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-page.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-pcomplete.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-replace.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-ring.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-services.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-sound.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-speedbar.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-spelling.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-stamp.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-track.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-truncate.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc-xdcc.el.gz
%{_datadir}/emacs/%{version}/lisp/erc/erc.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-alias.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-banner.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-basic.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-cmpl.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-dirs.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-glob.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-hist.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-ls.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-pred.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-prompt.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-rebind.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-script.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-smart.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-term.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-tramp.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-unix.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/em-xtra.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-arg.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-cmd.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-ext.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-io.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-module.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-opt.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-proc.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-util.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/esh-var.el.gz
%{_datadir}/emacs/%{version}/lisp/eshell/eshell.el.gz
%{_datadir}/emacs/%{version}/lisp/expand.el.gz
%{_datadir}/emacs/%{version}/lisp/ezimage.el.gz
%{_datadir}/emacs/%{version}/lisp/face-remap.el.gz
%{_datadir}/emacs/%{version}/lisp/facemenu.el.gz
%{_datadir}/emacs/%{version}/lisp/faces.el.gz
%{_datadir}/emacs/%{version}/lisp/ffap.el.gz
%{_datadir}/emacs/%{version}/lisp/filecache.el.gz
%{_datadir}/emacs/%{version}/lisp/filenotify.el.gz
%{_datadir}/emacs/%{version}/lisp/files-x.el.gz
%{_datadir}/emacs/%{version}/lisp/files.el.gz
%{_datadir}/emacs/%{version}/lisp/filesets.el.gz
%{_datadir}/emacs/%{version}/lisp/find-cmd.el.gz
%{_datadir}/emacs/%{version}/lisp/find-dired.el.gz
%{_datadir}/emacs/%{version}/lisp/find-file.el.gz
%{_datadir}/emacs/%{version}/lisp/find-lisp.el.gz
%{_datadir}/emacs/%{version}/lisp/finder.el.gz
%{_datadir}/emacs/%{version}/lisp/flow-ctrl.el.gz
%{_datadir}/emacs/%{version}/lisp/foldout.el.gz
%{_datadir}/emacs/%{version}/lisp/follow.el.gz
%{_datadir}/emacs/%{version}/lisp/font-core.el.gz
%{_datadir}/emacs/%{version}/lisp/font-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/format-spec.el.gz
%{_datadir}/emacs/%{version}/lisp/format.el.gz
%{_datadir}/emacs/%{version}/lisp/forms.el.gz
%{_datadir}/emacs/%{version}/lisp/frame.el.gz
%{_datadir}/emacs/%{version}/lisp/frameset.el.gz
%{_datadir}/emacs/%{version}/lisp/fringe.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/canlock.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/deuglify.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gmm-utils.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-agent.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-art.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-async.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-bcklg.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-bookmark.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cache.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cite.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cloud.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cus.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-delay.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-demon.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-diary.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dired.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-draft.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dup.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-eform.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-fun.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-gravatar.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-group.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-html.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-icalendar.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-int.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-kill.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-logic.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-mh.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-ml.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-mlspl.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-msg.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-notifications.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-picon.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-range.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-registry.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-rfc1843.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-salt.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-score.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-sieve.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-spec.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-srvr.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-start.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-sum.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-topic.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-undo.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-util.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-uu.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-vm.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-win.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gnus.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/gssapi.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/legacy-gnus-agent.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mail-source.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/message.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-archive.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-bodies.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-decode.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-encode.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-extern.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-partial.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-url.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-util.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-uu.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mm-view.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mml-sec.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mml-smime.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mml.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mml1991.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/mml2015.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnagent.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnbabyl.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nndiary.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nndir.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nndoc.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nndraft.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nneething.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnfolder.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nngateway.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnheader.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnimap.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnir.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnmail.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnmaildir.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnmairix.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnmbox.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnmh.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnml.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnnil.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnoo.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnregistry.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnrss.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnspool.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nntp.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnvirtual.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/nnweb.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/score-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/smiley.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/smime.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/spam-report.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/spam-stat.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/spam-wash.el.gz
%{_datadir}/emacs/%{version}/lisp/gnus/spam.el.gz
%{_datadir}/emacs/%{version}/lisp/help-at-pt.el.gz
%{_datadir}/emacs/%{version}/lisp/help-fns.el.gz
%{_datadir}/emacs/%{version}/lisp/help-macro.el.gz
%{_datadir}/emacs/%{version}/lisp/help-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/help.el.gz
%{_datadir}/emacs/%{version}/lisp/hex-util.el.gz
%{_datadir}/emacs/%{version}/lisp/hexl.el.gz
%{_datadir}/emacs/%{version}/lisp/hfy-cmap.el.gz
%{_datadir}/emacs/%{version}/lisp/hi-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/hilit-chg.el.gz
%{_datadir}/emacs/%{version}/lisp/hippie-exp.el.gz
%{_datadir}/emacs/%{version}/lisp/hl-line.el.gz
%{_datadir}/emacs/%{version}/lisp/htmlfontify.el.gz
%{_datadir}/emacs/%{version}/lisp/ibuf-ext.el.gz
%{_datadir}/emacs/%{version}/lisp/ibuf-macs.el.gz
%{_datadir}/emacs/%{version}/lisp/ibuffer.el.gz
%{_datadir}/emacs/%{version}/lisp/icomplete.el.gz
%{_datadir}/emacs/%{version}/lisp/ido.el.gz
%{_datadir}/emacs/%{version}/lisp/ielm.el.gz
%{_datadir}/emacs/%{version}/lisp/iimage.el.gz
%{_datadir}/emacs/%{version}/lisp/image-dired.el.gz
%{_datadir}/emacs/%{version}/lisp/image-file.el.gz
%{_datadir}/emacs/%{version}/lisp/image-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/image.el.gz
%{_datadir}/emacs/%{version}/lisp/image/compface.el.gz
%{_datadir}/emacs/%{version}/lisp/image/gravatar.el.gz
%{_datadir}/emacs/%{version}/lisp/imenu.el.gz
%{_datadir}/emacs/%{version}/lisp/indent.el.gz
%{_datadir}/emacs/%{version}/lisp/info-look.el.gz
%{_datadir}/emacs/%{version}/lisp/info-xref.el.gz
%{_datadir}/emacs/%{version}/lisp/info.el.gz
%{_datadir}/emacs/%{version}/lisp/informat.el.gz
%{_datadir}/emacs/%{version}/lisp/international/ccl.el.gz
%{_datadir}/emacs/%{version}/lisp/international/characters.el.gz
%{_datadir}/emacs/%{version}/lisp/international/charscript.el.gz
%{_datadir}/emacs/%{version}/lisp/international/cp51932.el.gz
%{_datadir}/emacs/%{version}/lisp/international/eucjp-ms.el.gz
%{_datadir}/emacs/%{version}/lisp/international/fontset.el.gz
%{_datadir}/emacs/%{version}/lisp/international/isearch-x.el.gz
%{_datadir}/emacs/%{version}/lisp/international/iso-ascii.el.gz
%{_datadir}/emacs/%{version}/lisp/international/iso-cvt.el.gz
%{_datadir}/emacs/%{version}/lisp/international/iso-transl.el.gz
%{_datadir}/emacs/%{version}/lisp/international/ja-dic-cnv.el.gz
%{_datadir}/emacs/%{version}/lisp/international/ja-dic-utl.el.gz
%{_datadir}/emacs/%{version}/lisp/international/kinsoku.el.gz
%{_datadir}/emacs/%{version}/lisp/international/kkc.el.gz
%{_datadir}/emacs/%{version}/lisp/international/latexenc.el.gz
%{_datadir}/emacs/%{version}/lisp/international/latin1-disp.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule-cmds.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule-conf.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule-diag.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule-util.el.gz
%{_datadir}/emacs/%{version}/lisp/international/mule.el.gz
%{_datadir}/emacs/%{version}/lisp/international/ogonek.el.gz
%{_datadir}/emacs/%{version}/lisp/international/quail.el.gz
%{_datadir}/emacs/%{version}/lisp/international/rfc1843.el.gz
%{_datadir}/emacs/%{version}/lisp/international/robin.el.gz
%{_datadir}/emacs/%{version}/lisp/international/titdic-cnv.el.gz
%{_datadir}/emacs/%{version}/lisp/international/ucs-normalize.el.gz
%{_datadir}/emacs/%{version}/lisp/international/utf-7.el.gz
%{_datadir}/emacs/%{version}/lisp/international/utf7.el.gz
%{_datadir}/emacs/%{version}/lisp/isearch.el.gz
%{_datadir}/emacs/%{version}/lisp/isearchb.el.gz
%{_datadir}/emacs/%{version}/lisp/jit-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/jka-cmpr-hook.el.gz
%{_datadir}/emacs/%{version}/lisp/jka-compr.el.gz
%{_datadir}/emacs/%{version}/lisp/json.el.gz
%{_datadir}/emacs/%{version}/lisp/kermit.el.gz
%{_datadir}/emacs/%{version}/lisp/kmacro.el.gz
%{_datadir}/emacs/%{version}/lisp/language/burmese.el.gz
%{_datadir}/emacs/%{version}/lisp/language/cham.el.gz
%{_datadir}/emacs/%{version}/lisp/language/china-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/chinese.el.gz
%{_datadir}/emacs/%{version}/lisp/language/cyril-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/cyrillic.el.gz
%{_datadir}/emacs/%{version}/lisp/language/czech.el.gz
%{_datadir}/emacs/%{version}/lisp/language/english.el.gz
%{_datadir}/emacs/%{version}/lisp/language/ethio-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/ethiopic.el.gz
%{_datadir}/emacs/%{version}/lisp/language/european.el.gz
%{_datadir}/emacs/%{version}/lisp/language/georgian.el.gz
%{_datadir}/emacs/%{version}/lisp/language/greek.el.gz
%{_datadir}/emacs/%{version}/lisp/language/hanja-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/hebrew.el.gz
%{_datadir}/emacs/%{version}/lisp/language/ind-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/indian.el.gz
%{_datadir}/emacs/%{version}/lisp/language/japan-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/japanese.el.gz
%{_datadir}/emacs/%{version}/lisp/language/khmer.el.gz
%{_datadir}/emacs/%{version}/lisp/language/korea-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/korean.el.gz
%{_datadir}/emacs/%{version}/lisp/language/lao-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/lao.el.gz
%{_datadir}/emacs/%{version}/lisp/language/misc-lang.el.gz
%{_datadir}/emacs/%{version}/lisp/language/romanian.el.gz
%{_datadir}/emacs/%{version}/lisp/language/sinhala.el.gz
%{_datadir}/emacs/%{version}/lisp/language/slovak.el.gz
%{_datadir}/emacs/%{version}/lisp/language/tai-viet.el.gz
%{_datadir}/emacs/%{version}/lisp/language/thai-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/thai-word.el.gz
%{_datadir}/emacs/%{version}/lisp/language/thai.el.gz
%{_datadir}/emacs/%{version}/lisp/language/tibet-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/tibetan.el.gz
%{_datadir}/emacs/%{version}/lisp/language/tv-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/utf-8-lang.el.gz
%{_datadir}/emacs/%{version}/lisp/language/viet-util.el.gz
%{_datadir}/emacs/%{version}/lisp/language/vietnamese.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/ja-dic/ja-dic.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/4Corner.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ARRAY30.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/CCDOSPY.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/CTLau-b5.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/CTLau.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ECDICT.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ETZY.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/PY-b5.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/PY.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/Punct-b5.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/Punct.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/QJ-b5.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/QJ.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/SW.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/TONEPY.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ZIRANMA.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ZOZY.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/arabic.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/croatian.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/cyril-jis.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/cyrillic.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/czech.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ethiopic.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/georgian.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/greek.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/hangul.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja-jis.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja3.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/hebrew.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/indian.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ipa-praat.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/ipa.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/japanese.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/lao.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-alt.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-ltx.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-post.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-pre.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/lrt.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/persian.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/programmer-dvorak.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/py-punct.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/pypunct-b5.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/quick-b5.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/quick-cns.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/rfc1345.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/sgml-input.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/sisheng.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/slovak.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/symbol-ksc.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/tamil-dvorak.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/thai.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/tibetan.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/tsang-b5.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/tsang-cns.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/uni-input.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/viqr.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/vntelex.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/vnvni.el.gz
%{_datadir}/emacs/%{version}/lisp/leim/quail/welsh.el.gz
%{_datadir}/emacs/%{version}/lisp/linum.el.gz
%{_datadir}/emacs/%{version}/lisp/loadhist.el.gz
%{_datadir}/emacs/%{version}/lisp/locate.el.gz
%{_datadir}/emacs/%{version}/lisp/lpr.el.gz
%{_datadir}/emacs/%{version}/lisp/ls-lisp.el.gz
%{_datadir}/emacs/%{version}/lisp/macros.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/binhex.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/emacsbug.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/feedmail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/flow-fill.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/footnote.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/hashcash.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/ietf-drums.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mail-extr.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mail-hist.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mail-parse.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mail-prsvr.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mail-utils.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mailabbrev.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mailalias.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mailclient.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mailheader.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/metamail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/mspools.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/qp.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/reporter.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rfc2045.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rfc2047.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rfc2231.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rfc2368.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rfc822.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmail-spam-filter.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmailedit.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmailkwd.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmailmm.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmailmsc.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmailout.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmailsort.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/rmailsum.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/sendmail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/smtpmail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/supercite.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/uce.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/undigest.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/unrmail.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/uudecode.el.gz
%{_datadir}/emacs/%{version}/lisp/mail/yenc.el.gz
%{_datadir}/emacs/%{version}/lisp/makesum.el.gz
%{_datadir}/emacs/%{version}/lisp/man.el.gz
%{_datadir}/emacs/%{version}/lisp/master.el.gz
%{_datadir}/emacs/%{version}/lisp/mb-depth.el.gz
%{_datadir}/emacs/%{version}/lisp/md4.el.gz
%{_datadir}/emacs/%{version}/lisp/menu-bar.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-alias.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-buffers.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-comp.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-compat.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-e.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-folder.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-funcs.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-gnus.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-identity.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-inc.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-junk.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-letter.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-limit.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-mime.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-print.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-scan.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-search.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-seq.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-show.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-speed.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-thread.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-tool-bar.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-utils.el.gz
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-xface.el.gz
%{_datadir}/emacs/%{version}/lisp/midnight.el.gz
%{_datadir}/emacs/%{version}/lisp/minibuf-eldef.el.gz
%{_datadir}/emacs/%{version}/lisp/minibuffer.el.gz
%{_datadir}/emacs/%{version}/lisp/misc.el.gz
%{_datadir}/emacs/%{version}/lisp/misearch.el.gz
%{_datadir}/emacs/%{version}/lisp/mouse-copy.el.gz
%{_datadir}/emacs/%{version}/lisp/mouse-drag.el.gz
%{_datadir}/emacs/%{version}/lisp/mouse.el.gz
%{_datadir}/emacs/%{version}/lisp/mpc.el.gz
%{_datadir}/emacs/%{version}/lisp/msb.el.gz
%{_datadir}/emacs/%{version}/lisp/mwheel.el.gz
%{_datadir}/emacs/%{version}/lisp/net/ange-ftp.el.gz
%{_datadir}/emacs/%{version}/lisp/net/browse-url.el.gz
%{_datadir}/emacs/%{version}/lisp/net/dbus.el.gz
%{_datadir}/emacs/%{version}/lisp/net/dig.el.gz
%{_datadir}/emacs/%{version}/lisp/net/dns.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudc-bob.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudc-export.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudc-hotlist.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudc-vars.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudc.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudcb-bbdb.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudcb-ldap.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eudcb-mab.el.gz
%{_datadir}/emacs/%{version}/lisp/net/eww.el.gz
%{_datadir}/emacs/%{version}/lisp/net/gnutls.el.gz
%{_datadir}/emacs/%{version}/lisp/net/goto-addr.el.gz
%{_datadir}/emacs/%{version}/lisp/net/hmac-def.el.gz
%{_datadir}/emacs/%{version}/lisp/net/hmac-md5.el.gz
%{_datadir}/emacs/%{version}/lisp/net/imap.el.gz
%{_datadir}/emacs/%{version}/lisp/net/ldap.el.gz
%{_datadir}/emacs/%{version}/lisp/net/mailcap.el.gz
%{_datadir}/emacs/%{version}/lisp/net/mairix.el.gz
%{_datadir}/emacs/%{version}/lisp/net/net-utils.el.gz
%{_datadir}/emacs/%{version}/lisp/net/netrc.el.gz
%{_datadir}/emacs/%{version}/lisp/net/network-stream.el.gz
%{_datadir}/emacs/%{version}/lisp/net/newst-backend.el.gz
%{_datadir}/emacs/%{version}/lisp/net/newst-plainview.el.gz
%{_datadir}/emacs/%{version}/lisp/net/newst-reader.el.gz
%{_datadir}/emacs/%{version}/lisp/net/newst-ticker.el.gz
%{_datadir}/emacs/%{version}/lisp/net/newst-treeview.el.gz
%{_datadir}/emacs/%{version}/lisp/net/newsticker.el.gz
%{_datadir}/emacs/%{version}/lisp/net/nsm.el.gz
%{_datadir}/emacs/%{version}/lisp/net/ntlm.el.gz
%{_datadir}/emacs/%{version}/lisp/net/pop3.el.gz
%{_datadir}/emacs/%{version}/lisp/net/quickurl.el.gz
%{_datadir}/emacs/%{version}/lisp/net/puny.el.gz
%{_datadir}/emacs/%{version}/lisp/net/rcirc.el.gz
%{_datadir}/emacs/%{version}/lisp/net/rfc2104.el.gz
%{_datadir}/emacs/%{version}/lisp/net/rlogin.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sasl-cram.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sasl-digest.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sasl-ntlm.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sasl-scram-rfc.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sasl.el.gz
%{_datadir}/emacs/%{version}/lisp/net/secrets.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sieve-manage.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sieve-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/net/sieve.el.gz
%{_datadir}/emacs/%{version}/lisp/net/shr-color.el.gz
%{_datadir}/emacs/%{version}/lisp/net/shr.el.gz
%{_datadir}/emacs/%{version}/lisp/net/snmp-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/net/soap-client.el.gz
%{_datadir}/emacs/%{version}/lisp/net/soap-inspect.el.gz
%{_datadir}/emacs/%{version}/lisp/net/socks.el.gz
%{_datadir}/emacs/%{version}/lisp/net/starttls.el.gz
%{_datadir}/emacs/%{version}/lisp/net/telnet.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tls.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-adb.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-cache.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-cmds.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-compat.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-ftp.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-gvfs.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-sh.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-smb.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp-uu.el.gz
%{_datadir}/emacs/%{version}/lisp/net/tramp.el.gz
%{_datadir}/emacs/%{version}/lisp/net/trampver.el.gz
%{_datadir}/emacs/%{version}/lisp/net/webjump.el.gz
%{_datadir}/emacs/%{version}/lisp/net/zeroconf.el.gz
%{_datadir}/emacs/%{version}/lisp/newcomment.el.gz
%{_datadir}/emacs/%{version}/lisp/notifications.el.gz
%{_datadir}/emacs/%{version}/lisp/novice.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-enc.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-maint.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-ns.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-outln.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-parse.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-rap.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-util.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-cmpct.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-dt.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-loc.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-maint.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-match.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-nxml.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-parse.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-pttrn.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-uri.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-util.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-valid.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/rng-xsd.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/xmltok.el.gz
%{_datadir}/emacs/%{version}/lisp/nxml/xsd-regexp.el.gz
%{_datadir}/emacs/%{version}/lisp/obarray.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/abbrevlist.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/assoc.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/bruce.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/cc-compat.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/cl-compat.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/complete.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/crisp.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/cust-print.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/erc-hecomplete.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/eudcb-ph.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/fast-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/gulp.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/gs.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/iswitchb.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/html2text.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/landmark.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/lazy-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/ledit.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/levents.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/lmenu.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/longlines.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/lucid.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/mailpost.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/meese.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/mouse-sel.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/old-emacs-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/old-whitespace.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/options.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/otodo-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/patcomp.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pc-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pc-select.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-def.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-gpg.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-parse.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-pgp.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-pgp5.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/rcompile.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/s-region.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/sregex.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/sup-mouse.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/terminal.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-edt.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-extras.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-mapper.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/vc-arch.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/vi.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/vip.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/ws-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/xesam.el.gz
%{_datadir}/emacs/%{version}/lisp/obsolete/yow.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-C.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-J.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-R.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-abc.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-asymptote.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-awk.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-calc.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-clojure.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-comint.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-coq.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-core.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-css.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-ditaa.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-dot.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-ebnf.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-emacs-lisp.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-eval.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-exp.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-forth.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-fortran.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-gnuplot.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-groovy.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-haskell.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-hledger.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-io.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-java.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-js.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-keys.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-latex.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-ledger.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-lilypond.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-lisp.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-lob.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-lua.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-makefile.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-matlab.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-maxima.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-mscgen.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-ocaml.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-octave.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-org.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-perl.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-picolisp.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-plantuml.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-processing.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-python.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-ref.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-ruby.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-sass.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-scheme.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-screen.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-sed.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-shell.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-shen.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-sql.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-sqlite.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-stan.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-table.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-tangle.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob-vala.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ob.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-agenda.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-archive.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-attach.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-bbdb.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-bibtex.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-capture.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-clock.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-colview.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-compat.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-crypt.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-ctags.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-datetree.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-docview.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-duration.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-element.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-entities.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-eshell.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-eww.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-faces.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-feed.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-footnote.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-gnus.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-habit.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-id.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-indent.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-info.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-inlinetask.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-irc.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-lint.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-list.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-macro.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-macs.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-mhe.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-mobile.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-mouse.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-pcomplete.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-plot.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-protocol.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-rmail.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-src.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-table.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-timer.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org-w3m.el.gz
%{_datadir}/emacs/%{version}/lisp/org/org.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-ascii.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-beamer.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-html.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-icalendar.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-latex.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-man.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-md.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-odt.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-org.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-publish.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox-texinfo.el.gz
%{_datadir}/emacs/%{version}/lisp/org/ox.el.gz
%{_datadir}/emacs/%{version}/lisp/outline.el.gz
%{_datadir}/emacs/%{version}/lisp/paren.el.gz
%{_datadir}/emacs/%{version}/lisp/password-cache.el.gz
%{_datadir}/emacs/%{version}/lisp/pcmpl-cvs.el.gz
%{_datadir}/emacs/%{version}/lisp/pcmpl-gnu.el.gz
%{_datadir}/emacs/%{version}/lisp/pcmpl-linux.el.gz
%{_datadir}/emacs/%{version}/lisp/pcmpl-rpm.el.gz
%{_datadir}/emacs/%{version}/lisp/pcmpl-unix.el.gz
%{_datadir}/emacs/%{version}/lisp/pcmpl-x.el.gz
%{_datadir}/emacs/%{version}/lisp/pcomplete.el.gz
%{_datadir}/emacs/%{version}/lisp/pixel-scroll.el.gz
%{_datadir}/emacs/%{version}/lisp/play/5x5.el.gz
%{_datadir}/emacs/%{version}/lisp/play/animate.el.gz
%{_datadir}/emacs/%{version}/lisp/play/blackbox.el.gz
%{_datadir}/emacs/%{version}/lisp/play/bubbles.el.gz
%{_datadir}/emacs/%{version}/lisp/play/cookie1.el.gz
%{_datadir}/emacs/%{version}/lisp/play/decipher.el.gz
%{_datadir}/emacs/%{version}/lisp/play/dissociate.el.gz
%{_datadir}/emacs/%{version}/lisp/play/doctor.el.gz
%{_datadir}/emacs/%{version}/lisp/play/dunnet.el.gz
%{_datadir}/emacs/%{version}/lisp/play/fortune.el.gz
%{_datadir}/emacs/%{version}/lisp/play/gamegrid.el.gz
%{_datadir}/emacs/%{version}/lisp/play/gametree.el.gz
%{_datadir}/emacs/%{version}/lisp/play/gomoku.el.gz
%{_datadir}/emacs/%{version}/lisp/play/handwrite.el.gz
%{_datadir}/emacs/%{version}/lisp/play/hanoi.el.gz
%{_datadir}/emacs/%{version}/lisp/play/life.el.gz
%{_datadir}/emacs/%{version}/lisp/play/morse.el.gz
%{_datadir}/emacs/%{version}/lisp/play/mpuz.el.gz
%{_datadir}/emacs/%{version}/lisp/play/pong.el.gz
%{_datadir}/emacs/%{version}/lisp/play/snake.el.gz
%{_datadir}/emacs/%{version}/lisp/play/solitaire.el.gz
%{_datadir}/emacs/%{version}/lisp/play/spook.el.gz
%{_datadir}/emacs/%{version}/lisp/play/studly.el.gz
%{_datadir}/emacs/%{version}/lisp/play/tetris.el.gz
%{_datadir}/emacs/%{version}/lisp/play/zone.el.gz
%{_datadir}/emacs/%{version}/lisp/plstore.el.gz
%{_datadir}/emacs/%{version}/lisp/printing.el.gz
%{_datadir}/emacs/%{version}/lisp/proced.el.gz
%{_datadir}/emacs/%{version}/lisp/profiler.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-prj.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-stmt.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ada-xref.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/antlr-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/asm-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/autoconf.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/bat-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/bug-reference.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-align.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-awk.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-bytecomp.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-cmds.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-defs.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-engine.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-fonts.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-guess.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-langs.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-menus.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-styles.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-vars.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cfengine.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cmacexp.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/compile.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cperl-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cpp.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/cwarn.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/dcl-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-abn.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-bnf.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-dtd.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-ebx.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-iso.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-otz.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-yac.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf2ps.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ebrowse.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/elisp-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/etags.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/executable.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/f90.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake-proc.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/fortran.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/gdb-mi.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/glasses.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/grep.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/gud.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/hideif.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/hideshow.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/icon.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-complete-structtag.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-help.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-shell.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-toolbar.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/idlwave.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/inf-lisp.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/js.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ld-script.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/m4-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/make-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/mantemp.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/meta-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/mixal-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/modula2.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/octave.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/opascal.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/pascal.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/perl-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/prog-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/project.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/prolog.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ps-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/python.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/ruby-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/scheme.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/sh-script.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/simula.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/sql.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/subword.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/tcl.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/vera-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/verilog-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/vhdl-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/which-func.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/xref.el.gz
%{_datadir}/emacs/%{version}/lisp/progmodes/xscheme.el.gz
%{_datadir}/emacs/%{version}/lisp/ps-bdf.el.gz
%{_datadir}/emacs/%{version}/lisp/ps-def.el.gz
%{_datadir}/emacs/%{version}/lisp/ps-mule.el.gz
%{_datadir}/emacs/%{version}/lisp/ps-print.el.gz
%{_datadir}/emacs/%{version}/lisp/ps-samp.el.gz
%{_datadir}/emacs/%{version}/lisp/recentf.el.gz
%{_datadir}/emacs/%{version}/lisp/rect.el.gz
%{_datadir}/emacs/%{version}/lisp/register.el.gz
%{_datadir}/emacs/%{version}/lisp/registry.el.gz
%{_datadir}/emacs/%{version}/lisp/repeat.el.gz
%{_datadir}/emacs/%{version}/lisp/replace.el.gz
%{_datadir}/emacs/%{version}/lisp/reposition.el.gz
%{_datadir}/emacs/%{version}/lisp/reveal.el.gz
%{_datadir}/emacs/%{version}/lisp/rfn-eshadow.el.gz
%{_datadir}/emacs/%{version}/lisp/rot13.el.gz
%{_datadir}/emacs/%{version}/lisp/ruler-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/rtree.el.gz
%{_datadir}/emacs/%{version}/lisp/savehist.el.gz
%{_datadir}/emacs/%{version}/lisp/saveplace.el.gz
%{_datadir}/emacs/%{version}/lisp/sb-image.el.gz
%{_datadir}/emacs/%{version}/lisp/scroll-all.el.gz
%{_datadir}/emacs/%{version}/lisp/scroll-bar.el.gz
%{_datadir}/emacs/%{version}/lisp/scroll-lock.el.gz
%{_datadir}/emacs/%{version}/lisp/select.el.gz
%{_datadir}/emacs/%{version}/lisp/server.el.gz
%{_datadir}/emacs/%{version}/lisp/ses.el.gz
%{_datadir}/emacs/%{version}/lisp/shadowfile.el.gz
%{_datadir}/emacs/%{version}/lisp/shell.el.gz
%{_datadir}/emacs/%{version}/lisp/simple.el.gz
%{_datadir}/emacs/%{version}/lisp/sort.el.gz
%{_datadir}/emacs/%{version}/lisp/soundex.el.gz
%{_datadir}/emacs/%{version}/lisp/speedbar.el.gz
%{_datadir}/emacs/%{version}/lisp/startup.el.gz
%{_datadir}/emacs/%{version}/lisp/strokes.el.gz
%{_datadir}/emacs/%{version}/lisp/subr.el.gz
%{_datadir}/emacs/%{version}/lisp/svg.el.gz
%{_datadir}/emacs/%{version}/lisp/t-mouse.el.gz
%{_datadir}/emacs/%{version}/lisp/tabify.el.gz
%{_datadir}/emacs/%{version}/lisp/talk.el.gz
%{_datadir}/emacs/%{version}/lisp/tar-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/tempo.el.gz
%{_datadir}/emacs/%{version}/lisp/term.el.gz
%{_datadir}/emacs/%{version}/lisp/term/AT386.el.gz
%{_datadir}/emacs/%{version}/lisp/term/bobcat.el.gz
%{_datadir}/emacs/%{version}/lisp/term/common-win.el.gz
%{_datadir}/emacs/%{version}/lisp/term/cygwin.el.gz
%{_datadir}/emacs/%{version}/lisp/term/internal.el.gz
%{_datadir}/emacs/%{version}/lisp/term/iris-ansi.el.gz
%{_datadir}/emacs/%{version}/lisp/term/konsole.el.gz
%{_datadir}/emacs/%{version}/lisp/term/linux.el.gz
%{_datadir}/emacs/%{version}/lisp/term/lk201.el.gz
%{_datadir}/emacs/%{version}/lisp/term/news.el.gz
%{_datadir}/emacs/%{version}/lisp/term/ns-win.el.gz
%{_datadir}/emacs/%{version}/lisp/term/pc-win.el.gz
%{_datadir}/emacs/%{version}/lisp/term/rxvt.el.gz
%{_datadir}/emacs/%{version}/lisp/term/screen.el.gz
%{_datadir}/emacs/%{version}/lisp/term/sun.el.gz
%{_datadir}/emacs/%{version}/lisp/term/tmux.el.gz
%{_datadir}/emacs/%{version}/lisp/term/tty-colors.el.gz
%{_datadir}/emacs/%{version}/lisp/term/tvi970.el.gz
%{_datadir}/emacs/%{version}/lisp/term/vt100.el.gz
%{_datadir}/emacs/%{version}/lisp/term/vt200.el.gz
%{_datadir}/emacs/%{version}/lisp/term/w32-win.el.gz
%{_datadir}/emacs/%{version}/lisp/term/w32console.el.gz
%{_datadir}/emacs/%{version}/lisp/term/wyse50.el.gz
%{_datadir}/emacs/%{version}/lisp/term/x-win.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/artist.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/bib-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/bibtex-style.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/bibtex.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/conf-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/css-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/dns-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/enriched.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/fill.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/flyspell.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/ispell.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/less-css-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/makeinfo.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/mhtml-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/nroff-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/page-ext.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/page.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/paragraphs.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/picture.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/po.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/refbib.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/refer.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/refill.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-auc.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-cite.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-dcr.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-global.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-index.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-parse.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-ref.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-sel.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-toc.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-vars.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/remember.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/rst.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/sgml-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/table.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/tex-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/texinfmt.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/texinfo.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/texnfo-upd.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/text-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/tildify.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/two-column.el.gz
%{_datadir}/emacs/%{version}/lisp/textmodes/underline.el.gz
%{_datadir}/emacs/%{version}/lisp/thingatpt.el.gz
%{_datadir}/emacs/%{version}/lisp/thumbs.el.gz
%{_datadir}/emacs/%{version}/lisp/time-stamp.el.gz
%{_datadir}/emacs/%{version}/lisp/time.el.gz
%{_datadir}/emacs/%{version}/lisp/timezone.el.gz
%{_datadir}/emacs/%{version}/lisp/tmm.el.gz
%{_datadir}/emacs/%{version}/lisp/tool-bar.el.gz
%{_datadir}/emacs/%{version}/lisp/tooltip.el.gz
%{_datadir}/emacs/%{version}/lisp/tree-widget.el.gz
%{_datadir}/emacs/%{version}/lisp/tutorial.el.gz
%{_datadir}/emacs/%{version}/lisp/type-break.el.gz
%{_datadir}/emacs/%{version}/lisp/uniquify.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-about.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-auth.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-cache.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-cid.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-cookie.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-dav.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-dired.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-domsuf.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-expand.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-file.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-ftp.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-future.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-gw.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-handlers.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-history.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-http.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-imap.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-irc.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-ldap.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-mailto.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-methods.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-misc.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-news.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-nfs.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-ns.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-parse.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-privacy.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-proxy.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-queue.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-tramp.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-util.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url-vars.el.gz
%{_datadir}/emacs/%{version}/lisp/url/url.el.gz
%{_datadir}/emacs/%{version}/lisp/userlock.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/add-log.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/compare-w.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/cvs-status.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/diff-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/diff.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-diff.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-help.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-hook.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-init.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-merg.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-mult.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-ptch.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-util.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-vers.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff-wind.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/ediff.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/emerge.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/log-edit.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/log-view.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-defs.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-info.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-parse.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-util.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/pcvs.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/smerge-mode.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-annotate.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-bzr.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-cvs.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-dav.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-dir.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-dispatcher.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-filewise.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-git.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-hg.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-hooks.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-mtn.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-rcs.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-sccs.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-src.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc-svn.el.gz
%{_datadir}/emacs/%{version}/lisp/vc/vc.el.gz
%{_datadir}/emacs/%{version}/lisp/vcursor.el.gz
%{_datadir}/emacs/%{version}/lisp/version.el.gz
%{_datadir}/emacs/%{version}/lisp/view.el.gz
%{_datadir}/emacs/%{version}/lisp/vt-control.el.gz
%{_datadir}/emacs/%{version}/lisp/vt100-led.el.gz
%{_datadir}/emacs/%{version}/lisp/w32-fns.el.gz
%{_datadir}/emacs/%{version}/lisp/w32-vars.el.gz
%{_datadir}/emacs/%{version}/lisp/wdired.el.gz
%{_datadir}/emacs/%{version}/lisp/whitespace.el.gz
%{_datadir}/emacs/%{version}/lisp/wid-browse.el.gz
%{_datadir}/emacs/%{version}/lisp/wid-edit.el.gz
%{_datadir}/emacs/%{version}/lisp/widget.el.gz
%{_datadir}/emacs/%{version}/lisp/windmove.el.gz
%{_datadir}/emacs/%{version}/lisp/window.el.gz
%{_datadir}/emacs/%{version}/lisp/winner.el.gz
%{_datadir}/emacs/%{version}/lisp/woman.el.gz
%{_datadir}/emacs/%{version}/lisp/x-dnd.el.gz
%{_datadir}/emacs/%{version}/lisp/xdg.el.gz
%{_datadir}/emacs/%{version}/lisp/xml.el.gz
%{_datadir}/emacs/%{version}/lisp/xt-mouse.el.gz
%{_datadir}/emacs/%{version}/lisp/xwidget.el.gz

%files -n etags
%defattr(-,root,root)
%doc etc/ETAGS.EBNF
%doc etc/ETAGS.README
%{_bindir}/etags
%{_bindir}/gnuctags
%{_mandir}/man1/etags.1%{ext_man}
%{_mandir}/man1/gnuctags.1%{ext_man}
%ghost %{_bindir}/ctags
%ghost %{_sysconfdir}/alternatives/ctags
%ghost %{_mandir}/man1/ctags.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/ctags.1%{ext_man}

%changelog
