#
# spec file for package gr-fcdproplus
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


%define libname libgnuradio-fcdproplus
%define sover 3_8_0
Name:           gr-fcdproplus
Version:        3.8~git.20200811
Release:        0
Summary:        Fcdproplus Linux addon for gnuradio
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/dl1ksv/gr-fcdproplus
#Git-Clone:     https://github.com/dl1ksv/gr-fcdproplus.git
Source:         %{name}-%{version}.tar.xz
Source1:        gr-fcdproplus.rules
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnuradio-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libhidapi-devel
BuildRequires:  libmpir-devel
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(portaudio-2.0)
%if 0%{?suse_version} <= 1500
BuildRequires:  python3-six
%endif

%description
gr-fcdproplus is a Linux addon for gnuradio to implement a FUNcube Dongle
Pro+ source. It autodetects the correct soundcard from /proc/asound/cards.
This idea was taken from the osmosdr drivers.
To control the device, the hidraw code of the HID API is used.

%package -n %{libname}%{sover}
Summary:        Fcdproplus Linux addon for gnuradio
Group:          System/Libraries
Recommends:     fcdproplus-udev

%description -n %{libname}%{sover}
gr-fcdproplus is a Linux addon for gnuradio to implement a FUNcube Dongle
Pro+ source. It autodetects the correct soundcard from /proc/asound/cards.
This idea was taken from the osmosdr drivers.
To control the device, the hidraw code of the HID API is used.

%package -n %{libname}-devel
Summary:        Development files for the fcdproplus gnuradio Linux addon
Group:          Development/Libraries/Other
Requires:       %{libname}%{sover} = %{version}

%description -n %{libname}-devel
gr-fcdproplus is a Linux addon for gnuradio to implement a FUNcube Dongle
Pro+ source. It autodetects the correct soundcard from /proc/asound/cards.
This idea was taken from the osmosdr drivers.
To control the device, the hidraw code of the HID API is used.

%package -n python-gr-fcdproplus
Summary:        Python bindings for gr-fcdproplus
Group:          Development/Libraries/Other
Requires:       %{libname}%{sover} = %{version}

%description -n python-gr-fcdproplus
gr-fcdproplus is a Linux addon for gnuradio to implement a FUNcube Dongle
Pro+ source. It autodetects the correct soundcard from /proc/asound/cards.
This idea was taken from the osmosdr drivers.
To control the device, the hidraw code of the HID API is used.

%package -n fcdproplus-udev
Summary:        Udev rules for funcube dongle pro+ devices
Group:          Hardware/Other
Requires(pre):  pwdutils
BuildArch:      noarch

%description -n fcdproplus-udev
Udev rules for funcube dongle pro+ devices.

%package devel-doc
Summary:        Documentation for gnuradio-osmosdr
Group:          Documentation/Other
Requires:       %{libname}-devel
BuildArch:      noarch

%description devel-doc
Documentation for gr-fcdproplus module for GNU Radio.

%prep
%setup -q

%build
%cmake \
    -DENABLE_DOXYGEN=1 \
    -DCMAKE_SHARED_LINKER_FLAGS=""
make %{?_smp_mflags}

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}%{_docdir}

install -Dm 0644 "%{SOURCE1}" %{buildroot}%{_udevrulesdir}/10-gr-fcdproplus.rules

%post   -n %{libname}%{sover} -p /sbin/ldconfig
%postun -n %{libname}%{sover} -p /sbin/ldconfig

%post -n fcdproplus-udev
%udev_rules_update

%postun -n fcdproplus-udev
%udev_rules_update

%files
%license COPYING
%doc README.md
%{_datadir}/gnuradio/grc/blocks/*.yml
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml

%files -n %{libname}%{sover}
%{_libdir}/libgnuradio-fcdproplus.so.*

%files -n %{libname}-devel
%{_includedir}/fcdproplus
%{_libdir}/libgnuradio-fcdproplus.so
%{_libdir}/cmake/gr-fcdproplus
%{_libdir}/pkgconfig/gnuradio-fcdproplus.pc

%files -n python-gr-fcdproplus
%{python3_sitearch}/fcdproplus

%files -n fcdproplus-udev
%{_udevrulesdir}/10-gr-fcdproplus.rules

%files devel-doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html
%{_docdir}/%{name}/xml

%changelog
