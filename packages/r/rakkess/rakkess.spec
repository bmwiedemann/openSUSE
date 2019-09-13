#
# spec file for package rakkess
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rakkess
Version:        0.4.1
Release:        0
Summary:        Utility to show an access matrix for k8s server resources
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/corneliusweig/rakkess
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.12
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
rakkess lists access rights for the current user and all server resources
on a provided kubernetes cluster.

%prep
%setup -qa1

%build
# use vendor directory and build as position independent executeable
sed -i -e 's|go build|go build -mod vendor -buildmode=pie|g' Makefile
%ifarch aarch64
export GOARCH=arm64
%endif
%ifarch s390x ppc64le
export GOARCH=%{_arch}
export CGO_ENABLED=0 
%endif
PLATFORMS=linux make all VERSION=%{version}

%install
# Install the binary.
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 out/rakkess-linux-* %{buildroot}%{_bindir}/rakkess

%files
%license LICENSE
%doc doc/*
%{_bindir}/rakkess

%changelog
