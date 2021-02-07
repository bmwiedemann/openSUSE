#
# spec file for package wlr-randr
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.2.0
Release:        0
Summary:        Utility to manage outputs of a Wayland compositor
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://github.com/emersion/wlr-randr
Source:         https://github.com/emersion/wlr-randr/releases/download/v0.2.0/wlr-randr-%{version}.tar.gz
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)

%description
wlr-randr is a command line utility to manage outputs of a Wayland compositor.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
