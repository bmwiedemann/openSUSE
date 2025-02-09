#
# spec file for package drumstick
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2005-2010 Pedro Lopez-Cabanillas <plcl@users.sourceforge.net>
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


Name:           drumstick
Version:        2.10.0
Release:        0
Summary:        MIDI Sequencer C++ Library Bindings
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://drumstick.sourceforge.io/
Source:         https://sourceforge.net/projects/drumstick/files/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(sonivox)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse-simple)

%description
This package includes test and example programs for drumstick libraries.

%lang_package

%package mimetypes
Summary:        MIDI Sequencer C++ Library MIME types
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Conflicts:      libdrumstick-file1

%description mimetypes
This package includes a mimetype for Cakewalk project files.

%package -n libdrumstick-rt2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Requires:       libdrumstick-rt2-plugins

%description -n libdrumstick-rt2
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes a class for managing realtime MIDI input/output backends.

%package -n libdrumstick-rt2-plugins
Summary:        MIDI Sequencer C++ Library
License:        Apache-2.0 AND GPL-2.0-or-later AND GPL-3.0-or-later

%description -n libdrumstick-rt2-plugins
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This package contains input/output plugins for libdrumstick-rt2.

%package -n libdrumstick-file2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Recommends:     drumstick-mimetypes

%description -n libdrumstick-file2
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes classes providing file input and output in formats
commonly used by MIDI programs. Currently, SMF (standard MIDI file)
read/write and WRK (Cakewalk) file read are supported. This library does not
depend on ALSA.

%package -n libdrumstick-alsa2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later

%description -n libdrumstick-alsa2
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes the ALSA Sequencer library classes, providing MIDI
recording and playback functionality to C++/Qt5 programs.

%package -n libdrumstick-widgets2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
# for the lang_package
Provides:       libdrumstick-widgets = %{version}

%description -n libdrumstick-widgets2
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes the Widgets library, providing
GUI, MIDI related, components for C++/Qt5 programs.

%lang_package -n libdrumstick-widgets

%package -n libdrumstick-devel
Summary:        Development package for the libdrumstick library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Requires:       alsa-devel
Requires:       glibc-devel
Requires:       libdrumstick-alsa2 = %{version}
Requires:       libdrumstick-file2 = %{version}
Requires:       libdrumstick-rt2 = %{version}
Requires:       libdrumstick-widgets2 = %{version}
Requires:       libstdc++-devel
Requires:       cmake(Qt6Core)

%description -n libdrumstick-devel
This package contains the files needed to compile programs that use the
libdrumstick libraries.

%package -n libdrumstick-doc
Summary:        Development documentation package for the drumstick libraries
License:        GPL-2.0-or-later AND GPL-3.0-or-later
BuildArch:      noarch

%description -n libdrumstick-doc
This package contains the developer's documentation of the drumstick libraries.

%prep
%autosetup -p1

# Update obsolete config file
doxygen -u Doxyfile.in
sed -i 's#%{_includedir}/QtCore#%{_includedir}/qt6/QtCore#' Doxyfile.in
sed -i 's#%{_includedir}/QtGui#%{_includedir}/qt6/QtGui#' Doxyfile.in

%build
%cmake_qt6 -DSTATIC_DRUMSTICK=0

%qt6_build

cmake --build %{__qt6_builddir} -t doxygen

%install
%qt6_install

%ldconfig_scriptlets
%ldconfig_scriptlets -n libdrumstick-alsa2
%ldconfig_scriptlets -n libdrumstick-file2
%ldconfig_scriptlets -n libdrumstick-rt2
%ldconfig_scriptlets -n libdrumstick-widgets2

%files
%license COPYING
%doc AUTHORS NEWS TODO ChangeLog
%{_bindir}/drumstick-*
%{_datadir}/applications/net.sourceforge.drumstick-*.desktop
%{_datadir}/icons/hicolor/*/apps/drumstick.png
%{_datadir}/icons/hicolor/scalable/apps/drumstick.svgz
%{_datadir}/metainfo/net.sourceforge.drumstick-*.xml
%{_mandir}/man1/drumstick-*.1%{?ext_man}

%files lang
%license COPYING
%dir %{_datadir}/drumstick
%{_datadir}/drumstick/drumstick-drumgrid_*.qm
%{_datadir}/drumstick/drumstick-guiplayer_*.qm
%{_datadir}/drumstick/drumstick-vpiano_*.qm

%files mimetypes
%{_datadir}/mime/packages/drumstick.xml

%files -n libdrumstick-rt2
%license COPYING
%{_libdir}/libdrumstick-rt.so.*

%files -n libdrumstick-rt2-plugins
%license COPYING
%{_libdir}/drumstick2/

%files -n libdrumstick-file2
%license COPYING
%{_libdir}/libdrumstick-file.so.*

%files -n libdrumstick-alsa2
%license COPYING
%{_libdir}/libdrumstick-alsa.so.*

%files -n libdrumstick-widgets2
%license COPYING
%{_libdir}/libdrumstick-widgets.so.*

%files -n libdrumstick-widgets-lang
%license COPYING
%dir %{_datadir}/drumstick
%{_datadir}/drumstick/drumstick-widgets_*.qm

%files -n libdrumstick-devel
%license COPYING
%dir %{_includedir}/drumstick
%{_includedir}/drumstick.h
%{_includedir}/drumstick/*.h
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-rt.so
%{_libdir}/libdrumstick-widgets.so
%{_libdir}/pkgconfig/drumstick-*.pc
%{_libdir}/cmake/drumstick
%dir %{_qt6_pluginsdir}/designer
%{_qt6_pluginsdir}/designer/libdrumstick-vpiano-plugin.so

%files -n libdrumstick-doc
%doc build/doc/html/*

%changelog
