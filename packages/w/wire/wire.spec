#
# spec file for package wire
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


%if 0%{?rhel} == 8
%global debug_package %{nil}
%endif

%if 0%{?rhel}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
%endif

Name:           wire
Version:        0.6.0
Release:        0
Summary:        Compile-time Dependency Injection for Go
License:        Apache-2.0
Group:          Development/Languages/Go
URL:            https://github.com/google/wire
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch1:         update_go_version.patch
BuildRequires:  golang(API) >= 1.22
%{?systemd_ordering}
ExcludeArch:    s390

%description
Wire is a code generation tool that automates connecting components using
dependency injection. Dependencies between components are represented in Wire
as function parameters, encouraging explicit initialization instead of global
variables. Because Wire operates without runtime state or reflection, code
written to be used with Wire is useful even for hand-written initialization.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

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
