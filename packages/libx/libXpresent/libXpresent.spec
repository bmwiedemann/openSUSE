#
# spec file for package libXpresent
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


%define lname libXpresent1
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

Name:           libXpresent
Version:        1.0.1
Release:        0
Summary:        An X Window System client interface to the Present extension to the X protocol
License:        MIT
Group:          Development/Libraries/X11
URL:            https://gitlab.freedesktop.org/xorg/lib/libxpresent
Source:         https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
%if 0%{?suse_version} < 01550 && 0%{?is_opensuse}
BuildRequires:  pkgconfig(presentproto)
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  pkgconfig

%description
libXpresent provides an X Window System client interface to the
Present extension to the X protocol.

The Present extension provides a way for applications to update their
window contents from a pixmap in a well defined fashion,
synchronizing with the display refresh and potentially using a more
efficient mechanism than copying the contents of the source pixmap.

%package -n %{lname}
Summary:        An X Window System client interface to the Present extension to the X protocol
Group:          System/Libraries

%description -n %{lname}
libXpresent provides an X Window System client interface to the
Present extension to the X protocol.

The Present extension provides a way for applications to update their
window contents from a pixmap in a well defined fashion,
synchronizing with the display refresh and potentially using a more
efficient mechanism than copying the contents of the source pixmap.

%package devel
Summary:        Development files for the Xpresent library
Group:          Development/Libraries/X11
Requires:       %{lname} = %{version}

%description devel
This package contains header files and documentation for the Xpresent library.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%fdupes %{buildroot}%{_mandir}

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libXpresent.so.1*

%files devel
%license COPYING AUTHORS
%doc README.md
%{_includedir}/X11/extensions/Xpresent.h
%{_libdir}/libXpresent.{a,so}
%{_libdir}/pkgconfig/xpresent.pc
%{_mandir}/man3/{Xpresent,XPresent*}.3%{ext_man}

%changelog
