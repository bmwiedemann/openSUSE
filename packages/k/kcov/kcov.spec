#
# spec file for package kcov
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


Name:           kcov
Version:        38
Release:        0
Summary:        Code coverage tool without special compilation options
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/SimonKagstrom/kcov
Source0:        https://github.com/SimonKagstrom/kcov/archive/v%{version}.tar.gz
Patch0:         link_order.patch
BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  python3
BuildRequires:  zlib-devel

%description
Kcov is a code coverage tester for compiled programs, Python scripts and shell
scripts.  It allows collecting code coverage information from executables
without special command-line arguments, and continuously produces output from
long-running applications.

%prep
%setup -q
%patch0 -p1
# remove LLDB headers bundled for MacOS
rm -frv external/

%build
%cmake
%make_build

%install
cd build
%make_install

%files
%doc ChangeLog README
%license COPYING*
%{_bindir}/*
%{_mandir}/man1/*
# ignore ChangeLog and COPYING* files from install
%exclude %{_datadir}/doc/kcov

%changelog
