#
# spec file for package tesseract
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


Name:           tesseract
Version:        2024_06_15
Release:        0
Summary:        First-person shooter with cooperative in-game map editing
License:        Zlib
Group:          Amusements/Games/3D/Shoot
URL:            http://tesseract.gg/
Source:         %{name}-%{version}.tar.xz
Source1:        tesseract.desktop
Source2:        tesseract.png
Source3:        update.sh
BuildRequires:  Mesa-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}

%description
Tesseract is a first-person shooter game focused on instagib deathmatch
and capture-the-flag gameplay as well as cooperative in-game map editing.

Tesseract is based on Cube2/Sauerbraten. New rendering features include fully
dynamic omnidirectional shadows, global illumination, HDR lighting, deferred
shading and morphological/temporal/multisample anti-aliasing.

%package server
Summary:        Tesseract standalone server
Group:          Amusements/Games/3D/Shoot

%description server
This package provides the server files for the Tesseract game.

%package data
Summary:        Data files for Tesseract
Group:          Amusements/Games/3D/Shoot
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
This package provides the data files for the Tesseract game.

%prep
%setup -q -n %{name}

%build
rm -r bin_unix
mkdir -p bin_unix
cd src
%make_build CXXFLAGS="-Wall -fsigned-char %{optflags}" CFLAGS="%{optflags}"
%make_build install
cd ../bin_unix
mv *client client
mv *server server

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a bin_unix %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
cat <<EOT >%{buildroot}%{_bindir}/%{name}-game
#!/bin/sh
TESSERACT_DIR=\$HOME/.tesseract
if test ! -e \$TESSERACT_DIR ; then
    mkdir \$TESSERACT_DIR
    ln -s %{_libexecdir}/%{name}/* \$TESSERACT_DIR
fi
cd \$TESSERACT_DIR
exec bin_unix/client "\$@"
EOT
chmod 755 %{buildroot}%{_bindir}/%{name}-game
ln -sf %{_libexecdir}/%{name}/bin_unix/server %{buildroot}%{_bindir}/%{name}-server

# copy data files
cp -a media/ config/ %{buildroot}%{_libexecdir}/tesseract/

# .desktop shortcut and icon
install -d %{buildroot}%{_datadir}/applications
cp %{SOURCE1} %{buildroot}%{_datadir}/applications

install -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
cp %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/

%fdupes -s %{buildroot}%{_libexecdir}/tesseract/media/

%files
%{_bindir}/%{name}-game
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/bin_unix
%{_libexecdir}/%{name}/bin_unix/client
%{_datadir}/applications/tesseract.desktop
%{_datadir}/icons/hicolor/64x64/apps/tesseract.png

%files server
%{_bindir}/%{name}-server
%dir %{_libexecdir}/%{name}/bin_unix
%{_libexecdir}/%{name}/bin_unix/server

%files data
%doc doc/dev/*
%dir %{_libexecdir}/tesseract
%{_libexecdir}/tesseract/media
%{_libexecdir}/tesseract/config

%changelog
