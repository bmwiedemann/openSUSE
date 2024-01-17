#
# spec file for package clash
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 Xu Zhao (i@xuzhao.net)
# Copyright (c) 2021 Orville Q. Song <orville@anislet.dev>
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


%global build_time      2022-01-03T14:57:41Z
# date -u +'%Y-%m-%dT%H:%M:%SZ'

%global provider        github
%global provider_tld    com
%global project         Dreamacro
%global repo            clash
%global provider_prefix %{provider}.%{provider_tld}/%{project}
%global import_path     %{provider_prefix}/%{repo}

Name:           clash
Version:        1.12.0
Release:        0
Summary:        A rule-based tunnel in Go
License:        GPL-3.0-only
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/Dreamacro/clash
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-vendor.tar.xz
Source2:        %{name}.yaml
Source3:        %{name}-system.service
Source4:        %{name}-user.service
BuildRequires:  golang-packaging
BuildRequires:  golang(API) > 1.16

%{go_nostrip}
%{go_provides}

%description
Clash is a rule-based tunnel in Go.

%prep
%setup -q -n %{name}-%{version}
%setup -a1 %{SOURCE1}

%build
%goprep .
mkdir -p vendor/%{provider_prefix}
ln -s . vendor/%{import_path}
%gobuild -ldflags "-s -w -X github.com/Dreamacro/clash/constant.Version=v%{version} -X github.com/Dreamacro/clash/constant.BuildTime=%{build_time}" .

%install
%goinstall

# Default config file
install -D -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/config.yaml
# System Services
install -D -m0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
# User Services
install -D -m0644 %{SOURCE4} %{buildroot}%{_userunitdir}/%{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%systemd_user_post %{name}.service

%preun
%service_del_preun %{name}.service
%systemd_user_preun %{name}.service

%postun
%service_del_postun %{name}.service
%systemd_user_postun %{name}.service

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/config.yaml
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service
%{_bindir}/%{name}

%changelog
