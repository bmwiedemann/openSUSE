#
# spec file for package unzix
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           unzix
Version:        0.4.0
Release:        0
Summary:        Command-Line Program to Extract WinZix Archives
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
Url:            http://banu.com/unzix/
Source:         https://download.banu.com/unzix/0.4/%{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig(zlib)

%description
Unzix is a small command-line program for extracting files from the new WinZix
archive format.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE NEWS README
%{_bindir}/unzix
%doc %{_mandir}/man1/unzix.1*

%changelog
