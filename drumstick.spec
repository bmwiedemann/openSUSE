#
# spec file for package drumstick
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.1.1
Release:        0
Summary:        MIDI Sequencer C++ Library Bindings
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
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
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets) >= 5.11.0
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse-simple)

%description
This package includes test and example programs for drumstick libraries.

%lang_package

%package mimetypes
Summary:        MIDI Sequencer C++ Library MIME types
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
Conflicts:      libdrumstick-file1

%description mimetypes
This package includes a mimetype for Cakewalk project files.

%package -n libdrumstick-rt2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Libraries
Requires:       libdrumstick-rt2-plugins

%description -n libdrumstick-rt2
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes a class for managing realtime MIDI input/output backends.

%package -n libdrumstick-rt2-plugins
Summary:        MIDI Sequencer C++ Library
License:        Apache-2.0 AND GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Libraries

%description -n libdrumstick-rt2-plugins
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This package contains input/output plugins for libdrumstick-rt2.

%package -n libdrumstick-file2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Libraries
Recommends:     %{name}-mimetypes

%description -n libdrumstick-file2
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes classes providing file input and output in formats
commonly used by MIDI programs. Currently, SMF (standard MIDI file)
read/write and WRK (Cakewalk) file read are supported. This library does not
depend on ALSA.

%package -n libdrumstick-alsa2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Libraries

%description -n libdrumstick-alsa2
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes the ALSA Sequencer library classes, providing MIDI
recording and playback functionality to C++/Qt5 programs.

%package -n libdrumstick-widgets2
Summary:        MIDI Sequencer C++ Library
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Libraries
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
Group:          Development/Libraries/C and C++
Requires:       alsa-devel
Requires:       glibc-devel
Requires:       libdrumstick-alsa2 = %{version}
Requires:       libdrumstick-file2 = %{version}
Requires:       libdrumstick-rt2 = %{version}
Requires:       libdrumstick-widgets2 = %{version}
Requires:       libstdc++-devel
Requires:       cmake(Qt5Core)

%description -n libdrumstick-devel
This package contains the files needed to compile programs that use the
libdrumstick libraries.

%package -n libdrumstick-doc
Summary:        Development documentation package for the drumstick libraries
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description -n libdrumstick-doc
This package contains the developer's documentation of the drumstick libraries.

%prep
%setup -q

# Update obsolete config file
doxygen -u Doxyfile.in
sed -i 's#%{_includedir}/QtCore#%{_includedir}/qt5/QtCore#' Doxyfile.in
sed -i 's#%{_includedir}/QtGui#%{_includedir}/qt5/QtGui#' Doxyfile.in

%build
%cmake -DSTATIC_DRUMSTICK=0 -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
make %{?_smp_mflags} doxygen

%install
%cmake_install
%suse_update_desktop_file -n drumstick-drumgrid Midi
%suse_update_desktop_file -n drumstick-guiplayer Midi
%suse_update_desktop_file -n drumstick-vpiano Midi

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libdrumstick-file2 -p /sbin/ldconfig
%postun -n libdrumstick-file2 -p /sbin/ldconfig
%post -n libdrumstick-alsa2 -p /sbin/ldconfig
%postun -n libdrumstick-alsa2 -p /sbin/ldconfig
%post -n libdrumstick-rt2 -p /sbin/ldconfig
%postun -n libdrumstick-rt2 -p /sbin/ldconfig
%post -n libdrumstick-widgets2 -p /sbin/ldconfig
%postun -n libdrumstick-widgets2 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS TODO ChangeLog
%{_bindir}/%{name}-*
%{_datadir}/applications/%{name}-*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_mandir}/man1/%{name}-*.1%{?ext_man}

%files lang
%license COPYING
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/drumstick-drumgrid_*.qm
%{_datadir}/%{name}/drumstick-guiplayer_*.qm
%{_datadir}/%{name}/drumstick-vpiano_*.qm

%files mimetypes
%{_datadir}/mime/packages/%{name}.xml

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
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/drumstick-widgets_*.qm

%files -n libdrumstick-devel
%license COPYING
%dir %{_includedir}/%{name}
%dir %{_libqt5_plugindir}/designer
%{_includedir}/%{name}.h
%{_includedir}/%{name}/*.h
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-rt.so
%{_libdir}/libdrumstick-widgets.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_libdir}/cmake/%{name}
%{_libqt5_plugindir}/designer/libdrumstick-vpiano-plugin.so

%files -n libdrumstick-doc
%doc build/doc/html/*

%changelog
