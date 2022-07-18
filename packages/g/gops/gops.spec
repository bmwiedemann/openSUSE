#
# spec file for package gops
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


%global provider        github
%global provider_tld    com
%global project         google
%global repo            gops
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           gops
Version:        0.3.25
Release:        0
Summary:        A tool to list and diagnose Go processes currently running on your system
License:        BSD-3-Clause-Clear
Group:          System/Monitoring
URL:            https://%{provider_prefix}
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.13

%description
gops is a command to list and diagnose Go processes currently running on your
system. For processes that starts the diagnostics agent, gops can report
additional information such as the current stack trace, Go version, memory stats,
etc. It is possible to use gops tool both in local and remote mode.

%prep
%autosetup -a 1

%build
go build \
   -mod=vendor \
   -v -p 4 -x \
%ifnarch ppc64 ppc64le riscv64
   -buildmode=pie \
%endif
   %{import_path}

%install
go install \
   -mod=vendor \
   -v -p 4 -x \
%ifnarch ppc64 ppc64le riscv64
   -buildmode=pie \
%endif
   %{import_path}
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
