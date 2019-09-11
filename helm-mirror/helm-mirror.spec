#
# spec file for package helm-mirror
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


# Project name when using go tooling.
%define project github.com/openSUSE/helm-mirror

Name:           helm-mirror
Version:        0.2.4
Release:        0
Summary:        Tool to mirror Helm repositories
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/openSUSE/helm-mirror
Source:         %{name}-%{version}.tar.gz
BuildRequires:  go >= 1.11.3
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.11
Requires(post): %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This utility mirrors Helm repositories to a local directory and it
can extract used container images.

%prep
%setup -q

%build

# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}

export VERSION=$(sed -n -e 's/version:[ "]*\([^"]*\).*/\1/p' plugin.yaml)
if [ "$VERSION" != "%{version}" ]; then
  VERSION="%{version}_suse"
fi

make VERSION="$VERSION" mirror
make doc

%install
# Install the plugin.
install -D -m 0755 ./bin/mirror "%{buildroot}/%{_bindir}/%{name}"

# Install all of the docs.
for file in doc/man/*.1; do
  install -D -m 0644 $file "%{buildroot}/%{_mandir}/man1/$(basename $file)"
done

%files
%defattr(-,root,root)
%doc README.md LICENSE doc/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
