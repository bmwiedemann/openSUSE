#
# spec file for package xdotool
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xdotool
Version:        3.20211022.1
Release:        0
Summary:        Fake keyboard/mouse input
License:        BSD-3-Clause
Group:          System/X11/Utilities
URL:            https://www.semicomplete.com/projects/xdotool/
Source:         https://github.com/jordansissel/xdotool/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xtst)

%description
This tool lets you programatically (or manually) simulate keyboard input and
mouse activity, move and resize windows, etc. It does this using X11's XTEST
extension and other Xlib functions.

%package devel
Summary:        Development and Library files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}
Requires:       pkgconfig(x11)

%description devel
This tool lets you programatically (or manually) simulate keyboard input and
mouse activity, move and resize windows, etc. It does this using X11's XTEST
extension and other Xlib functions.

Library and Header files for %{name}

%prep
%setup -q

%build
# Fix file permissions
chmod 0644 examples/ffsp.sh
export WARNFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install \
    PREFIX=%{_prefix} \
    INSTALLLIB=%{_libdir} \
    INSTALLMAN=%{_mandir} \

chmod 0644 examples/*

%post -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%doc CHANGELIST COPYRIGHT README.md
%doc examples
%{_mandir}/man1/%{name}.1%{ext_man}
%{_libdir}/libxdo.so.*

%files devel
%attr(0644,root,root) %{_includedir}/*.h
%{_libdir}/libxdo.so
%{_libdir}/pkgconfig/libxdo.pc

%changelog
