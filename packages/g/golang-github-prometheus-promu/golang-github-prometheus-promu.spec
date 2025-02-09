#
# spec file for package golang-github-prometheus-promu
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


%if 0%{?rhel}
%global debug_package %{nil}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
%endif

%define shortname promu

Name:           golang-github-prometheus-promu
Version:        0.17.0
Release:        0
Summary:        Prometheus Utility Tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/prometheus/promu
Source:         %{shortname}-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE Do not pass -static to external linker by default
Patch2:         extldflags-no-static.patch
ExcludeArch:    s390
%if 0%{?rhel}
BuildRequires:  golang >= 1.21
%else
BuildRequires:  golang(API) >= 1.21
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
%if 0%{?rhel}
rm -f %{buildroot}/usr/lib/debug%{_bindir}/%{shortname}*.debug
rm -rf %{buildroot}/usr/lib/debug/.build-id/*
rm -rf %{buildroot}%{_usrsrc}/debug/%{name}-%{version}-*
%endif

%install
install -D -m 0755 %{shortname} "%{buildroot}/%{_bindir}/%{shortname}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{shortname}

%changelog
