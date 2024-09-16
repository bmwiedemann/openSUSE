#
# spec file for package gitopper
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           gitopper
Version:        0.0.20
Release:        0
Summary:        Gitops for non-Kubernetes folks
License:        Apache-2.0
URL:            https://github.com/miekg/gitopper
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
Gitopper is GitOps for non-Kubernetes folks it watches a remote git repo, pulls
changes and HUP the server (service) process.

A sparse (but with full history) git checkout will be done, so each service
will only see the files it will actually need. Several bind mounts are then
setup to give the service access to the file(s) in Git. If the target
directories don't exist, they will be created, with the current user - if
specified.

This tool does little more than just pull the repo, but the little it brings to
the table allows for a GitOps workflow without resorting to Kubernetes like
environments.

The Git repository that you are using to provision the services must have at
least one (sub)directory for each service.

Gitopper will install packages if told to do so. It will not upgrade or
downgrade them, assuming there is a better way of doing those.

The remote interface of gitopper uses SSH keys for authentication, this
hopefully helps to fit in, in a sysadmin organisation.

The following features are implemented:

* Metrics: are included see below, they export a Git hash, so a rollout can be
  tracked.
* Diff detection: possible using the metrics or gitopperctl.
* Out of band rollbacks: use gitopperctl to bypass the normal Git workflow.
* No client side processing: files are used as they are in the Git repo.
* Canarying: give a service a different branch to check out.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# server systemd unit file
install -D -m 0644 ./gitopper.service %{buildroot}%{_unitdir}/%{name}.service

# configuration in /etc/openbao/
install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}/

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %attr(750,root,root) %{_sysconfdir}/%{name}/

%changelog
