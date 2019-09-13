#
# spec file for package anjuta-extras
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _major_minor 3.25
Name:           anjuta-extras
Version:        3.26.0
Release:        0
Summary:        Extra plugins for anjuta
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            http://download.gnome.org/sources/anjuta-extras
Source:         https://download.gnome.org/sources/anjuta-extras/3.26/%{name}-%{version}.tar.xz
# For directory ownership; okay since we have a Requires on anjuta
BuildRequires:  anjuta >= 3.7.4
BuildRequires:  gcc-c++
BuildRequires:  intltool >= 0.35.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.16.0
BuildRequires:  pkgconfig(libanjuta-3.0) >= %{_major_minor}.0
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       anjuta
Requires:       gsettings-desktop-schemas
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
The package contains the following plugins:

    * Scintilla Editor
    * Scratchbox Support

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%find_lang anjuta-manual %{?no_lang_C} %{name}.lang

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%files
%doc %{_datadir}/help/C/anjuta-manual/
# Explicitly list .plugin files so we know what we ship
%{_libdir}/anjuta/anjuta-editor.plugin
%{_libdir}/anjuta/anjuta-sample.plugin
%{_libdir}/anjuta/anjuta-scratchbox.plugin
%{_libdir}/anjuta/*.so*
%{_datadir}/pixmaps/anjuta/*
%{_datadir}/anjuta/*
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.*.gschema.xml

%files lang -f %{name}.lang

%changelog
