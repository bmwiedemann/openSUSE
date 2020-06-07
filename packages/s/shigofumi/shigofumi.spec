#
# spec file for package shigofumi
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           shigofumi
Version:        0.8
Release:        0
Summary:        Command line client for accessing the Czech Data Boxes
License:        GPL-3.0+
Group:          Applications/Internet
Url:            http://xpisar.wz.cz/%{name}/
Source0:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz
Patch0:         shigofumi.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  file-devel
BuildRequires:  pkg-config
BuildRequires:  po4a
BuildRequires:  readline-devel
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libisds) >= 0.10
BuildRequires:  pkgconfig(libxml-2.0)

%description
This is Shigofumi, an ISDS (Informační systém datových schránek / Data Box
Information System) client.

%prep
%autosetup -p1

%build
%configure \
    --disable-fatalwarnings
%make_build

%install
%make_install
%find_lang %{name}

%check
make %{?_smp_mflags} check

%files -f %{name}.lang
%doc AUTHORS NEWS TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{_mandir}/man5/*
%{_mandir}/*/man5/*

%changelog
