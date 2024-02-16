#
# spec file for package golang-github-prometheus-promu
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


%define shortname promu

Name:           golang-github-prometheus-promu
Version:        0.15.0
Release:        0
Summary:        Prometheus Utility Tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/prometheus/promu
Source:         %{shortname}-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-UPSTREAM Fix setting reproducible user and host during the build
# https://github.com/prometheus/promu/pull/267
Patch1:         0001-do_not_discover_user_host_for_reproducible_builds.patch
# PATCH-FIX-OPENSUSE Do not pass -static to external linker by default
Patch2:         extldflags-no-static.patch
ExcludeArch:    s390
%if 0%{?rhel}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
BuildRequires:  golang >= 1.19
%else
BuildRequires:  golang(API) >= 1.19
%endif

%description
The Prometheus Utility Tool is used by the Prometheus project to build other components.

%prep
%autosetup -a1 -p1 -n %{shortname}-%{version}

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
# execute the binary as a basic check
./%{shortname} --help

%install
install -D -m 0755 %{shortname} "%{buildroot}/%{_bindir}/%{shortname}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{shortname}

%changelog
