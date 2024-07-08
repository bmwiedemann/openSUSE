#
# spec file for package xemacs
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xemacs
# this is tricky to fix for PIE support. revisit to remove occasionaly after 21.5.34 version
#!BuildIgnore:	gcc-PIE
#!BuildIgnore:  diffstat
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  compface
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  info
BuildRequires:  krb5
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  par
BuildRequires:  texinfo
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xaw3d)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)

%if 0%{?suse_version} > 1130
BuildRequires:  gpm-devel
%else
BuildRequires:  gpm
%endif
%define _id     995257d0c590
%define _hg     hg%{_id}
Version:        21.5.34
Release:        0
Summary:        XEmacs
License:        GPL-3.0-or-later
Group:          Productivity/Editors/Emacs
%define	appdefdir  /usr/share/X11
%define xbindir    /usr/bin
%define xincludes  /usr/include
%define xlibraries /usr/%{_lib}
URL:            http://www.xemacs.org
# Howto get the Mercurial tree of XEmacs:
# See: http://xemacs.digimirror.nl/Develop/hgaccess.html
# hg clone http://hg.debian.org/hg/xemacs/xemacs-beta
#
# delete the .hg directory before creating the tarball in order
# not to make the source rpm huge.
Source0:        http://ftp.xemacs.org/pub/xemacs/xemacs-21.5/%{name}-%{version}.tar.gz
Source1:        xe-list.el
Source2:        fix-load-history.el
Source3:        xemacs.desktop
Source4:        xemacs.png
Source5:        suse-xft-init.el
Source6:        site-start.el
Source7:        skel.init.el
Source90:       xemacs-rpmlintrc
Patch0:         xemacs.patch
# keep in sync with the similar patch to the app-defaults in the main xemacs-packages package:
Patch3:         xemacs-app-defaults.patch
Patch18:        xemacs-21.4.8-xevent.patch
Patch20:        xemacs-21.4.13-ppc64.patch
Patch23:        xemacs-ptmx.dif
Patch27:        xemacs-level3.patch
Patch28:        xemacs-21.5.18-movemail.patch
Patch32:        do-not-create-backups-in-temp-directories.patch
Patch33:        set-locale-to-c-when-not-supported-by-x.patch
Patch39:        xemacs-tinfo.dif
Patch43:        set-language-unicode-precedence-list.patch
Patch45:        fix-defface-custom-modified-face.patch
Patch50:        menus-always-utf8.patch
Patch51:        bnc502716-fontmenu.patch
Patch52:        bnc502716-xft.patch
Patch53:        xemacs-21.5.31-array.patch
Patch54:        xemacs-21.5.34-gcc5.patch
Patch56:        xemacs-libpng15.patch
Patch292811:    bugzilla-292811-make-x-make-font-bold-italic-xft-work.patch
Patch301352:    bugzilla-301352-fix-wrong-incrementing-in-macros.patch
# PATCH-FIX-UPSTREAM bsc#930170
Patch57:        xemacs-21.5.34-Xaw3D_I18N.patch
# PATCH-FIX-SUSE bsc#932321
Patch58:        xemacs-21.5.34-custom-fonts.patch
# PATCH-FIX-SUSE do wait on alsa
Patch59:        xemacs-21.5.34-alsaplay.patch
# PATCH-FIX-SUSE avoid redefinition of sbrk
Patch60:        xemacs-21.5.34-sbrk.patch
# PATCH-FIX-SUSE fix make build race
Patch61:        xemacs-21.5.34-boo1115177.patch
Patch62:        xemacs-libX11-boo1175028.patch
# PATCH-FIX-SUSE sys_siglist is deprecated
Patch63:        xemacs-21.5.34-strsignal.patch
Patch64:        xemacs-21.5.34-fix2038.patch
# PATCH-FIX-SUSE drop hostname+timestamp from .elc
Patch65:        reproducible.patch
Requires(pre):  permissions
Requires:       ctags
Requires:       efont-unicode
Requires:       ifnteuro
Requires:       xemacs-info
Requires:       xemacs-packages
Requires:       xorg-x11-fonts
Requires:       xorg-x11-fonts-core
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:      gnuserv
%define _default_patch_fuzz 2

%bcond_with lock

%description
This is the current version of XEmacs, formerly known as Lucid-Emacs.
It is related to other versions of Emacs, in particular GNU Emacs. Its
emphasis is on modern graphical user interface support and an open
software development model, similar to Linux.

Lisp macros are not necessarily interchangeable between GNU-Emacs and
XEmacs. This is mainly important for translated .elc files and the key
macros.

%package     -n xemacs-el
Summary:        Emacs-Lisp source files for XEmacs
Group:          Productivity/Editors/Emacs
Requires:       xemacs = %{version}
Requires:       xemacs-packages-el
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description -n xemacs-el
Most Emacs-Lisp source files are not needed for running XEmacs. Most of
them are also available in byte compiled form and therefore not
necessary at runtime. The true XEmacs addict will install them
nevertheless because it is often useful and enlightening to have a look
at the Lisp sources.

%package     -n xemacs-info
Summary:        Info Files for XEmacs
Group:          Productivity/Editors/Emacs
Requires:       xemacs-packages-info
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description -n xemacs-info
This package contains all info files for XEmacs. All these files can be
read online with XEmacs and describe XEmacs and some of its modes.

%prep
%ifarch ia64
# ia64 has different memory laylout then x86 or x86_64 have!
%global pdump_broken 1
%endif
# Currently XEmacs is not fully usable for Xfreetype support
# therefore we use XFontSet support:
%{!?enable_xfs:%global enable_xfs 1}
%{!?pdump_broken:%global pdump_broken 0}
%{!?kkcc_broken:%global kkcc_broken 0}
%if ! %enable_xfs
echo Use xft, requires X11, Xft, Xrender, freetype, and fontconfig support.
%else
echo Use xfs, that is XFontSet support for internationalized menubar.
%endif
%setup -q
%patch -P 3 -p1
%patch -P 18 -p0 -b .xevent
%patch -P 20 -p1
%patch -P 23 -p1
%patch -P 27 -p1 -b .lvl3
%patch -P 28 -p1 -b .movemail
%patch -P 32 -p1
%patch -P 33 -p1
%patch -P 39 -p0
%patch -P 43 -p1
%patch -P 45 -p0
%patch -P 50 -p1
%if ! %enable_xfs
%patch -P 51 -p0
%patch -P 52 -p0
%endif
%patch -P 53 -p0
%patch -P 54 -p0
%patch -P 56 -p1
%patch -P 292811 -p1
%patch -P 301352 -p1
%patch -P 57 -p0
%patch -P 58 -p0
%patch -P 59 -p1
%patch -P 60 -p0
%patch -P 61 -p0
%patch -P 62 -p0
%patch -P 63 -p0
%patch -P 0 -p1
find lisp/ etc/ -name '*.elc' | xargs -r rm -f
find . -name CVS -type d | xargs rm -rf
find . -name .cvsignore -type f | xargs rm -f
chmod -R u+w *
# Without making the timestamps equal here, some files will not be
# byte compiled:
find . | xargs touch -r .

# make sure that the binaries work (pagesize on build must be the same as on target, bnc#726769)
%if 0%{?suse_version} >= 1110
%ifarch ppc ppc64 ia64
%if %(getconf PAGESIZE) != 65536
%error "Error: wrong build host, PAGESIZE must be 65536"
exit 1
%endif
%endif
%endif
%patch -P 64 -p1
%patch -P 65 -p1

%build
  cflags ()
  {
      local flag=$1; shift
      local var=$1; shift
      test -n "${flag}" -a -n "${var}" || return
      case "${!var}" in
      *${flag}*) return
      esac
      set -o noclobber
      case "$flag" in
      -Wl,*)
	  if echo 'int main () { return 0; }' | \
	      ${CC:-gcc} -Werror $flag -o /dev/null -xc ldtest.c > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
	  ;;
      *)
	  if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
      esac
      set +o noclobber
  }

# libtoolize --force
# autoreconf --force --install --verbose
# rm configure
autoconf --force
VERSION=%{version}
  SHARE=/usr/share
    LIB=/usr/lib
    SYS=${RPM_ARCH}-suse-linux
%ifarch %ix86
    cflags -fprefetch-loop-arrays LOOP
    cflags -funroll-loops         LOOP
%endif
    cflags -Wno-unused-but-set-variable RPM_OPT_FLAGS
    cflags -Wno-unused-value            RPM_OPT_FLAGS
    cflags -Wno-switch                  RPM_OPT_FLAGS
    cflags -fno-strict-aliasing         RPM_OPT_FLAGS
   INFO=${SHARE}/xemacs/info
LIBEXEC=${LIB}/xemacs/${VERSION}
   ARCH=${LIBEXEC}/${SYS}
   DATA=${SHARE}
   LISP=${DATA}/xemacs/${VERSION}/lisp
    ETC=${DATA}/xemacs/${VERSION}/etc
    MOD=${ARCH}/modules
  STATE=/var/lib/xemacs
    MAN=/usr/share/man/man1
 CFLAGS="-Wall ${RPM_OPT_FLAGS} -pipe ${LOOP} -DLDAP_DEPRECATED "
%ifarch s390x
 CFLAGS="$CFLAGS -O1"
%endif
# To to the menu translations, add:
# $CFLAGS="$CFLAGS -DPRINT_XLWMENU_RESOURCE_CONVERSIONS "
# this prints the Xresources used for the Menus to stdout
# when the Menus are used.
#
# Maybe there are emacs and xemacs on the
# same system, therefore put binaries into /usr/X11R6/bin
#
PREFIX="--prefix=/usr \
	--exec-prefix=/usr \
	--bindir=%{xbindir} \
	--datadir=${SHARE} \
	--with-archlibdir=${ARCH} \
	--with-docdir=${ARCH} \
	--with-lispdir=${LISP} \
	--with-etcdir=${ETC} \
	--with-statedir=${STATE} \
	--with-moduledir=${MOD} \
	--infodir=${INFO} \
	--mandir=${MAN} \
"
#
# --with-sound=both requires NAS (Network Audio System)
#
# --with-socks and --with-term needs some nonexisting libs
#                              (maybe included in {g}libc)
# --with-tooltalk needs tt_c.h
# --with-canna needs X11 canna support
# --with-wnn needs X11 wnn support
#
# We need site-lisp because the long time (x)emacs users
# expect something like this.
#
#  --with-system-malloc only for libc.5.4.3x and higher
#
#  when using "--rel-alloc, XEmacs 21.5.18 crashes often when using
#  'compile-goto-error'.
SPECIAL="--with-database=berkdb,gdbm \
	 --with-ncurses \
	 --with-tty=yes \
	 --with-site-lisp \
%if %kkcc_broken
	 --disable-kkcc \
%endif
%if 0%{?suse_version} > 1320
	 --with-system-malloc \
%endif
%ifnarch s390
	 --enable-sound=native \
	 --with-gpm \
%else
	 --with-sound=nonative,alsa \
%endif
%if %pdump_broken
	 --without-pdump \
%endif
"
#
#  * --with-xfs Compile with XFontSet support for bilingual menubar.
#               Can't use this option with --with-xim=motif or xlib.
#               And should have --with-menubars=lucid.
#               (this is necessary to get German, French, Japanese
#               and Romanian texts in the menus.
#
FONTS="\
%if %enable_xfs
	 --with-xfs \
%else
	 --with-xft=all \
%endif
"
#
# Graphics and X window system
#  * --with-cde needs Motif
#
X11="--with-xpm \
     --with-gif \
     --with-tiff \
     --with-jpeg \
     --with-png \
     --with-x \
     --with-athena=3d \
     --with-menubars=lucid \
     --with-widgets=athena \
     --with-dialogs=athena \
     --with-scrollbars=lucid \
     --x-includes=%{xincludes} \
     --x-libraries=%{xlibraries} \
     --with-xim=xlib \
"
#
# Mail
#  * --mail-locking should be self detected
#  * --with-xface requires compface library
#
MAIL="--enable-clash-detection \
      --with-ldap \
      --with-pop
"
#
# Mule
#
MULE="--with-mule"
#
# Compilation
#
COMP="--with-gcc \
      --with-dynamic \
      --with-debug \
      --enable-error-checking=none \
      --with-cflags=\"${CFLAGS}\" \
"
eval ./configure $SYS $COMP $PREFIX $SPECIAL $X11 $MULE $FONTS $MAIL
if grep -q _DEFAULT_SOURCE /usr/include/features.h ; then
    sed -ri '/^(#[[:blank:]]*define[[:blank:]]+_(BSD|SVID)_SOURCE)/{
	s/_BSD_SOURCE/_DEFAULT_SOURCE/
	s/_SVID_SOURCE/_DEFAULT_SOURCE/
    }' src/config.h
fi
make %{?_smp_mflags}

%install
set +o posix
#
mkdir -p %{buildroot}%{_datadir}/xemacs/site-lisp/lisp
mkdir -p %{buildroot}%{_datadir}/xemacs/site-packages/lisp/term
%if %{with lock}
mkdir -p %{buildroot}%{_localstatedir}/lib/xemacs/lock
chmod 1777 %{buildroot}%{_localstatedir}/lib/xemacs/lock
%endif
make install DESTDIR=%{buildroot}
mv %{buildroot}%{xbindir}/xemacs-21.?-??? %{buildroot}%{xbindir}/xemacs
# fix up the load-history to make it possible to use find-function
# on functions which are in dumped lisp files, even if XEmacs was not
# dumped at the place where it is finally running.
#
# Suggested by Jeff Mincy <jeff@delphioutpost.com>, see:
#
# http://list-archive.xemacs.org/xemacs-design/200204/msg00365.html
#
# Test whether this works by evaluating (find-function 'next-line)
#
install -m 644 %{_sourcedir}/fix-load-history.el \
               %{buildroot}%{_datadir}/xemacs/site-packages/lisp/
rm -rf %{buildroot}%{_datadir}/xemacs/%{version}/src/
rm -rf %{buildroot}%{_datadir}/xemacs/%{version}/lib-src/
rm -f  %{buildroot}%{_datadir}/xemacs/%{version}/Installation
######################################################################
test -L %{buildroot}%{xbindir}/xemacs && \
    rm  %{buildroot}%{xbindir}/xemacs
ver=%{version}
test -x %{buildroot}%{xbindir}/xemacs-${ver%%.*}-b${ver##*.} && \
    mv  %{buildroot}%{xbindir}/xemacs-${ver%%.*}-b${ver##*.} %{buildroot}%{xbindir}/xemacs
chmod 755 %{buildroot}%{xbindir}/xemacs
rm -f %{buildroot}%{xbindir}/xemacs-script
rm -rf %{buildroot}%{_datadir}/xemacs/%{version}/etc/tests
for f in %{buildroot}%{_prefix}/man/man1/*.1 \
         %{buildroot}%{_mandir}/man1/*.1 \
	 %{buildroot}%{_datadir}/xemacs/info/*info* \
	 %{buildroot}%{_datadir}/xemacs/%{version}/etc/*.1 \
	 %{buildroot}%{_datadir}/xemacs/%{version}/etc/mule/*.1
do
    test "${f##*.}" = "gz" && continue
    test -e $f || continue
    gzip -9nf $f
done
find %{buildroot}%{_datadir}/xemacs/%{version}/ -name '*.orig'     | xargs -r rm -f
find %{buildroot}%{_datadir}/xemacs/%{version}/ -name '*.el.ediff' | xargs -r rm -f
find %{buildroot}%{_datadir}/xemacs/%{version}/ -name '*.el.vm'    | xargs -r rm -f
# ctags and etags are part of the ctags package
# b2m and rcs-checkin are in the emacs package.
# As all binaries are in /usr/bin/ with X11R7, xemacs would conflict
# with emacs if xemacs packaged b2m and rcs-checkin as well.
# Therefore we remove them from the xemacs package here.
# They are rarely needed anyway.
rm -f %{buildroot}%{xbindir}/ctags \
      %{buildroot}%{xbindir}/etags \
      %{buildroot}%{xbindir}/b2m \
      %{buildroot}%{xbindir}/rcs-checkin \
      %{buildroot}%{_mandir}/man1/ctags.1.gz \
      %{buildroot}%{_mandir}/man1/etags.1.gz \
      %{buildroot}%{_datadir}/xemacs/%{version}/etc/ctags.1.gz \
      %{buildroot}%{_datadir}/xemacs/%{version}/etc/etags.1.gz
# Some .elc's are not needed:
find  %{buildroot}%{_datadir}/xemacs/ -name '_pkg.elc'   | xargs -r rm -f
find  %{buildroot}%{_datadir}/xemacs/ -name 'auto-autoloads.el?' | xargs -r rm -f
find  %{buildroot}%{_prefix}/lib/xemacs/   -name 'auto-autoloads.el?' | xargs -r rm -f
rm -f %{buildroot}%{_datadir}/xemacs/%{version}/lisp/default.elc
rm -f %{buildroot}%{_datadir}/xemacs/%{version}/lisp/vm/vm.elc
#if test -e /usr/share/xemacs/%{version}/lisp/xpm-button.el -a \
#	-e /usr/share/xemacs/%{version}/lisp/xemacs-base/xpm-button.el
#then
#      rm -f /usr/share/xemacs/%{version}/lisp/xpm-button.el
#      rm -f /usr/share/xemacs/%{version}/lisp/xpm-button.elc
#fi
# no .origs
rm -f %{buildroot}%{_datadir}/xemacs/info/xemacs-faq.info.orig*
#
# Make TUTORIAL's visible
for t in %{buildroot}%{_datadir}/xemacs/%{version}/etc/mule/TUTORIAL.* ; do
      test -e $t || break
      test -e %{buildroot}%{_datadir}/xemacs/%{version}/etc/${t##*/} && rm -f $t
      test -e $t && mv $t %{buildroot}%{_datadir}/xemacs/%{version}/etc/${t##*/}
done
# install the standard app-defaults file used for all languages
# which don't have their own app-defaults file above:
mkdir -p %{buildroot}%{appdefdir}/app-defaults/
install -m 644 etc/Emacs.ad %{buildroot}%{appdefdir}/app-defaults/XEmacs
# SuSE extension
install -m 0644 %{_sourcedir}/site-start.el %{buildroot}%{_datadir}/xemacs/site-packages/lisp/
install -m 0644 %{_sourcedir}/suse-xft-init.el %{buildroot}%{_datadir}/xemacs/site-packages/lisp/
install -m 0644 site-packages/lisp/term/func-keys.el %{buildroot}%{_datadir}/xemacs/site-packages/lisp/term/
install -m 0644 site-packages/lisp/term/linux.el %{buildroot}%{_datadir}/xemacs/site-packages/lisp/term/
install -m 0644 site-packages/lisp/term/xterm.el %{buildroot}%{_datadir}/xemacs/site-packages/lisp/term/
install -m 0644 site-packages/lisp/term/gnome.el %{buildroot}%{_datadir}/xemacs/site-packages/lisp/term/
install -m 0644 site-packages/lisp/term/kvt.el   %{buildroot}%{_datadir}/xemacs/site-packages/lisp/term/
./src/xemacs -batch -no-site-file -vanilla -f batch-byte-compile %{buildroot}%{_datadir}/xemacs/site-packages/lisp/term/*.el
mkdir -p %{buildroot}/%{_docdir}/xemacs
install -m 0644 suse/README.SUSE %{buildroot}/%{_docdir}/xemacs/README.SUSE
ln -sf  /usr/share/xemacs/%{version}/etc %{buildroot}/%{_docdir}/xemacs/etc
mkdir -p %{buildroot}%{_sysconfdir}/skel/.xemacs
install -m 0644 %{_sourcedir}/skel.init.el %{buildroot}%{_sysconfdir}/skel/.xemacs/init.el
%fdupes -s %{buildroot}%{_datadir}
#
# replace buildroot in comments in .elc files by spaces with the same total length:
REPLACEMENT=$(echo %{buildroot} | tr '[:print:]' ' ')
for i in $(find %{buildroot} -name "*.elc")
do
    perl -pi -e "s|(;;; from file )%{buildroot}(/usr/share/xemacs/.*)|\1$REPLACEMENT\2|" $i
done
#
# gzip .el files: (doesn't completely work for me yet -> later)
#for i in $(find %{buildroot} -name "*.el")
#do
#    gzip --best $i
#done
#
( find %{buildroot} \
       \( \( \( -not -type d \) -a \( -not -type l \) \) -printf '%%p\n' \) -o \
       \( -type d -printf '%%p/\n' \) -o \( -type l -printf '%%p\n'  \) ;  \
  find %{buildroot}%{_datadir}/xemacs/ %{buildroot}%{_prefix}/lib/xemacs/ -type f -o -type l )     |  \
       grep -v "/usr/share/xemacs/%{version}/etc" | \
       sort -t /| uniq | perl -p -e "s|%{buildroot}||" > xe-list
./src/xemacs -batch -no-site-file -l %{_sourcedir}/xe-list.el -f xe-list-generate-list-files
cat xe-list-el-without-elc xe-list-elc-without-el xe-list-elc-with-el \
    >> xe-list-el-without-elc_xe-list-elc-without-el_xe-list-elc-with-el
##
# install desktop file
%suse_update_desktop_file -i xemacs TextEditor Utility
##
# do no include header files because RPMLINT complains about header files in non-devel
# packages:
rm -rf %{buildroot}%{_prefix}/lib/xemacs/%{version}/*-suse-linux/include/

%if %{with lock}
%if %{defined verify_permissions}
%verifyscript
%verify_permissions -e /var/lib/xemacs/lock
%endif

%if %{defined set_permissions}

%post
%set_permissions /var/lib/xemacs/lock
%endif
%endif

%files -f xe-list-el-without-elc_xe-list-elc-without-el_xe-list-elc-with-el
%defattr(-,root,root)
%dir %{_sysconfdir}/skel/.xemacs
%config %{_sysconfdir}/skel/.xemacs/init.el
%{_datadir}/applications/xemacs.desktop
%{_datadir}/pixmaps/xemacs.png
%{xbindir}/ellcc
%{xbindir}/gnuattach
%{xbindir}/gnuclient
%{xbindir}/gnudoit
%{xbindir}/ootags
%verify(not mode) %{xbindir}/xemacs
%if %pdump_broken
%{xbindir}/xemacs*.dmp
%endif
%{appdefdir}/app-defaults/XEmacs
%dir %{_prefix}/lib/xemacs
%dir %{_prefix}/lib/xemacs/%{version}
%dir %{_prefix}/lib/xemacs/%{version}/*-suse-linux/
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/DOC
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/add-big-package.sh
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/config.values
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/cvtmail
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/digest-doc
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/fakemail
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/gnuserv
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/gzip-el.sh
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/hexl
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/make-docfile
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/mmencode
%dir %{_prefix}/lib/xemacs/%{version}/*-suse-linux/modules/
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/modules/*.ell
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/movemail
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/profile
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/rcs2log
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/sorted-doc
%{_prefix}/lib/xemacs/%{version}/*-suse-linux/vcdiff
%dir %{_prefix}/lib/xemacs/site-modules/
%dir %{_docdir}/xemacs/
%doc %{_docdir}/xemacs/README.SUSE
%{_docdir}/xemacs/etc
%doc %{_mandir}/man1/gnuattach.1.gz
%doc %{_mandir}/man1/gnuclient.1.gz
%doc %{_mandir}/man1/gnudoit.1.gz
%doc %{_mandir}/man1/gnuserv.1.gz
%doc %{_mandir}/man1/xemacs.1.gz
%dir %{_datadir}/xemacs/
%dir %{_datadir}/xemacs/%{version}/
%dir %{_datadir}/xemacs/%{version}/etc/
%{_datadir}/xemacs/%{version}/etc/*
%dir %{_datadir}/xemacs/%{version}/lisp/
%doc %{_datadir}/xemacs/%{version}/lisp/ChangeLog*
%doc %{_datadir}/xemacs/%{version}/lisp/README
%dir %{_datadir}/xemacs/%{version}/lisp/mule/
%doc %{_datadir}/xemacs/%{version}/lisp/mule/mule-locale.txt
%dir %{_datadir}/xemacs/%{version}/lisp/term
%doc %{_datadir}/xemacs/%{version}/lisp/term/README
%dir %{_datadir}/xemacs/site-packages/
%dir %{_datadir}/xemacs/site-packages/lisp/
%dir %{_datadir}/xemacs/site-packages/lisp/term/
%dir %{_datadir}/xemacs/site-lisp/
%dir %{_datadir}/xemacs/site-lisp/lisp/
%if %{with lock}
%dir %{_localstatedir}/lib/xemacs/
%dir %verify(not mode group) %attr(1775,root,trusted) /var/lib/xemacs/lock
%endif

%files       -n xemacs-info
%defattr(-,root,root)
%dir %{_datadir}/xemacs/
%dir %{_datadir}/xemacs/info/
%doc %{_datadir}/xemacs/info/*

%files       -n xemacs-el -f xe-list-el-with-elc
%defattr(-,root,root)
%dir %{_datadir}/xemacs/
%dir %{_datadir}/xemacs/%{version}/lisp/
%dir %{_datadir}/xemacs/%{version}/lisp/mule/
%dir %{_datadir}/xemacs/%{version}/lisp/term/
%dir %{_datadir}/xemacs/site-packages/
%dir %{_datadir}/xemacs/site-packages/lisp/
%dir %{_datadir}/xemacs/site-packages/lisp/term/

%changelog
