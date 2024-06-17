#
# spec file for package google-osconfig-agent
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


%global provider        github
%global provider_tld    com
%global project         GoogleCloudPlatform
%global repo            osconfig
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           google-osconfig-agent
Version:        20240607.00
Release:        0
Summary:        Google Cloud Guest Agent
License:        Apache-2.0
Group:          System/Daemons
URL:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        rpmlintrc
BuildRequires:  golang(API) = 1.21
BuildRequires:  golang-packaging
Requires:       google-guest-configs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build



%{go_nostrip}
%{go_provides}

%description
Google Cloud OSConfig Agent

%prep
%setup -q -n %{repo}-%{version}
%setup -q -D -T -a 1 -n %{repo}-%{version}

%build
%goprep %{import_path}
CGO_ENABLED=0 go build -ldflags="-s -w -X main.version=%{version}-%{release}" -mod=vendor -o google_osconfig_agent

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}/etc/osconfig
install -p -m 0755 google_osconfig_agent %{buildroot}%{_bindir}/google_osconfig_agent
install -d %{buildroot}%{_unitdir}
install -p -m 0644 %{name}.service %{buildroot}%{_unitdir}
for srv_name in %{buildroot}%{_unitdir}/*.service; do rc_name=$(basename -s '.service' $srv_name); ln -s service %{buildroot}%{_sbindir}/rc$rc_name; done

%pre
    %service_add_pre google-osconfig-agent.service

%preun
    %service_del_preun google-osconfig-agent.service

%post
    %service_add_post google-osconfig-agent.service

    if [ "$1" = "2" ] && ! [ -e /.buildenv ]; then
      # If the old directory exists make sure we set the file there.
      [ -e %{_sysconfdir}/osconfig ] && touch %{_sysconfdir}/osconfig/osconfig_agent_restart_required
      install -D /dev/null %{_var}/lib/google_osconfig_agent/osconfig_agent_restart_required
    fi

%postun
    %service_del_postun_without_restart google-osconfig-agent.service

%files
%defattr(0644,root,root,0755)
%doc README.md
%license LICENSE THIRD_PARTY_LICENSES
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%{_unitdir}/%{name}.service

%changelog
