#
# spec file for package umoci
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# nodebuginfo


# Remove stripping of Go binaries.
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

# Project name when using go tooling.
%define project github.com/openSUSE/umoci

Name:           umoci
Version:        0.4.4
Release:        0
Summary:        Open Container Image manipulation tool
License:        Apache-2.0
Group:          System/Management
Url:            https://umo.ci
Source0:        https://github.com/openSUSE/umoci/releases/download/v%{version}/umoci.tar.xz#/%{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/umoci/releases/download/v%{version}/umoci.tar.xz.asc#/%{name}-%{version}.tar.xz.asc
Source2:        https://umo.ci/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  go >= 1.6
BuildRequires:  go-go-md2man
ExcludeArch:    s390

%description
umoci modifies Open Container images. umoci is a manipulation tool for OCI
images. In particular, it is a more complete alternative to oci-image-tools
provided by the OCI.

%prep
%setup -q

%build

# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -ar * $HOME/go/src/%{project}

export VERSION="$(cat ./VERSION)"
if [ "$VERSION" != "%{version}" ]; then
  VERSION="%{version}_suse"
fi

# Build the binary.
make VERSION="$VERSION" umoci

# Build the docs if we have go-md2man.
make doc

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Install all of the docs.
for file in doc/man/*.1; do
  install -D -m 0644 $file "%{buildroot}/%{_mandir}/man1/$(basename $file)"
done

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md doc/*
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/umoci*

%changelog
