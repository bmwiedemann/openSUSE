#
# spec file for package libxcvt
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           libxcvt
%define lname   libxcvt0
Version:        0.1.1
Release:        0
Summary:        CVT library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://gitlab.freedesktop.org/xorg/lib/libxcvt
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  meson

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.
libxcvt also provides a standalone version of the command line tool
cvt copied from the Xorg implementation and is meant to be a direct
replacement to the version provided by the Xorg server.

%package -n %lname
Summary:        CVT library
Group:          System/Libraries

%description -n %lname
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.
libxcvt also provides a standalone version of the command line tool
cvt copied from the Xorg implementation and is meant to be a direct
replacement to the version provided by the Xorg server.

%package devel
Summary:        Development files for the CVT library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.
libxcvt also provides a standalone version of the command line tool 
cvt copied from the Xorg implementation and is meant to be a direct 
replacement to the version provided by the Xorg server.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%{meson}
%{meson_build}

%install
%{meson_install}

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files
%doc COPYING README.md
/usr/bin/cvt
%{_mandir}/man1/cvt.1.gz

%files -n %lname
%defattr(-,root,root)
%_libdir/libxcvt.so.0*

%files devel
%defattr(-,root,root)
%_includedir/libxcvt/
%_libdir/libxcvt.so
%_libdir/pkgconfig/libxcvt.pc

%changelog
