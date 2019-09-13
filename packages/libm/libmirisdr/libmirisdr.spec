#
# spec file for package libmirisdr
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2014 Wojciech Kazubski, wk@ire.pw.edu.pl
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


%define sover 0
%define libname libmirisdr%{sover}
Name:           libmirisdr
Version:        0.0.0+git.20130608
Release:        0
Summary:        Support programs for MRi2500
License:        GPL-2.0
Group:          Productivity/Hamradio/Other
Url:            http://cgit.osmocom.org/libmirisdr/
Source:         %{name}-%{version}.tar.xz
Patch0:         libmirisdr-cmake-libsuffix.diff
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Programs that controls Mirics MRi2500 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package -n %{libname}
Summary:        SDR driver for MRi2500
Group:          System/Libraries
Provides:       %{name} = %{version}
Requires:       mirisdr-udev

%description -n %{libname}
Library to run Mirics MRi2500 based DVB dongle as a SDR receiver.

%package -n mirisdr
Summary:        Support programs for MRi2500
Group:          Productivity/Hamradio/Other

%description -n mirisdr
Programs that controls Mirics MRi2500 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package devel
Summary:        Development files for libmirisdr
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
Library headers and other development files for mirisdr driver.

%package -n mirisdr-udev
Summary:        Udev rules for Mirics MRi2500 based DVB dongles
Group:          Hardware/Other

%description -n mirisdr-udev
Udev rules for Mirics MRi2500 based DVB dongles.


%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
rm %{buildroot}%{_libdir}/libmirisdr.a

#install udev rules
install -D -p -m 0644 mirisdr.rules %{buildroot}%{_udevrulesdir}/10-mirisdr.rules

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n mirisdr-udev
%udev_rules_update

%postun -n mirisdr-udev
%udev_rules_update

%files -n mirisdr
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/miri_sdr

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/libmirisdr.so.%{sover}*

%files -n mirisdr-udev
%defattr(-,root,root)
%{_udevrulesdir}/10-mirisdr.rules

%files devel
%defattr(-,root,root)
%{_libdir}/libmirisdr.so
%{_includedir}/mirisdr.h
%{_includedir}/mirisdr_export.h
%{_libdir}/pkgconfig/libmirisdr.pc

%changelog
