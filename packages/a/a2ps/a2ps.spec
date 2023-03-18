#
# spec file for package a2ps
#
# Copyright (c) 2023 SUSE LLC
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


Name:           a2ps
Version:        4.15
Release:        0
Summary:        Tool to convert ASCII/Latin Text into PostScript
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/a2ps/a2ps.html
Source0:        https://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        a2ps-ko.po
Source4:        a2ps-open
Source5:        a2ps-4.14-manuals.diff
Patch0:         a2ps-4.14.diff
Patch2:         a2ps-4.14-ogonkify.patch
Patch3:         a2ps-4.14-tempfile.patch
Patch6:         a2ps-4.13-include.patch
Patch8:         a2ps-4.13-base.patch
Patch9:         a2ps-4.13-utf8.patch
Patch10:        a2ps-4.13-types.patch
Patch13:        a2ps-4.14-linker.patch
Patch17:        a2ps-buildcompare.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  emacs-nox
BuildRequires:  flex
BuildRequires:  ghostscript-fonts-std
BuildRequires:  glibc-locale
BuildRequires:  gv
BuildRequires:  libpaper-devel
BuildRequires:  libtool
BuildRequires:  psutils
BuildRequires:  texlive-latex
BuildRequires:  timezone
BuildRequires:  pkgconfig(bdw-gc)
Requires:       file
Requires:       ghostscript-fonts-std
Requires:       glibc
Requires:       glibc-locale
Requires:       sed
Requires:       w3m
Requires:       wdiff
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
Suggests:       ImageMagick
Suggests:       acroread
Suggests:       gv
Suggests:       psutils
Suggests:       texinfo
Suggests:       texlive-latex
Provides:       a2ps-bin
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1220
BuildRequires:  gperf
BuildRequires:  groff
BuildRequires:  makeinfo
BuildRequires:  texi2html
BuildRequires:  texinfo
%endif

%description
a2ps converts ASCII text into PostScript. This feature is used by
apsfilter, for example, to pretty-print ASCII text.

Warning: a2ps is not able to convert complex Unicode (UTF-8) text to
PostScript.  Only language text which can be converted from UTF-8 to
Latin encodings are supported.

%package -n liba2ps1
Summary:        Library to convert ASCII/Latin text into PostScript

%description -n liba2ps1
The library liba2ps used by the program a2ps to convert ASCII text into PostScript.

%package     -n a2ps-devel
Summary:        Library and header file for the interface of a2ps
Requires:       glibc-devel
Requires:       liba2ps1 = %{version}

%description -n a2ps-devel
a2ps converts ASCII text into PostScript. This feature is used by
apsfilter, for example, to pretty-print ASCII text.

Warning: a2ps is not able to convert complex Unicode (UTF-8) text to
PostScript.  Only language text which can be converted from UTF-8 to
Latin encodings are supported.

%lang_package

%prep
%setup -q -n a2ps-4.15
touch -r configure.ac .ref
%patch2  -p1
%patch3  -p1
%patch6  -p1 -b .incld
%patch8   -b .base
%patch9   -b .utf8
%patch10  -b .types
%patch13 -p1 -b .p13
%patch17 -p1 -b .p17
%patch0   -b .p0
cp -f %{SOURCE3} po/ko.po
find -type f | grep -vE '(parseppd|parsessh).y' | xargs \
sed -ri 's/59 Temple Place(,| -) Suite 330/51 Franklin Street, Fifth Floor/;s/02111-1307/02110-1301/'
find -name Makefile.in | xargs touch

%build
 autoreconf -fiv -I $PWD -I $PWD/m4
 export PATH=$PWD:$PATH
 export CFLAGS="%{optflags} -D_GNU_SOURCE $(getconf LFS_CFLAGS) -funroll-loops -Wall -pipe -fstack-protector -fPIE"
 export LPR=lpr
 export CC=gcc
 export TZ=UTC
 export COM_psselect=yes
%configure --enable-shared --disable-static --with-medium=LC_PAPER \
	--with-encoding=LC_CTYPE

 for mf in $(find -name Makefile); do
   sed -ri -e '/^am--refresh: Makefile/,/\t@:/d' \
           -e '/^\$\(top_builddir\)\/config.status:/,/^\t/d' \
           -e '/^\$\(top_srcdir\)\/configure/,/^\t/d' \
           -e '/^\$\(ACLOCAL_M4\):/,/^\t/d' \
           -e '/^\t\s+\$\(SHELL\)\s\.\/config\.status;;\s\\/{s/\.\/config.status/-c true/}' $mf
 done

 make -C contrib/ LDFLAGS="-pie" AUTOMAKE=/bin/true
 # the build system is awful so we need to build with -B and avoid parallelism
 make PSFONT_PATH=%{_datadir}/ghostscript/fonts LDFLAGS="-pie" AUTOMAKE=/bin/true AUTOHEADER=/bin/true MAKEINFO='makeinfo --force' GPERF=/usr/bin/gperf -B all
 pushd doc
   texi2html a2ps.texi
 popd
 pushd contrib/emacs
   echo "(setq load-path (cons nil load-path))" > script
   for el in a2ps.el a2ps-print.el
   do
     emacs -batch -q -l script -f batch-byte-compile $el
   done
 popd
 pushd liba2ps
   gcc -shared .libs/*.o -Wl,-soname -Wl,liba2ps.so.1 -o .libs/liba2ps.so.1.0.0
   ln -s liba2ps.so.1.0.0 .libs/liba2ps.so.1
   ln -s liba2ps.so.1.0.0 .libs/liba2ps.so
   rm -vf liba2ps.a
   sed -ri -e "/dlname/{ s/(dlname=')(')/\1liba2ps.so.1\2/ }" \
           -e "/old_library=/{ s/liba2ps\.a/liba2ps.so/ }" \
           -e "/library_names/{ s/(library_names=')(')/\1liba2ps.so.1.0.0 liba2ps.so.1 liba2ps.so\2/ }" liba2ps.la
 popd
 pushd src
   rm a2ps
   make AUTOMAKE=/bin/true AUTOHEADER=/bin/true a2ps
 popd
 # Run a test with UTF-8 Umlauts
 mkdir -p .root/.a2ps
 echo "This is a test text äöüßœéïçèãøæđ" > test.utf8
 ln -sf $PWD/ps/*		.root/.a2ps/
 ln -sf $PWD/afm/*		.root/.a2ps/
 ln -sf $PWD/encoding/*		.root/.a2ps/
 ln -sf $PWD/ogonkify/*		.root/.a2ps/
 ln -sf $PWD/ppd/*		.root/.a2ps/
 ln -sf $PWD/sheets/*		.root/.a2ps/
 A2PS_CONFIG=$PWD%{_sysconfdir}/a2ps.cfg \
        HOME=$PWD/.root LD_LIBRARY_PATH=$PWD/liba2ps/.libs \
    LC_CTYPE=en_US.UTF-8 ./src/a2ps --output=test.latin test.utf8
 grep '(This is a test text' test.latin | iconv -f latin1 -t utf8
 chmod u+rw,g+r,o+r man/*.1
 cp -p man/a2ps.1 man/a2ps.1.backup
 patch --reject-format=unified --quoting-style=literal -f -p0 -F0 < %{S:5} || :
 if test -e man/a2ps.1.rej ; then
    cat man/a2ps.1.rej
    exit 1
 else
    sed -ri '/^\.B lt-a2ps/{s/lt-(a2ps)/\1/}' man/a2ps.1 || :
 fi

%install
 make -C contrib/ install DESTDIR=%{buildroot}
 %make_install PSFONT_PATH=%{_datadir}/ghostscript/fonts
 rm -r %{buildroot}/%{_infodir}/regex*
 rm -f %{buildroot}%{_libdir}/liba2ps.la
 install -m 0755 %{SOURCE4} %{buildroot}/%{_bindir}/
 pushd contrib/emacs
   for el in a2ps.el a2ps-print.el
   do
     install ${el}c %{buildroot}%{_datadir}/emacs/site-lisp/
   done
 popd
 pushd liba2ps
   mkdir -p %{buildroot}%{_libdir}
   mkdir -p %{buildroot}%{_includedir}
   install .libs/liba2ps.so.1.0.0 %{buildroot}%{_libdir}/
   ln -s liba2ps.so.1.0.0 %{buildroot}%{_libdir}/liba2ps.so.1
   ln -s liba2ps.so.1.0.0 %{buildroot}%{_libdir}/liba2ps.so
   install liba2ps.h %{buildroot}%{_includedir}
 popd
 for sc in card fixps lp2 pdiff
 do
   sed -ri '1 {s@/env +@/@}' %{buildroot}%{_bindir}/$sc
 done
%find_lang %{name} %{name}.lang
%find_lang %{name}-gnulib %{name}.lang

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ogonkify.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ogonkify.info.gz

%post   -n liba2ps1 -p /sbin/ldconfig
%postun -n liba2ps1 -p /sbin/ldconfig

%files
%doc AUTHORS ABOUT-NLS ChangeLog NEWS THANKS README doc/a2ps.html
%config %{_sysconfdir}/a2ps-site.cfg
%config %{_sysconfdir}/a2ps.cfg
%{_bindir}/a2ps
%{_bindir}/a2ps-open
%{_bindir}/a2ps-lpr-wrapper
%{_bindir}/card
%{_bindir}/composeglyphs
#{_bindir}/fixnt
%{_bindir}/fixps
%{_bindir}/ogonkify
%{_bindir}/pdiff
#{_bindir}/psmandup
%{_bindir}/lp2
#{_bindir}/psset
#{_bindir}/texi2dvi4a2ps
%{_infodir}/*.gz
%{_mandir}/man1/*.1.gz
%{_datadir}/a2ps
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/emacs/site-lisp/*.elc
%{_datadir}/ogonkify

%files lang -f %{name}.lang

%files -n liba2ps1
%{_libdir}/liba2ps.so.*

%files -n a2ps-devel
%{_includedir}/liba2ps.h
%{_libdir}/liba2ps.so

%changelog
