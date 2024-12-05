#
# spec file for package rustdesk-server
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


Name:           rustdesk-server
Version:        1.1.12
Release:        0
Summary:        RustDesk Server Program
License:        AGPL-3.0-only
URL:            https://github.com/rustdesk/rustdesk-server
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        rustdesk-server.sysusers
Source3:        hbbr.service
Source4:        hbbs.service
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.70
BuildRequires:  sysuser-tools
Requires:       %{name}-hbbr == %{version}
Requires:       %{name}-hbbs == %{version}
Requires:       %{name}-utils == %{version}
Requires:       system-user-rustdesk == %{version}

%package -n system-user-rustdesk
Summary:        System user for rustdesk-server
BuildArch:      noarch
%{sysusers_requires}

%description -n system-user-rustdesk
%summary.

%package hbbr
Summary:        Relay Server for Rustdesk
Requires:       system-user-rustdesk == %{version}

%description hbbr
This package only contains the Relay Server part.

%package hbbs
Summary:        Signal Server for Rustdesk
Requires:       system-user-rustdesk == %{version}

%description hbbs
This package only contains the Signal Server part.

%package utils
Summary:        Utilities for Rustdesk

%description utils
the utilities for Rustdesk Server

%description
Self-host your own RustDesk server.

%prep
%autosetup -a1

%build
%sysusers_generate_pre %{SOURCE2} system-user-rustdesk system-user-rustdesk.conf
%{cargo_build}

%install
%{cargo_install} --frozen
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/system-user-rustdesk.conf
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_unitdir}/hbbr.service
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/hbbs.service
mkdir -p %{buildroot}/var/lib/%{name}

%pre -n system-user-rustdesk -f system-user-rustdesk.pre

%pre hbbr
%service_add_pre hbbr.service

%pre hbbs
%service_add_pre hbbs.service

%post hbbr
%service_add_post hbbr.service

%post hbbs
%service_add_post hbbs.service

%preun hbbr
%systemd_preun hbbr.service

%preun hbbs
%systemd_preun hbbs.service

%postun hbbr
%service_del_postun_with_restart hbbr.service

%postun hbbs
%service_del_postun_with_restart hbbs.service

%files
%license LICENSE
%doc README.md README-DE.md README-NL.md

%files -n system-user-rustdesk
%{_sysusersdir}/system-user-rustdesk.conf
%defattr(644,rustdesk,rustdesk,775)
%{_sharedstatedir}/%{name}

%files hbbr
%{_bindir}/hbbr
%{_unitdir}/hbbr.service

%files hbbs
%{_bindir}/hbbs
%{_unitdir}/hbbs.service

%files utils
%{_bindir}/rustdesk-utils

%changelog
