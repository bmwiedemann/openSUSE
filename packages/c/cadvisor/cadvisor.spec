#
# spec file for package cadvisor
#
# Copyright (c) 2022 SUSE LLC
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
# nodebuginfo


%global goipath github.com/google/cadvisor
Name:           cadvisor
Version:        0.46.0
Release:        0
Summary:        A Simple and Comprehensive Vulnerability Scanner for Containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/google/cadvisor
Source:         %{name}-%{version}.tar.zst
Source1:        vendor-cmd.tar.zst
Source2:        cadvisor.service
Source3:        sysconfig.cadvisor
BuildRequires:  golang(API) = 1.19
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  zstd
Requires:       ca-certificates
Requires:       git-core
Requires:       rpm
Requires(post): %fillup_prereq

%description
Trivy (`tri` pronounced like trigger, `vy` pronounced like envy) is a simple and
comprehensive vulnerability scanner for containers and other artifacts. A
software vulnerability is a glitch, flaw, or weakness present in the software or
in an Operating System. Trivy detects vulnerabilities of OS packages (Alpine,
RHEL, CentOS, etc.) and application dependencies (Bundler, Composer, npm, yarn,
etc.). Trivy is easy to use. Just install the binary and you're ready to
scan. All you need to do for scanning is to specify a target such as an image
name of the container.

%prep
%setup -qa1
%autopatch -p1

%build
%{goprep} %{goipath}

pushd cmd
%{gobuild} -tags netgo -ldflags '-X github.com/google/cadvisor/version.Version=%{version}' ./cmd
popd

%install
%{goinstall}
mv %{buildroot}%{_bindir}/{cmd,cadvisor}

#
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}


%pre
%service_add_pre cadvisor.service

%post
%service_add_post cadvisor.service
%{fillup_only -n cadvisor}

%preun
%service_del_preun cadvisor.service

%postun
%service_del_postun cadvisor.service

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/cadvisor
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}

%changelog
