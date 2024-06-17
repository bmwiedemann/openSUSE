#
# spec file for package vgrep
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


# Remove stripping of Go binaries.
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
# Project name when using go tooling.
%define project github.com/vrothberg/vgrep
Name:           vgrep
Version:        2.8.0
Release:        0
Summary:        Frontend for git-grep and grep
License:        GPL-3.0-only
Group:          Productivity/Text/Utilities
URL:            https://github.com/vrothberg/vgrep
Source0:        https://github.com/vrothberg/vgrep/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  golang(API) >= 1.21
Requires:       git-core
Requires:       grep

%description
vgrep is a command-line tool to search textual patterns in directories. It
serves as a frontend to grep and git-grep and allows to open the indexed
matching lines in a user-specified editor. vgrep is inspired by the ancient
cgvg scripts but extended to perform further operations such as listing
statistics of files and directory trees or showing the context lines before and
after the matches.

%prep
%autosetup

%build

# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}

# Build the binary.
cd $HOME/go/src/%{project}
go build -mod=vendor -o ./build/vgrep -buildmode=pie -ldflags "-s -w -X main.version=%{version}"

%install
# Install the binary.
install -D -m 0755 $HOME/go/src/%{project}/build/%{name} "%{buildroot}/%{_bindir}/%{name}"

%fdupes %{buildroot}/%{_prefix}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
