#
# spec file for package lapdog
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           lapdog
Version:        1.1
Release:        0
Summary:        Take actions when specific devices appear/disappear from your LAN
License:        GPL-3.0+
Group:          Productivity/Networking/Other
URL:            https://github.com/ltworf/lapdog
Source0:        https://github.com/ltworf/lapdog/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM lapdog-1.1-pass_cxxflags.patch -- include flags passed via command line -- aloisio@gmx.com
Patch0:         lapdog-1.1-pass_cxxflags.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(liboping)
%{?systemd_requires}

%description
lapdog is a service that monitors the presence/absence of the devices
on your LAN and executes some actions accordingly.

It pings the devices to discover if they are connected or not.
And uses their MAC address and not their IP, so it works on networks
with DHCP.

%prep
%setup -q
%patch0 -p1
sed -e '/CHANGELOG/d' -e '/init.d/d' \
    -e 's|/lib/systemd/system/|%{_unitdir}|' -i CMakeLists.txt

%build
%cmake
%make_jobs

%install
%cmake_install
pushd %{buildroot}/%{_sbindir}
ln -s service rc%{name}
popd

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc CHANGELOG CREDITS README.md
%license LICENSE
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%config %{_sysconfdir}/%{name}.conf
%config %{_sysconfdir}/%{name}
%{_unitdir}/%{name}.service

%changelog
