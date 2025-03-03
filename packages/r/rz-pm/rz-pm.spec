#
# spec file for package rz-pm
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


Name:           rz-pm
Version:        0.3.3
Release:        0
Summary:        Rizin package manager
License:        LGPL-3.0-only
URL:            https://github.com/rizinorg/rz-pm.git
Source:         %{name}-%{version}.tar
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22
Requires:       rizin

%description
This tool aims to be a cross platform package manager for the reverse engineering framework Rizin.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
%ifnarch ppc64 # Does not support pie
   -buildmode=pie
%endif

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
