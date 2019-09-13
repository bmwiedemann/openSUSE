#
# spec file for package uhd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           uhd
%define libname libuhd003
Version:        3.9.7
Release:        0
%define src_ver 003.009.007
%define img_ver 003.009.007
Summary:        The driver for USRP SDR boards
License:        GPL-3.0-or-later
Group:          Hardware/Other
Url:            http://ettus-apps.sourcerepo.com/redmine/ettus/projects/uhd/wiki
Source0:        http://files.ettus.com/binaries/uhd_stable/uhd_%{src_ver}-release/uhd_%{version}-release.tar.gz
Source1:        http://files.ettus.com/binaries/images/uhd-images_%{img_ver}-release.tar.xz
# PATCH-FIX-OPENSUSE fix-for-armv6l-armv7l-build-failure.patch
Patch0:         fix-for-armv6l-armv7l-build-failure.patch
# PATCH-FIX-OPENSUSE uhd-fix-for-boost-1_66.patch
Patch1:         uhd-fix-for-boost-1_66.patch
Patch2:         uhd-fix-for-boost-1_67.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
# WORKAROUND: force docutils to use python 2
BuildRequires:  python2-docutils
%else
BuildRequires:  boost-devel >= 1.36.0
%endif
BuildRequires:  cmake >= 2.6
BuildRequires:  docutils
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gpsd-devel
BuildRequires:  memory-constraints
BuildRequires:  orc
BuildRequires:  pkg-config
BuildRequires:  python-Mako >= 0.4
BuildRequires:  python-cheetah >= 2.0.0
BuildRequires:  python-devel >= 2.6
BuildRequires:  udev
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       udev
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%if 0%{?suse_version} > 1325
Requires:       libboost_filesystem-devel
Requires:       libboost_program_options-devel
Requires:       libboost_regex-devel
Requires:       libboost_serialization-devel
Requires:       libboost_test-devel
Requires:       libboost_thread-devel
%else
Requires:       boost-devel
%endif
Recommends:     %{name}-doc

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
%setup -q -n %{name}_%{version}-release
%patch0 -p1
%patch1 -p1
%patch2 -p1

# remove buildtime from documentation
echo "HTML_TIMESTAMP         = NO" >> docs/Doxyfile.in

%build
touch ../README.md
%limit_build
%cmake \
  -DPYTHON_EXECUTABLE=/usr/bin/python2 \
  -DENABLE_GPSD=0
%make_jobs

%check
%ctest

%install
%cmake_install

# Fix udev rules and allow access only to users in usrp group
sed -i 's/BUS==/SUBSYSTEM==/;s/SYSFS{/ATTRS{/;s/MODE:="0666"/GROUP:="usrp", MODE:="0660"/' %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules
install -m 0644 -D %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules %{buildroot}%{_udevrulesdir}/10-usrp-uhd.rules
rm %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules

# Move documentation at the default docdir
mkdir -p  %{buildroot}%{_docdir}/uhd
mv %{buildroot}%{_datadir}/doc/uhd %{buildroot}%{_docdir}/
mv %{buildroot}%{_libdir}/uhd/utils/*[!.rules] %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/uhd/examples/* %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/uhd/tests/*_test %{buildroot}%{_bindir}

rm -rf %{buildroot}%{_libdir}/uhd/tests
rm -rf %{buildroot}%{_libdir}/uhd/examples

rm -rf %{buildroot}%{_docdir}/uhd/LICENSE
rm -rf %{buildroot}%{_docdir}/uhd/README.md

# two executable files are installed to /usr/share/uhd
mv %{buildroot}%{_libdir}/uhd/utils/query_gpsdo_sensors %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/uhd/utils/usrp_n2xx_simple_net_burner %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/uhd/utils/b2xx_fx3_utils %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/uhd/utils/usrp_x3xx_fpga_burner %{buildroot}%{_bindir}

# extract firmware
mkdir -p %{buildroot}%{_datadir}/uhd
tar -xJvf %{SOURCE1} --transform="s,^uhd-images_%{img_ver}-release/share/uhd/,," --show-transformed-names -C %{buildroot}%{_datadir}/uhd

# find dupes
%fdupes -s %{buildroot}%{_prefix}

%pre -n %{libname}
getent group usrp >/dev/null || %{_sbindir}/groupadd -r usrp

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/*.so.*.*

%files udev
%defattr(-,root,root)
%{_udevrulesdir}/10-usrp-uhd.rules

%files devel
%defattr(-,root,root)
%dir %{_includedir}/uhd
%dir %{_datadir}/uhd
%exclude %{_datadir}/uhd/images
%{_includedir}/uhd/*
%{_includedir}/uhd.h
%{_bindir}/*
%{_libdir}/libuhd.so
%{_libdir}/libuhd.so.003
%{_libdir}/pkgconfig/uhd.pc
%{_libdir}/cmake/uhd
%{_mandir}/man1/*

%files firmware
%defattr(-,root,root)
%{_datadir}/uhd/images/

%files doc
%defattr(-,root,root)
%dir %{_docdir}/uhd
%{_docdir}/uhd/doxygen
#{_docdir}/uhd/manual

%changelog
