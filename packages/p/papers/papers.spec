#
# spec file for package papers
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2024 mantarimay
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


%bcond_without test
%define major_ver 4
%define api_ver %{major_ver}_0
%define plugin_ver 6
%define appid org.gnome.Papers
Name:           papers
Version:        49.2
Release:        0
Summary:        GNOME Document Viewer
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/papers
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  blueprint-compiler
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  meson >= 0.53.0
BuildRequires:  nautilus-devel
BuildRequires:  python3-gi-docgen
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.17.1
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(poppler-glib)
Recommends:     papers-plugin-pdfdocument
Suggests:       papers-plugin-comicsdocument
Suggests:       papers-plugin-djvudocument
Suggests:       papers-plugin-tiffdocument

%description
Papers is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package -n libppsdocument%{api_ver}-%{plugin_ver}
Summary:        GNOME Document Viewer System Library

%description -n libppsdocument%{api_ver}-%{plugin_ver}
Papers is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package -n libppsview%{api_ver}-5
Summary:        GNOME Document Viewer System Library

%description -n libppsview%{api_ver}-5
Papers is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package -n typelib-1_0-PapersDocument-%{api_ver}
Summary:        Introspection bindings for the Papers Document Viewer

%description -n typelib-1_0-PapersDocument-%{api_ver}
Papers is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package -n typelib-1_0-PapersView-%{api_ver}
Summary:        Introspection bindings for the Papers Document Viewer

%description -n typelib-1_0-PapersView-%{api_ver}
Papers is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package devel
Summary:        Header files for the Papers Document Viewer
Requires:       %{name} = %{version}
Requires:       typelib-1_0-PapersDocument-%{api_ver} = %{version}
Requires:       typelib-1_0-PapersView-%{api_ver} = %{version}

%description devel
Papers is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

This package contains the header files for building additional plugins.

%package plugin-comicsdocument
Summary:        Comics document support for Papers
Requires:       %{name} = %{version}

%description plugin-comicsdocument
A plugin for Papers to read Comics documents.

%package plugin-djvudocument
Summary:        DjVu document support for Papers
Requires:       %{name} = %{version}

%description plugin-djvudocument
A plugin for Papers to read DjVu documents.

%package plugin-pdfdocument
Summary:        PDF document support for Papers
Requires:       %{name} = %{version}

%description plugin-pdfdocument
A plugin for Papers to read PDF documents.

%package plugin-tiffdocument
Summary:        TIFF document support for Papers
Requires:       %{name} = %{version}

%description plugin-tiffdocument
A plugin for Papers to read TIFF images.

%package -n nautilus-extension-papers
Summary:        Papers document support for nautilus
Requires:       %{name} = %{version}

%description -n nautilus-extension-papers
A extension for support document on nautilus.

%lang_package

%prep
%autosetup -a1

%build
%meson \
	--libexecdir=%{_libexecdir}/%{name} \
	-D documentation=false \
	-D user_doc=false \
	-D tests=false \
	-D sysprof=disabled \
    %{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}/%{_prefix}

%find_lang %{name}

%ldconfig_scriptlets -n libppsdocument%{api_ver}-%{plugin_ver}
%ldconfig_scriptlets -n libppsview%{api_ver}-5

%check
%if %{with test}
%meson_test
%endif

%files
%license COPYING
%doc NEWS* README.md
%{_bindir}/papers
%{_bindir}/papers-previewer
%{_bindir}/papers-thumbnailer
%{_mandir}/man?/*%{ext_man}
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/applications/%{appid}-previewer.desktop
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*
%{_datadir}/thumbnailers

%files -n libppsdocument%{api_ver}-%{plugin_ver}
%{_libdir}/libppsdocument-%{major_ver}.0.so.%{plugin_ver}*

%files -n libppsview%{api_ver}-5
%{_libdir}/libppsview-%{major_ver}.0.so.5*

%files -n typelib-1_0-PapersDocument-%{api_ver}
%{_libdir}/girepository-1.0/PapersDocument-%{major_ver}.0.typelib

%files -n typelib-1_0-PapersView-%{api_ver}
%{_libdir}/girepository-1.0/PapersView-%{major_ver}.0.typelib

%files devel
%{_includedir}/papers
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_libdir}/pkgconfig/papers*.pc

%files plugin-comicsdocument
%dir %{_libdir}/papers/
%dir %{_libdir}/papers/%{plugin_ver}
%dir %{_libdir}/papers/%{plugin_ver}/backends
%{_datadir}/metainfo/org.gnome.Papers.ComicsDocument.metainfo.xml
%{_libdir}/papers/%{plugin_ver}/backends/org.gnome.Papers.ComicsDocument.papers-backend
%{_libdir}/papers/%{plugin_ver}/backends/libcomicsdocument.so

%files plugin-djvudocument
%{_datadir}/metainfo/org.gnome.Papers.DjvuDocument.metainfo.xml
%{_libdir}/papers/%{plugin_ver}/backends/org.gnome.Papers.DjvuDocument.papers-backend
%{_libdir}/papers/%{plugin_ver}/backends/libdjvudocument.so

%files plugin-pdfdocument
%{_datadir}/metainfo/org.gnome.Papers.PdfDocument.metainfo.xml
%{_libdir}/papers/%{plugin_ver}/backends/org.gnome.Papers.PdfDocument.papers-backend
%{_libdir}/papers/%{plugin_ver}/backends/libpdfdocument.so

%files plugin-tiffdocument
%{_datadir}/metainfo/org.gnome.Papers.TiffDocument.metainfo.xml
%{_libdir}/papers/%{plugin_ver}/backends/org.gnome.Papers.TiffDocument.papers-backend
%{_libdir}/papers/%{plugin_ver}/backends/libtiffdocument.so

%files -n nautilus-extension-papers
%{_libdir}/nautilus/extensions-4/libpapers-document-properties.so

%files lang -f %{name}.lang

%changelog
