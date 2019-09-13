#
# spec file for package hydrogen
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soversion 1
%define soage 0
%define sorevision 0
%define tarvers 1.0.0
# WARNING: ATM librubberband2 support is experimental currently it is recommended that you disable
# this config option to ensure backwards compatibility with songs created under 0.9.5 which use
# rubberband. Use the rubberband -cli package instead.
%define librubberband 0
Name:           hydrogen
Version:        0.9.9pre1
Release:        0
Summary:        A Real-Time Drum Machine and Sequencer
# NOTE: Don't forget to update the libsuffix macro.
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
Url:            http://www.hydrogen-music.org/
Source0:        https://github.com/hydrogen-music/%{name}/archive/%{tarvers}-beta1.tar.gz#/%{name}-%{version}.tar.gz
Source1:        h2cli.1
Source2:        COPYING
# Remove current date and time from sources.
Patch1:         hydrogen-no-current-time.patch
# libhydrogencore has no soname and installs in _libexecdir
Patch2:         hydrogen-0.9.6-lib64.patch
# PATCH-FIX-UPSTREAM hydrogen-gcc47.patch boris@steki.net -- Fix build with gcc 4.7.
Patch3:         hydrogen-gcc47.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  util-linux
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
#pkgconfig(ladspa-1.13)
%if 0%{?librubberband} == 1
BuildRequires:  pkgconfig(rubberband)
%else
BuildRequires:  rubberband-cli
Requires:       rubberband-cli
%endif

%description
Hydrogen is a software synthesizer which can be used alone, emulating
a drum machine based on patterns, or via an external MIDI
keyboard/sequencer software.

It features a modular and graphical interface based on QT4, has a
sample-based stereo audio engine, with import of sound samples in PCM
formats. Furthermore, a pattern-based sequencer with the ability to
chain patterns into a song. Up to 64 ticks per pattern with
individual level per event and variable pattern length are possible.
32 instrument tracks with volume, mute, solo, pan capabilities are
provided, and there is multi-layer support for instruments (up to 16
samples for each instrument). Human velocity, human time, pitch and
swing functions are implemented as well.

%package -n libhydrogen-core%{soversion}
Summary:        Library essential for the hydrogen drum machine software
Group:          System/Libraries

%description -n libhydrogen-core%{soversion}
Hydrogen is a software synthesizer which can be used alone, emulating
a drum machine based on patterns, or via an external MIDI
keyboard/sequencer software.

This library is the core of hydrogen's operation.

%package -n libhydrogen-core-devel
Summary:        Development files and headers for libhydrogen-core
Group:          Development/Libraries/C and C++
Requires:       libhydrogen-core%{soversion} = %{version}-%{release}

%description -n libhydrogen-core-devel
These are the headers needed to develop apps that
link with libhydrogen-core.

%prep
%setup -q -n %{name}-%{tarvers}-beta1

%autopatch -p1

# copy licence with correct fsf address
install -m 0644 %{SOURCE2} ./

%build

%cmake \
	-DWANT_SHARED:BOOL=on \
	-DWANT_LIBARCHIVE:BOOL=on \
	-DWANT_LRDF:BOOL=off \
	-DLADSPA_INCLUDE_DIR:PATH=%{_includedir} \
	-DLADSPA_LIBRARIES:PATH=%{_libdir}/ladspa \
	-DCMAKE_CURRENT_LIBRARY_DIR:PATH="%{_lib}" \
	-Dcoreversion:STRING=%{soversion} \
	-Dsoage:STRING=%{soage} \
	-Dsorevision:STRING=%{sorevision}

# For some reason cmake won't produce a correct soname with only the version so this is a hack to fix it.
pushd src/core/CMakeFiles/hydrogen-core.dir && \
cat link.txt|sed 's/-soname,libhydrogen-core.so.%{tarvers}/-soname,libhydrogen-core.so.%{soversion}/'>\
link.txt~;mv link.txt~ link.txt

cat relink.txt|sed 's/-soname,libhydrogen-core.so.%{tarvers}/-soname,libhydrogen-core.so.%{soversion}/'>\
relink.txt~;mv relink.txt~ relink.txt

popd

make %{?_smp_mflags}

# LD_LIBRARY_PATH=%%{_libdir}/mpi/gcc/openmpi/%%{_lib}
# LD_RUN_PATH=%%{_libdir}

%install

#export QTDIR=%%{_libdir}/qt4/
%cmake_install VERBOSE_MAKEFILE=1
mkdir -p %{buildroot}%{_libdir} && cp -v build/src/core/libhydrogen-core.so.%{tarvers} %{buildroot}%{_libdir}/
# libhydrogen-core's internal SONAME = libhydrogen-core.so.0 so we provide a link.
pushd %{buildroot}%{_libdir} && ln -s libhydrogen-core.so.%{tarvers} libhydrogen-core.so.%{soversion}
ln -s libhydrogen-core.so.%{tarvers} libhydrogen-core.so
popd

# Install the h2cli man page created by help2man
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
# Move hydrogen man page to the correct directory
mv %{buildroot}%{_prefix}/man/man1/hydrogen.1 %{buildroot}%{_mandir}/man1/

# temporary link i18n files from usr/share/hydrogen/data/i18n to _datadir/locale for find_lang to find.
ln -s %{_datadir}/hydrogen/data/i18n %{buildroot}%{_datadir}/locale
%find_lang %{name} %{name}.lang --without-kde --with-qt --all-name --without-mo
rm -rf %{buildroot}%{_datadir}/locale
cat %{name}.lang

# Set executable bit on scripts in buildroot/_datadir/name/data/i18n
for i in $(find %{buildroot}%{_datadir}/hydrogen/data/i18n -type f -perm 0644 -print0|xargs -0r grep -l '#!'); \
do chmod 0755 ${i}; done
rm -f %{buildroot}%{_datadir}/hydrogen/data/i18n/stats.py

%fdupes -s %{buildroot}%{_datadir}

# Make icon avalable for desktop file
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/ \
&& pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ln -s ../../../../%{name}/data/img/gray/h2-icon.svg h2-icon.svg
#usr/share/hydrogen/data/img/gray/h2-icon.svg
popd && %suse_update_desktop_file -i %{name} AudioVideo Sequencer

%post
%desktop_database_post

%postun
%desktop_database_postun

%files -f %{name}.lang
%{_bindir}/*
%doc AUTHORS ChangeLog README.txt
%license COPYING
%dir %{_datadir}/%{name}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/appdata
%{_mandir}/man1/hydrogen.1%{ext_man}
%{_mandir}/man1/h2cli.1%{ext_man}
%{_datadir}/%{name}/data/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/h2-icon.svg
%{_datadir}/pixmaps/h2-icon.svg

%post -n libhydrogen-core%{soversion} -p /sbin/ldconfig
%postun -n libhydrogen-core%{soversion} -p /sbin/ldconfig

%files -n libhydrogen-core%{soversion}
%{_libdir}/libhydrogen-core.so.%{soversion}*

%files -n libhydrogen-core-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libhydrogen-core.so

%changelog
