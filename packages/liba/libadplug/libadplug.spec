#
# spec file for package libadplug
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


%define sover 0
%define soname 2_3_3-%{sover}
%define libname libadplug%{soname}
Name:           libadplug
Version:        2.3.3
Release:        0
Summary:        AdLib Sound Player Library
License:        LGPL-2.1-only
Group:          System/Libraries
#Git-Clone:     https://github.com/adplug/adplug.git
URL:            https://adplug.github.io/
Source:         https://github.com/adplug/adplug/archive/refs/tags/adplug-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbinio)

%description
AdPlug is a hardware independent AdLib sound player library.
AdPlug plays sound data, originally created for the AdLib (OPL2) and
Sound Blaster (Dual OPL2/OPL3) audio boards, directly from its original
format on top of an emulator or by using the real hardware.
No OPL chip is required for playback.

%package -n %{libname}
Summary:        AdLib Sound Player Library
Group:          System/Libraries

%description -n %{libname}
AdPlug is a hardware independent AdLib sound player library.
AdPlug plays sound data, originally created for the AdLib (OPL2) and
Sound Blaster (Dual OPL2/OPL3) audio boards, directly from its original
format on top of an emulator or by using the real hardware.
No OPL chip is required for playback.

%package -n libadplug-devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}
Requires:       pkgconfig(libbinio)

%description -n libadplug-devel
AdPlug is a hardware independent AdLib sound player library.
AdPlug plays sound data, originally created for the AdLib (OPL2) and
Sound Blaster (Dual OPL2/OPL3) audio boards, directly from its original
format on top of an emulator or by using the real hardware.
No OPL chip is required for playback.

This subpackage contains libraries and header files for developing
applications that want to make use of libadplug.

%package -n adplugdb
Summary:        AdPlug Database Maintenance Utility
Group:          Productivity/Multimedia/Sound/Utilities

%description -n adplugdb
adplugdb maintains database files in AdPlug database format. It can add, list
and remove records within a central database, or merge a set of databases
together into one single database.

%prep
%setup -q -n "adplug-adplug-%{version}"

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc ChangeLog NEWS README
%{_libdir}/libadplug-%{version}.so.%{sover}*

%files -n libadplug-devel
%{_includedir}/adplug
%{_libdir}/libadplug.so
%{_libdir}/pkgconfig/adplug.pc
%{_infodir}/libadplug.info%{?ext_info}

%files -n adplugdb
%license COPYING
%doc README
%{_bindir}/adplugdb
%{_mandir}/man1/adplugdb.1%{?ext_man}

%changelog
