#
# spec file for package ctop
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


Name:           ctop
Version:        0.7.7
Release:        0
Summary:        Top-like interface for container metrics
License:        MIT
Group:          System/Monitoring
URL:            https://ctop.sh/
Source:         https://github.com/bcicen/ctop/archive/refs/tags/v%{version}.tar.gz#/ctop-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  zstd

%description
Top-like interface for container metrics.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
