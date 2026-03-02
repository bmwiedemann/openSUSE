#
# spec file for package amazon-cloudwatch-agent
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

%global provider        github
%global provider_tld    com
%global project         aws
%global repo            amazon-cloudwatch-agent
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           amazon-cloudwatch-agent
Version:        1.300064.0
Release:        0
Summary:        Amazon CloudWatch Agent
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/aws/amazon-cloudwatch-agent
Source0:        %{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.23.6
BuildRequires:  golang-packaging
ExcludeArch:    %{arm} %{ix86}

%{go_nostrip}
%{go_provides}

%description
CloudWatch Agent enables you to collect and export host-level
metrics and logs on instances running Linux or Windows server.

%prep
%setup -q -n %{repo}-%{version}
%setup -q -D -T -a 1 -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild -buildmode=pie -mod=vendor ""...
cp licensing/THIRD-PARTY-LICENSES .

%install
install -Dm 755 %{_builddir}/go/bin/amazon-cloudwatch-agent %{buildroot}%{_bindir}/amazon-cloudwatch-agent
install -Dm 755 %{_builddir}/go/bin/amazon-cloudwatch-agent-config-wizard %{buildroot}%{_bindir}/amazon-cloudwatch-agent-config-wizard
install -Dm 755 packaging/dependencies/amazon-cloudwatch-agent-ctl %{buildroot}%{_bindir}/amazon-cloudwatch-agent-ctl
install -Dm 755 %{_builddir}/go/bin/config-downloader %{buildroot}%{_bindir}/config-downloader
install -Dm 755 %{_builddir}/go/bin/config-translator %{buildroot}%{_bindir}/config-translator
install -Dm 755 %{_builddir}/go/bin/start-amazon-cloudwatch-agent %{buildroot}%{_bindir}/start-amazon-cloudwatch-agent
install -Dm 755 %{_builddir}/go/bin/xray-migration %{buildroot}%{_bindir}/xray-migration
install -Dm 644 packaging/dependencies/amazon-cloudwatch-agent.service %{buildroot}%{_unitdir}/%{name}.service
# Fix path of start-amazon-cloudwatch-agent binary in service file
sed -i 's/\/opt\/aws\/amazon-cloudwatch-agent/\/usr/g' %{buildroot}%{_unitdir}/%{name}.service

%pre
    %service_add_pre amazon-cloudwatch-agent.service

%preun
    %service_del_preun amazon-cloudwatch-agent.service

%post
    %service_add_post amazon-cloudwatch-agent.service

%postun
    %service_del_postun_without_restart amazon-cloudwatch-agent.service

%files
%doc NOTICE RELEASE_NOTES
%license LICENSE THIRD-PARTY-LICENSES
%{_bindir}/amazon-cloudwatch-agent
%{_bindir}/amazon-cloudwatch-agent-config-wizard
%{_bindir}/amazon-cloudwatch-agent-ctl
%{_bindir}/config-downloader
%{_bindir}/config-translator
%{_bindir}/start-amazon-cloudwatch-agent
%{_bindir}/xray-migration

%{_unitdir}/%{name}.service

%changelog
