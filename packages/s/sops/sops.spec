#
# spec file for package sops
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sops
Version:        3.7.3
Release:        0
Summary:        Simple and flexible tool for managing secrets
License:        MPL-2.0
Group:          Productivity/Security
URL:            https://github.com/mozilla/sops
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.15

%description
Simple and flexible tool for managing secrets

%prep
%setup -q
%setup -q -T -D -a 1

%build
export GOFLAGS=-mod=vendor
%{goprep} go.mozilla.org/sops/v3/cmd/sops
%{gobuild} .

#%%check
#export GOFLAGS=-mod=vendor
#%%{gotest} github.com/mozilla/sops/...

%install
%{goinstall}
rm -rf %{buildroot}/%{_libdir}/go/contrib

%files
%license LICENSE
%doc CHANGELOG.rst README.rst
%{_bindir}/%{name}

%changelog
