#
# spec file for package accel-config
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


%define pkg_libname libaccel-config1

Name:           accel-config
Version:        3.1
Release:        0
Summary:        Configure accelerator subsystem devices
License:        GPL-2.0-only
URL:            https://github.com/intel/idxd-config
Source:         https://github.com/intel/idxd-config/archive/accel-config-v%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  xmlto
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(uuid)
Requires:       %{pkg_libname} = %{version}-%{release}
ExclusiveArch:  x86_64 i586

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
%setup -q -n idxd-config-accel-config-v%{version}

%build
echo %{version} > version
./autogen.sh
%configure
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -n %{pkg_libname} -p /sbin/ldconfig

%postun -n %{pkg_libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses LICENSE_GPL_2_0
%{_bindir}/accel-config
%{_mandir}/man1/accel-config*
%dir %{_sysconfdir}/accel-config
%config %{_sysconfdir}/accel-config/accel-config.conf.sample

%files -n %{pkg_libname}
%defattr(-,root,root)
%doc README.md
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/libaccel-config-licenses accfg/lib/LICENSE_LGPL_2_1
%{_libdir}/libaccel-config.so.*

%files -n %{name}-devel
%defattr(-,root,root)
%license Documentation/COPYING
%{_includedir}/accel-config/
%{_libdir}/libaccel-config.so
%{_libdir}/pkgconfig/libaccel-config.pc

%changelog
