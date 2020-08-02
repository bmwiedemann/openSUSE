#
# spec file for package unzix
#
# Copyright (c) 2020 SUSE LLC
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


Name:           unzix
Version:        0.4.0
Release:        0
Summary:        Command-Line Program to Extract WinZix Archives
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
URL:            http://banu.com/unzix/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
Unzix is a small command-line program for extracting files from the new WinZix
archive format.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS NEWS README
%{_bindir}/unzix
%{_mandir}/man1/unzix.1%{?ext_man}

%changelog
