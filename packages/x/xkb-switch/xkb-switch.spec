#
# spec file for package xkb-switch
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xkb-switch
Version:        1.8.5
Release:        0
Summary:        Switch X keyboard layouts from the command line
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://github.com/grwlf/xkb-switch
Source:         https://github.com/grwlf/xkb-switch/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libxkbfile-devel

%description
xkb-switch is a C++ program that allows to query and change the XKB layout state.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
# Move libraries to lib64 if necessary
if [ ! -d %{buildroot}%{_libdir}/ ]; then
  mv %{buildroot}%{_prefix}/lib/ %{buildroot}%{_libdir}
fi
rm -f %{buildroot}%{_libdir}/libxkbswitch.so
mv %{buildroot}%{_mandir}/man1/xkb-switch.1.gzip %{buildroot}%{_mandir}/man1/xkb-switch.1.gz

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license COPYING
%{_bindir}/xkb-switch
%{_libdir}/libxkbswitch.so.1
%{_libdir}/libxkbswitch.so.%{version}
%{_mandir}/man1/xkb-switch.1%{?ext_man}

%changelog
