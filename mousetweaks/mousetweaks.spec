#
# spec file for package mousetweaks
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


Name:           mousetweaks
Version:        3.32.0
Release:        0
Summary:        GNOME mouse settings tweaker
License:        GPL-3.0-only
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/mousetweaks
Source0:        https://download.gnome.org/sources/mousetweaks/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang

%description
The Mousetweaks package provides mouse accessibility enhancements for
the GNOME desktop.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
export LANG=C.UTF-8
%configure \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{prefix}

%files
%doc AUTHORS NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*.1%{ext_man}
%{_datadir}/GConf/gsettings/mousetweaks.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.gschema.xml
%{_datadir}/mousetweaks/

%files lang -f %{name}.lang

%changelog
