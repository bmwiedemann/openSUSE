#
# spec file for package drumstick
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           drumstick
Version:        1.1.2
Release:        0
Summary:        MIDI Sequencer C++ Library Bindings
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            http://drumstick.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE
Patch:          Dont-use-QOverload.patch
BuildRequires:  alsa-devel
BuildRequires:  cmake >= 2.8.11
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  kf5-filesystem
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Requires(post): shared-mime-info
Requires(postun): shared-mime-info

%description
This package includes test and example programs for drumstick libraries.

%package -n libdrumstick-rt1
Summary:        MIDI Sequencer C++ Library
Group:          System/Libraries
Requires:       libdrumstick-rt-plugins

%description -n libdrumstick-rt1
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes a class for managing realtime MIDI input/output backends.

%package -n libdrumstick-rt-plugins
Summary:        MIDI Sequencer C++ Library
Group:          System/Libraries

%description -n libdrumstick-rt-plugins
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This package contains input/output plugins for libdrumstick-rt1.

%package -n libdrumstick-file1
Summary:        MIDI Sequencer C++ Library
Group:          System/Libraries

%description -n libdrumstick-file1
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes classes providing file input and output in formats
commonly used by MIDI programs. Currently, SMF (standard MIDI file)
read/write and WRK (Cakewalk) file read are supported. This library does not
depend on ALSA.

%package -n libdrumstick-alsa1
Summary:        MIDI Sequencer C++ Library
Group:          System/Libraries

%description -n libdrumstick-alsa1
MIDI Sequencer C++ Library Bindings for Qt5 and ALSA.
This library includes the ALSA Sequencer library classes, providing MIDI
recording and playback functionality to C++/Qt5 programs.

%package -n libdrumstick-devel
Summary:        Development package for the libdrumstick library
Group:          Development/Libraries/C and C++
Requires:       alsa-devel
Requires:       glibc-devel
Requires:       libdrumstick-alsa1 = %{version}
Requires:       libdrumstick-file1 = %{version}
Requires:       libdrumstick-rt1 = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig(Qt5Core)

%description -n libdrumstick-devel
This package contains the files needed to compile programs that use the
libdrumstick libraries.

%package -n libdrumstick-doc
Summary:        Development documentation package for the drumstick libraries
Group:          Documentation/Other
BuildArch:      noarch

%description -n libdrumstick-doc
This package contains the developer's documentation of the drumstick libraries.

%prep
%setup -q
%if 0%{?suse_version} < 1500
%patch -p1
%endif

%build
%cmake_kf5  -- -DSTATIC_DRUMSTICK=0
%make_jobs
make %{?_smp_mflags} doxygen

%install
%make_install
%suse_update_desktop_file -n drumstick-drumgrid Midi
%suse_update_desktop_file -n drumstick-guiplayer Midi
%suse_update_desktop_file -n drumstick-vpiano Midi

%post
%mime_database_post
/sbin/ldconfig

%postun
%mime_database_postun
/sbin/ldconfig

%post -n libdrumstick-file1 -p /sbin/ldconfig
%postun -n libdrumstick-file1 -p /sbin/ldconfig
%post -n libdrumstick-alsa1 -p /sbin/ldconfig
%postun -n libdrumstick-alsa1 -p /sbin/ldconfig
%post -n libdrumstick-rt1 -p /sbin/ldconfig
%postun -n libdrumstick-rt1 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README TODO ChangeLog
%{_bindir}/%{name}-*
%{_datadir}/applications/%{name}-*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_mandir}/man1/%{name}-*.1%{?ext_man}

%files -n libdrumstick-rt1
%license COPYING
%{_libdir}/libdrumstick-rt.so.*

%files -n libdrumstick-rt-plugins
%license COPYING
%{_libdir}/drumstick/

%files -n libdrumstick-file1
%license COPYING
%{_datadir}/mime/packages/%{name}.xml
%{_libdir}/libdrumstick-file.so.*

%files -n libdrumstick-alsa1
%license COPYING
%{_libdir}/libdrumstick-alsa.so.*

%files -n libdrumstick-devel
%license COPYING
%dir %{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_includedir}/%{name}/*.h
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-rt.so
%{_libdir}/pkgconfig/%{name}-*.pc

%files -n libdrumstick-doc
%doc doc/html/*

%changelog
