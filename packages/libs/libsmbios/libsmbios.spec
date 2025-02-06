#
# spec file for package libsmbios
#
# Copyright (c) 2025 SUSE LLC
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


%define sonum 2
%define libname libsmbios_c%{sonum}
Name:           libsmbios
Version:        2.4.3.3.gf01a217
Release:        0
Summary:        SMBIOS table library and utilities
License:        GPL-2.0-or-later OR OSL-2.1
Group:          Hardware/Other
URL:            https://github.com/dell/libsmbios
Source:         %{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/dell/libsmbios/pull/149 drop unittest.makeSuite (dropped in python 3.13)
Patch:          unittest-drop-makeSuite.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  libcppunit-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
# libsmbios only ever makes sense on intel compatible arches
# no DMI tables on ppc, s390, etc.
ExclusiveArch:  x86_64 ia64 %{ix86}

%description
libsmbios provides a library to interface with the SMBIOS tables. It
also provides extensions for proprietary methods of interfacing with
Dell specific SMBIOS tables.

%lang_package

%package -n %{libname}
Summary:        SMBIOS table interface library
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{libname}
libsmbios provides a library to interface with the SMBIOS tables. It
also provides extensions for proprietary methods of interfacing with
Dell specific SMBIOS tables.

This package provides the C API library.

%package -n python3-smbios
Summary:        Python interface to Libsmbios C library
Group:          System/Libraries
Requires:       %{libname} = %{version}
# We provide only python3 bindings thus obsolete the old ones
Obsoletes:      python-smbios

%description -n python3-smbios
This package provides a Python interface to libsmbios

%package -n smbios-utils
Summary:        Utilities that use libsmbios
Group:          System/Management
Recommends:     %{name}-lang = %{version}
Recommends:     python3-smbios-utils = %{version}
# Give away the bin subpkg and just pull them all here instead of playing with
# metapackages
Provides:       libsmbios-bin = %{version}
Provides:       smbios-utils-bin
Obsoletes:      libsmbios-bin < %{version}
Provides:       libsmbios-unsupported-bin = %{version}
Obsoletes:      libsmbios-unsupported-bin < %{version}

%description -n smbios-utils
Get BIOS information, such as System product name, product id, service tag and
asset tag.

%package -n python3-smbios-utils
Summary:        Python executables that use libsmbios
Group:          System/Management
Requires:       python3-smbios = %{version}
# Former name replacement
Provides:       smbios-utils-python = %{version}

%description -n python3-smbios-utils
Get BIOS information, such as System product name, product id, service tag and
asset tag. Set service and asset tags on Dell machines. Manipulate wireless
cards/bluetooth on Dell laptops. Set BIOS password on select Dell systems.
Update BIOS on select Dell systems. Set LCD brightness on select Dell laptops.

%package -n libsmbios-devel
Summary:        Development headers and archives
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       libsmbios2-devel = %{version}
Obsoletes:      libsmbios2-devel < %{version}

%description -n libsmbios-devel
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package contains the headers and .a files necessary to compile new client
programs against libsmbios.

%prep
%autosetup -p1
# That conflicts with --disable-static
sed -i"" "s/ -static//" src/bin/Makefile.am

%build
autoreconf -fvi
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure \
	--disable-static \
	--enable-nls \
	--enable-python \
	--enable-as-needed \
	--enable-doxygen \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# python3 duplicates
%fdupes %{buildroot}%{python3_sitearch}

# include files
mkdir -p %{buildroot}/%{_includedir}
cd src/include
find . -name "*.h" -exec install -m 0644 -D {} %{buildroot}/%{_includedir}/{} \;
cd ../..
cp -a out/public-include/* %{buildroot}%{_includedir}/

%find_lang %{name}

# backwards compatible
mkdir -p %{buildroot}%{_bindir}
ln -s %{_sbindir}/smbios-wireless-ctl %{buildroot}/%{_bindir}/dellWirelessCtl
ln -s smbios-sys-info %{buildroot}/%{_sbindir}/getSystemId
ln -s smbios-wireless-ctl %{buildroot}/%{_sbindir}/dellWirelessCtl
ln -s smbios-lcd-brightness %{buildroot}/%{_sbindir}/dellLcdBrightness

%python3_fix_shebang

%check
%make_build check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING-GPL COPYING-OSL
%license src/bin/getopts_LICENSE.txt
%{_libdir}/libsmbios_c.so.%{sonum}
%{_libdir}/libsmbios_c.so.*
%{_datadir}/locale/en/

%files lang -f %{name}.lang
# english locale should be in the main package
%exclude %{_datadir}/locale/en

%files -n libsmbios-devel
%{_includedir}/smbios
%{_includedir}/smbios_c
%{_libdir}/libsmbios_c.so
%{_libdir}/pkgconfig/*.pc

%files -n smbios-utils
# C utilities
%{_sbindir}/smbios-state-byte-ctl
%{_mandir}/man?/smbios-state-byte-ctl.*
%{_sbindir}/smbios-get-ut-data
%{_mandir}/man?/smbios-get-ut-data.*
%{_sbindir}/smbios-upflag-ctl
%{_mandir}/man?/smbios-upflag-ctl.*
%{_sbindir}/smbios-sys-info-lite
%{_mandir}/man?/smbios-sys-info-lite.*

%files -n python3-smbios
%{python3_sitearch}/*

%files -n python3-smbios-utils
%dir %{_sysconfdir}/libsmbios
%config(noreplace) %{_sysconfdir}/libsmbios/*
# python utilities
%{_sbindir}/smbios-battery-ctl
%{_mandir}/man?/smbios-battery-ctl.*
%{_sbindir}/smbios-sys-info
%{_mandir}/man?/smbios-sys-info.*
%{_sbindir}/smbios-token-ctl
%{_mandir}/man?/smbios-token-ctl.*
%{_sbindir}/smbios-passwd
%{_mandir}/man?/smbios-passwd.*
%{_sbindir}/smbios-wakeup-ctl
%{_mandir}/man?/smbios-wakeup-ctl.*
%{_sbindir}/smbios-wireless-ctl
%{_mandir}/man?/smbios-wireless-ctl.*
%{_sbindir}/smbios-lcd-brightness
%{_mandir}/man?/smbios-lcd-brightness.*
%{_sbindir}/smbios-keyboard-ctl
%{_mandir}/man?/smbios-keyboard-ctl.*
%{_sbindir}/smbios-thermal-ctl
%{_mandir}/man?/smbios-thermal-ctl.*
# used by HAL in old location, so keep it around until HAL is updated.
%{_sbindir}/dellLcdBrightness
%{_sbindir}/getSystemId
%{_sbindir}/dellWirelessCtl
%{_bindir}/dellWirelessCtl
# data files
%{_datadir}/smbios-utils

%changelog
