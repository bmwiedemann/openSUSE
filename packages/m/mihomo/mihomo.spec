#
# spec file for package mihomo
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           mihomo
Version:        1.19.29
Release:        0
Summary:        The universal proxy platform
License:        GPL-3.0-only
URL:            https://github.com/MetaCubeX/mihomo
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        config.yaml
Source3:        %{name}.service
Source4:        start.sh
BuildRequires:  golang(API) >= 1.20
BuildRequires:  golang-packaging
Requires:       bash
# mihomo is the maintained successor to clash (the original Dreamacro/clash was
# archived; its final release was 1.18.0) and to the former Clash.Meta
Provides:       clash = %{version}
Obsoletes:      clash < %{version}
Provides:       clash-meta = %{version}
Obsoletes:      clash-meta < %{version}

%description
mihomo (formerly Clash.Meta) is a rule-based tunnel / universal proxy platform
written in Go. It is the actively maintained successor to the original clash.

%prep
%autosetup -a1

%build
# reproducible BuildTime from the changelog-derived SOURCE_DATE_EPOCH
build_time="$(date -u -d "@${SOURCE_DATE_EPOCH:-0}" +'%%Y-%%m-%%dT%%H:%%M:%%SZ')"
go build -trimpath -buildmode=pie \
    -ldflags "-X github.com/metacubex/mihomo/constant.Version=v%{version} \
              -X github.com/metacubex/mihomo/constant.BuildTime=${build_time}" \
    -tags with_gvisor -o %{name}

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/config.yaml
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0755 %{SOURCE4} %{buildroot}%{_libexecdir}/%{name}/start

%check
%{buildroot}%{_bindir}/%{name} -v

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.yaml
%{_unitdir}/%{name}.service
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/start
%{_bindir}/%{name}

%changelog
