#
# spec file for package Bear
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


# Tests are resolvable only on Tumbleweed
%if 0%{?suse_version} > 1500
%bcond_without tests
%else
%bcond_with tests
%endif
Name:           Bear
Version:        2.4.2
Release:        0
Summary:        Tool to generate compilation database for clang tooling
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/rizsotto/Bear
Source:         %{URL}/archive/%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  cmake
%if %{with tests}
BuildRequires:  clang
BuildRequires:  gcc-c++
BuildRequires:  python3-lit
BuildRequires:  python3-setuptools
%endif

%description
Bear is a tool to generate compilation database for clang tooling.

One way to get compilation database is to use cmake as build tool. When the
project compiles with no cmake, but another build system, there is no free json
file. Bear is a tool to generate such file during the build process.

%prep
%autosetup

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%cmake_build

%install
%cmake_install
sed -i "s|env python.*$|python3|g" %{buildroot}%{_bindir}/bear
rm -rf %{buildroot}%{_datadir}/doc/bear

%if %{with tests}
%check
pushd build
make check
popd
%endif

%files
%license COPYING
%doc ChangeLog.md README.md
%{_bindir}/bear
%{_datadir}/bash-completion/completions/bear
%{_mandir}/man1/bear.1%{?ext_man}
%dir %{_libdir}/bear
%{_libdir}/bear/libear.so

%changelog
