#
# spec file for package zvm
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


Name:           zvm
Version:        0.8.5
Release:        0
Summary:        Easily install/upgrade between different versions of Zig
License:        MIT
URL:            https://github.com/tristanisham/zvm
Source:         https://github.com/tristanisham/zvm/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.xz
# PATCH-FIX-UPSTREAM: Disable auto upgrade features
Patch0:         disable-auto-upgrade.patch
BuildRequires:  golang(API) >= 1.22

%description
Zig Version Manager (zvm) is a tool for managing your Zig installs. With std
under heavy development and a large feature roadmap, Zig is bound to continue
changing. Breaking existing builds, updating valid syntax, and introducing new
features like a package manager. While this is great for developers, it also
can lead to headaches when you need multiple versions of a language installed
to compile your projects, or a language gets updated frequently.

%prep
%autosetup -p1 -a1 -n zvm-%{version}

%build
go build \
   -ldflags="-s -w" \
   -mod=vendor \
   -buildmode=pie \
   -v

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
go test ./cli -v

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog

