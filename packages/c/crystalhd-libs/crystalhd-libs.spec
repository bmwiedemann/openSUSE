#
# spec file for package crystalhd-libs
#
# Copyright (c) 2021 SUSE LLC
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


%if %{undefined _firmwaredir}
%define _firmwaredir /lib/firmware
%endif
Name:           crystalhd-libs
Version:        3.6.5
Release:        0
Summary:        Broadcom Crystal HD device interface library
License:        LGPL-2.1-or-later
Group:          Hardware/Other
URL:            http://www.broadcom.com/support/crystal_hd/
Source0:        crystalhd-libs_%{version}-1.tar.bz2
Source1:        README
Source2:        LICENSE
Source3:        baselibs.conf
Patch0:         %{name}-define-first.patch
Patch1:         crystalhd-firmwaredir.patch
BuildRequires:  gcc-c++
ExclusiveArch:  %ix86 x86_64

%description
This package contains the library to support the hardware decoding of
H.264 video stream with Broadcom Crystal HD chips.

%package -n libcrystalhd3
Summary:        Broadcom Crystal HD device interface library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libcrystalhd3
This package contains the library to support the hardware decoding of
H.264 video stream with Broadcom Crystal HD chips.

%package -n libcrystalhd-devel
Summary:        Development package for libcrystalhd
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       libcrystalhd3 = %{version}-%{release}

%description -n libcrystalhd-devel
Development libraries needed to build applications with libcrystalhd.

%package -n crystalhd-firmware
Summary:        Firmware for the Broadcom Crystal HD video decoder
License:        SUSE-Firmware
Group:          Hardware/Other

%description -n crystalhd-firmware
Firmwares for the Broadcom Crystal HD video decoders.

%prep
%setup -n crystalhd-libs
%patch0
%patch1
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
export CXXFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install LIBDIR=%{_libdir} FIRMWAREDIR="%{_firmwaredir}"

%post -n libcrystalhd3 -p /sbin/ldconfig
%postun -n libcrystalhd3 -p /sbin/ldconfig

%files -n libcrystalhd3
%{_libdir}/libcrystalhd.so.*

%files -n libcrystalhd-devel
%license LICENSE
%doc README*
%{_includedir}/libcrystalhd
%{_libdir}/libcrystalhd.so

%files -n crystalhd-firmware
%{_firmwaredir}/*

%changelog
