#
# spec file for package praat
#
# Copyright (c) 2023 SUSE LLC
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


Name:           praat
Version:        6.3.03
Release:        0
Summary:        Phonetics by computer
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Other
URL:            http://www.praat.org
Source0:        https://github.com/praat/praat/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source3:        %{name}.changes
# PATCH-FIX-OPENSUSE praat-use_system_libs.patch -- replace some embedded libs with system ones
Patch1:         praat-use_system_libs.patch
# PATCH-FIX-OPENSUSE praat-no-return-in-nonvoid.patch -- make the compiler happy
Patch2:         praat-no-return-in-nonvoid.patch
# PATCH-FEATURE-OPENSUSE praat-allow-system-flags.patch badshah400@gmail.com -- Allow compilation and linker flags to incorporate appropriate env flags
Patch3:         praat-allow-system-flags.patch
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  icns-utils
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)

%description
Praat is an open-software tool for the analysis of speech in phonetics.
Through its graphical interface, several speech analysis functionalities
are available: spectrograms, cochleograms, and pitch and formant extraction.
Articulatory synthesis, as well as synthesis from pitch, formant, and
intensity are also available. Other features are segmentation, labelling
using the phonetic alphabet, and computation of statistics.
Praat is configurable and extensible through its own scripting language and has
provisions for communicating with other programs.

%prep
%autosetup -p1

%build
cp makefiles/makefile.defs.linux.pulse ./makefile.defs
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build

%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}/pixmaps \
         %{buildroot}/%{_datadir}/applications
install -m 0755 %{name} %{buildroot}/%{_bindir}

icns2png -x -d32 main/Praat.icns
for s in 16 32 48 64 128 256 512; do
   if [ -f Praat_${s}x${s}x32.png ]; then
      mkdir -pv %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
      install -m 0644 Praat_${s}x${s}x32.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
   fi
done

# create .desktop file
tee %{buildroot}/%{_datadir}/applications/%{name}.desktop << "EOF"
[Desktop Entry]
Version=1.0
Type=Application
Name=Praat
GenericName=Computer phonetics
Comment=Doing phonetics by computer
Exec=praat %U
TryExec=praat
Icon=praat
Terminal=false
Categories=Science;NumericalAnalysis;GTK;
StartupNotify=true
MimeType=text/praat-textgrid;text/praat-pitch;
EOF

%files
%license main/GNU_General_Public_License.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
