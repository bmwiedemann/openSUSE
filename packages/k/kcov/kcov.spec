#
# spec file for package kcov
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


Name:           kcov
Version:        41
Release:        0
Summary:        Code coverage tool without special compilation options
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/SimonKagstrom/kcov
Source0:        https://github.com/SimonKagstrom/kcov/archive/v%{version}.tar.gz
Patch0:         link_order.patch
BuildRequires:  binutils-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    s390x

%description
Kcov is a code coverage tester for compiled programs, Python scripts and shell
scripts.  It allows collecting code coverage information from executables
without special command-line arguments, and continuously produces output from
long-running applications.

%prep
%autosetup -p1
# remove LLDB headers bundled for MacOS
rm -frv external/

%build
%if 0%{?suse_version} > 1500
export CFLAGS="%{optflags} -lsframe -lzstd"
%endif
%cmake
%cmake_build

%install
%cmake_install
# ignore ChangeLog and COPYING*, they are handled with doc and license macros
rm -r %{buildroot}%{_datadir}/doc/kcov

%files
%doc ChangeLog README.md
%license COPYING*
%{_bindir}/kcov
%{_bindir}/kcov-system-daemon
%{_mandir}/man1/kcov.1%{?ext_man}

%changelog
