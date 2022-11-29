#
# spec file for package accel-config
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


%define pkg_libname libaccel-config1
%define src_name idxd-config-accel-config-v%{version}
Name:           accel-config
Version:        3.5.0
Release:        0
Summary:        Configure accelerator subsystem devices
License:        GPL-2.0-only
URL:            https://github.com/intel/idxd-config
Source:         %{url}/archive/accel-config-v%{version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(uuid)
Requires:       %{pkg_libname} = %{version}-%{release}
ExclusiveArch:  x86_64

%description
Utility library and command-line tool for configuring the Intel
Data Streaming Accelerator (DSA) and Intel Analytics Accelerator
(IAX).

%package -n %{name}-devel
Summary:        Development files for libaccfg
License:        LGPL-2.1-only
Requires:       %{pkg_libname} = %{version}-%{release}

%description -n %{name}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{pkg_libname}
Summary:        Configuration library for accelerator subsystem devices
License:        LGPL-2.1-only
Requires:       kmod(idxd.ko)

%description -n %{pkg_libname}
Libraries for %{name}.

%prep
%setup -q -n %{src_name}

%build
echo %{version} > version
./autogen.sh
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{pkg_libname} -p /sbin/ldconfig
%postun -n %{pkg_libname} -p /sbin/ldconfig

%files
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses LICENSE_GPL_2_0
%{_bindir}/accel-config
%{_mandir}/man1/accel-config*
%dir %{_sysconfdir}/accel-config
%dir %{_sysconfdir}/accel-config/contrib
%dir %{_sysconfdir}/accel-config/contrib/configs
%config %{_sysconfdir}/accel-config/contrib/configs/app_profile.conf
%config %{_sysconfdir}/accel-config/contrib/configs/net_profile.conf
%config %{_sysconfdir}/accel-config/contrib/configs/os_profile.conf
%config %{_sysconfdir}/accel-config/contrib/configs/profilenote.txt
%config %{_sysconfdir}/accel-config/contrib/configs/storage_profile.conf

%files -n %{pkg_libname}
%doc README.md
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/libaccel-config-licenses accfg/lib/LICENSE_LGPL_2_1
%{_libdir}/libaccel-config.so.*

%files -n %{name}-devel
%license Documentation/COPYING
%{_includedir}/accel-config/
%{_libdir}/libaccel-config.so
%{_libdir}/pkgconfig/libaccel-config.pc

%changelog
