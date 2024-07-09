#
# spec file for package amazon-ssm-agent
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


Name:           amazon-ssm-agent
Version:        3.3.551.0
Release:        0
Summary:        Amazon Remote System Config Management
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/aws/amazon-ssm-agent
Source0:        https://github.com/aws/amazon-ssm-agent/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go >= 1.21
BuildRequires:  pkgconfig(systemd)
Requires:       systemd
Provides:       bundled(golang(github.com/Microsoft/go-winio))
Provides:       bundled(golang(github.com/Workiva/go-datastructures))
Provides:       bundled(golang(github.com/aws/aws-sdk-go))
Provides:       bundled(golang(github.com/carlescere/scheduler))
Provides:       bundled(golang(github.com/cenkalti/backoff))
Provides:       bundled(golang(github.com/cihub/seelog))
Provides:       bundled(golang(github.com/coreos/go-semver))
Provides:       bundled(golang(github.com/creack/pty))
Provides:       bundled(golang(github.com/davecgh/go-spew))
Provides:       bundled(golang(github.com/emirpasic/gods))
Provides:       bundled(golang(github.com/fsnotify/fsnotify))
Provides:       bundled(golang(github.com/gabs))
Provides:       bundled(golang(github.com/go-git/gcfg))
Provides:       bundled(golang(github.com/go-git/go-billy))
Provides:       bundled(golang(github.com/go-git/go-git))
Provides:       bundled(golang(github.com/go-github))
Provides:       bundled(golang(github.com/go-ini/ini))
Provides:       bundled(golang(github.com/go-yaml/yaml))
Provides:       bundled(golang(github.com/google/go-querystring))
Provides:       bundled(golang(github.com/google/shlex))
Provides:       bundled(golang(github.com/gorhill/cronexpr))
Provides:       bundled(golang(github.com/gorilla/websocket))
Provides:       bundled(golang(github.com/hectane/go-acl))
Provides:       bundled(golang(github.com/imdario/mergo))
Provides:       bundled(golang(github.com/jbenet/go-context))
Provides:       bundled(golang(github.com/jmespath/go-jmespath))
Provides:       bundled(golang(github.com/kevinburke/ssh_config))
Provides:       bundled(golang(github.com/lsegal/gucumber))
Provides:       bundled(golang(github.com/mitchellh/go-homedir))
Provides:       bundled(golang(github.com/mitchellh/go-ps))
Provides:       bundled(golang(github.com/nightlyone/lockfile))
Provides:       bundled(golang(github.com/pborman/ansi))
Provides:       bundled(golang(github.com/pmezard/go-difflib))
Provides:       bundled(golang(github.com/sergi/go-diff))
Provides:       bundled(golang(github.com/shiena/ansicolor))
Provides:       bundled(golang(github.com/stretchr/objx))
Provides:       bundled(golang(github.com/stretchr/testify))
Provides:       bundled(golang(github.com/twinj/uuid))
Provides:       bundled(golang(github.com/xanzy/ssh-agent))
Provides:       bundled(golang(github.com/xtaci/smux))
Provides:       bundled(golang(go.nanomsg.org/mangos))
Provides:       bundled(golang(golang.org/x/crypto))
Provides:       bundled(golang(golang.org/x/net))
Provides:       bundled(golang(golang.org/x/oauth2))
Provides:       bundled(golang(golang.org/x/sync))
Provides:       bundled(golang(golang.org/x/sys))
Provides:       bundled(golang(gopkg.in/warnings.v0))

ExclusiveArch:  aarch64 x86_64

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
sed -i -e 's#const[ \s]*Version.*#const Version = "%{version}"#g' agent/version/version.go
sed -i 's#/bin/#/sbin/#' packaging/linux/amazon-ssm-agent.service
sed -i 's#var defaultWorkerPath = "/usr/bin/"#var defaultWorkerPath = "/usr/sbin/"#' agent/appconfig/constants_unix.go

%build
export GO111MODULE="auto"
cp -r Tools agent common core internal packaging vendor src

PKG_ROOT=`pwd`
GOPATH=${PKG_ROOT}/vendor:${PKG_ROOT}
ln -s ${PKG_ROOT} ${PKG_ROOT}/vendor/github.com/aws/aws-sdk-go
export GOPATH

CGO_ENABLED=0 go build -ldflags "-s -w -extldflags=-Wl,-z,now,-z,relro,-z,defs" -buildmode=pie -o bin/amazon-ssm-agent -v core/agent.go core/agent_unix.go core/agent_parser.go
CGO_ENABLED=0 go build -ldflags "-s -w -extldflags=-Wl,-z,now,-z,relro,-z,defs" -buildmode=pie -o bin/ssm-agent-worker -v agent/agent.go agent/agent_unix.go agent/agent_parser.go
CGO_ENABLED=0 go build -ldflags "-s -w -extldflags=-Wl,-z,now,-z,relro,-z,defs" -buildmode=pie -o bin/ssm-document-worker -v agent/framework/processor/executer/outofproc/worker/main.go
CGO_ENABLED=0 go build -ldflags "-s -w -extldflags=-Wl,-z,now,-z,relro,-z,defs" -buildmode=pie -o bin/ssm-session-worker -v agent/framework/processor/executer/outofproc/sessionworker/main.go
CGO_ENABLED=0 go build -ldflags "-s -w -extldflags=-Wl,-z,now,-z,relro,-z,defs" -buildmode=pie -o bin/ssm-session-logger -v agent/session/logging/main.go
CGO_ENABLED=0 go build -ldflags "-s -w -extldflags=-Wl,-z,now,-z,relro,-z,defs" -buildmode=pie -o bin/ssm-cli -v agent/cli-main/cli-main.go

%install
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/amazon/ssm
install -d -m 755 %{buildroot}%{_localstatedir}/log/amazon/ssm
install -d -m 755 %{buildroot}%{_localstatedir}/lib/amazon/ssm
install -m 755 bin/amazon-ssm-agent %{buildroot}%{_sbindir}
install -m 755 bin/ssm-agent-worker %{buildroot}%{_sbindir}
install -m 755 bin/ssm-cli %{buildroot}%{_sbindir}
install -m 755 bin/ssm-document-worker %{buildroot}%{_sbindir}
install -m 755 bin/ssm-session-worker %{buildroot}%{_sbindir}
install -m 755 bin/ssm-session-logger %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_unitdir}
cp seelog_unix.xml %{buildroot}%{_sysconfdir}/amazon/ssm/seelog.xml.template
cp amazon-ssm-agent.json.template %{buildroot}%{_sysconfdir}/amazon/ssm/
install -m 644 packaging/linux/amazon-ssm-agent.service %{buildroot}%{_unitdir}

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/amazon
%dir %{_sysconfdir}/amazon/ssm
%dir %{_localstatedir}/log/amazon
%dir %{_localstatedir}/lib/amazon
%license LICENSE
%doc CONTRIBUTING.md NOTICE.md README.md RELEASENOTES.md
%config(noreplace) %{_sysconfdir}/amazon/ssm/amazon-ssm-agent.json.template
%config(noreplace) %{_sysconfdir}/amazon/ssm/seelog.xml.template
%{_sbindir}/*
%{_unitdir}/%{name}.service
%{_localstatedir}/lib/amazon/ssm
%ghost %{_localstatedir}/log/amazon/ssm/

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%changelog
