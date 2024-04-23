#
# spec file for package wlr-randr
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


Name:           wlr-randr
Version:        0.4.1
Release:        0
Summary:        Utility to manage outputs of a Wayland compositor
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://git.sr.ht/~emersion/wlr-randr
Source:         https://git.sr.ht/~emersion/wlr-randr/refs/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://git.sr.ht/~emersion/wlr-randr/refs/download/v%{version}/%{name}-%{version}.tar.gz.sig
# https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19
Source2:        %{name}.keyring
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)

%description
wlr-randr is a command line utility to manage outputs of a Wayland compositor.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
