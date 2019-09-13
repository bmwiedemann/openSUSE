#
# spec file for package container-diff
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


%define project github.com/GoogleContainerTools/container-diff
Name:           container-diff
Version:        0.15.0
Release:        0
Summary:        Tool to analyze and compare container images
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/GoogleCloudPlatform/container-diff
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.7
Recommends:     docker
# disable stripping of binaries
%{go_nostrip}

%description
container-diff is a tool for analyzing and comparing container images.
container-diff can examine images along several different criteria, including:
- Docker Image History
- Image file system
- Apt packages
- RPM packages
- pip packages
- npm packages

These analyses can be performed on a single image, or a diff can be performed
on two images to compare.

%prep
%setup -q

%build
# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

# Patch the version variable
# Build container-diff
export BUILDTAGS=""
go build -tags "$BUILDTAGS" \
         -buildmode=pie \
         -ldflags '-s -w -X %{project}/version.version=v%{version}' \
         -o bin/container-diff \
         %{project}

%check
# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

# Test container-diff.  Exclude ppc64le, which has known issue with gotest.
# Also exclude cmd/diff_test.go as it requires pulling remote images
PKG_LIST=$(go list ./... | grep -v "%{project}/vendor")
mv cmd/diff_test.go cmd/diff_test.go.exclude
%ifnarch ppc64le
go test $PKG_LIST
%endif

%install
cd $HOME/go/src/%{project}
install -Dpm 0755 bin/container-diff \
  %{buildroot}/%{_bindir}/container-diff

%files
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/container-diff

%changelog
