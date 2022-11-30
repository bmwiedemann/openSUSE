#
# spec file for package aravis
#
# Copyright (c) 2022 SUSE LLC
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


%define url_ver %(echo %{version}|cut -d. -f1,2)
%define api   0.8
%define sover 0
%define sorel %(echo %{api} | tr . _)
%define libname lib%{name}-%{sorel}-%{sover}
%define devname lib%{name}-%{sorel}-devel
%define typelibname typelib-1_0-Aravis-%{api}
Name:           aravis
Version:        0.8.22
Release:        0
Summary:        Glib/gobject based library implementing a Genicam interface
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/AravisProject/aravis
Source0:        https://github.com/AravisProject/%{name}/releases/download/%{version}/aravis-%{version}.tar.xz
BuildRequires:  %{python_module gobject}
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gi-docgen) >= 2021.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Aravis is a glib/gobject based library implementing a Genicam interface,
which can be used for the acquisition of video streams coming from either
ethernet, firewire or USB cameras. It currently only implements an ethernet
camera protocol used for industrial cameras.

%package viewer
Summary:        Glib/gobject based library implementing a Genicam interface
Group:          Productivity/Multimedia/Video/Players
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-base
Recommends:     gstreamer-plugins-good

%description viewer
This package contains arv-viewer, GUI application for aravis.

%package -n %{libname}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{libname}
Aravis is a glib/gobject based library implementing a Genicam interface,
which can be used for the acquisition of video streams coming from either
ethernet, firewire or USB cameras. It currently only implements an ethernet
camera protocol used for industrial cameras.

This package contains the shared library for %{name}.

%package -n %{typelibname}
Summary:        Introspection bindings for %{name}
Group:          System/Libraries

%description -n %{typelibname}
This package provides the GObject Introspection bindings for %{name}.

%package -n gstreamer-plugin-%{name}
Summary:        Gstreamer support for %{name}
Group:          Productivity/Multimedia/Other

%description -n gstreamer-plugin-%{name}
This package contains the gstreamer plugin for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{devname}
This package contains the development files for %{name}

%prep
%setup -q

%build
%meson -Ddocumentation=enabled
%meson_build

%install
%meson_install

%suse_update_desktop_file -r arv-viewer-%{api} AudioVideo AudioVideoEditing

%find_lang %{name}-%{api}

%check
%meson_test

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/arv-camera-test-%{api}
%{_bindir}/arv-fake-gv-camera-%{api}
%{_bindir}/arv-test-%{api}
%{_bindir}/arv-tool-%{api}
%{_mandir}/man1/arv-tool-*

%files viewer -f %{name}-%{api}.lang
%{_bindir}/arv-viewer-%{api}
%{_mandir}/man1/arv-viewer-*
%{_datadir}/icons/hicolor/*/apps/aravis*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/arv-viewer-%{api}.appdata.xml
%{_datadir}/applications/arv-viewer-%{api}.desktop

%files -n %{libname}
%license COPYING
%doc AUTHORS README.md NEWS.md
%{_libdir}/libaravis-%{api}.so.*

%files -n %{typelibname}
%{_libdir}/girepository-1.0/Aravis-%{api}.typelib

%files -n gstreamer-plugin-%{name}
%{_libdir}/gstreamer-1.0/libgstaravis.%{api}.so
%exclude %{_libdir}/gstreamer-1.0/libgstaravis.%{api}.la

%files -n %{devname}
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/doc/%{name}-%{api}
%{_datadir}/gir-1.0/Aravis-%{api}.gir

%changelog
