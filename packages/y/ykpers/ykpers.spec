#
# spec file for package ykpers
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


Name:           ykpers
Version:        1.20.0
Release:        0
Summary:        Reference implementation for configuration of YubiKeys
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
URL:            https://developers.yubico.com/yubikey-personalization/
Source0:        https://developers.yubico.com/yubikey-personalization/Releases/ykpers-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubikey-personalization/Releases/ykpers-%{version}.tar.gz.sig
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM ykpers-json.patch gh#Yubico/yubikey-personalization#159
Patch0:         ykpers-json.patch
BuildRequires:  libyubikey-devel >= 1.12
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c) >= 0.10
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)
Provides:       yubikey-personalization = %{version}

%description
Yubico's YubiKey can be re-programmed. This project provides a reference implementation for configuration of YubiKeys.

%package    -n libykpers-1-1
Summary:        Reference implementation for configuration of YubiKeys
Group:          System/Libraries

%description -n libykpers-1-1
Yubico's YubiKey can be re-programmed. This project provides a reference implementation for configuration of YubiKeys.

%package -n libykpers-devel
Summary:        Development files for the ykpers library
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libykpers-1-1 = %{version}

%description -n libykpers-devel
Yubico's YubiKey can be re-programmed. This project provides a reference implementation for configuration of YubiKeys.

%prep
%autosetup
# Add access for group "users"
sed -i 's|--device=$env{DEVNAME}"|--device=$env{DEVNAME}" GROUP="users"|g' 70-yubikey.rules
# PATCH-FIX-UPSTREAM gh#Yubico/yubikey-personalization#155 -- Fix build with gcc 10
sed -i 's|^const char|extern const char|g' ykpers-args.h

%build
%configure --disable-static --with-pic \
    --with-udevrulesdir=%{_udevrulesdir} \
    --with-backend=libusb-1.0 --without-libusb-prefix
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post
%{?udev_rules_update:%udev_rules_update}

%post -n libykpers-1-1 -p /sbin/ldconfig
%postun -n libykpers-1-1 -p /sbin/ldconfig

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/*
%{_mandir}/man?/*
%{_udevrulesdir}/*-yubikey.rules

%files -n libykpers-1-1
%{_libdir}/libykpers-1.so.*

%files -n libykpers-devel
%dir %{_includedir}/ykpers-1
%{_includedir}/ykpers-1/*.h
%{_libdir}/pkgconfig/ykpers-1.pc
%{_libdir}/libykpers-1.so

%changelog
