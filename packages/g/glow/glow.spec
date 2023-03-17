#
# spec file for package glow
#
# Copyright (c) 2023 SUSE LLC
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


%{go_nostrip}
# Disable LTO flags to stop builds failing on some architectures
%global _lto_cflags %nil
Name:           glow
Version:        1.5.0
Release:        0
Summary:        Render markdown on the CLI
#
License:        MIT
#
Group:          System/Console
URL:            https://github.com/charmbracelet/glow
#
Source0:        https://github.com/charmbracelet/glow/archive/v%{version}/%{name}-%{version}.tar.gz
# `osc service disabledrun`
Source1:        vendor.tar.zst
#
Source2:        README.suse-maint.md
#
BuildRequires:  zstd
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.11

%description
Glow is a terminal based markdown reader designed from the ground up to bring
out the beauty—and power—of the CLI.

Use it to discover markdown files, read documentation directly on the command
line and stash markdown files to your own private collection so you can read
them anywhere. Glow will find local markdown files in subdirectories or a local
Git repository.

%prep
%autosetup -p1 -a1

%build
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export CGO_CFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
export CGO_CPPFLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.revision=%{version}"

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%check
./glow --version

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/glow

%changelog
