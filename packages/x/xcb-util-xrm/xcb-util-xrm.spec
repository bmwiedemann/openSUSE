#
# spec file for package xcb-util-xrm
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define clib    libxcb-xrm0
Name:           xcb-util-xrm
Version:        1.2
Release:        0
Summary:        XCB utility module for the X Resource Manager
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/Airblader/%{name}
Source:         https://github.com/Airblader/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  xcb-util-devel
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- xrm: utility functions for the X resource manager

%package -n %{clib}
Summary:        XCB utility module for the X Resource Manager
Group:          System/Libraries

%description -n %{clib}
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- xrm: utility functions for the X resource manager

%package devel
Summary:        Development files for the XCB X Resource Manager utility module
Group:          Development/Libraries/C and C++
Requires:       %{clib} = %{version}

%description devel
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in libxcb-xrm0.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post -n %{clib} -p /sbin/ldconfig
%postun -n %{clib} -p /sbin/ldconfig

%files -n %{clib}
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_libdir}/libxcb-xrm.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/xcb/
%{_libdir}/libxcb-xrm.so
%{_libdir}/pkgconfig/xcb-xrm.pc

%changelog
