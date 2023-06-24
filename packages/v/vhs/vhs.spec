#
# spec file for package vhs
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

%global _lto_cflags %nil
Name:           vhs
Version:        0.5.0
Release:        0
Summary:        CLI video recorder
URL:            https://github.com/charmbracelet/vhs
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
License:        MIT
BuildRequires:  zstd
BuildRequires:  golang(API)
Requires:       ffmpeg
Requires:       ttyd

%description
VHS records your terminal as videos or gifs for demos.

%prep
%setup -qa1

%build
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export CGO_CFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
export CGO_CPPFLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.Version=%{version}"

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc examples README.md

%changelog
