#
# spec file for package parlatype
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define c_lib   libparlatype1
Name:           parlatype
Version:        1.5.6
Release:        0
Summary:        GNOME audio player for transcriptions
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://gkarsay.github.io/parlatype/
Source:         https://github.com/gkarsay/parlatype/releases/download/v%{version}/parlatype-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
Requires:       %{c_lib} = %{version}
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-ugly
Recommends:     %{name}-lang

%description
Parlatype is a minimal audio player for manual speech transcription, written for the GNOME desktop environment. It plays audio sources to transcribe them in your favourite text application.

%package -n libparlatype-devel
Summary:        Development files for parlatype
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description -n libparlatype-devel
Parlatype ships its own library, libparlatype, which provides a GStreamer backend (PtPlayer) and a waveviewer widget (PtWaveviewer) which is a GtkWidget.

%package -n %{c_lib}
Summary:        Library for parlatype
Group:          System/Libraries
Recommends:     libparlatype-lang

%description -n %{c_lib}
Parlatype ships its own library, libparlatype, which provides a GStreamer backend (PtPlayer) and a waveviewer widget (PtWaveviewer) which is a GtkWidget.

%lang_package

%prep
%setup -q

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libparlatype.la

%find_lang %{name}
%find_lang libparlatype

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/parlatype
%{_mandir}/man1/parlatype.1%{?ext_man}
%{_datadir}/applications/com.github.gkarsay.parlatype.desktop
%{_datadir}/metainfo/com.github.gkarsay.parlatype.appdata.xml
%{_datadir}/metainfo/com.github.gkarsay.parlatype.libreoffice-helpers.metainfo.xml
%{_datadir}/help/
%{_datadir}/icons/hicolor/
%{_libdir}/libreoffice/share/Scripts/python/Parlatype.py
%{_datadir}/dbus-1/services/com.github.gkarsay.parlatype.service
%{_datadir}/glib-2.0/schemas/com.github.gkarsay.parlatype.gschema.xml
%{_libdir}/girepository-1.0/Parlatype-1.0.typelib
%dir %{_libdir}/libreoffice
%dir %{_libdir}/libreoffice/share
%dir %{_libdir}/libreoffice/share/Scripts
%dir %{_libdir}/libreoffice/share/Scripts/python

%files -n libparlatype-devel
%{_libdir}/libparlatype.so
%{_includedir}/parlatype/
%{_datadir}/gtk-doc/
%{_libdir}/pkgconfig/parlatype.pc
%{_datadir}/gir-1.0/Parlatype-1.0.gir

%files -n %{c_lib}
%{_libdir}/libparlatype.so.*

%files lang -f %{name}.lang

%files lang -f libparlatype.lang
%{_datadir}/locale/*/LC_MESSAGES/libparlatype.*

%changelog
