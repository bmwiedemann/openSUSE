#
# spec file for package mathmod
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


%define binname MathMod
Name:           mathmod
Version:        12.0
Release:        0
Summary:        Mathematical modelling to visualise implicit and parametric surfaces
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://sourceforge.net/projects/mathmod/
Source0:        http://sourceforge.net/projects/mathmod/files/MathMod-%{version}/%{name}-%{version}-source.zip
Source1:        %{name}.desktop
BuildRequires:  ImageMagick
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Core) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
MathMod is a mathematical modeling software to model, plot and animate
3D/4D parametric and implicit surfaces.

Features:
 * 3D and 4D plotting and animation
 * OBJ output file format
 * Scripting language in JSON file format
 * Texture and pigmentation support
 * Noise and Turbulence effects support
 * Large set of scripted examples

%prep
%setup -q -n %{name}-%{version}

dos2unix -k Readme.txt

%build
mkdir build
pushd build
%qmake5 ../%{binname}.pro
%make_jobs
popd

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps
install -Dm 0755 build/%{binname} %{buildroot}%{_libdir}/%{name}/%{name}
ln -s %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
for f in $(find -maxdepth 1 -name \*.js); do
j=$(basename $f)
install -Dm 0644 $f %{buildroot}%{_libdir}/%{name}/$j
done
for i in $(find images/icon -name \*.png); do
r=$(echo $i|sed 's/[^0-9x]//g')
install -Dm 0644 $i %{buildroot}%{_datadir}/icons/hicolor/${r}/apps/%{name}.png
done
convert -monitor images/icon/catenoid_mini_64x64.ico %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
# Remove spurious icon file
rm %{buildroot}%{_datadir}/icons/hicolor/apps/mathmod.png

install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license Licence.txt
%doc Readme.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
