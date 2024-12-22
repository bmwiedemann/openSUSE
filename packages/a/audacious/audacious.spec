#
# spec file for package audacious
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


%define aud_plugin_ver_min 4.4
%define aud_plugin_ver_max 4.4.99
%define core_soname 5
%define gtk_soname 6
%define qt_soname 3
%define tag_soname 3

%if 0%{?suse_version} < 1600
# on Leap/SLE 15 force gcc-13 as QT6 requires C++17 compatibility
%define force_gcc_version 13
%endif

Name:           audacious
Version:        4.4.2
Release:        0
Summary:        Audio player with graphical UI and library functionality
License:        BSD-2-Clause
URL:            https://audacious-media-player.org/
Source:         https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
Requires:       %{name}-plugins%{?_isa} <= %{aud_plugin_ver_max}
Requires:       %{name}-plugins%{?_isa} >= %{aud_plugin_ver_min}
Recommends:     %{name}-plugins-extra >= %{aud_plugin_ver_min}

%description
Audacious is an audio player. It is based on Qt and supports a wide
range of audio codecs. It still features an alternative skinned user
interface (based on Winamp 2.x skins). Historically, it started as a
fork of a fork of XMMS.

%lang_package

%package -n libaudcore%{core_soname}
Summary:        Main functionality library of Audacious
Provides:       libaudcore%{?_isa} = %{version}

%description -n libaudcore%{core_soname}
Library from the Audacious audio player.

%package -n libaudqt%{qt_soname}
Summary:        Qt GUI implementation of Audacious
Requires:       libaudcore%{core_soname} >= %{version}

%description -n libaudqt%{qt_soname}
Library from the Audacious audio player.

%package -n libaudgui%{gtk_soname}
Summary:        GTK GUI implementation of Audacious
Requires:       libaudcore%{core_soname} >= %{version}

%description -n libaudgui%{gtk_soname}
Library from the Audacious audio player.

%package -n libaudtag%{tag_soname}
Summary:        ID3 and APE metadata support for Audacious
Requires:       libaudcore%{core_soname} >= %{version}

%description -n libaudtag%{tag_soname}
Library from the Audacious audio player.

%package devel
Summary:        Development files for Audacious
Requires:       libaudcore%{core_soname} = %{version}
Requires:       libaudgui%{gtk_soname} = %{version}
Requires:       libaudqt%{qt_soname} = %{version}
Requires:       libaudtag%{tag_soname} = %{version}

%description devel
Development files for Audacious audio player.

%prep
%setup -q

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif

# append this to $PATH as Leap/SLE 15 have the QT6 binaries there
export PATH="%{_libdir}/qt6/libexec:$PATH"

%meson \
  -Dqt=true  \
  -Dgtk=true  \
%meson_build

%install
%meson_install

install -Dpm 0644 contrib/%{name}.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%post -n libaudcore%{core_soname} -p /sbin/ldconfig

%postun -n libaudcore%{core_soname} -p /sbin/ldconfig

%post -n libaudqt%{qt_soname} -p /sbin/ldconfig

%postun -n libaudqt%{qt_soname} -p /sbin/ldconfig

%post -n libaudgui%{gtk_soname} -p /sbin/ldconfig

%postun -n libaudgui%{gtk_soname} -p /sbin/ldconfig

%post -n libaudtag%{tag_soname} -p /sbin/ldconfig

%postun -n libaudtag%{tag_soname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_bindir}/audtool
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_mandir}/man?/audtool.?%{?ext_man}

%files lang -f %{name}.lang

%files -n libaudcore%{core_soname}
%{_libdir}/libaudcore.so.%{core_soname}*

%files -n libaudqt%{qt_soname}
%{_libdir}/libaudqt.so.%{qt_soname}*

%files -n libaudgui%{gtk_soname}
%{_libdir}/libaudgui.so.%{gtk_soname}*

%files -n libaudtag%{tag_soname}
%{_libdir}/libaudtag.so.%{tag_soname}*

%files devel
%{_includedir}/%{name}/
%{_includedir}/libaudcore/
%{_libdir}/libaudcore.so
%{_includedir}/libaudqt/
%{_libdir}/libaudqt.so
%{_includedir}/libaudgui/
%{_libdir}/libaudgui.so
%{_libdir}/libaudtag.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
