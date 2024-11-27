#
# spec file for package libnvme
#
# Copyright (c) 2024 SUSE LLC
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

%bcond_without check

Name:           libnvme
Version:        1.11
Release:        0
Summary:        Linux-native nvme device management library
License:        LGPL-2.1-or-later
URL:            https://github.com/linux-nvme/libnvme/
Source0:        libnvme-%{version}.tar.gz
Patch01:        0001-linux-fix-derive_psk_digest-OpenSSL-1.1-version.patch
Patch02:        0002-test-mock-pass-thru-unknown-ioctls.patch
BuildRequires:  dbus-1-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  keyutils-devel
BuildRequires:  libjson-c-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  swig

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
Requires:       %{name}-mi%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        mi%{sover}
Summary:        NVMe Managament Interface library for %{name}

%description    mi%{sover}
Provides library functions for managing NVMe devices via the NVMe
Managament Interface.

%package -n     python3-libnvme
Summary:        Python binding for %{name}

%description -n python3-libnvme
Provides library functions for accessing and managing NVMe devices on a Linux
system.

Python binding part.

%prep
%autosetup -p1

%build
export KBUILD_BUILD_TIMESTAMP=@${SOURCE_DATE_EPOCH:-$(date +%s)}
%meson \
    -Ddocs=man \
    %{?_with_docs_build:-Ddocs-build=true} \
    -Dversion-tag=%{version} \
    -Dlibdbus=enabled
%meson_build

%if %{with check}
%check
%meson_test
%endif

%install
%meson_install

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%post -n %{name}-mi%{sover} -p /sbin/ldconfig
%postun -n %{name}-mi%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.%{sover}*

%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-mi.pc
%{_mandir}/*/*.gz

%files -n %{name}-mi%{sover}
%license COPYING
%doc README.md
%{_libdir}/%{name}-mi.so.%{sover}*

%files -n python3-libnvme
%{python3_sitearch}/*

%changelog
