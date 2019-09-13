#
# spec file for package airspyhf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define sover   0
%define airspyhf_group    airspyhf
%define libname lib%{name}%{sover}
Name:           airspyhf
Version:        1.1.5
Release:        0
Summary:        Support programs for Airspy HF+ SDR
License:        BSD-3-Clause
Group:          Productivity/Hamradio/Other
Url:            http://www.airspy.com/airspy-hf-plus
#Git-Clone:     https://github.com/airspy/airspyhf.git
Source:         https://github.com/airspy/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         airspyhf-fix-libm-linking.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Host software for Airspy HF+, a software defined radio
for the HF and VHF bands.

%package -n %{libname}
Summary:        Driver for Airspy HF+
Group:          System/Libraries
Requires:       %{name}-udev

%description -n %{libname}
Library to run Airspy HF+ SDR receiver.

%package udev
Summary:        Udev rules for Airspy HF+ SDR
Group:          Hardware/Other
Requires(pre):  shadow

%description udev
Udev rules for Airspy HF+ SDR.

%package devel
Summary:        Development files for Airspy HF+
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description devel
Library headers for Airspy HF+ driver.

%prep
%setup -q
%patch0 -p1

# HACK: set udev group to airspyhf
sed -i "s/plugdev/airspyhf/g" tools/52-airspyhf.rules

%build
%cmake \
%if 0%{?suse_version} < 1330
    -DCMAKE_C_FLAGS=-std=c99 \
%endif
  -DINSTALL_UDEV_RULES=ON
make %{?_smp_mflags}

%install
%cmake_install
rm %{buildroot}%{_libdir}/libairspyhf.a

mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspyhf.rules %{buildroot}%{_udevrulesdir}

%post -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig
%pre udev
getent group %{airspyhf_group} >/dev/null || groupadd -r %{airspyhf_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files -n %{libname}
%doc README.md LICENSE
%{_libdir}/libairspyhf.so.*

%files udev
%{_udevrulesdir}/52-airspyhf.rules

%files devel
%{_libdir}/libairspyhf.so
%{_includedir}/libairspyhf
%{_libdir}/pkgconfig/libairspyhf.pc

%changelog
