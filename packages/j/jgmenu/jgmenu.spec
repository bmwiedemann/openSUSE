#
# spec file for package jgmenu
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


Name:           jgmenu
Version:        4.5.0
Release:        0
Summary:        Small X11 menu intended to be used with openbox and tint2
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            https://github.com/johanmalm/jgmenu
Source:         https://github.com/johanmalm/jgmenu/archive/v%{version}.tar.gz
# Needed for typelib() - Requires.
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.46
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

%description
jgmenu is a simple X11 menu intended to be used with tint2 and openbox.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} prefix=%{_prefix}

%install
make %{?_smp_mflags} prefix=%{_prefix} DESTDIR=%{buildroot} install
%suse_update_desktop_file -r %{name} Utility DesktopUtility
%python3_fix_shebang

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_libexecdir}/%{name}
%{_mandir}/man?/%{name}*.?%{ext_man}

%changelog
