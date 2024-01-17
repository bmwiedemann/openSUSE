#
# spec file for package enigma
#
# Copyright (c) 2021 SUSE LLC
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


Name:           enigma
Version:        1.30
Release:        0
Summary:        An Excellent Oxyd Clone
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            http://www.nongnu.org/enigma/
Source0:        https://github.com/Enigma-Game/Enigma/releases/download/%{version}/Enigma-%{version}-src.tar.gz
Source1:        %{name}-help.desktop
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        %{name}-help.png
Source5:        enigma_de.pdf
Source6:        french_russian.tar.bz2
BuildRequires:  ImageMagick
BuildRequires:  enet-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-tools
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xerces-c)

%description
Enigma is similar to the well known game Oxyd.

%prep
%setup -q

%build
%configure \
    --with-system-enet
make %{?_smp_mflags}

%install
%make_install
install -D -m 644 %{_sourcedir}/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m 644 %{_sourcedir}/%{name}-help.png %{buildroot}%{_datadir}/pixmaps/%{name}-help.png
%suse_update_desktop_file -i %{name}
%suse_update_desktop_file -i %{name}-help

mkdir -p %{buildroot}%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/enigma/ %{buildroot}%{_defaultdocdir}/%{name}
install -m 644 %{SOURCE5} %{buildroot}%{_defaultdocdir}/%{name}
tar -xjf %{SOURCE6} -C %{buildroot}%{_defaultdocdir}/%{name}
%png_fix_dir %{buildroot}/%{_datadir}/enigma
%fdupes %{buildroot}%{_datadir}

%files
%doc %{_defaultdocdir}/%{name}
%{_bindir}/enigma
%{_mandir}/man6/enigma.6%{?ext_man}
%{_datadir}/enigma/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-help.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-help.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
