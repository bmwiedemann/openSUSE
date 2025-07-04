#
# spec file for package evince
#
# Copyright (c) 2025 SUSE LLC
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


%define evdocument_so 3-4
%define evview_so 3-3
%define typelibAPI 3_0
%define pluginAPI 4

Name:           evince
Version:        48.1
Release:        0
Summary:        GNOME Document Viewer
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://wiki.gnome.org/Apps/Evince
Source0:        %{name}-%{version}.tar.zst
# PATCH-FIX-SLE alarrosa@suse.com - Reverse upstream bump of synctex required version to build with texlive 2017
Patch0:         0001-reversed-synctex-Annotate-more-functions-that-wraps-formatting-strings.patch
# PATCH-FIX-SLE
Patch1:         0002-reversed-synctex-Sync-against-upstream-synctex.patch
# PATCH-FIX-SLE
Patch2:         0003-reversed-cut-n-paste-Annotate-functions-that-wraps-formatting-strings.patch
# PATCH-FIX-SLE
Patch3:         0001-reversed-synctex-Move-_GNU_SOURCE-to-the-top-of-the-source-code.patch
# PATCH-FIX-SLE
Patch4:         0002-reversed-synctex-Remove-unused-labels.patch
# PATCH-FIX-SLE
Patch5:         0003-reversed-synctex-Silence-error-when-no-synctex-file-is-present.patch
# PATCH-FIX-SLE
Patch6:         0004-reversed-synctex-Annotate-functions-that-wrap-vfprintf.patch
# PATCH-FIX-SLE
Patch7:         0005-reversed-synctex-Fix-compilation.patch
# PATCH-FIX-SLE
Patch8:         0006-reversed-synctex-Update-from-version-1.18-to-1.21.patch

# PATCH-FIX-UPSTREAM evince-kpathsea.patch -- Fix build with gcc 15
Patch1000:      evince-kpathsea.patch

BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-x11
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  texlive-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(adwaita-icon-theme) >= 2.17.1
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(ddjvuapi) >= 3.5.22
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.0
BuildRequires:  pkgconfig(gspell-1) >= 1.6.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libarchive) >= 3.6.0
BuildRequires:  pkgconfig(libgxps) >= 0.2.1
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-1) >= 0.5
BuildRequires:  pkgconfig(libspectre) >= 0.2.0
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(poppler-glib) >= 22.02.0
BuildRequires:  pkgconfig(sm) >= 1.0.0
BuildRequires:  pkgconfig(synctex) >= 1.18
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
# Disable the browser plugin and package, and make main package provide-obsolete plugin package for upgrade; see bgo#738270
Provides:       evince-browser-plugin = %{version}
Obsoletes:      evince-browser-plugin < 41.2
Obsoletes:      nautilus-evince < 44.0

%description
Evince is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

Separate plugin packages, e.g. evince-plugin-pdfdocument, need to be present
for certain formats to be recognized.

%package -n libevdocument%{evdocument_so}
Summary:        GNOME Document Viewer System Library
Group:          System/Libraries

%description -n libevdocument%{evdocument_so}
Evince is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package -n libevview%{evview_so}
Summary:        GNOME Document Viewer System Library
Group:          System/Libraries

%description -n libevview%{evview_so}
Evince is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package -n typelib-1_0-EvinceDocument-%{typelibAPI}
Summary:        Introspection bindings for the Evince Document Viewer
Group:          System/Libraries

%description -n typelib-1_0-EvinceDocument-%{typelibAPI}
Evince is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package -n typelib-1_0-EvinceView-%{typelibAPI}
Summary:        Introspection bindings for the Evince Document Viewer
Group:          System/Libraries

%description -n typelib-1_0-EvinceView-%{typelibAPI}
Evince is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

%package devel
Summary:        Header files for the Evince Document Viewer
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       libevdocument%{evdocument_so} = %{version}
Requires:       libevview%{evview_so} = %{version}
Requires:       typelib-1_0-EvinceDocument-%{typelibAPI} = %{version}
Requires:       typelib-1_0-EvinceView-%{typelibAPI} = %{version}

%description devel
Evince is a document viewer capable of displaying single-page and multi-page
document formats like PDF and PostScript.

This package contains the header files for building additional plugins.

%package -n evince-plugin-comicsdocument
Summary:        Comics document support for Evince
Group:          Productivity/Office/Other
Requires:       %{name}
Enhances:       %{name}

%description -n evince-plugin-comicsdocument
A plugin for Evince to read Comics documents.

%package -n evince-plugin-djvudocument
Summary:        DjVu document support for Evince
Group:          Productivity/Office/Other
Requires:       %{name}
Enhances:       %{name}

%description -n evince-plugin-djvudocument
A plugin for Evince to read DjVu documents.

%package -n evince-plugin-dvidocument
Summary:        DVI document support for Evince
Group:          Productivity/Office/Other
Requires:       %{name}
Enhances:       %{name}

%description -n evince-plugin-dvidocument
A plugin for Evince to read DVI documents.

%package -n evince-plugin-pdfdocument
Summary:        PDF document support for Evince
Group:          Productivity/Office/Other
Requires:       %{name}
Supplements:    %{name}

%description -n evince-plugin-pdfdocument
A plugin for Evince to read PDF documents.

%package -n evince-plugin-psdocument
Summary:        PostScript document support for Evince
Group:          Productivity/Office/Other
Requires:       %{name}

%description -n evince-plugin-psdocument
A plugin for Evince to read PostScript documents.

%package -n evince-plugin-tiffdocument
Summary:        TIFF document support for Evince
Group:          Productivity/Office/Other
Requires:       %{name}
Enhances:       %{name}

%description -n evince-plugin-tiffdocument
A plugin for Evince to read TIFF images.

%package -n evince-plugin-xpsdocument
Summary:        XPS document support for Evince
Group:          Productivity/Office/Other
Requires:       %{name}
Enhances:       %{name}

%description -n evince-plugin-xpsdocument
A plugin for Evince to read XPS documents.

%lang_package

%prep
%setup
%if %{pkg_vcmp pkgconfig(synctex) < 1.19}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%endif
%autopatch -p1 -m 1000

%build
%meson \
	--libexecdir=%{_libexecdir}/%{name} \
	-D ps=enabled \
	-D nautilus=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C} --metainfo %{name}
%fdupes %{buildroot}/%{_prefix}

%ldconfig_scriptlets -n libevdocument%{evdocument_so}
%ldconfig_scriptlets -n libevview%{evview_so}

%files
%license COPYING
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.evince.Daemon.service
%{_datadir}/evince
%{_datadir}/glib-2.0/schemas/org.gnome.Evince.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Evince*
%{_datadir}/metainfo/org.gnome.Evince.metainfo.xml
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/evince.thumbnailer
# backends directory structure - backends go to their own packages
%dir %{_libdir}/evince/
%dir %{_libdir}/evince/%{pluginAPI}
%dir %{_libdir}/evince/%{pluginAPI}/backends
# helpers & daemon
%dir %{_libexecdir}/evince
%{_libexecdir}/evince/evinced
%{_mandir}/man?/*%{ext_man}
%{_userunitdir}/org.gnome.Evince.service

%files -n libevdocument%{evdocument_so}
%{_libdir}/libevdocument*.so.*

%files -n libevview%{evview_so}
%{_libdir}/libevview*.so.*

%files -n typelib-1_0-EvinceDocument-%{typelibAPI}
%{_libdir}/girepository-1.0/EvinceDocument-*.typelib

%files -n typelib-1_0-EvinceView-%{typelibAPI}
%{_libdir}/girepository-1.0/EvinceView-*.typelib

%files devel
%{_includedir}/evince
%{_libdir}/*.so
%{_libdir}/pkgconfig/evince*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/doc/libevview/
%{_datadir}/doc/libevdocument/

%files -n evince-plugin-comicsdocument
%{_datadir}/metainfo/evince-comicsdocument.metainfo.xml
%{_libdir}/evince/%{pluginAPI}/backends/comicsdocument.evince-backend
%{_libdir}/evince/%{pluginAPI}/backends/libcomicsdocument.so

%files -n evince-plugin-djvudocument
%{_datadir}/metainfo/evince-djvudocument.metainfo.xml
%{_libdir}/evince/%{pluginAPI}/backends/djvudocument.evince-backend
%{_libdir}/evince/%{pluginAPI}/backends/libdjvudocument.so

%files -n evince-plugin-dvidocument
%{_datadir}/metainfo/evince-dvidocument.metainfo.xml
%{_libdir}/evince/%{pluginAPI}/backends/dvidocument.evince-backend
%{_libdir}/evince/%{pluginAPI}/backends/libdvidocument.so

%files -n evince-plugin-pdfdocument
%{_datadir}/metainfo/evince-pdfdocument.metainfo.xml
%{_libdir}/evince/%{pluginAPI}/backends/pdfdocument.evince-backend
%{_libdir}/evince/%{pluginAPI}/backends/libpdfdocument.so

%files -n evince-plugin-psdocument
%{_datadir}/metainfo/evince-psdocument.metainfo.xml
%{_libdir}/evince/%{pluginAPI}/backends/psdocument.evince-backend
%{_libdir}/evince/%{pluginAPI}/backends/libpsdocument.so

%files -n evince-plugin-tiffdocument
%{_datadir}/metainfo/evince-tiffdocument.metainfo.xml
%{_libdir}/evince/%{pluginAPI}/backends/tiffdocument.evince-backend
%{_libdir}/evince/%{pluginAPI}/backends/libtiffdocument.so

%files -n evince-plugin-xpsdocument
%{_datadir}/metainfo/evince-xpsdocument.metainfo.xml
%{_libdir}/evince/%{pluginAPI}/backends/xpsdocument.evince-backend
%{_libdir}/evince/%{pluginAPI}/backends/libxpsdocument.so

%files lang -f %{name}.lang

%changelog
