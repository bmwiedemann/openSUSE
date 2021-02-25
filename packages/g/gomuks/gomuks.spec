#
# spec file for package gomuks
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
Name:           gomuks
Version:        0.2.3
Release:        0
Summary:        A terminal Matrix client written in Go
License:        AGPL-3.0-only
URL:            https://maunium.net/go/gomuks
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go >= 1.14
BuildRequires:  go-md2man
BuildRequires:  golang-github-kr-pty
BuildRequires:  golang-packaging
BuildRequires:  olm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
ExcludeArch:    s390
%if 0%{?is_opensuse}
ExcludeArch:    s390x
%endif

%description
A terminal Matrix client written in Go using mautrix and mauview.

Basic usage is possible, but expect bugs and missing features.

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
   -ldflags "-s -w -X main.version=$VERSION" \
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
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1%{?ext_man}

%changelog
