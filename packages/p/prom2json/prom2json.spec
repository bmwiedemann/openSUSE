#
# spec file for package prom2json
#
# Copyright (c) 2025 SUSE LLC
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
# nodebuginfo


# Remove stripping of Go binaries.
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
# Project name when using go tooling.
%define project github.com/prometheus/prom2json
# Project upstream commit.
%define commit 9180c89
Name:           prom2json
Version:        1.3.2
Release:        0
Summary:        CLI tool to scrape a Prometheus client and dump the result as JSON
License:        Apache-2.0
Group:          System/Management
URL:            https://%{project}
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  fdupes
BuildRequires:  go >= 1.17
BuildRequires:  go-md2man
ExcludeArch:    s390
%if 0%{?is_opensuse}
ExcludeArch:    s390x
%endif

%description
The prom2json CLI tool scrapes a Prometheus client
in protocol buffer or text format
and dumps the result as JSON to stdout

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}, generated during the build.

%prep
%setup -q
%setup -q -T -D -a 1

%build

# Build the binary.
export VERSION=%{version}
export COMMIT=%{commit}
export CGO_ENABLED=0
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-s -w -X main.gitCommit=$COMMIT -X main.version=$VERSION" \
   %{project}/cmd/%{name} ;

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Build the man page from markdown documentation.
go-md2man -in README.md -out %{name}.1

# Install the man page.
install -D -m 0644 %{name}.1 "%{buildroot}/%{_mandir}/man1/%{name}.1"
rm %{name}.1

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1.gz

%changelog
