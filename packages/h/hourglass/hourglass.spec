#
# spec file for package hourglass
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


Name:           hourglass
Version:        1.2.3
Release:        0
Summary:        Clock gadget for Elementary OS
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://github.com/sgpthomas
Source:         https://github.com/sgpthomas/hourglass/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
Recommends:     %{name}-lang

%description
A clock application that is designed to fit perfectly into
Elementary's design scheme.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.sgpthomas.hourglass GTK Utility Clock
%find_lang com.github.sgpthomas.hourglass %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/com.github.sgpthomas.hourglass
%{_bindir}/com.github.sgpthomas.hourglass-daemon
%{_datadir}/applications/com.github.sgpthomas.hourglass.desktop
%{_datadir}/glib-2.0/schemas/com.github.sgpthomas.hourglass.gschema.xml
%{_datadir}/icons/hicolor/*/*/com.github.sgpthomas.hourglass.??g
%{_datadir}/metainfo/com.github.sgpthomas.hourglass.appdata.xml
%{_datadir}/pixmaps/com.github.sgpthomas.hourglass.??g
%{_sysconfdir}/xdg/autostart/com.github.sgpthomas.hourglass-daemon.desktop

%files lang -f %{name}.lang

%changelog
