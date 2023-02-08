#
# spec file for package uhd
#
# Copyright (c) 2021-2023 SUSE LLC
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

%define libname libuhd4_4_0
Name:           uhd
Version:        4.4.0.0
Release:        0
Summary:        The driver for USRP SDR boards
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://files.ettus.com/manual/
Source0:        https://github.com/EttusResearch/uhd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/EttusResearch/uhd/releases/download/v%{version}/uhd-images_%{version}.tar.xz
BuildRequires:  cmake >= 2.6
BuildRequires:  docutils
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gpsd-devel
BuildRequires:  memory-constraints
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3-devel
BuildRequires:  python3-Mako >= 0.4.2
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-setuptools
Requires:       udev
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel

%description
The UHD is the "Universal Software Radio Peripheral" hardware driver.
The goal of the UHD is to provide a host driver and API for current
and future Ettus Research products. Users will be able to use the
UHD driver standalone or with 3rd party applications.

%package     -n %{libname}
Summary:        The UHD driver
Group:          Hardware/Other
Requires:       %{name}-udev >= %{version}
# PRE script requires /usr/sbin/groupadd, that exists in the "shadow" package
Requires(pre):  shadow

%description -n %{libname}
The UHD is the "Universal Software Radio Peripheral" hardware driver.
The goal of the UHD is to provide a host driver and API for current
and future Ettus Research products. Users will be able to use the
UHD driver standalone or with 3rd party applications.

%package        utils
Summary:        Utility programs for USRP hardware
Group:          Hardware/Other
Requires:       python3-%{name} >= %{version}

%description    utils
The UHD is the "Universal Software Radio Peripheral" hardware driver.
The goal of the UHD is to provide a host driver and API for current
and future Ettus Research products. Users will be able to use the
UHD driver standalone or with 3rd party applications.

This package contains utility programs for handling USRP frontens

%package     -n python3-%{name}
Summary:        Python bindings for uhd
Group:          Hardware/Other

%description  -n python3-%{name}
The UHD is the "Universal Software Radio Peripheral" hardware driver.
The goal of the UHD is to provide a host driver and API for current
and future Ettus Research products. Users will be able to use the
UHD driver standalone or with 3rd party applications.

This package contains Python bindings UHD.

%package        udev
Summary:        UHD udev rules
Group:          Hardware/Other

%description    udev
The UHD is the "Universal Software Radio Peripheral" hardware driver.
The goal of the UHD is to provide a host driver and API for current
and future Ettus Research products. Users will be able to use the
UHD driver standalone or with 3rd party applications.

This package contains udev rules for UHD.

%package        devel
Summary:        Development files for uhd
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}
Recommends:     %{name}-doc
Requires:       libboost_filesystem-devel
Requires:       libboost_program_options-devel
Requires:       libboost_regex-devel
Requires:       libboost_serialization-devel
Requires:       libboost_test-devel
Requires:       libboost_thread-devel

%description    devel
The UHD is the "Universal Software Radio Peripheral" hardware driver.
The goal of the UHD is to provide a host driver and API for current
and future Ettus Research products. Users will be able to use the
UHD driver standalone or with 3rd party applications.

This package contains all the necessary tools, examples and include
files for development with the UHD Driver.

%package        doc
Summary:        Documentation files for uhd
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
This package contains the documentation for the Universal Hardware Driver (UHD).

%package        firmware
Summary:        Firmware images for uhd
Group:          Hardware/Other
Requires:       %{libname} = %{version}
BuildArch:      noarch

%description    firmware
This package contains binary firmware images for the Universal Hardware Driver (UHD).

%prep
%autosetup -p1
# fix python shebangs
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{_bindir}/python3|' {} \;
find . -type f -name "*_bist" -exec sed -i '/^#!/ s|.*|#!%{_bindir}/python3|' {} \;
find . -type f -name "*_update_fs" -exec sed -i '/^#!/ s|.*|#!%{_bindir}/python3|' {} \;
# remove buildtime from documentation
echo "HTML_TIMESTAMP         = NO" >> host/docs/Doxyfile.in

%build
%limit_build
cd host
%cmake \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
  -DENABLE_TESTS=OFF \
%ifarch %arm
  -DNEON_SIMD_ENABLE=OFF \
%endif
  -DENABLE_GPSD=OFF
%cmake_build

%check
# Do not run check for now - compilation of tests programs is broken:
# See: https://github.com/EttusResearch/uhd/issues/267
#cd host
#%%ctest

%install
cd host
%cmake_install

# Fix udev rules and allow access only to users in usrp group
sed -i 's/BUS==/SUBSYSTEM==/;s/SYSFS{/ATTRS{/;s/MODE:="0666"/GROUP:="usrp", MODE:="0660"/' %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules
install -m 0644 -D %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules %{buildroot}%{_udevrulesdir}/10-usrp-uhd.rules
rm %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules

## Move documentation to the default docdir
mkdir -p  %{buildroot}%{_docdir}/uhd
mv %{buildroot}%{_datadir}/doc/uhd %{buildroot}%{_docdir}/
mv %{buildroot}%{_libdir}/uhd/utils/*[!.rules] %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/uhd/examples/* %{buildroot}%{_bindir}
mv %{buildroot}%{_bindir}/python/* %{buildroot}%{_bindir}
rm -R %{buildroot}%{_bindir}/python
#mv %%{buildroot}%%{_libdir}/uhd/tests/*_test %%{buildroot}%%{_bindir}
#
#rm -R %%{buildroot}%%{_libdir}/uhd/tests
#rm -R %%{buildroot}%%{_libdir}/uhd/examples
#
rm %{buildroot}%{_docdir}/uhd/LICENSE
rm %{buildroot}%{_docdir}/uhd/README.md
#
## two executable files are installed to /usr/share/uhd
mv %{buildroot}%{_libdir}/uhd/utils/b2xx_fx3_utils %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/uhd/utils/query_gpsdo_sensors %{buildroot}%{_bindir}

#
## extract firmware
mkdir -p %{buildroot}%{_datadir}/uhd/images
tar -xxvf %{SOURCE1} --transform="s,^uhd-images_%{version}/,," --show-transformed-names -C %{buildroot}%{_datadir}/uhd/images/
rm -R %{buildroot}%{_datadir}/uhd/images/winusb_driver/

# find dupes
%fdupes -s %{buildroot}%{_prefix}

%pre -n %{libname}
getent group usrp >/dev/null || %{_sbindir}/groupadd -r usrp

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license host/LICENSE
%doc host/README.md
%{_libdir}/libuhd.so.*

%files utils
%{_bindir}/*
%{_bindir}/uhd_images_downloader.py
%{_bindir}/usrp2_card_burner.py
%dir %{_datadir}/uhd
%exclude %{_datadir}/uhd/images
%{_datadir}/uhd/cal
%{_datadir}/uhd/rfnoc
%{_mandir}/man1/*

%files -n python3-%{name}
%{python3_sitearch}/uhd
%{python3_sitearch}/usrp_mpm

%files udev
%{_udevrulesdir}/10-usrp-uhd.rules

%files devel
%dir %{_includedir}/uhd
%{_includedir}/uhd/*
%{_includedir}/uhd.h
%{_libdir}/libuhd.so
%{_libdir}/pkgconfig/uhd.pc
%{_libdir}/cmake/uhd

%files firmware
%{_datadir}/uhd/images/

%files doc
%dir %{_docdir}/uhd
%{_docdir}/uhd/doxygen

%changelog
