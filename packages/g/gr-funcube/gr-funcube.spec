#
# spec file for package gr-funcube
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


%define libname libgnuradio-funcube
%define sover 3_10_0
Name:           gr-funcube
Version:        3.10.0.rc3
Release:        0
Summary:        FCD and FCDpro Plus Linux addon for gnuradio
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/dl1ksv/gr-funcube
#Git-Clone:     https://github.com/dl1ksv/gr-funcube.git
Source:         https://github.com/dl1ksv/gr-funcube/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnuradio-devel >= 3.10.0
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libhidapi-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libunwind-devel
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-pybind11-devel >= 2.4.3
BuildRequires:  python3-six
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(portaudio-2.0)

%description
gr-funcube is an linux oot-module for gnuradio to implement a FUNcube
Dongle and a FUNcube Dongle PRO+ source. It autodetects the correct
soundcard from /proc/asound/cards. This idea was taken from the osmosdr
 drivers. To control the device, the hidraw code of the HID API is used.

%package -n %{libname}%{sover}
Summary:        FCD and FCDpro Plus Linux addon for gnuradio
Group:          System/Libraries
Recommends:     fuuncube-udev
Obsoletes:      libgnuradio-fcdproplus3_8_0

%description -n %{libname}%{sover}
gr-funcube is an linux oot-module for gnuradio to implement a FUNcube
Dongle and a FUNcube Dongle PRO+ source. It autodetects the correct
soundcard from /proc/asound/cards. This idea was taken from the osmosdr
 drivers. To control the device, the hidraw code of the HID API is used.

%package -n %{libname}-devel
Summary:        Development files for the FCD and FCDpro Plus addon
Group:          Development/Libraries/Other
Requires:       %{libname}%{sover} = %{version}

%description -n %{libname}-devel
gr-funcube is an linux oot-module for gnuradio to implement a FUNcube
Dongle and a FUNcube Dongle PRO+ source. It autodetects the correct
soundcard from /proc/asound/cards. This idea was taken from the osmosdr
 drivers. To control the device, the hidraw code of the HID API is used.

%package -n python3-gr-funcube
Summary:        Python bindings for FCD and FCDpro Plus
Group:          Development/Libraries/Other
Requires:       %{libname}%{sover} = %{version}

%description -n python3-gr-funcube
gr-funcube is an linux oot-module for gnuradio to implement a FUNcube
Dongle and a FUNcube Dongle PRO+ source. It autodetects the correct
soundcard from /proc/asound/cards. This idea was taken from the osmosdr
 drivers. To control the device, the hidraw code of the HID API is used.

%package -n funcube-udev
Summary:        Udev rules for FCD and FCDpro Plus devices
Group:          Hardware/Other
Requires(pre):  shadow
Obsoletes:      fcdproplus-udev
BuildArch:      noarch

%description -n funcube-udev
Udev rules for FCD and FCDpro Plus devices.

%package doc
Summary:        Documentation for gr-funcube
Group:          Documentation/Other
Requires:       %{libname}%{sover} = %{version}
BuildArch:      noarch

%description doc
Documentation for gr-funcube module for GNU Radio.

%prep
%autosetup

%build
%cmake \
    -DENABLE_DOXYGEN=1 \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}%{_docdir}

install -Dm 0644 50-funcube.rules %{buildroot}%{_udevrulesdir}/50-funcube.rules

%post   -n %{libname}%{sover} -p /sbin/ldconfig
%postun -n %{libname}%{sover} -p /sbin/ldconfig
%post -n funcube-udev
%udev_rules_update

%postun -n funcube-udev
%udev_rules_update

%files
%license COPYING
%doc README.md
%{_datadir}/gnuradio/grc/blocks/*.yml
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml

%files -n %{libname}%{sover}
%{_libdir}/libgnuradio-funcube.so.*

%files -n %{libname}-devel
%{_includedir}/funcube
%{_libdir}/libgnuradio-funcube.so
%{_libdir}/cmake/funcube

%files -n python3-gr-funcube
%{python3_sitearch}/funcube

%files -n funcube-udev
%{_udevrulesdir}/50-funcube.rules

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html
%{_docdir}/%{name}/xml

%changelog
