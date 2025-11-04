#
# spec file for package kubecolor
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


Name:           kubecolor
Version:        0.5.3
Release:        0
Summary:        Colorize your kubectl output
License:        MIT
URL:            https://kubecolor.github.io/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.gz
BuildRequires:  go1.25 >= 1.25.3
Requires:       kubernetes-client-provider

%description
A command-line wrapper used to add colors to your kubectl output

%prep
%autosetup -p 1 -a 1

%build
go build \
    -mod=vendor \
    -buildmode=pie \
    -ldflags="-X 'main.Version=%{version}'"

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
