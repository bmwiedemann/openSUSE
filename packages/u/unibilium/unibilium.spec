#
# spec file for package unibilium
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


%define sover 4
Name:           unibilium
Version:        2.1.0
Release:        0
Summary:        A terminfo parsing library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/neovim/neovim/wiki/Deps#forks
Source:         https://github.com/neovim/unibilium/archive/v%{version}/unibilium-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

%package -n lib%{name}%{sover}
Summary:        A terminfo parsing library
Group:          System/Libraries

%description -n lib%{name}%{sover}
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

This package holds the shared library.

%package devel
Summary:        Development files for unibilium, a terminfo parsing library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

This package holds the development files.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" \
     PREFIX="%{_prefix}" \
     LIBDIR="%{_libdir}" \
     %{?_smp_mflags}

%install
%make_install CFLAGS="%{optflags}" \
     PREFIX="%{_prefix}" \
     LIBDIR="%{_libdir}"

# Remove libtool files.
find %{buildroot} -type f -name "*.la" -delete -print

# Remove static library file.
rm -vf %{buildroot}%{_libdir}/lib%{name}.a

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE
%doc Changes GPLv3 LGPLv3 README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/unibi*.3*

%changelog
