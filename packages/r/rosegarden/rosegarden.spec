#
# spec file for package rosegarden
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


%define vers    22.12

Name:           rosegarden
Version:        24.06
Release:        0
License:        GPL-2.0-or-later
Summary:        Midi, Audio And Notation Editor
URL:            https://www.rosegardenmusic.com/
Group:          Productivity/Multimedia/Sound/Midi
Source0:        https://github.com/tedfelix/%{name}-official/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.xpm
Source2:        %{name}.1
# PATCH-FIX-OPENSUSE davejplater@gmail.com This patch fixes the file search paths for examples, templates and midi driver libraries.
Patch1:         rosegarden-10.10-filepaths.patch
# PATCH-FIX-OPENSUSE ledest@gmail.com fix bashisms in scripts
Patch2:         rosegarden-14.02-fix-bashisms.patch
# PATCH-FIX-OPENSUSE port scripts/sf2rg.py to Python 3
Patch3:         scripts-sf2rg-python3.patch
BuildRequires:  alsa-devel
BuildRequires:  cmake >= 2.8.12
BuildRequires:  dssi-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  liblrdf-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lilypond-fonts-common >= 2.20
BuildRequires:  lirc-devel
BuildRequires:  pkg-config
BuildRequires:  zstd
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
#BuildRequires:  pkgconfig(libxml++-2.6)
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       dssi
Requires:       ladspa
Requires:       ladspa-swh-plugins
Requires:       lilypond-fonts-common >= 2.20
Requires:       xsynth-dssi
Recommends:     fluidsynth-dssi
Recommends:     jack
Recommends:     qsynth
Icon:           rosegarden.xpm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    i586 i686

%description
Rosegarden is a well-rounded audio and MIDI sequencer,
score editor, and general-purpose music composition and
editing environment. Rosegarden is an easy-to-learn,
attractive application that runs on Linux, ideal for
composers, musicians, music students, and small studio or
home recording environments.

%prep
%setup -q -n %{name}-official-%{version}
%autopatch -p1

# When we build svn we need to execute bootstrap.sh
#sh bootstrap.sh
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

%build
#export DEBUG_LADSPA
#export QTDIR=/usr/
export CFLAGS="%{optflags} -fno-strict-aliasing -ggdb"
export CXXFLAGS="$CFLAGS"
# -fmessage-length=0 -O2 -fno-strict-aliasing -Wall -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables
# Now uses cmake
#%%configure --enable-debug --localedir=%%{_datadir}/%%{name}/locale/
%cmake \
       -DCMAKE_INSTALL_LOCALEDIR:PATH=%{_datadir}/locale/

#make svnheader
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/scripts
cp -p scripts/* %{buildroot}%{_datadir}/%{name}/scripts/
cp -r data/* %{buildroot}%{_datadir}/%{name}/

pushd build
%make_install
popd
rm -rf %{buildroot}%{_datadir}/%{name}/desktop
rm -rf %{buildroot}%{_datadir}/%{name}/mime
rm -f %{buildroot}%{_datadir}/%{name}/*.cpp
rm -f %{buildroot}%{_datadir}/%{name}/*.o
chmod 755 %{buildroot}%{_datadir}/%{name}/scripts/*
chmod 644 %{buildroot}%{_datadir}/%{name}/scripts/lircrc.rosegarden
chmod 644 %{buildroot}%{_datadir}/%{name}/scripts/README
chmod 644 %{buildroot}%{_datadir}/%{name}/scripts/color-list
#chmod 644 %%{buildroot}%%{_datadir}/%%{name}/scripts/simple-makefile
rm -f %{buildroot}%{_datadir}/%{name}/scripts/svn-to-hg-and-git.sh
install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/pixmaps/%{name}.xpm"
%suse_update_desktop_file %{buildroot}/%{_datadir}/applications/com.rosegardenmusic.%{name}.desktop
#This is a man page made by help2man to satisfy factories hunger for one /usr/bin/ one man page.
mkdir -p %{buildroot}%{_mandir}/man1
install -D -m 0644 "%{SOURCE2}" "%{buildroot}%{_mandir}/man1/"
%fdupes -s %{buildroot}%{_datadir}/

%files
%defattr(-,root,root)
%doc AUTHORS README.md
%license COPYING
%dir %{_datadir}/metainfo
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/autoload
%dir %{_datadir}/%{name}/chords
%dir %{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/fonts
%dir %{_datadir}/%{name}/library
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/profile
%dir %{_datadir}/%{name}/scripts
%dir %{_datadir}/%{name}/styles
%dir %{_datadir}/%{name}/templates
%dir %{_datadir}/%{name}/templates
%{_datadir}/icons/hicolor/*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/com.rosegardenmusic.%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_bindir}/%{name}
%{_libdir}/lib%{name}private.so
%{_mandir}/man1/*
%{_datadir}/%{name}/*
%{_datadir}/%{name}/presets/*
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/%{name}/autoload/*
%{_datadir}/%{name}/chords/*
%{_datadir}/%{name}/examples/*
%{_datadir}/%{name}/fonts/*
%{_datadir}/%{name}/library/*
%{_datadir}/%{name}/locale/*
%{_datadir}/%{name}/profile/*
%{_datadir}/%{name}/scripts/*
%{_datadir}/%{name}/styles/*
%{_datadir}/%{name}/templates/*
%{_datadir}/mime/packages/%{name}.xml

%changelog
