#
# spec file for package texinfo4
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           texinfo4
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  libbz2-devel
BuildRequires:  libzio-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-gettext
BuildRequires:  zlib-devel
Version:        4.13a
Release:        0
%global         version_t2h 1.82
%global         version_t2r 2.0
Summary:        Old version of texinfo 4, a toolset to create docs from texinfo sources
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Publishing/Texinfo
Url:            http://www.texinfo.org
PreReq:         %{install_info_prereq}
Provides:       texi2html4 = %{version_t2h}
Provides:       texi2roff4 = %{version_t2r}
#Conflicts:	texinfo
#Conflicts:	texi2html
#Conflicts:	texi2roff
%if %suse_version > 1220
Requires:       latex2html
Requires:       makeinfo4
Requires:       texlive-bibtex
Requires:       texlive-latex
Requires:       texlive-makeindex
Requires:       texlive-pdftex
Requires:       texlive-tex
Requires:       texlive-texinfo
%endif
Source0:        texinfo-%{version}.tar.bz2
Source1:        texi2html-%{version_t2h}.tar.bz2
# texinfo.org: the domain is expired.
# http://texinfo.org/texi2roff/texi2roff-%%{version_t2r}.tar.bz2
Source2:        texi2roff-%{version_t2r}.tar.bz2
Source10:       info-dir
Patch:          texinfo-4.12.dif
Patch1:         texi2html-1.78.dif
Patch2:         texi2roff-2.0.dif
Patch3:         texi2roff.patch.bz2
Patch4:         texinfo-4.12-zlib.patch
Patch5:         texinfo-4.8-echo.patch
Patch6:         texi2roff-2.0-gcc4.patch
Patch7:         texinfo-4.13a-bug640417.diff
Patch8:         texinfo-4.13a-bug713517.diff
Patch9:         automake-1.12.patch
Patch10:        texinfo-4.13a-bug788574.diff
Patch12:        texinfo4.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package is only for building lilypond documentation in the
build service. Please don't install
Aggregated with texinfo in this package is texi2html and texi2roff.

%package -n info4
Summary:        Old version of the "info" manual browser
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Texinfo
PreReq:         bash

%description -n info4
This package is only for building lilypond documentation in the
build service. Please don't install

%package -n makeinfo4
Summary:        Old version of the texinfo->info file converter
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Texinfo
Provides:       texinfo:/usr/bin/makeinfo
Suggests:       texinfo4

%description -n makeinfo4
This package is only for building lilypond documentation in the
build service. Please don't install

%prep
rm -rf texi2html-%{version_t2h} texi2roff-%{version_t2r}
%setup -q -b 1 -b 2 -n texinfo-4.13
%patch4 -p0 -b .zlib
%patch5 -p0 -b .echo
%patch7 -p1 -b .size_t
%patch8 -p0 -b .egrep
%patch9 -p1
%patch10 -p0 -b .appendix
%patch -p0
mkdir -p .backup
cp -v util/texi2pdf util/pdftexi2dvi .
%patch12
cp -v util/texi2pdf util/pdftexi2dvi .backup
cp -v texi2pdf pdftexi2dvi util/
pushd ../texi2html-%{version_t2h}
%patch1 -p0
popd
pushd ../texi2roff-%{version_t2r}
%patch3 -p0 -b .Bader
%patch2 -p0
%patch6 -p1
popd

%build
    HOST=%{_target_cpu}-suse-linux
    CFLAGS="%{optflags} -pipe"
    LDFLAGS=""
    CC=gcc
    export CFLAGS LDFLAGS CC
    export SUSE_ASNEEDED=0
    AUTOPOINT=true autoreconf -fi
    ./configure --build=$HOST		\
	--prefix=%{_prefix}		\
	--mandir=%{_mandir}		\
	--datadir=%{_datadir}		\
	--infodir=%{_infodir}		\
	--without-included-gettext	\
	--enable-nls			\
	--program-suffix=4

    PATH=${PWD}/makeinfo:${PWD}/util:$PATH
    export PATH
    make %{?_smp_mflags};
pushd ../texi2html-%{version_t2h}
    cp ../texinfo-4.13/build-aux/config.{guess,sub} .
    ./configure --build=$HOST		\
	--prefix=%{_prefix}		\
	--mandir=%{_mandir}		\
	--datadir=%{_datadir}		\
	--infodir=%{_infodir}		\
	--without-included-gettext	\
	--enable-nls			\
	--program-suffix=4
    make %{?_smp_mflags};
popd
pushd ../texi2roff-%{version_t2r}
    rm -f texi2roff
    make %{?_smp_mflags};
popd

%install
    export SUSE_ASNEEDED=0
    make DESTDIR=%{buildroot} \
	infodir=%{_infodir}	   \
	htmldir=%{_defaultdocdir}/texi2html4 install
    rm -f %{buildroot}%{_infodir}/info.info*
    mkdir -p %{buildroot}/sbin
    mv %{buildroot}%{_bindir}/install-info4 %{buildroot}/sbin/
    ln -sf ../../sbin/install-info4 %{buildroot}%{_bindir}/install-info4
    mkdir -p %{buildroot}%{_infodir}
    install -m 644 %{S:10}       %{buildroot}%{_infodir}/dir
pushd ../texi2html-%{version_t2h}
    make DESTDIR=%{buildroot} \
	infodir=%{_infodir}	   \
	texinfohtmldir=%{_defaultdocdir}/texi2html4 install
    install -m 644 README        %{buildroot}%{_defaultdocdir}/texi2html4/
    install -m 644 NEWS          %{buildroot}%{_defaultdocdir}/texi2html4/
    install -m 644 COPYING       %{buildroot}%{_defaultdocdir}/texi2html4/
popd
pushd ../texi2roff-%{version_t2r}
    doc=%{_defaultdocdir}/texi2roff4
    mv texi2roff texi2roff4
    mv texi2index texi2index4
    mv texi2roff.1 texi2roff4.1
    install -m 755 texi2roff4     %{buildroot}%{_bindir}/
    install -m 755 texi2index4    %{buildroot}%{_bindir}/
    install -m 644 texi2roff4.1   %{buildroot}%{_mandir}/man1/
    mkdir -p                     %{buildroot}${doc}
    install -m 644 Readme        %{buildroot}${doc}
    install -m 644 copyright     %{buildroot}${doc}
popd

install -v .backup/texi2pdf %{buildroot}%{_bindir}/texi2pdf4
install -v .backup/pdftexi2dvi %{buildroot}%{_bindir}/pdftexi2dvi4

rm -rf %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{_datadir}/info
mv %{buildroot}%{_datadir}/texi2html %{buildroot}%{_datadir}/texi2html4
mv %{buildroot}%{_datadir}/texinfo %{buildroot}%{_datadir}/texinfo4
%fdupes -s %{buildroot}%{_mandir}

%if 1 == 0
%post
%install_info --info-dir=%{_infodir} %{_infodir}/texinfo4.gz
%install_info --info-dir=%{_infodir} %{_infodir}/texi2html4.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/texinfo4.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/texi2html4.info.gz

%post -n info4
%install_info --info-dir=%{_infodir} %{_infodir}/info-stnd.info4.gz

%postun -n info4
%install_info_delete --info-dir=%{_infodir} %{_infodir}/info-stnd4.info.gz
%endif

%files
%defattr(-, root, root)
%dir %{_defaultdocdir}/texi2html4
%dir %{_defaultdocdir}/texi2roff4
%doc ABOUT-NLS AUTHORS COPYING INTRODUCTION NEWS README TODO
%doc doc/texinfo.tex doc/txi-*.tex
%doc %{_defaultdocdir}/texi2html4/*
%doc %{_defaultdocdir}/texi2roff4/*
%{_bindir}/pdftexi*
%{_bindir}/texi*
#%%{_infodir}/texinfo*.gz
#%%{_infodir}/texi2html*.gz
%{_mandir}/man1/pdftexi2dvi4.1.gz
%{_mandir}/man1/texi*.1.gz
%{_mandir}/man5/texinfo4.5.gz
%{_datadir}/texinfo4
%{_datadir}/texi2html4

%files -n makeinfo4
%defattr(-,root,root)
%{_bindir}/makeinfo4
%{_mandir}/man1/makeinfo4.1.gz

%files -n info4
%defattr(-,root,root)
#%%config(noreplace) %%verify(not md5 size mtime) %%{_infodir}/dir
/sbin/install-info4
%{_bindir}/install-info4
%{_bindir}/info4
%{_bindir}/infokey4
#%%{_infodir}/info-stnd.info*
%{_mandir}/man1/info4.1*
%{_mandir}/man1/infokey4.1*
%{_mandir}/man1/install-info4.1*
%{_mandir}/man5/info4.5*

%changelog
