#
# spec file for package ledmon
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


Name:           ledmon
Version:        1.1.0
Release:        0
Summary:        Enclosure LED Utilities
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/intel/ledmon/
Source0:        https://github.com/intel/ledmon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         harden_ledmon.service.patch
Patch1:         260.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  libsgutils-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
Provides:       sgpio:/sbin/ledmon
Provides:       sgpio:/{%{_bindir}}/ledctl
%{?systemd_requires}

%description
The ledctl application and ledmon daemon are part of Intel(R) LED
ControlUtilities. They help to enable LED management for software RAID
solutions.

%package -n libled1
Summary:        Enclosure LED Control Library
License:        LGPL-2.1-or-later

%description -n libled1
libled enable enclosure LED control for applications.

%package devel
Summary:        Document and Include Files for Enclosure LED Control Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libled1 = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains the files that are necessary for software development
using libled.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
autoreconf -fiv
%configure \
  --enable-systemd=yes \
  --enable-library=yes
%make_build

%install
%make_install
ln -sv %{_sbindir}/service \
  %{buildroot}%{_sbindir}/rc%{name}
rm %{buildroot}%{_datarootdir}/doc/ledmon/README.md
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f -name "*.la" -delete -print

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%ldconfig_scriptlets -n libled1

%files
%license COPYING
%doc README.md
%{_sbindir}/ledmon
%{_sbindir}/ledctl
%{_sbindir}/rcledmon
%{_unitdir}/ledmon.service
%{_mandir}/man5/ledmon.conf.5%{?ext_man}
%{_mandir}/man8/ledctl.8%{?ext_man}
%{_mandir}/man8/ledmon.8%{?ext_man}

%files -n libled1
%license COPYING.LIB
%{_libdir}/libled.so.1
%{_libdir}/libled.so.1.*

%files devel
%license COPYING.LIB
%doc src/lib/LIBRARY.md
%dir %{_includedir}/led/
%{_includedir}/led/libled.h
%{_libdir}/libled.so
%{_libdir}/pkgconfig/ledmon.pc

%changelog
