#
# spec file for package emacs
#
# Copyright (c) 2022 SUSE LLC
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
%bcond_without  nativecomp
%else
%bcond_with     mailutils
%bcond_with     nativecomp
%endif
%bcond_without  cairo
%bcond_with     tex4pdf
%bcond_with     memmmap

Name:           emacs
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
BuildRequires:  gettext-devel
BuildRequires:  giflib-devel
BuildRequires:  git
BuildRequires:  glibc-locale
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
BuildRequires:  libxml2-devel
BuildRequires:  m17n-lib-devel
BuildRequires:  pkgconfig(libudev)
%if %{with mailutils}
BuildRequires:  mailutils
BuildRequires:  mailutils-devel
%endif
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  user(games)
%endif
BuildRequires:  systemd-rpm-macros
%if %{with tex4pdf}
BuildRequires:  texlive-collection-basic
BuildRequires:  texlive-collection-langcyrillic
BuildRequires:  texlive-collection-langczechslovak
BuildRequires:  texlive-collection-langpolish
BuildRequires:  texlive-lh
%endif
BuildRequires:  procps
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
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(valgrind)
%if %{with tex4pdf}
BuildRequires:  tex(babel.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(german.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(ifpdf.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(multicol.sty)
BuildRequires:  tex(supertabular.sty)
BuildRequires:  tex(t2aenc.def)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(verbatim.sty)
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libacl)
%else
BuildRequires:  libacl-devel
%endif
%if %{with nativecomp}
BuildRequires:  libgccjit-devel
%endif
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(lcms2)
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
URL:            http://www.gnu.org/software/emacs/
Version:        28.2
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
Source:         https://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.xz
Source1:        app-defaults.Emacs
Source2:        site-lisp.tar.bz2
Source3:        dot.gnu-emacs
Source4:        emacs-rpmlintrc
Source5:        emacs.sh
Source6:        https://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.xz.sig
# https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source7:        %{name}.keyring
Source8:        emacs-%{version}-pdf.tar.xz
Patch:          emacs-28.1.dif
# Currently disabled
Patch2:         emacs-24.4-glibc.patch
Patch4:         emacs-24.3-asian-print.patch
Patch5:         emacs-24.4-ps-bdf.patch
Patch7:         emacs-24.1-ps-mule.patch
Patch8:         emacs-24.4-nonvoid.patch
Patch12:        emacs-24.3-x11r7.patch
Patch15:        emacs-24.3-iconic.patch
Patch16:        emacs-24.4-flyspell.patch
Patch22:        pdump.patch
Patch23:        emacs-25.1-custom-fonts.patch
# this patch works with both ImageMagick-6 and ImageMagick-7 for us,
# but that is because we ship /usr/include/ImageMagick-7/wand compat
# symlink
Patch24:        emacs-25.2-ImageMagick7.patch
Patch25:        emacs-26.1-xft4x11.patch
Patch26:        emacs-27.1-pdftex.patch
Patch29:        emacs-27.1-Xauthority4server.patch
Patch30:        d48bb487.patch

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
%if %{undefined ext_el}
%define ext_el      .gz
%endif
%define info_files emacs eintr elisp auth autotype bovine calc ccmode cl dbus dired-x ebrowse ede ediff edt eieio emacs-mime epa erc ert eshell eudc efaq eww flymake forms gnus emacs-gnutls htmlfontify idlwave ido info.info mairix-el message mh-e modus-themes newsticker nxml-mode octave-mode org pcl-cvs pgg rcirc remember reftex sasl sc semantic ses sieve smtpmail speedbar srecode todo-mode transient tramp url vhdl-mode vip viper widget wisent woman

%description
Basic package for the GNU Emacs editor.  For a documentation see https://www.emacsdocs.org/.
This package requires emacs-x11 and/or emacs-nox to have the GNU Emacs editor its self.

%package     -n emacs-nox
Requires(post): fileutils
Requires:       emacs = %{version}-%{release}
%if %{with nativecomp}
Requires:       emacs-eln = %{version}
%endif
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
%if %{with nativecomp}
Requires:       emacs-eln = %{version}
%endif
Provides:       emacs_program = %{version}-%{release}
Requires:       gnu-unifont-bitmap-fonts
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

%if %{with nativecomp}
%package     -n emacs-eln
# Without the el.gz files a starting emacs with support of native compiled
# lisp code will show an error
# >> Symbol's value as variable is void: auto-save-list-file-prefix <<
# and exceeds the limit for open files as it opens warnings.elc several
# times up to the set open file limit
Requires:       emacs-el = %{version}
Summary:        GNU Emacs-nox: Emacs Lisp native compiled binary files
Group:          Productivity/Text/Editors

%define _libeln %{_prefix}/lib

%description -n emacs-eln
Emacs Lisp (Elisp) is the Lisp dialect used by the Emacs text editor
family. GNU Emacs can currently execute Elisp code either interpreted
or byte-interpreted after it has been compiled to byte-code.
The native compiler employs the byte-compiler's internal representation
as input and exploits libgccjit to achieve code generation using the GNU
Compiler Collection (GCC) infrastructure. Generated executables are stored
as binary files and can be loaded and unloaded dynamically.
%endif

%package     -n emacs-el
Requires:       emacs = %{version}-%{release}
Provides:       emacs-devel = %{version}-%{release}
Summary:        Several Lisp Files for GNU Emacs
Group:          Development/Libraries/Other
BuildArch:      noarch

%description -n emacs-el
Several Lisp files not needed for running GNU Emacs. Most of these
files are pre-byte compiled and therefore not necessary.

%package     -n emacs-info
Summary:        Info files for GNU Emacs
Group:          Documentation/Other
%if 0%{?suse_version} <= 1500
Requires(post): %install_info_prereq
Requires(preun):%install_info_prereq
%endif
BuildArch:      noarch

%description -n emacs-info
This package contains all the Info files for GNU Emacs. These files can
be read online with GNU Emacs. They describe Emacs and some of its
modes.

%package     -n etags
Summary:        Generate Tag Files for Use with Emacs
Group:          Development/Tools/Navigators
Requires(post): coreutils update-alternatives
Requires(preun):coreutils update-alternatives
Provides:       ctags:/usr/bin/etags

%description -n etags
ETags generates tag files from source code in Pascal, Cobol, Ada, Perl,
LaTeX, Scheme, Emacs Lisp/Common Lisp, Postscript, Erlang, Python, Prolog,
and most assembler-like syntaxes.

%prep
%setup -q -b 2
%if %{with memmmap}
%patch2  -p0 -b .glibc
%endif
%patch4  -p0 -b .print
%patch5  -p0 -b .psbdf
%patch7  -p0 -b .psmu
%patch8  -p0 -b .nvoid
%patch12 -p0 -b .x11r7
%patch15 -p0 -b .iconic
%patch16 -p0 -b .flyspell
%patch22 -p0 -b .pd
%patch23 -p0 -b .custfnt
%patch24 -p1 -b .imag
%patch25 -p0 -b .xft
%patch26 -p0 -b .fmt
%patch29 -p0 -b .xauth
%patch30 -p0 -b .cve202245939
%patch   -p0 -b .0
%if %{without tex4pdf}
pushd etc/refcards/
    tar --use-compress-program=xz -xf %{S:8}
popd
%endif

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
  cflags -pipe                   CFLAGS
  cflags -Wno-pointer-sign       CFLAGS
  cflags -Wno-unused-variable    CFLAGS
  cflags -Wno-unused-label       CFLAGS
  cflags -fno-optimize-sibling-calls CFLAGS
  cflags -Wl,-O2		 LDFLAGS
%ifarch ia64
 CFLAGS=$(echo "${CFLAGS}"|sed -r 's/-O[0-9]?/-O1/g')
%endif
   LANG=POSIX; LC_CTYPE=en_US.UTF-8
export CC CFLAGS LANG LC_CTYPE LDFLAGS
 PREFIX="--prefix=%{_prefix} \
	 --mandir=%{_mandir} \
	 --infodir=%{_infodir} \
	 --datadir=%{_datadir} \
	 --localstatedir=%{_localstatedir} \
	 --sharedstatedir=%{_localstatedir}/lib \
	 --libexecdir=%{_libexecdir} \
	 --with-file-notification=yes \
%if %{with nativecomp}
	 --with-native-compilation \
%endif
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
	 --without-harfbuzz \
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

# new giflib5 does not have this function and it is unused anyway...
ac_cv_lib_gif_EGifPutExtensionLast=yes
export ac_cv_lib_gif_EGifPutExtensionLast

CFLAGS="$CFLAGS -DPDMP_BASE='\"emacs-nox\"'" ./configure ${COMP} ${PREFIX} ${NOX11} ${SYS} --with-dumping=pdumper
%make_build V=1
make -C lisp/ updates compile V=1
for i in $(find site-lisp/ -name '*.el'); do
    EMACSLOADPATH='' src/emacs -batch -q --no-site -f batch-byte-compile $i
done
cp src/emacs emacs-nox
cp src/emacs.pdmp emacs-nox.pdmp
find -name '*.eln'
make distclean
#
CFLAGS="$CFLAGS -DPDMP_BASE='\"emacs-gtk\"'" ./configure ${COMP} ${PREFIX} ${GTK} ${SYS} --with-dumping=pdumper
%make_build
cp src/emacs emacs-gtk
cp src/emacs.pdmp emacs-gtk.pdmp
find -name '*.eln'
make distclean
#
CFLAGS="$CFLAGS -DPDMP_BASE='\"emacs-x11\"'" ./configure ${COMP} ${PREFIX} ${X11} ${SYS} --with-dumping=pdumper
%make_build
cp src/emacs emacs-x11
cp src/emacs.pdmp emacs-x11.pdmp
find -name '*.eln'

%if %{with tex4pdf}
#
make -C etc/refcards/
%endif

#
pushd ../site-lisp/
EMACSLOADPATH='' ../emacs-%{version}/src/emacs -batch -q --no-site -f batch-byte-compile *.el
rm -vf site-start.elc
rm -vf site-start.el.orig
popd

%install
#
PATH=/sbin:$PATH
##
VERSION=%{version}
eval $(sed -rn "/^configuration=/p" config.log)
sed -ri 's@/usr/lib/X11/fonts@/usr/share/fonts@g;s@(/usr/)local/(info|share|lib)@\1\2@;s@\$VERSION@%{version}@g;s@\$ARCH@'${configuration}'@g' doc/man/emacs.1
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}/emacs/%{version}/${configuration}
install -m 0755 emacs-nox %{buildroot}%{_bindir}
install -m 0755 emacs-gtk %{buildroot}%{_bindir}
install -m 0755 emacs-x11 %{buildroot}%{_bindir}
install -m 0644 emacs-nox.pdmp %{buildroot}%{_libexecdir}/emacs/%{version}/${configuration}/
install -m 0644 emacs-gtk.pdmp %{buildroot}%{_libexecdir}/emacs/%{version}/${configuration}/
install -m 0644 emacs-x11.pdmp %{buildroot}%{_libexecdir}/emacs/%{version}/${configuration}/
make install DESTDIR=%{buildroot} systemdunitdir=%{_userunitdir}
rm -vf %{buildroot}/usr/bin/emacs
rm -vf %{buildroot}%{_libexecdir}/emacs/%{version}/${configuration}/emacs.pdmp
install -p %{S:5} %{buildroot}/usr/bin/emacs
chmod 0755        %{buildroot}/usr/bin/emacs
tar cf - `find site-lisp/ -name '*.el'  -o -name '*.elc'` | \
tar -x -f - -C %{buildroot}%{_datadir}/emacs/%{version}/
mkdir -p %{buildroot}%{_docdir}/emacs
ln -sf %{_datadir}/emacs/%{version}/etc %{buildroot}%{_docdir}/emacs/doc
find %{buildroot}%{_datadir}/emacs/%{version}/ -name '*,v' -o -name '*.orig' | xargs -r rm -f
#for f in %{buildroot}%{_infodir}/* ; do
#    case "$f" in
#	*.gz)			;;
#	*/dir)	rm -f ${f}	;;
#	*)	test -e  ${f}.gz && rm ${f}.gz
#		gzip -9f ${f}
#    esac
#done
rm -vf %{buildroot}%{_infodir}/dir
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
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/etc/refcards/*.fmt
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/etc/emacs.service.xauth
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
rm -vf %{buildroot}%{_datadir}/emacs/%{version}/lisp/server.el.xauth
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
cp etc/images/icons/hicolor/32x32/apps/emacs.png $RPM_SOURCE_DIR/emacs.png
for df in %{buildroot}%{_datadir}/emacs/%{version}/etc/emacs*.desktop
do
    test -e "$df" || break
    base=${df##*/}
    mv etc/${base} etc/${base}.orig
    cp $df etc/${base}
    echo 'X-KDE-StartupNotify=false' >> etc/${base}
    rm -vf $df
    %suse_update_desktop_file -r -i ${base%%.desktop} TextEditor Utility
done
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/ctags		%{buildroot}%{_bindir}/ctags
ln -sf %{_sysconfdir}/alternatives/ctags.1%{ext_man}	%{buildroot}%{_mandir}/man1/ctags.1%{ext_man}
ln -sf %{_bindir}/gnuctags				%{buildroot}%{_sysconfdir}/alternatives/ctags
ln -sf %{_mandir}/man1/gnuctags.1%{ext_man}		%{buildroot}%{_sysconfdir}/alternatives/ctags.1%{ext_man}

%if %{with nativecomp}
touch eln.list
for eln in %{buildroot}%{_libeln}/emacs/%{version}/native-lisp/%{version}-*/*.eln
do
   if test -e $eln
   then
	echo '%%{_libeln}/emacs/%%{version}/native-lisp/%%{version}-*/*.eln' >> eln.list
   fi
   break
done
for eln in %{buildroot}%{_libeln}/emacs/%{version}/native-lisp/%{version}-*/preloaded/*.eln
do
   if test -e $eln
   then
	echo '%%{_libeln}/emacs/%%{version}/native-lisp/%%{version}-*/preloaded/*.eln' >> eln.list
   fi
   break
done
%endif

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

%if 0%{?suse_version} <= 1500
%post info
for f in %info_files; do
  test "$f" = "info.info" && continue
  test -e "$f" || f="${f}.info"
  %install_info --info-dir=%{_infodir} "%{_infodir}/$f.%{%ext_info}"
done

%preun info
for f in %info_files; do
  test "$f" = "info.info" && continue
  test -e "$f" || f="${f}.info"
  %install_info_delete --info-dir=%{_infodir} "%{_infodir}/$f.%{%ext_info}"
done
%endif

%post -n etags
test -L %{_bindir}/ctags || rm -f %{_bindir}/ctags
%{_sbindir}/update-alternatives --quiet --force --install \
	  %{_bindir}/ctags			ctags	%{_bindir}/gnuctags 10 \
  --slave %{_mandir}/man1/ctags.1%{ext_man}	ctags.1	%{_mandir}/man1/gnuctags.1%{ext_man}
%{_sbindir}/update-alternatives --auto ctags

%postun -n etags
if test ! -f %{_bindir}/gnuctags ; then
    %{_sbindir}/update-alternatives --quiet --remove ctags %{_bindir}/gnuctags
fi

%files -f site-lisp.lst -n emacs
%defattr(-, root, root)
%config /etc/skel/.gnu-emacs
%{_bindir}/ebrowse
%{_bindir}/emacs
%{_bindir}/emacsclient
%dir %{_libexecdir}/emacs/
%dir %{_libexecdir}/emacs/%{version}/
%dir %{_libexecdir}/emacs/%{version}/*-suse-linux*/
%{_libexecdir}/emacs/%{version}/*-suse-linux*/hexl
%if %{without mailutils}
%{_libexecdir}/emacs/%{version}/*-suse-linux*/movemail
%endif
%{_libexecdir}/emacs/%{version}/*-suse-linux*/rcs2log
%if 0
%attr(04755,games,games) %{_libexecdir}/emacs/%{version}/*-suse-linux*/update-game-score
%else
%{_libexecdir}/emacs/%{version}/*-suse-linux*/update-game-score
%endif
%{_userunitdir}/emacs.service
%dir %{_datadir}/doc/packages/emacs/
%{_datadir}/doc/packages/emacs/doc
%dir %{_datadir}/emacs/
%dir %{_datadir}/emacs/%{version}/
%dir %{_datadir}/emacs/%{version}/etc/
%doc %{_datadir}/emacs/%{version}/etc/AUTHORS
%doc %{_datadir}/emacs/%{version}/etc/CALC-NEWS
%doc %{_datadir}/emacs/%{version}/etc/COPYING
%doc %{_datadir}/emacs/%{version}/etc/DEBUG
%doc %{_datadir}/emacs/%{version}/etc/DEVEL.HUMOR
%doc %{_datadir}/emacs/%{version}/etc/DISTRIB
%{_datadir}/emacs/%{version}/etc/DOC
%doc %{_datadir}/emacs/%{version}/etc/ERC-NEWS
%doc %{_datadir}/emacs/%{version}/etc/HELLO
%doc %{_datadir}/emacs/%{version}/etc/HISTORY
%doc %{_datadir}/emacs/%{version}/etc/JOKES
%doc %{_datadir}/emacs/%{version}/etc/MACHINES
%doc %{_datadir}/emacs/%{version}/etc/MH-E-NEWS
%{_datadir}/emacs/%{version}/etc/NEWS
%doc %{_datadir}/emacs/%{version}/etc/NEWS.*
%doc %{_datadir}/emacs/%{version}/etc/NEXTSTEP
%doc %{_datadir}/emacs/%{version}/etc/NXML-NEWS
%doc %{_datadir}/emacs/%{version}/etc/ORG-NEWS
%doc %{_datadir}/emacs/%{version}/etc/PROBLEMS
%doc %{_datadir}/emacs/%{version}/etc/README
%doc %{_datadir}/emacs/%{version}/etc/TERMS
%doc %{_datadir}/emacs/%{version}/etc/TODO
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
%dir %{_datadir}/emacs/%{version}/etc/org/
%dir %{_datadir}/emacs/%{version}/etc/org/csl/
%{_datadir}/emacs/%{version}/etc/org/csl/README
%{_datadir}/emacs/%{version}/etc/org/csl/chicago-author-date.csl
%{_datadir}/emacs/%{version}/etc/org/csl/locales-en-US.xml
%dir %{_datadir}/emacs/%{version}/etc/e/
%doc %{_datadir}/emacs/%{version}/etc/e/README
%{_datadir}/emacs/%{version}/etc/e/eterm-color
%{_datadir}/emacs/%{version}/etc/e/eterm-color.ti
%{_datadir}/emacs/%{version}/etc/edt-user.el
%{_datadir}/emacs/%{version}/etc/emacs-buffer.gdb
%{_datadir}/emacs/%{version}/etc/emacs.icon
%{_datadir}/emacs/%{version}/etc/emacs.metainfo.xml
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
%{_datadir}/emacs/%{version}/etc/images/checkbox-mixed.svg
%{_datadir}/emacs/%{version}/etc/images/checked.svg
%{_datadir}/emacs/%{version}/etc/images/down.svg
%{_datadir}/emacs/%{version}/etc/images/left.svg
%{_datadir}/emacs/%{version}/etc/images/radio-checked.svg
%{_datadir}/emacs/%{version}/etc/images/radio-mixed.svg
%{_datadir}/emacs/%{version}/etc/images/radio.svg
%{_datadir}/emacs/%{version}/etc/images/right.svg
%{_datadir}/emacs/%{version}/etc/images/unchecked.svg
%{_datadir}/emacs/%{version}/etc/images/up.svg
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
%{_datadir}/emacs/%{version}/etc/images/icons/hicolor/scalable/apps/emacs.ico
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
%{_datadir}/emacs/%{version}/etc/images/splash.bmp
%{_datadir}/emacs/%{version}/etc/images/splash.pbm
%{_datadir}/emacs/%{version}/etc/images/splash.png
%{_datadir}/emacs/%{version}/etc/images/splash.svg
%{_datadir}/emacs/%{version}/etc/images/splash.xpm
%dir %{_datadir}/emacs/%{version}/etc/images/tabs/
%doc %{_datadir}/emacs/%{version}/etc/images/tabs/README
%{_datadir}/emacs/%{version}/etc/images/tabs/close.xpm
%{_datadir}/emacs/%{version}/etc/images/tabs/left-arrow.xpm
%{_datadir}/emacs/%{version}/etc/images/tabs/new.xpm
%{_datadir}/emacs/%{version}/etc/images/tabs/right-arrow.xpm
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
%{_datadir}/emacs/%{version}/etc/schema/OpenDocument-schema-v1.3+libreoffice.rnc
%{_datadir}/emacs/%{version}/etc/schema/OpenDocument-schema-v1.3.rnc
%{_datadir}/emacs/%{version}/etc/schema/calstbl.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbcalstbl.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbhier.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbnotn.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbpool.rnc
%{_datadir}/emacs/%{version}/etc/schema/dbstart.rnc
%{_datadir}/emacs/%{version}/etc/schema/docbook.rnc
%{_datadir}/emacs/%{version}/etc/schema/locate.rnc
%{_datadir}/emacs/%{version}/etc/schema/od-manifest-schema-v1.2-os.rnc
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
%{_datadir}/emacs/%{version}/etc/srecode/proj-test.srt
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
%{_datadir}/emacs/%{version}/etc/themes/modus-operandi-theme.el
%{_datadir}/emacs/%{version}/etc/themes/modus-themes.el
%{_datadir}/emacs/%{version}/etc/themes/modus-vivendi-theme.el
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
%{_datadir}/emacs/%{version}/etc/w32-feature.el
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
%{_datadir}/emacs/%{version}/lisp/calendar/iso8601.elc
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
%{_datadir}/emacs/%{version}/lisp/cedet/mode-local.elc
%{_datadir}/emacs/%{version}/lisp/cedet/pulse.elc
%dir %{_datadir}/emacs/%{version}/lisp/cedet/semantic/
%{_datadir}/emacs/%{version}/lisp/cedet/semantic.elc
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
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grm-wy-boot.elc
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
%{_datadir}/emacs/%{version}/lisp/display-fill-column-indicator.elc
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
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/backtrace.elc
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
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/comp-cstr.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/comp.elc
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
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/faceup.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/find-func.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/float-sup.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generator.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generic.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/gv.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/helper.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/hierarchy.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/inline.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/let-alist.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mnt.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mode.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/macroexp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map-ynp.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/memory-report.elc
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
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/shortdoc.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/shorthands.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/smie.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/subr-x.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/syntax.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tabulated-list.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tcover-ses.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/testcover.elc
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/text-property-search.elc
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
%{_datadir}/emacs/%{version}/lisp/epa-ks.elc
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
%{_datadir}/emacs/%{version}/lisp/erc/erc-loaddefs.el
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
%{_datadir}/emacs/%{version}/lisp/erc/erc-status-sidebar.elc
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
%{_datadir}/emacs/%{version}/lisp/fileloop.elc
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
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dbus.elc
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
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-search.elc
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
%{_datadir}/emacs/%{version}/lisp/gnus/nnselect.elc
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
%{_datadir}/emacs/%{version}/lisp/image/exif.elc
%{_datadir}/emacs/%{version}/lisp/image/gravatar.elc
%{_datadir}/emacs/%{version}/lisp/image/image-converter.elc
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
%{_datadir}/emacs/%{version}/lisp/international/emoji-zwj.elc
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
%{_datadir}/emacs/%{version}/lisp/jsonrpc.elc
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
%{_datadir}/emacs/%{version}/lisp/language/pinyin.elc
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
%{_datadir}/emacs/%{version}/lisp/leim/quail/cham.elc
%{_datadir}/emacs/%{version}/lisp/leim/quail/compose.elc
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
%{_datadir}/emacs/%{version}/lisp/leim/quail/sami.elc
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
%{_datadir}/emacs/%{version}/lisp/mail/mspools.elc
%{_datadir}/emacs/%{version}/lisp/mail/qp.elc
%{_datadir}/emacs/%{version}/lisp/mail/reporter.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc2045.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc2047.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc2231.elc
%{_datadir}/emacs/%{version}/lisp/mail/rfc6068.elc
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
%{_datadir}/emacs/%{version}/lisp/net/dictionary-connection.elc
%{_datadir}/emacs/%{version}/lisp/net/dictionary.elc
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
%{_datadir}/emacs/%{version}/lisp/net/eudcb-macos-contacts.elc
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
%{_datadir}/emacs/%{version}/lisp/net/sasl-scram-sha256.elc
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
%{_datadir}/emacs/%{version}/lisp/net/telnet.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-archive.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-adb.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-cache.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-cmds.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-compat.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-crypt.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-ftp.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-fuse.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-gvfs.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-integration.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/net/tramp-sh.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-smb.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-sshfs.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-sudoedit.elc
%{_datadir}/emacs/%{version}/lisp/net/tramp-rclone.elc
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
%{_datadir}/emacs/%{version}/lisp/obsolete/cl.elc
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
%{_datadir}/emacs/%{version}/lisp/obsolete/info-edit.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/inversion.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/iswitchb.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/landmark.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/lazy-lock.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/longlines.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/mantemp.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/mailpost.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/meese.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/messcompat.el
%{_datadir}/emacs/%{version}/lisp/obsolete/metamail.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/mouse-sel.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/nnir.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/old-emacs-lock.elc
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
%{_datadir}/emacs/%{version}/lisp/obsolete/rfc2368.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/s-region.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/sb-image.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/sregex.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/starttls.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/sup-mouse.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/terminal.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/tls.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-edt.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-extras.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-mapper.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/url-ns.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/vc-arch.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/vi.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/vip.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/ws-mode.elc
%{_datadir}/emacs/%{version}/lisp/obsolete/yow.elc
%dir %{_datadir}/emacs/%{version}/lisp/org/
%{_datadir}/emacs/%{version}/lisp/org/ob-C.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-R.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-awk.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-calc.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-clojure.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-comint.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-core.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-css.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ditaa.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-dot.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-emacs-lisp.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-eshell.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-eval.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-exp.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-forth.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-fortran.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-gnuplot.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-groovy.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-haskell.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-java.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-julia.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-js.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-latex.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lilypond.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lisp.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lob.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-lua.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-makefile.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-matlab.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-maxima.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ocaml.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-octave.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-org.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-perl.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-plantuml.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-processing.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-python.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ref.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-ruby.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sass.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-scheme.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-screen.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sed.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-shell.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sql.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-sqlite.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-table.elc
%{_datadir}/emacs/%{version}/lisp/org/ob-tangle.elc
%{_datadir}/emacs/%{version}/lisp/org/ob.elc
%{_datadir}/emacs/%{version}/lisp/org/oc-basic.elc
%{_datadir}/emacs/%{version}/lisp/org/oc-biblatex.elc
%{_datadir}/emacs/%{version}/lisp/org/oc-csl.elc
%{_datadir}/emacs/%{version}/lisp/org/oc-natbib.elc
%{_datadir}/emacs/%{version}/lisp/org/oc.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-bbdb.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-bibtex.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-docview.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-doi.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-eshell.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-eww.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-gnus.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-info.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-irc.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-mhe.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-man.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-rmail.elc
%{_datadir}/emacs/%{version}/lisp/org/ol-w3m.elc
%{_datadir}/emacs/%{version}/lisp/org/ol.elc
%{_datadir}/emacs/%{version}/lisp/org/org-agenda.elc
%{_datadir}/emacs/%{version}/lisp/org/org-archive.elc
%{_datadir}/emacs/%{version}/lisp/org/org-attach.elc
%{_datadir}/emacs/%{version}/lisp/org/org-attach-git.elc
%{_datadir}/emacs/%{version}/lisp/org/org-capture.elc
%{_datadir}/emacs/%{version}/lisp/org/org-clock.elc
%{_datadir}/emacs/%{version}/lisp/org/org-colview.elc
%{_datadir}/emacs/%{version}/lisp/org/org-compat.elc
%{_datadir}/emacs/%{version}/lisp/org/org-crypt.elc
%{_datadir}/emacs/%{version}/lisp/org/org-ctags.elc
%{_datadir}/emacs/%{version}/lisp/org/org-datetree.elc
%{_datadir}/emacs/%{version}/lisp/org/org-duration.elc
%{_datadir}/emacs/%{version}/lisp/org/org-element.elc
%{_datadir}/emacs/%{version}/lisp/org/org-entities.elc
%{_datadir}/emacs/%{version}/lisp/org/org-faces.elc
%{_datadir}/emacs/%{version}/lisp/org/org-feed.elc
%{_datadir}/emacs/%{version}/lisp/org/org-footnote.elc
%{_datadir}/emacs/%{version}/lisp/org/org-goto.elc
%{_datadir}/emacs/%{version}/lisp/org/org-habit.elc
%{_datadir}/emacs/%{version}/lisp/org/org-id.elc
%{_datadir}/emacs/%{version}/lisp/org/org-indent.elc
%{_datadir}/emacs/%{version}/lisp/org/org-inlinetask.elc
%{_datadir}/emacs/%{version}/lisp/org/org-install.el
%{_datadir}/emacs/%{version}/lisp/org/org-keys.elc
%{_datadir}/emacs/%{version}/lisp/org/org-lint.elc
%{_datadir}/emacs/%{version}/lisp/org/org-list.elc
%{_datadir}/emacs/%{version}/lisp/org/org-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/org/org-macro.elc
%{_datadir}/emacs/%{version}/lisp/org/org-macs.elc
%{_datadir}/emacs/%{version}/lisp/org/org-mobile.elc
%{_datadir}/emacs/%{version}/lisp/org/org-mouse.elc
%{_datadir}/emacs/%{version}/lisp/org/org-num.elc
%{_datadir}/emacs/%{version}/lisp/org/org-pcomplete.elc
%{_datadir}/emacs/%{version}/lisp/org/org-plot.elc
%{_datadir}/emacs/%{version}/lisp/org/org-protocol.elc
%{_datadir}/emacs/%{version}/lisp/org/org-refile.elc
%{_datadir}/emacs/%{version}/lisp/org/org-src.elc
%{_datadir}/emacs/%{version}/lisp/org/org-table.elc
%{_datadir}/emacs/%{version}/lisp/org/org-tempo.elc
%{_datadir}/emacs/%{version}/lisp/org/org-timer.elc
%{_datadir}/emacs/%{version}/lisp/org/org-version.el
%{_datadir}/emacs/%{version}/lisp/org/org.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-ascii.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-beamer.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-html.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-icalendar.elc
%{_datadir}/emacs/%{version}/lisp/org/ox-koma-letter.elc
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
%{_datadir}/emacs/%{version}/lisp/progmodes/cl-font-lock.elc
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
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake-cc.elc
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
%{_datadir}/emacs/%{version}/lisp/so-long.elc
%{_datadir}/emacs/%{version}/lisp/sort.elc
%{_datadir}/emacs/%{version}/lisp/soundex.elc
%{_datadir}/emacs/%{version}/lisp/speedbar.elc
%{_datadir}/emacs/%{version}/lisp/startup.elc
%{_datadir}/emacs/%{version}/lisp/strokes.elc
%{_datadir}/emacs/%{version}/lisp/subdirs.el
%{_datadir}/emacs/%{version}/lisp/subr.elc
%{_datadir}/emacs/%{version}/lisp/svg.elc
%{_datadir}/emacs/%{version}/lisp/t-mouse.elc
%{_datadir}/emacs/%{version}/lisp/tab-bar.elc
%{_datadir}/emacs/%{version}/lisp/tab-line.elc
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
%{_datadir}/emacs/%{version}/lisp/term/fbterm.elc
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
%{_datadir}/emacs/%{version}/lisp/term/st.elc
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
%{_datadir}/emacs/%{version}/lisp/textmodes/etc-authors-mode.elc
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
%{_datadir}/emacs/%{version}/lisp/textmodes/texinfo-loaddefs.el
%{_datadir}/emacs/%{version}/lisp/textmodes/texnfo-upd.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/text-mode.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/tildify.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/two-column.elc
%{_datadir}/emacs/%{version}/lisp/textmodes/underline.elc
%{_datadir}/emacs/%{version}/lisp/thingatpt.elc
%{_datadir}/emacs/%{version}/lisp/thread.elc
%{_datadir}/emacs/%{version}/lisp/thumbs.elc
%{_datadir}/emacs/%{version}/lisp/time-stamp.elc
%{_datadir}/emacs/%{version}/lisp/time.elc
%{_datadir}/emacs/%{version}/lisp/timezone.elc
%{_datadir}/emacs/%{version}/lisp/tmm.elc
%{_datadir}/emacs/%{version}/lisp/tool-bar.elc
%{_datadir}/emacs/%{version}/lisp/tooltip.elc
%{_datadir}/emacs/%{version}/lisp/transient.elc
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
%dir %attr(775,games,games) %{_localstatedir}/games/emacs
%attr(660,games,games) %{_localstatedir}/games/emacs/snake-scores
%attr(660,games,games) %{_localstatedir}/games/emacs/tetris-scores

%files       -n emacs-nox
%defattr(-, root, root)
%{_bindir}/emacs-nox
%{_libexecdir}/emacs/%{version}/*-suse-linux*/emacs-nox.pdmp

%files       -n emacs-x11
%defattr(-, root, root)
%{_bindir}/emacs-x11
%{_bindir}/emacs-gtk
%{_libexecdir}/emacs/%{version}/*-suse-linux*/emacs-x11.pdmp
%{_libexecdir}/emacs/%{version}/*-suse-linux*/emacs-gtk.pdmp
%dir %{appDefaultsDir}
%{appDefaultsFile}
%{_datadir}/applications/emacs*.desktop
%{_datadir}/icons/hicolor/128x128/apps/emacs.png
%{_datadir}/icons/hicolor/16x16/apps/emacs.png
%{_datadir}/icons/hicolor/24x24/apps/emacs.png
%{_datadir}/icons/hicolor/32x32/apps/emacs.png
%{_datadir}/icons/hicolor/48x48/apps/emacs.png
%{_datadir}/icons/hicolor/scalable/apps/emacs.ico
%{_datadir}/icons/hicolor/scalable/apps/emacs.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document23.svg
%if 0%{?suse_version} <= 1315
%dir %{_datadir}/metainfo/
%endif
%{_datadir}/metainfo/emacs.metainfo.xml
%{_datadir}/pixmaps/emacs.png

%if %{with nativecomp}
%files       -n emacs-eln -f eln.list
%defattr(-, root, root)
%dir %{_libeln}/emacs/
%dir %{_libeln}/emacs/%{version}/
%dir %{_libeln}/emacs/%{version}/native-lisp/
%dir %{_libeln}/emacs/%{version}/native-lisp/%{version}-*/
%dir %{_libeln}/emacs/%{version}/native-lisp/%{version}-*/preloaded/
%endif

%files       -n emacs-info
%defattr(-, root, root)
%doc %{_infodir}/*%{ext_info}
%if 0%{?include_info} == 0
%exclude %{_infodir}/info.info%{ext_info}
%endif

%files       -n emacs-el
%defattr(-, root, root)
%{_x11inc}/emacs-module.h
%{_datadir}/emacs/%{version}/lisp/abbrev.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/align.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/allout-widgets.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/allout.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ansi-color.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/apropos.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/arc-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/array.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/auth-source-pass.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/auth-source.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/autoarg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/autoinsert.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/autorevert.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/avoid.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/battery.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/bookmark.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/bs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/buff-menu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/button.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-aent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-alg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-arith.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-bin.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-comb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-cplx.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-embed.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-ext.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-fin.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-forms.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-frac.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-funcs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-graph.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-help.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-incom.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-keypd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-lang.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-macs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-map.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-math.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-menu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-misc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-mtx.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-nlfit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-poly.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-prog.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-rewr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-rules.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-sel.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-stat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-store.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-stuff.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-trail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-undo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-units.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-vec.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc-yank.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calcalg2.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calcalg3.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calccomp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calc/calcsel2.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calculator.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/appt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-bahai.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-china.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-coptic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-dst.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-french.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-hebrew.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-html.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-islam.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-iso.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-julian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-mayan.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-menu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-move.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-persia.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-tex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/cal-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/calendar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/diary-lib.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/holidays.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/icalendar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/iso8601.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/lunar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/parse-time.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/solar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/time-date.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/timeclock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/calendar/todo-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/case-table.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cdl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-cscope.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-files.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-global.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/cedet-idutils.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/cedet.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/data-debug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/auto.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/autoconf-edit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/base.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/config.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/cpp-root.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/custom.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/detect.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/dired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/emacs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/files.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/generic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/linux.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/locate.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/make.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/makefile-edit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/pconf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/pmake.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-archive.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-aux.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-comp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-elisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-info.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-misc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-obj.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-prog.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-scheme.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj-shared.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/proj.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/project-am.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/shell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/simple.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/source.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/speedbar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/srecode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/system.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/ede/util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/mode-local.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/pulse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/complete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/debug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/fcn.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/analyze/refs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/c-by.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/c.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/debug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/el.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/gcc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/grammar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/make-by.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/make.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/scm-by.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/bovine/scm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/chart.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/complete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ctxt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-debug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-ebrowse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-el.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-file.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-find.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-global.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-javascript.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-ref.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db-typecache.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/db.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/debug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate/include.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/decorate/mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/dep.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/doc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ede-grammar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/edit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/find.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/format.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/fw.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grammar-wy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grammar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/grm-wy-boot.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/html.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ia-sb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/ia.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/idle.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/imenu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/java.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/lex-spp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/lex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/mru-bookmark.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/sb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/scope.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/senator.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/sort.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/cscope.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/filter.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/global.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/grep.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/idutils.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/symref/list.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-file.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-ls.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag-write.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/tag.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/texi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/util-modes.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/comp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/grammar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/java-tags.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/javascript.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/javat-wy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/js-wy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/python-wy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/python.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/semantic/wisent/wisent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/args.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/compile.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/cpp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/ctxt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/dictionary.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/document.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/el.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/expandproto.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/extract.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/fields.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/filters.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/find.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/getset.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/insert.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/java.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/map.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/semantic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt-wy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/srt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/table.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/template.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cedet/srecode/texi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/char-fold.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/chistory.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cmuscheme.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/color.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/comint.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/completion.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/composite.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cus-dep.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cus-edit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cus-face.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/cus-theme.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/custom.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dabbrev.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/delim-col.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/delsel.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/descr-text.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/desktop.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dframe.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dired-aux.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dired-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dirtrack.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/disp-table.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/display-fill-column-indicator.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/display-line-numbers.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dnd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/doc-view.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dom.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dos-fns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dos-vars.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dos-w32.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/double.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/dynamic-setting.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ebuff-menu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/echistory.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ecomplete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/edmacro.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ehelp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/elec-pair.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/electric.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/elide-head.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/advice.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/autoload.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/avl-tree.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/backtrace.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/backquote.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/benchmark.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/bindat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/byte-opt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/byte-run.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/bytecomp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cconv.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/chart.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/check-declare.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/checkdoc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/comp-cstr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/comp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-extra.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-generic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-indent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-lib.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-macs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-preloaded.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-print.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cl-seq.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/copyright.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/crm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/cursor-sensor.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/debug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/derived.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/disass.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/easy-mmode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/easymenu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/edebug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-base.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-compat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-core.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-custom.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-datadebug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-opt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio-speedbar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eieio.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/eldoc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/elint.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/elp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ert-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ert.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ewoc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/faceup.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/find-func.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/float-sup.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generator.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/generic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/gv.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/helper.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/hierarchy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/inline.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/let-alist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mnt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/lisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/macroexp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map-ynp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/map.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/memory-report.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/nadvice.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/package-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/package.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/pcase.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/pp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/re-builder.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/regexp-opt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/regi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/ring.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/rx.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/seq.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/shadow.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/shortdoc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/shorthands.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/smie.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/subr-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/syntax.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/radix-tree.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/rmc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tabulated-list.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tcover-ses.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/testcover.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/text-property-search.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/thunk.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/timer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/timer-list.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/tq.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/trace.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/unsafep.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lisp/warnings.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emacs-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/cua-base.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/cua-gmrk.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/cua-rect.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/edt-lk201.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/edt-mapper.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/edt-pc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/edt-vt100.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/edt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/keypad.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper-cmd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper-ex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper-init.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper-keym.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper-macs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper-mous.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/emulation/viper.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/env.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epa-dired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epa-file.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epa-hook.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epa-ks.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epa-mail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epa.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epg-config.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/epg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-autoaway.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-backend.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-button.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-capab.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-compat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-dcc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-desktop-notifications.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-ezbounce.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-fill.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-goodies.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-ibuffer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-identd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-imenu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-join.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-lang.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-list.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-log.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-match.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-menu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-netsplit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-networks.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-notify.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-page.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-pcomplete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-replace.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-ring.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-services.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-sound.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-speedbar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-spelling.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-stamp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-status-sidebar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-track.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-truncate.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc-xdcc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/erc/erc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-alias.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-banner.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-basic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-cmpl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-dirs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-glob.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-hist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-ls.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-pred.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-prompt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-rebind.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-script.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-smart.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-term.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-tramp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-unix.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/em-xtra.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-arg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-cmd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-ext.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-io.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-module.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-opt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-proc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/esh-var.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/eshell/eshell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/expand.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ezimage.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/face-remap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/facemenu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/faces.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ffap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/filecache.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/fileloop.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/filenotify.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/files-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/files.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/filesets.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/find-cmd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/find-dired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/find-file.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/find-lisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/finder.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/flow-ctrl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/foldout.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/follow.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/font-core.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/font-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/format-spec.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/format.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/forms.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/frame.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/frameset.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/fringe.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/canlock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/deuglify.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gmm-utils.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-agent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-art.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-async.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-bcklg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-bookmark.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cache.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cite.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cloud.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-cus.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dbus.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-delay.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-demon.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-diary.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-draft.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-dup.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-eform.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-fun.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-gravatar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-group.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-html.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-icalendar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-int.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-kill.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-logic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-mh.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-ml.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-mlspl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-msg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-notifications.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-picon.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-range.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-registry.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-rfc1843.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-salt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-score.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-search.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-sieve.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-spec.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-srvr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-start.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-sum.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-topic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-undo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-uu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-vm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus-win.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gnus.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/gssapi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/legacy-gnus-agent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mail-source.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/message.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-archive.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-bodies.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-decode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-encode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-extern.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-partial.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-url.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-uu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mm-view.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mml-sec.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mml-smime.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mml.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mml1991.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/mml2015.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnagent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnbabyl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nndiary.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nndir.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nndoc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nndraft.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nneething.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnfolder.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nngateway.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnheader.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnimap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnmail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnmaildir.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnmairix.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnmbox.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnmh.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnml.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnnil.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnoo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnregistry.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnrss.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnselect.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnspool.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nntp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnvirtual.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/nnweb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/score-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/smiley.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/smime.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/spam-report.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/spam-stat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/spam-wash.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/gnus/spam.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/help-at-pt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/help-fns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/help-macro.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/help-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/help.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/hex-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/hexl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/hfy-cmap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/hi-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/hilit-chg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/hippie-exp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/hl-line.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/htmlfontify.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ibuf-ext.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ibuf-macs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ibuffer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/icomplete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ido.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ielm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/iimage.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image-dired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image-file.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image/compface.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image/exif.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image/gravatar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/image/image-converter.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/imenu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/indent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/info-look.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/info-xref.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/info.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/informat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/ccl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/characters.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/charscript.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/cp51932.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/emoji-zwj.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/eucjp-ms.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/fontset.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/isearch-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/iso-ascii.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/iso-cvt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/iso-transl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/ja-dic-cnv.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/ja-dic-utl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/kinsoku.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/kkc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/latexenc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/latin1-disp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/mule-cmds.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/mule-conf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/mule-diag.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/mule-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/mule.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/ogonek.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/quail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/rfc1843.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/robin.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/titdic-cnv.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/ucs-normalize.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/utf-7.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/international/utf7.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/isearch.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/isearchb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/jit-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/jka-cmpr-hook.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/jka-compr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/json.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/jsonrpc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/kermit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/kmacro.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/burmese.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/cham.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/china-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/chinese.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/cyril-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/cyrillic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/czech.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/english.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/ethio-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/ethiopic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/european.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/georgian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/greek.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/hanja-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/hebrew.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/ind-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/indian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/japan-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/japanese.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/khmer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/korea-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/korean.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/lao-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/lao.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/misc-lang.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/pinyin.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/romanian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/sinhala.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/slovak.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/tai-viet.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/thai-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/thai-word.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/thai.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/tibet-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/tibetan.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/tv-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/utf-8-lang.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/viet-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/language/vietnamese.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/ja-dic/ja-dic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/4Corner.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ARRAY30.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/CCDOSPY.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/CTLau-b5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/CTLau.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ECDICT.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ETZY.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/PY-b5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/PY.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/Punct-b5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/Punct.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/QJ-b5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/QJ.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/SW.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/TONEPY.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ZIRANMA.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ZOZY.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/arabic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/cham.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/compose.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/croatian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/cyril-jis.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/cyrillic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/czech.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ethiopic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/georgian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/greek.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/hangul.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja-jis.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/hanja3.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/hebrew.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/indian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ipa-praat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/ipa.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/japanese.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/lao.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-alt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-ltx.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-post.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/latin-pre.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/lrt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/persian.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/programmer-dvorak.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/py-punct.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/pypunct-b5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/quick-b5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/quick-cns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/rfc1345.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/sami.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/sgml-input.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/sisheng.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/slovak.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/symbol-ksc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/tamil-dvorak.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/thai.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/tibetan.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/tsang-b5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/tsang-cns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/uni-input.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/viqr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/vntelex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/vnvni.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/leim/quail/welsh.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/linum.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/loadhist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/locate.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/lpr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ls-lisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/macros.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/binhex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/emacsbug.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/feedmail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/flow-fill.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/footnote.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/hashcash.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/ietf-drums.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mail-extr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mail-hist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mail-parse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mail-prsvr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mail-utils.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mailabbrev.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mailalias.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mailclient.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mailheader.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/mspools.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/qp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/reporter.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rfc2045.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rfc2047.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rfc2231.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rfc6068.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rfc822.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmail-spam-filter.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmailedit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmailkwd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmailmm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmailmsc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmailout.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmailsort.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/rmailsum.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/sendmail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/smtpmail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/supercite.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/uce.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/undigest.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/unrmail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/uudecode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mail/yenc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/makesum.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/man.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/master.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mb-depth.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/md4.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/menu-bar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-alias.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-buffers.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-comp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-compat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-e.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-folder.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-funcs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-gnus.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-identity.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-inc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-junk.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-letter.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-limit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-mime.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-print.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-scan.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-search.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-seq.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-show.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-speed.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-thread.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-tool-bar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-utils.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mh-e/mh-xface.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/midnight.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/minibuf-eldef.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/minibuffer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/misc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/misearch.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mouse-copy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mouse-drag.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mouse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mpc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/msb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/mwheel.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/ange-ftp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/browse-url.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/dbus.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/dictionary-connection.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/dictionary.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/dig.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/dns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudc-bob.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudc-export.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudc-hotlist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudc-vars.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudcb-bbdb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudcb-ldap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudcb-mab.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eudcb-macos-contacts.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/eww.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/gnutls.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/goto-addr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/hmac-def.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/hmac-md5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/imap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/ldap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/mailcap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/mairix.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/net-utils.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/netrc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/network-stream.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/newst-backend.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/newst-plainview.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/newst-reader.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/newst-ticker.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/newst-treeview.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/newsticker.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/nsm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/ntlm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/pop3.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/quickurl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/puny.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/rcirc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/rfc2104.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/rlogin.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sasl-cram.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sasl-digest.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sasl-ntlm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sasl-scram-rfc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sasl-scram-sha256.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sasl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/secrets.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sieve-manage.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sieve-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/sieve.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/shr-color.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/shr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/snmp-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/soap-client.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/soap-inspect.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/socks.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/telnet.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-archive.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-adb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-cache.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-cmds.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-compat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-crypt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-ftp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-fuse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-gvfs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-integration.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-rclone.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-sh.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-smb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-sshfs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-sudoedit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp-uu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/tramp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/trampver.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/webjump.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/net/zeroconf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/newcomment.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/notifications.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/novice.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-enc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-maint.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-ns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-outln.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-parse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-rap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/nxml-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-cmpct.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-dt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-loc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-maint.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-match.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-nxml.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-parse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-pttrn.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-uri.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-valid.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/rng-xsd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/xmltok.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/nxml/xsd-regexp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obarray.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/abbrevlist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/assoc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/bruce.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/cl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/cc-compat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/cl-compat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/complete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/crisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/cust-print.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/erc-hecomplete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/eudcb-ph.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/fast-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/gulp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/gs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/iswitchb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/html2text.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/info-edit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/inversion.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/landmark.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/lazy-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/longlines.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/mailpost.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/mantemp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/metamail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/meese.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/mouse-sel.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/nnir.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/old-emacs-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/otodo-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/patcomp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pc-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pc-select.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-def.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-gpg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-parse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-pgp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg-pgp5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/pgg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/rcompile.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/rfc2368.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/s-region.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/sb-image.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/sregex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/starttls.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/sup-mouse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/terminal.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/tls.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-edt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-extras.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/tpu-mapper.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/url-ns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/vc-arch.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/vi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/vip.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/ws-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/obsolete/yow.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-C.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-R.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-awk.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-calc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-clojure.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-comint.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-core.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-css.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-ditaa.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-dot.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-emacs-lisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-eshell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-eval.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-exp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-forth.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-fortran.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-gnuplot.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-groovy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-haskell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-java.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-julia.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-js.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-latex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-lilypond.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-lisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-lob.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-lua.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-makefile.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-matlab.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-maxima.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-ocaml.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-octave.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-org.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-perl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-plantuml.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-processing.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-python.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-ref.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-ruby.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-sass.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-scheme.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-screen.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-sed.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-shell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-sql.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-sqlite.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-table.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob-tangle.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ob.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/oc-basic.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/oc-biblatex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/oc-csl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/oc-natbib.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/oc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-bbdb.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-bibtex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-docview.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-doi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-eshell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-eww.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-gnus.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-info.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-irc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-man.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-mhe.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-rmail.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol-w3m.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ol.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-agenda.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-archive.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-attach.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-attach-git.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-capture.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-clock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-colview.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-compat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-crypt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-ctags.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-datetree.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-duration.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-element.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-entities.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-faces.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-feed.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-footnote.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-goto.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-habit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-id.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-indent.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-inlinetask.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-keys.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-lint.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-list.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-macro.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-macs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-mobile.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-mouse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-num.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-pcomplete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-plot.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-protocol.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-refile.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-src.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-table.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-tempo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org-timer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/org.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-ascii.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-beamer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-html.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-icalendar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-koma-letter.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-latex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-man.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-md.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-odt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-org.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-publish.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox-texinfo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/org/ox.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/outline.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/paren.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/password-cache.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pcmpl-cvs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pcmpl-gnu.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pcmpl-linux.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pcmpl-rpm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pcmpl-unix.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pcmpl-x.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pcomplete.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/pixel-scroll.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/5x5.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/animate.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/blackbox.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/bubbles.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/cookie1.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/decipher.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/dissociate.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/doctor.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/dunnet.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/fortune.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/gamegrid.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/gametree.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/gomoku.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/handwrite.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/hanoi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/life.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/morse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/mpuz.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/pong.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/snake.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/solitaire.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/spook.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/studly.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/tetris.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/play/zone.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/plstore.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/printing.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/proced.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/profiler.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/antlr-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/asm-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/autoconf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/bat-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/bug-reference.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-align.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-awk.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-bytecomp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-cmds.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-defs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-engine.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-fonts.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-guess.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-langs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-menus.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-styles.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cc-vars.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cfengine.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cl-font-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cmacexp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/compile.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cperl-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cpp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/cwarn.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/dcl-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-abn.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-bnf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-dtd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-ebx.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-iso.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-otz.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf-yac.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebnf2ps.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ebrowse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/elisp-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/etags.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/executable.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/f90.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake-cc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/flymake-proc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/fortran.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/gdb-mi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/glasses.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/grep.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/gud.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/hideif.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/hideshow.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/icon.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-complete-structtag.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-help.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-shell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/idlw-toolbar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/idlwave.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/inf-lisp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/js.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ld-script.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/m4-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/make-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/meta-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/mixal-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/modula2.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/octave.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/opascal.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/pascal.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/perl-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/prog-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/project.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/prolog.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ps-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/python.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/ruby-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/scheme.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/sh-script.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/simula.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/sql.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/subword.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/tcl.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/vera-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/verilog-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/vhdl-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/which-func.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/xref.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/progmodes/xscheme.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ps-bdf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ps-def.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ps-mule.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ps-print.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ps-samp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/recentf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/rect.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/register.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/registry.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/repeat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/replace.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/reposition.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/reveal.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/rfn-eshadow.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/rot13.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ruler-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/rtree.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/savehist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/saveplace.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/scroll-all.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/scroll-bar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/scroll-lock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/select.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/server.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/ses.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/shadowfile.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/shell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/simple.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/so-long.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/sort.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/soundex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/speedbar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/startup.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/strokes.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/subr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/svg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/t-mouse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tab-bar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tab-line.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tabify.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/talk.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tar-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tempo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/AT386.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/bobcat.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/common-win.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/cygwin.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/fbterm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/internal.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/iris-ansi.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/konsole.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/linux.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/lk201.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/news.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/ns-win.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/pc-win.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/rxvt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/screen.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/st.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/sun.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/tmux.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/tty-colors.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/tvi970.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/vt100.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/vt200.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/w32-win.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/w32console.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/wyse50.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/term/x-win.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/artist.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/bib-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/bibtex-style.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/bibtex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/conf-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/css-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/dns-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/etc-authors-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/enriched.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/fill.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/flyspell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/ispell.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/less-css-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/makeinfo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/mhtml-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/nroff-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/page-ext.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/page.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/paragraphs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/picture.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/po.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/refbib.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/refer.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/refill.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-auc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-cite.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-dcr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-global.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-index.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-parse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-ref.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-sel.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-toc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex-vars.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/reftex.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/remember.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/rst.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/sgml-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/table.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/tex-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/texinfmt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/texinfo.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/texnfo-upd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/text-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/tildify.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/two-column.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/textmodes/underline.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/thingatpt.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/thread.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/thumbs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/time-stamp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/time.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/timezone.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tmm.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tool-bar.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tooltip.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/transient.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tree-widget.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/tutorial.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/type-break.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/uniquify.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-about.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-auth.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-cache.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-cid.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-cookie.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-dav.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-dired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-domsuf.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-expand.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-file.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-ftp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-future.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-gw.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-handlers.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-history.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-http.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-imap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-irc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-ldap.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-mailto.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-methods.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-misc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-news.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-nfs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-parse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-privacy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-proxy.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-queue.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-tramp.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url-vars.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/url/url.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/userlock.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/add-log.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/compare-w.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/cvs-status.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/diff-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/diff.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-diff.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-help.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-hook.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-init.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-merg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-mult.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-ptch.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-vers.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff-wind.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/ediff.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/emerge.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/log-edit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/log-view.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-defs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-info.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-parse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/pcvs-util.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/pcvs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/smerge-mode.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-annotate.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-bzr.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-cvs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-dav.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-dir.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-dispatcher.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-filewise.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-git.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-hg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-hooks.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-mtn.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-rcs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-sccs.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-src.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc-svn.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vc/vc.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vcursor.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/version.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/view.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vt-control.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/vt100-led.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/w32-fns.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/w32-vars.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/wdired.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/whitespace.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/wid-browse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/wid-edit.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/widget.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/windmove.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/window.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/winner.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/woman.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/x-dnd.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/xdg.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/xml.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/xt-mouse.el%{ext_el}
%{_datadir}/emacs/%{version}/lisp/xwidget.el%{ext_el}

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
