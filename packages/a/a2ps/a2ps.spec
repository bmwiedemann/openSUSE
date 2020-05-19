#
# spec file for package a2ps
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


Name:           a2ps
Version:        4.14
Release:        0
Summary:        Tool to convert ASCII/Latin Text into PostScript
License:        GPL-3.0-or-later
Url:            http://www.gnu.org/software/a2ps/a2ps.html
Source0:        http://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        a2ps-ko.po
Source4:        a2ps-open
Source5:        a2ps-4.14-manuals.diff
Patch0:         a2ps-4.14.diff
Patch1:         a2ps-4.13-security.patch
Patch2:         a2ps-4.14-ogonkify.patch
Patch3:         a2ps-4.14-tempfile.patch
Patch4:         a2ps-4.14-automake.patch
Patch6:         a2ps-4.13-include.patch
Patch7:         a2ps-4.14-acroread.patch
Patch8:         a2ps-4.13-base.patch
Patch9:         a2ps-4.13-utf8.patch
Patch10:        a2ps-4.13-types.patch
Patch11:        a2ps-4.13-psgen.patch
Patch12:        a2ps-4.14-iswprint.patch
Patch13:        a2ps-4.14-linker.patch
# PATCH-FIX-USTREAM Bug 871097 - CVE-2014-0466: a2ps: fixps does not use -dSAFER
Patch14:        CVE-2014-0466.diff
Patch15:        a2ps-4.14-gperf.patch
# PATCH-FIX-SUSE Bug 955194 - CVE-2015-8107: CVE-2015-8107 - a2ps(gnu) v4.14 format string vulnerability
Patch16:        a2ps-4.14-bnc955194.patch
Patch17:        a2ps-buildcompare.patch
Patch18:        reproducible.patch
# PATCH-FIX-SUSE New texinfo 6.7 does not like KOI8-R endcoded characters within UTF-8 environment
Patch19:        a2ps-4.14-texinfo-6.7.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  emacs-nox
BuildRequires:  flex
BuildRequires:  ghostscript-fonts-std
BuildRequires:  gv
BuildRequires:  psutils
BuildRequires:  texlive-latex
BuildRequires:  timezone
Requires:       file
Requires:       ghostscript-fonts-std
Requires:       glibc
Requires:       sed
Requires:       w3m
Requires:       wdiff
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
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
liba2ps converts ASCII text into PostScript.

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

%prep
%setup -q -n a2ps-4.14
touch -r configure.in .ref
%patch1   -b .security
%patch2  -p1
%patch3  -p1
%patch4   -b .norefresh
%patch6  -p1 -b .incld
%ifarch %ix86 x86_64
%patch7 -p1
%endif
%patch8   -b .base
%patch9   -b .utf8
%patch10  -b .types
%patch11  -b .psgen
%patch12  -b .iswprint
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p0
%patch17 -p1
%patch0   -b .p0
%patch18 -p1
%patch19 -p0 -b .p19
cp -f %{SOURCE3} po/ko.po
find -type f | grep -vE '(parseppd|parsessh).y' | xargs \
sed -ri 's/59 Temple Place(,| -) Suite 330/51 Franklin Street, Fifth Floor/;s/02111-1307/02110-1301/'
touch -r .ref configure.in
find -name Makefile.in | xargs touch

%build
 #XXX: ugly hack; necessary??
 #YYY: Not a hack and it is necessary!!
 #     The a2ps source is much to old to (re)run auto conf tools
 cp -p %{_datadir}/automake-*/config.{guess,sub} auxdir/
 cp -p /bin/true auxdir/missing
 export AUTOMAKE=/bin/true
 export ACLOCAL=/bin/true
 export AUTOCONF=/bin/true
 export AUTOHEADER=/bin/true
 export PATH=$PWD:$PATH
 export CFLAGS="%{optflags} -D_GNU_SOURCE $(getconf LFS_CFLAGS) -funroll-loops -Wall -pipe -fstack-protector -fPIE"
 export LPR=lpr
 export CC=gcc
 export TZ=UTC
%configure --enable-shared --disable-static --with-medium=LC_PAPER \
	--with-encoding=LC_CTYPE
 con=""
 pushd contrib
   for m4 in *.m4; do
     in=${m4%.*}.in
     rm -f ${in} ${m4%.*}
     con="$con ${in##*/}"
   done
 popd
 make -C contrib/ ${con} LDFLAGS="-pie"
 sh ./config.status
 # the build system is awful so we need to build with -B and avoid parallelism
 make PSFONT_PATH=%{_datadir}/ghostscript/fonts LDFLAGS="-pie" MAKEINFO='makeinfo --force' -B
 pushd doc
   texi2html a2ps.texi
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
        HOME=$PWD/.root \
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
 %make_install PSFONT_PATH=%{_datadir}/ghostscript/fonts
 rm -r %{buildroot}/%{_infodir}/regex*
 %find_lang %{name}
 rm -f %{buildroot}%{_libdir}/liba2ps.la
 install -m 0755 %{SOURCE4} %{buildroot}/%{_bindir}/

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ogonkify.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ogonkify.info.gz

%post   -n liba2ps1 -p /sbin/ldconfig
%postun -n liba2ps1 -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS COPYING ABOUT-NLS ChangeLog NEWS THANKS README doc/a2ps.html
%config %{_sysconfdir}/a2ps-site.cfg
%config %{_sysconfdir}/a2ps.cfg
%{_bindir}/a2ps
%{_bindir}/a2ps-open
%{_bindir}/card
%{_bindir}/composeglyphs
%{_bindir}/fixnt
%{_bindir}/fixps
%{_bindir}/ogonkify
%{_bindir}/pdiff
%{_bindir}/psmandup
%{_bindir}/psset
%{_bindir}/texi2dvi4a2ps
%{_infodir}/*.gz
%{_mandir}/man1/*.1.gz
%{_datadir}/a2ps
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/emacs/site-lisp/*.elc
%{_datadir}/ogonkify

%files -n liba2ps1
%{_libdir}/liba2ps.so.*

%files -n a2ps-devel
%{_includedir}/liba2ps.h
%{_libdir}/liba2ps.so

%changelog
