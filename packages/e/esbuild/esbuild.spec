#
# spec file for package esbuild
#
# Copyright (c) 2021 SUSE LLC
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



Name:           esbuild
Version:        0.15.11
Release:        0
Summary:        A JavaScript bundler written for speed
License:        MIT
Group:          Development/Languages/Other
URL:            https://esbuild.github.io
Source0:        https://github.com/evanw/esbuild/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Patch0:         remove-version-check.patch
%if 0%{?fedora}
BuildRequires:  golang
BuildRequires:  go-rpm-macros
%else
BuildRequires:  golang(API)
BuildRequires:  golang-packaging
%endif
BuildRequires: util-linux

#macros for Fedora
%global goipath  github.com/evanw/esbuild
%global tag   v%{version}
%global extractdir0 esbuild-%version


%description
esbuild is a JavaScript bundler and minifier.

%gopkg

%prep
%autosetup -a1 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"


%if 0%{?fedora}
%goprep -k -e
%gobuild ./cmd/esbuild
%else
%goprep .
go build -v -p 4 -x -buildmode=pie -mod vendor ./cmd/esbuild
%endif



%install
install -pvDm755 %name "%{buildroot}/%{_bindir}/%{name}"

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
