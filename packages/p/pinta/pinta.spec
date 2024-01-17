#
# spec file for package pinta
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.7.1
Release:        0
Summary:        Image editing application
License:        MIT
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://pinta-project.com/
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
BuildArch:      noarch

%description
Pinta is a free, open source drawing/editing application designed
after Paint.NET. Its goal is to provide users with a simple yet
powerful way to draw and manipulate images.

%lang_package

%prep
%autosetup

%build
%configure --libdir=%{_prefix}/lib/mono/%{name}/
%make_build

%install
%make_install
rm -rf %{buildroot}%{_prefix}/lib/mono/%{name}/pkgconfig/
%find_lang %{name}

%check
make check

%files
%license license-mit.txt
%doc readme.md
%{_bindir}/%{name}
%{_prefix}/lib/mono/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
