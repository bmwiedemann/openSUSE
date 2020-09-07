#
# spec file for package rofi
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


Name:           rofi
Version:        1.6.0
Release:        0
Summary:        A window switcher, run dialog and dmenu replacement
License:        MIT
Group:          System/GUI/Other
URL:            https://davedavenport.github.io/rofi/
Source:         https://github.com/DaveDavenport/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         xdg-terminal.patch
# PATCH-FIX-SUSE
Patch1:         fix-shebangs.patch
# Required version 0.11 is not yet in TW BuildRequires:  check-devel
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  cppcheck
BuildRequires:  flex >= 2.5.39
BuildRequires:  libjpeg8-devel
BuildRequires:  librsvg-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel
Requires:       xdg-utils

%description
rofi is a popup window switcher roughly based on "superswitcher",
requiring only xlib and pango. This version started off as a clone of
simpleswitcher, the version from Sean Pringle. Rofi developed extra
features, like a run dialog, SSH launcher and can act as a drop-in
dmenu replacement.

%package devel
Summary:        Development files for rofi
Group:          Development/Libraries/C and C++

%description devel
Development files and headers for rofi

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --disable-check
%make_build

%install
%make_install

%files
%license COPYING
%doc Changelog README.md
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%dir %{_datadir}/rofi/
%{_datadir}/rofi/themes/
%{_mandir}/man1/rofi.1%{?ext_man}
%{_mandir}/man1/rofi-sensible-terminal.1%{?ext_man}
%{_mandir}/man1/rofi-theme-selector.1%{?ext_man}
%{_mandir}/man5/rofi-theme.5%{?ext_man}
%{_mandir}/man5/rofi-script.5%{?ext_man}

%files devel
%{_includedir}/rofi/
%{_libdir}/pkgconfig/rofi.pc

%changelog
