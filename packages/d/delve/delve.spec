#
# spec file for package delve
#
# Copyright (c) 2022 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define shortname dlv

Name:           delve
Version:        1.20.0
Release:        0
Summary:        Static website generator written in Go
License:        MIT
Group:          Development/Languages/Go
URL:            https://github.com/go-delve/delve
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.16
ExcludeArch:    s390x ppc64le %arm

%description
Delve is a debugger for the Go programming language. The goal of
the project is to provide a simple, full featured debugging tool
for Go. Delve should be easy to invoke and easy to use. Chances are
if you're using a debugger, things aren't going your way. With that
in mind, Delve should stay out of your way as much as possible.

%prep
%autosetup -a 1

%build
# Build the binary, use PIE unless on ppc64le or s390x
# Upstream reports these as unsupported platforms so meta pkg disable
go build \
   -mod=vendor \
%ifnarch ppc64 s390x
   -buildmode=pie \
%endif
   -o %{shortname} \
   ./cmd/%{shortname}
# Upstream Makefile uses these options to build static
# fails with /usr/bin/ld: cannot find -lc
# -ldflags "-extldflags -static" \

%install
# Install the binary.
install -D -m 0755 %{shortname} "%{buildroot}/%{_bindir}/%{shortname}"

%files
%doc README.md
%doc Documentation
%license LICENSE
%{_bindir}/%{shortname}

%changelog
