#
# spec file for package praat
#
# Copyright (c) 2020 SUSE LLC
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
Version:        6.1.22
Release:        0
Summary:        Phonetics by computer
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Other
URL:            http://www.praat.org
Source0:        https://github.com/praat/praat/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source3:        %{name}.changes
# PATCH-FIX-OPENSUSE praat-use_system_libs.patch -- replace some embedded libs with system ones
Patch1:         praat-use_system_libs.patch
# PATCH-FIX-OPENSUSE praat-no-return-in-nonvoid.patch -- address rpmlint complaint
Patch2:         praat-no-return-in-nonvoid.patch
BuildRequires:  ImageMagick
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)

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
sed -e '/^CFLAGS/s/$/\ %{optflags}/' \
    -e '/^CC/s/=/?=/' -e '/^CXX/s/=/?=/' \
    -e '/^LINK/s/=/?=/' -i makefile.defs
%make_build

%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}/pixmaps \
         %{buildroot}/%{_datadir}/applications
install -m 0755 %{name} %{buildroot}/%{_bindir}
convert -strip -resize 128x128 main/praat_win.ico %{name}.png
install -m 0644 %{name}.png %{buildroot}/%{_datadir}/pixmaps
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
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
