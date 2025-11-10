#
# spec file for package kubectl-explore
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           kubectl-explore
Version:        0.14.1
Release:        0
Summary:        A better kubectl explain with the fuzzy finder
License:        MIT
URL:            https://github.com/keisku/kubectl-explore
Source:         kubectl-explore-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.25

%description
This plugin fuzzy-finds the field explanation from supported API resources. It
implements different explanations for particular API version.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
