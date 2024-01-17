#
# spec file for package sampler
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
# Project name when using go tooling.
%define project github.com/sqshq/sampler
# Project upstream commit.
%define commit a086d99
Name:           sampler
Version:        1.1.0
Release:        0
Summary:        A tool for shell commands execution, visualization and alerting
License:        GPL-3.0-only
URL:            https://sampler.dev/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  fdupes
BuildRequires:  go >= 1.11
BuildRequires:  go-md2man
BuildRequires:  pkgconfig(alsa)
ExcludeArch:    s390

%description
Sampler is a tool for shell commands execution, visualization and alerting. Configured with a simple YAML file.

%prep
%setup -q
%setup -q -T -D -a 1

%build
export VERSION=%{version}
export COMMIT=%{commit}
export CGO_ENABLED=1
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-s -w -X main.gitCommit=$COMMIT -X main.version=$VERSION" \
   -o %{name} ;

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"
# Build the man page.
go-md2man -in README.md -out %{name}.1

# Install the man page.
install -D -m 0644 %{name}.1 "%{buildroot}/%{_mandir}/man1/%{name}.1"
rm %{name}.1

%fdupes %{buildroot}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1.gz

%changelog
