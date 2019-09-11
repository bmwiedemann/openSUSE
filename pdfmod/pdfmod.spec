#
# spec file for package pdfmod
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pdfmod
Version:        0.9.1
Release:        0
Summary:        PDF Modifier
License:        GPL-2.0+
Group:          Productivity/Publishing/PDF
Url:            http://live.gnome.org/PdfMod
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM pdfmod-mono-2.10.patch bgo644516  dimstar@opensuse.org -- Fix build with recent mono, taken from git
Patch0:         pdfmod-mono-2.10.patch
# PATCH-FIX-UPSTREAM pdfmod-dotnet4.patch dimstar@opensuse.org -- Build for .Net 4.0 target
Patch1:         pdfmod-dotnet4.patch
# PATCH-FEATURE-UPSTREAM https://bugzilla.gnome.org/show_bug.cgi?id=736860
Source1:        pdfmod.appdata.xml
BuildRequires:  gconf-sharp2
BuildRequires:  glib-sharp2
BuildRequires:  mono(gmime-sharp)
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  gtk-sharp2
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  hyena >= 0.3
BuildRequires:  intltool
BuildRequires:  mono-basic
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  mono-nunit
BuildRequires:  ndesk-dbus
BuildRequires:  ndesk-dbus-glib-devel
# To be able to automatically adjust the lib name in the dll map and get proper requires for it.
BuildRequires:  libpoppler-glib-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
Requires:       gtk-sharp2
# Require the libpoppler-glib package we used at build time.
Requires:       mono
Requires:       mono-core
Requires:       %(rpm -qa libpoppler-glib[0-9]* --qf "%%{name}")
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PDF Mod is a simple tool for modifying your PDFs: moving, removing,
extracting, and rotating pages.

%lang_package
%prep
%setup -q
translation-update-upstream
%patch0 -p1
%patch1 -p1
# Adjust poppler-sharp.dll.config -> It needs to point to the right library. Fail if we need to touch this manually.
LIBPOPPLER=$(readelf %{_libdir}/libpoppler-glib.so -a | grep "SONAME" | grep -P -o "\[.*\].*" | tr -d "[]")
grep "libpoppler-glib.so.4" lib/poppler-sharp/poppler-sharp/poppler-sharp.dll.config
sed -i "s:libpoppler-glib.so.4:$LIBPOPPLER:" lib/poppler-sharp/poppler-sharp/poppler-sharp.dll.config

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall
%suse_update_desktop_file pdfmod Utility DesktopUtility
%find_lang %{name} %{?no_lang_C}
install -Dm0644 %{S:1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%if 0%{?suse_version} > 1130
%post
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} > 1130
%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README COPYING
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}/
%doc %{_datadir}/gnome/help/%{name}/C/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang

%changelog
