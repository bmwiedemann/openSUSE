#
# spec file for package reg
#
# Copyright (c) 2019 SUSE LLC
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


Name:           reg
Version:        0.16.1
Release:        0
Summary:        Container registry command line client
License:        MIT
Group:          System/Management
URL:            https://github.com/genuinetools/reg
Source:         %{name}-%{version}.tar.gz
Patch:          go-mod-vendor.patch
BuildRequires:  golang(API) >= 1.12
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
Container registry v2 command line client and repo listing generator
with security checks. It can be used to get and manipulate several 
informations about container images, manifestes and layers from a
container registry including vulnerability reports and can generate a
static website for a registry.

%prep
%setup -q
%patch -p0

%build
make build GITCOMMIT=4a4d0e5d108ca9558879bdf1aba94d09e921cf1e

%install
# Install the binary.
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 reg %{buildroot}%{_bindir}/reg

%files
%license LICENSE
%doc README.md
%{_bindir}/reg

%changelog
