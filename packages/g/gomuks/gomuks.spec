#
# spec file for package gomuks
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        26.03+git.1780250926.564a8707
Release:        0
Summary:        A terminal Matrix client written in Go
License:        AGPL-3.0-only
URL:            https://github.com/gomuks/gomuks
# Source0:        https://github.com/gomuks/gomuks/archive/refs/tags/v%%{upstream_tag}.tar.gz#/gomuks-%%{upstream_tag}.tar.gz
Source0:        gomuks-%{version}.tar.bz2
Source1:        vendor.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go >= 1.26.2
BuildRequires:  go-md2man
BuildRequires:  golang-packaging
BuildRequires:  olm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libheif)
ExclusiveArch:  x86_64 aarch64 riscv64

%description
A terminal Matrix client written in Go using mautrix and mauview.

Basic usage is possible, but expect bugs and missing features.

%prep
%autosetup -p1 -a1

%build
mkdir -p web/dist
touch web/dist/empty
export BINARY_NAME=%{name} MAU_VERSION_PACKAGE=go.mau.fi/gomuks/version
go tool maubuild -v -mod=vendor -buildmode=pie
export BINARY_NAME=%{name}-terminal MAU_VERSION_PACKAGE=go.mau.fi/gomuks/version
go tool maubuild -v -mod=vendor -buildmode=pie

%install
# Install the binary.
install -D -m 0755 -t "%{buildroot}/%{_bindir}/" %{name} %{name}-terminal
# Build the man page.
go-md2man -in README.md -out %{name}.1
go-md2man -in README.md -out %{name}-terminal.1

# Install the man page.
install -D -m 0644 -t "%{buildroot}/%{_mandir}/man1/" %{name}.1 %{name}-terminal.1

%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-terminal
%{_mandir}/man1/%{name}*.1%{?ext_man}

%changelog
