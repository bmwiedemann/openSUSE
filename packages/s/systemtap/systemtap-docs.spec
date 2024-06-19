#
# spec file for package systemtap-docs
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


Name:           systemtap-docs
Version:        5.1
Release:        0
Summary:        Documents and examples for systemtap
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://sourceware.org/systemtap/
Source0:        https://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz
Source1:        https://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz.asc
Source2:        systemtap.keyring
Source3:        README-BEFORE-ADDING-PATCHES
Source4:        README-KEYRING
Patch1:         systemtap-docdir-fix.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(json-c)
# for documents
BuildRequires:  fop
BuildRequires:  gcc-c++
BuildRequires:  latex2html
BuildRequires:  libdw-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-metafont-bin
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  tex(charter.sty)
BuildRequires:  tex(fancybox.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(float.sty)
BuildRequires:  tex(fullpage.sty)
BuildArch:      noarch

%description
SystemTap is an instrumentation system for systems running Linux.
This package contains the documents and examples for systemtap.

%prep
%setup -q -n systemtap-%{version}
%autopatch -p1

%build
# fix interpreter
find testsuite examples -name "*.stp" | xargs -n1 sed -i -e 's, /bin/env, %{_bindir}/env,'
find testsuite examples -type f | xargs chmod 644
autoreconf -fi
%configure --docdir=%{_docdir}/systemtap --disable-nls --with-python3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} doc
# COPYING packaged by main spec
cp README AUTHORS NEWS %{buildroot}%{_docdir}/systemtap/
# remove binaries and runtime stuff
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_sbindir}
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_libexecdir}
rm -rf %{buildroot}%{_datadir}/systemtap
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_sysconfdir}
rm -rf %{buildroot}%{_unitdir}
# these man pages are in each sub package
rm -rf %{buildroot}%{_mandir}/man[178]
rm -rf %{buildroot}%{_mandir}/cs/man[178]

%files
%defattr(-,root,root)
%doc %{_docdir}/systemtap
%{_mandir}/man3/*
%{_mandir}/cs/man3/*

%changelog
