#
# spec file for package esbuild
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


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
# Go source packages are horribly broken on Leap (mismatching versions between libraries and compiler)
%bcond_with vendor
%else
%bcond_without vendor
%endif

#macros for Fedora
%global goipath  github.com/evanw/esbuild
%global tag   v%{version}
%global extractdir0 esbuild-%{version}
Name:           esbuild
Version:        0.23.0
Release:        0
Summary:        A JavaScript bundler written for speed
License:        MIT
Group:          Development/Languages/Other
URL:            https://esbuild.github.io
Source0:        https://github.com/evanw/esbuild/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Patch0:         remove-version-check.patch
BuildRequires:  util-linux
%if 0%{?fedora}
BuildRequires:  go-rpm-macros
BuildRequires:  golang
%else
BuildRequires:  golang-packaging
BuildRequires:  golang(API)
%endif

%if %{without vendor}
%if 0%{?fedora}
BuildRequires:  golang-ipath(golang.org/x/sys)
%else
BuildRequires:  golang-org-x-sys
%endif
%endif

%description
esbuild is a JavaScript bundler and minifier.

%{gopkg}

%prep
%if %{with vendor}
%autosetup -a1 -p1
%else
%autosetup -p1
%endif

%build
export CFLAGS="%{optflags} -fpie -fno-fat-lto-objects"
export CXXFLAGS="$CFLAGS"

export CGO_CFLAGS="$CFLAGS"
export CGO_CXXFLAGS="$CFLAGS"
export CGO_LDFLAGS="%{?build_ldflags}"

export GOFLAGS='-ldflags=-compressdwarf=false' #fix broken debuginfo bsc#1215402

%if 0%{?fedora}
%goprep -k -e
%else
%goprep %goipath
export GO111MODULE=off
%endif
%gobuild ./cmd/esbuild

%install
install -pvDm755 \
%if 0%{?fedora}
%name \
%else
%{_builddir}/go/bin/%{name} \
%endif
"%{buildroot}/%{_bindir}/%{name}"

%check
export CFLAGS="%{optflags} -fpie -fno-fat-lto-objects"
export CXXFLAGS="$CFLAGS"
export CGO_CFLAGS="$CFLAGS"
export CGO_CXXFLAGS="$CFLAGS"
export CGO_LDFLAGS="%{?build_ldflags}"
export GOFLAGS='-ldflags=-compressdwarf=false'
%if 0%{?fedora}
%gocheck
%else
export GO111MODULE=off
%gotest %goipath/...
%endif

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
