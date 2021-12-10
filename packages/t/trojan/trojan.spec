#
# spec file for package trojan
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

Name:           trojan
Version:        1.16.0
Release:        0
Summary:        An unidentifiable mechanism that helps you bypass Internet censorship
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/trojan-gfw/trojan
Source0:        https://github.com/trojan-gfw/trojan/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  libboost_program_options-devel-impl >= 1.66.0
BuildRequires:  libboost_system-devel-impl >= 1.66.0
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

%description
Trojan features multiple protocols over TLS to avoid both active/passive
detections and ISP QoS limitations.

Trojan is not a fixed program or protocol. It's an idea, an idea that imitating
the most common service, to an extent that it behaves identically, could help
you get across the Great FireWall permanently, without being identified ever. We
are the GreatER Fire; we ship Trojan Horses.

%lang_package

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

install -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service %{name}@.service

%post
%service_add_post %{name}.service %{name}@.service

%preun
%service_del_preun %{name}.service %{name}@.service

%postun
%service_del_postun %{name}.service %{name}@.service

%files
%doc CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/config.json
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/*.service
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
