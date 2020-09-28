#
# spec file for package pinta
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


Name:           pinta
Version:        1.7
Release:        0
Summary:        Drawing/editing application on C#
License:        MIT
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://pinta-project.com/
Source:         https://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  mono-addins-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono) >= 6.0
BuildRequires:  pkgconfig(mono-cairo)
# is this still necessary?
Recommends:     %{name}-lang = %{version}
BuildArch:      noarch

%description
Pinta is a free, open source drawing/editing application designed
after Paint.NET. Its goal is to provide users with a simple yet
powerful way to draw and manipulate images.

%lang_package

%prep
%autosetup

%build
autoreconf -fi
# perhaps this should go into %%_libexecdir/Mono ?
%configure --libdir=%{_libexecdir}
%make_build

%install
%make_install
%find_lang %{name}
rm -rf %{buildroot}%{_datadir}/appdata %{buildroot}%{_libexecdir}/pkgconfig

%check
make check

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license license-mit.txt
%doc readme.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
