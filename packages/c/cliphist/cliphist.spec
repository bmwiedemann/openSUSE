#
# spec file for package cliphist
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Lorenz Holzbauer
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


Name:           cliphist
Version:        0.6.1
Release:        0
Summary:        A wayland clipboard manager with support for multimedia
License:        GPL-3.0-only
URL:            https://github.com/sentriz/cliphist
Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  zstd
Requires:       wl-clipboard
Requires:       xdg-utils

%description
A wayland clipboard manager with support for multimedia

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc readme.md
%{_bindir}/%{name}

%changelog
