#
# spec file for package amazon-ssm-agent
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


Name:           amazon-ssm-agent
Version:        2.3.1205.0
Release:        0
Summary:        Amazon Remote System Config Management
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/aws/amazon-ssm-agent
Source0:        https://github.com/aws/amazon-ssm-agent/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Patch1:         fix-config.patch
Patch2:         fix-version.patch
Patch3:         remove-unused-import.patch
BuildRequires:  go >= 1.7.4
BuildRequires:  pkgconfig(systemd)
Requires:       systemd
ExcludeArch:    s390

%description
This package provides the Amazon SSM Agent for managing EC2 Instances using
Amazon EC2 Systems Manager (SSM).

The SSM Agent runs on EC2 or on-premise instances and enables you to quickly
and easily execute remote commands or scripts against one or more instances.
When you execute a command, the agent on the instance processes the document
and configures the instance as specified.

This collection of capabilities helps you automate management tasks such as
collecting system inventory, applying operating system (OS) patches, automating
the creation of Amazon Machine Images (AMIs), and configuring operating systems
(OSs) and applications at scale. Systems Manager works with managed instances:
Amazon EC2 instances, or servers and virtual machines (VMs) in your on-premises
environment that are configured for Systems Manager.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -rf vendor/src/github.com/aws/aws-sdk-go/vendor/

mkdir -p src/github.com/aws/amazon-ssm-agent
mv Tools agent vendor makefile amazon-ssm-agent.json.template \
seelog_unix.xml packaging src/github.com/aws/amazon-ssm-agent/

PKG_ROOT=`pwd`/src/github.com/aws/amazon-ssm-agent
GOPATH=${PKG_ROOT}/vendor:`pwd`
export GOPATH

go build -ldflags "-s -w" -buildmode=pie -o bin/amazon-ssm-agent -v \
${PKG_ROOT}/agent/agent.go \
${PKG_ROOT}/agent/agent_unix.go \
${PKG_ROOT}/agent/agent_parser.go

go build -ldflags "-s -w" -buildmode=pie -o bin/ssm-cli -v \
${PKG_ROOT}/agent/cli-main/cli-main.go

go build -ldflags "-s -w" -buildmode=pie -o bin/ssm-document-worker -v \
${PKG_ROOT}/agent/framework/processor/executer/outofproc/worker/main.go

go build -ldflags "-s -w" -buildmode=pie -o bin/ssm-session-worker -v \
${PKG_ROOT}/agent/framework/processor/executer/outofproc/sessionworker/main.go

go build -ldflags "-s -w" -buildmode=pie -o bin/ssm-session-logger -v \
${PKG_ROOT}/agent/session/logging/main.go

%install
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/init
install -d -m 755 %{buildroot}%{_sysconfdir}/amazon/ssm
install -m 755 bin/amazon-ssm-agent %{buildroot}%{_sbindir}
install -m 755 bin/ssm-cli %{buildroot}%{_bindir}
install -m 755 bin/ssm-document-worker %{buildroot}%{_bindir}
install -m 755 bin/ssm-session-worker %{buildroot}%{_bindir}
install -m 755 bin/ssm-session-logger %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %SOURCE1 %{buildroot}%{_unitdir}

PKG_ROOT=`pwd`/src/github.com/aws/amazon-ssm-agent
cp ${PKG_ROOT}/seelog_unix.xml %{buildroot}%{_sysconfdir}/amazon/ssm/seelog.xml.template
cp ${PKG_ROOT}/amazon-ssm-agent.json.template %{buildroot}%{_sysconfdir}/amazon/ssm/
cp ${PKG_ROOT}/packaging/linux/amazon-ssm-agent.conf %{buildroot}%{_sysconfdir}/init/

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/init
%dir %{_sysconfdir}/amazon
%dir %{_sysconfdir}/amazon/ssm
%license LICENSE
%doc CONTRIBUTING.md NOTICE.md README.md
%config(noreplace) %{_sysconfdir}/init/amazon-ssm-agent.conf
%config(noreplace) %{_sysconfdir}/amazon/ssm/amazon-ssm-agent.json.template
%config(noreplace) %{_sysconfdir}/amazon/ssm/seelog.xml.template
%{_sbindir}/*
%{_bindir}/*
%{_unitdir}/%{name}.service

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%changelog
