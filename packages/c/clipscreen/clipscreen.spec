#
# spec file for package clipscreen
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


Name:           clipscreen
Version:        0+git.20241113
Release:        0
Summary:        Mirror a portion of your screen to a virtual monitor for easier screen sharing
License:        MIT
URL:            https://github.com/splitbrain/clipscreen
Source0:        %{name}-%{version}.tar.xz
Source1:        meson.build
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
Recommends:     slop

%description
clipscreen is a simple application that creates a virtual monitor that mirrors
a portion of your screen. A green rectangle highlights the specified area.

Why's this useful? You can use any screen sharing tool (Google Meet, Microsoft
Teams, Jitsi Meet, etc.) to share the virtual monitor instead of your entire
screen. No need to share individual windows and having to switch between them,
just move any window you want to share into the green border.

%prep
%autosetup
cp %{SOURCE1} ./

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%doc README.md

%changelog
