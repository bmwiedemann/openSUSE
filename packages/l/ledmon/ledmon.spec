#
# spec file for package ledmon
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


Name:           ledmon
Version:        0.94
Release:        0
Summary:        Enclosure LED Utilities
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/intel/ledmon/
Source0:        https://github.com/intel/ledmon/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libsgutils-devel
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

%prep
%autosetup

%build
%define _lto_cflags %{nil}
autoreconf -fiv
%configure \
  --enable-systemd=yes
%make_build

%install
%make_install
ln -sv %{_sbindir}/service \
  %{buildroot}%{_sbindir}/rc%{name}
rm %{buildroot}%{_datarootdir}/doc/ledmon/README

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc README
%{_sbindir}/ledmon
%{_sbindir}/ledctl
%{_sbindir}/rcledmon
%{_unitdir}/ledmon.service
%{_mandir}/man5/ledmon.conf.5.5%{?ext_man}
%{_mandir}/man8/ledctl.8.8%{?ext_man}
%{_mandir}/man8/ledmon.8.8%{?ext_man}

%changelog
