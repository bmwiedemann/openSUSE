#
# spec file for package iwd
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


Name:           iwd
Version:        2.0
Release:        0
Summary:        Wireless daemon for Linux
License:        LGPL-2.1-or-later
URL:            https://git.kernel.org/pub/scm/network/wireless/iwd.git
Source:         https://kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.xz
Source1:        https://kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.sign
# https://kernel.org/doc/wot/holtmann.html
Source2:        %{name}.keyring
# needed for the tests to generate certificates
# BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ell) >= 0.54
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
The iNet Wireless Daemon (iwd) project provides a wireless
connectivity solution. It attempts to optimise resource utilisation
of storage, runtime memory and link-time costs. It utilises the
features provided by the Linux kernel.

%prep
%autosetup -p1

%build
%configure \
    --libexecdir=%{_libexecdir}/%{name} \
    --enable-external-ell \
    %{nil}
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sbindir}/
ln -s service %{buildroot}%{_sbindir}/rc%{name}

# kernel-obs-build is missing af_alg.ko currently and the tests
# use -Wl,--wrap, incompatible with LTO (https://gcc.gnu.org/bugzilla/show_bug.cgi?id=88643)
#%%check
#%%make_build check

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
%doc AUTHORS ChangeLog README
%{_bindir}/iwctl
%{_bindir}/iwmon
%{_sbindir}/rc%{name}
%{_libexecdir}/%{name}/
%dir %{_prefix}/lib/modules-load.d/
%{_prefix}/lib/modules-load.d/pkcs8.conf
%dir %{_prefix}/lib/systemd/network
%{_prefix}/lib/systemd/network/80-iwd.link
%{_unitdir}/%{name}.service
%dir %{_datadir}/dbus-1/system.d/
%{_datadir}/dbus-1/system.d/%{name}*.conf
%{_datadir}/dbus-1/system-services/*%{name}.service
%{_mandir}/man1/iwctl.1%{?ext_man}
%{_mandir}/man1/iwmon.1%{?ext_man}
%{_mandir}/man5/iwd.config.5%{?ext_man}
%{_mandir}/man5/iwd.network.5%{?ext_man}
%{_mandir}/man5/iwd.ap.5%{?ext_man}
%{_mandir}/man7/iwd.debug.7%{?ext_man}
%{_mandir}/man8/iwd.8%{?ext_man}

%changelog
