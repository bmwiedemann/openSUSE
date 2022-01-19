#
# spec file for package libnvme
#
# Copyright (c) 2022 SUSE LLC
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

%define sover 1

Name:           libnvme
Version:        1.0~0
Release:        0
Summary:        Linux-native nvme device management library
License:        LGPL-2.1
URL:            https://github.com/linux-nvme/libnvme/
Source0:        libnvme-%{version}.tar.gz
BuildRequires:  meson >= 0.47.0
BuildRequires:  gcc gcc-c++ make
BuildRequires:  libuuid-devel
BuildRequires:  libjson-c-devel
BuildRequires:  openssl-devel
BuildRequires:  swig
BuildRequires:  python3-devel
BuildRequires:  python3-Sphinx

%description
Provides library functions for accessing and managing NVMe devices on a Linux
system.

%package -n %{name}%{sover}
Summary:        Linux-native nvme device management library

%description -n %{name}%{sover}
Provides library functions for accessing and managing NVMe devices on a Linux
system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	python3-libnvme
Summary:        Python binding for %{name}

%description -n python3-libnvme
Provides library functions for accessing and managing NVMe devices on a Linux
system.

Python binding part.

%prep
%autosetup -p1

%build
%meson \
    -Dman=true
%meson_build

%install
%meson_install

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.%{sover}*

%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/*/*

%files -n python3-libnvme
%{python3_sitearch}/libnvme
%{python3_sitearch}/libnvme/*.so
%{python3_sitearch}/libnvme/__init__.py
%{python3_sitearch}/libnvme/nvme.py

%changelog
