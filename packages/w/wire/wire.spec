#
# spec file for package wire
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           wire
Version:        0.5.0
Release:        0
Summary:	Compile-time Dependency Injection for Go
License:        Apache-2.0
Group:          Development/Languages/Go
Url:            https://github.com/google/wire
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
%{?systemd_ordering}

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

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog

