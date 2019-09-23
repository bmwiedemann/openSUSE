#
# spec file for package Bear
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


Name:           Bear
Version:        2.3.13
Release:        0
Summary:        Tool to generate compilation database for clang tooling
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/rizsotto/Bear
Source:         https://github.com/rizsotto/Bear/archive/%{version}.tar.gz
Source2:        %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  libconfig-devel
BuildRequires:  pkgconfig

%description
Bear is a tool to generate compilation database for clang tooling.

One way to get compilation database is to use cmake as build tool. When the
project compiles with no cmake, but another build system, there is no free json
file. Bear is a tool to generate such file during the build process.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%make_jobs

%install
%cmake_install
sed -i "s|env python|python2|g" %{buildroot}%{_bindir}/bear
rm -rf %{buildroot}%{_datadir}/doc/bear

%files
%license COPYING
%doc ChangeLog.md README.md
%{_bindir}/bear
%{_mandir}/man1/bear.1%{?ext_man}
%dir %{_libdir}/bear
%{_libdir}/bear/libear.so

%changelog
