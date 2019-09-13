#
# spec file for package ois
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 1_3_0

Name:           ois
Version:        1.3.0
Release:        0
Summary:        Object Oriented Input System
License:        Zlib
Group:          System/Libraries
Url:            http://sourceforge.net/projects/wgois
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM ois-gcc47.patch
Patch0:         %{name}-gcc47.patch
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Object Oriented Input System (OIS) is a solution for using all kinds
of Input Devices (Keyboards, Mice, Joysticks, etc) and feedback
devices (e.g. forcefeedback).

%package -n libOIS-%{sover}
Summary:        Object Oriented Input System development package
Group:          System/Libraries

%description -n libOIS-%{sover}
Object Oriented Input System (OIS) is a solution for using all kinds
of Input Devices (Keyboards, Mice, Joysticks, etc) and feedback
devices (e.g. forcefeedback).

%package -n libOIS-devel
Summary:        Object Oriented Input System development package
Group:          Development/Libraries/C and C++
Requires:       libOIS-%{sover} = %{version}
Requires:       libstdc++-devel

%description -n libOIS-devel
Object Oriented Input System (OIS) is a solution for using all kinds
of Input Devices (Keyboards, Mice, Joysticks, etc) and feedback
devices (e.g. forcefeedback).

%prep
%setup -q -n ois
%patch0 -p1
chmod +x bootstrap
dos2unix ReadMe.txt

%build
./bootstrap
%if 0%{?suse_version} <= 1010
export LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%endif
export LDFLAGS="$LDFLAGS -Wl,--no-undefined"
export CXXFLAGS="%optflags -fvisibility-inlines-hidden"
%configure --disable-static
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/lib*.la

%post -n libOIS-%{sover} -p /sbin/ldconfig
%postun -n libOIS-%{sover} -p /sbin/ldconfig

%files -n libOIS-%{sover}
%defattr(0644,root,root)
%{_libdir}/libOIS-%{version}.so

%files -n libOIS-devel
%defattr(-,root,root)
%doc ReadMe.txt
%{_includedir}/OIS
%{_libdir}/libOIS.so
%{_libdir}/pkgconfig/OIS.pc

%changelog
