#
# spec file for package wire
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?rhel} == 8
%global debug_package %{nil}
%endif

%if 0%{?rhel}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
%endif

Name:           wire
Version:        0.5.0
Release:        0
Summary:        Compile-time Dependency Injection for Go
License:        Apache-2.0
Group:          Development/Languages/Go
URL:            https://github.com/google/wire
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
%if 0%{?sle_version} == 150300
# Needed due to bsc#1203599
BuildRequires:  golang(API) = 1.18
%else
BuildRequires:  golang(API) >= 1.19
%endif
%{?systemd_ordering}
ExcludeArch:    s390

%description
Wire is a code generation tool that automates connecting components using
dependency injection. Dependencies between components are represented in Wire
as function parameters, encouraging explicit initialization instead of global
variables. Because Wire operates without runtime state or reflection, code
written to be used with Wire is useful even for hand-written initialization.

%prep
%autosetup -a1 -n %{name}-%{version}

%build
%goprep github.com/google/wire
%gobuild -mod=vendor "" ...

%install
%goinstall

%if 0%{?rhel} == 8
%check
# Fix OBS debug_package execution.
rm -f %{buildroot}/usr/lib/debug/%{_bindir}/%{name}-%{version}-*.debug
%endif

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
