#
# spec file for package wlrctl
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


Name:           wlrctl
Version:        0.2.2~0
Release:        0
Summary:        Utility for miscellaneous wlroots Wayland extensions
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://git.sr.ht/~brocellous/wlrctl
Source:         %{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
# Build failure on arch with unsigned char - https://todo.sr.ht/~brocellous/wlrctl/4
ExclusiveArch: %{ix86} x86_64

%description
wlrctl is a command line utility for miscellaneous wlroots Wayland extensions.

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
%{_datadir}/zsh/site-functions/_wlrctl
%{_mandir}/man1/wlrctl.1%{?ext_man}

%changelog
