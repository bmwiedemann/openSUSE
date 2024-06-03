#
# spec file for package parlatype
#
# Copyright (c) 2024 SUSE LLC
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


%define c_lib   libparlatype7
Name:           parlatype
Version:        4.2
Release:        0
Summary:        GNOME audio player for transcriptions
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.parlatype.xyz
Source:         https://github.com/gkarsay/parlatype/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  AppStream-devel
BuildRequires:  automake
BuildRequires:  glib2-devel >= 2.70
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk4-devel >= 4.10
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  libadwaita-devel >= 1.4
BuildRequires:  libtool
BuildRequires:  meson >= 0.47.2
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
%meson -Dpocketsphinx=false
%meson_build

%install
%meson_install

%find_lang %{name}
%find_lang xyz.parlatype.Parlatype %{no_lang_C} %{name}.lang
%find_lang %{c_lib}

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/parlatype
%{_mandir}/man1/parlatype.1%{?ext_man}
%{_datadir}/help/C/xyz.parlatype.Parlatype/
%{_datadir}/icons/hicolor/
%{_datadir}/applications/xyz.parlatype.Parlatype.desktop
%{_datadir}/dbus-1/services/xyz.parlatype.Parlatype.service
%{_datadir}/glib-2.0/schemas/xyz.parlatype.Parlatype.gschema.xml
%{_datadir}/metainfo/xyz.parlatype.Parlatype.metainfo.xml

%files -n libparlatype-devel
%{_libdir}/libparlatype.so
%{_includedir}/parlatype/
%{_libdir}/pkgconfig/parlatype.pc

%files -n %{c_lib}
%{_libdir}/libparlatype.so.*

%files lang -f %{name}.lang

%files lang -f %{c_lib}.lang

%changelog
