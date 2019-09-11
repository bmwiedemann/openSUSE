#
# spec file for package mozo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 1.23
Name:           mozo
Version:        1.23.0
Release:        0
Summary:        MATE Desktop menu editor
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libmate-menu) >= %{_version}
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       mate-menus >= %{_version}
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
# mate-menu-editor was last used in openSUSE 13.1.
Provides:       mate-menu-editor = %{version}
Obsoletes:      mate-menu-editor < %{version}
Obsoletes:      mate-menu-editor-lang < %{version}
BuildArch:      noarch

%description
This package provides Mozo, a menu editor for the MATE Desktop,
using the freedesktop.org menu specification.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{python_sitelib}/
%suse_update_desktop_file %{name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{python3_sitelib}/Mozo/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
