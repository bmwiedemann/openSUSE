#
# spec file for package converseen
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


Name:           converseen
Version:        0.9.11.1
Release:        0
Summary:        Batch Image Conversion Tool
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Convertors
URL:            https://converseen.fasterland.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(MagickCore)
BuildRequires:  pkgconfig(MagickWand)
Recommends:     %{name}-lang

%description
Converseen is a batch image conversion tool. Converseen allows you
to convert images in more than 100 different formats.

With converseen you can:
- Carry out a single or a multiple conversion.
- Resize one or more images.
- Compress images for your web pages.
- Rotate and flip images.
- Rename a bunch of images using a progressive number or a prefix/suffix.
- Selecting a resampling filter to resize images.

%lang_package

%prep
%setup -q
chmod -x README.md COPYING

%build
%cmake
%cmake_build

%install
# Create desktop file because the original one is incorrect.
cat > res/net.fasterland.%{name}.desktop << EOF
[Desktop Entry]
Name=Converseen
GenericName=Batch Image Converter
GenericName[it]=Convertitore batch di immagini
GenericName[ru]=Конвертер изображений
Comment=Batch image converter
Comment[it]=Convertitore batch di immagini
Comment[ru]=Преобразование изображений
Exec=converseen
Icon=converseen
Categories=Qt;Graphics;RasterGraphics;
StartupNotify=true
Terminal=false
Type=Application
EOF

%cmake_install
rm -rf %{buildroot}%{_datadir}/kservices5/ 

# strip incorrect sRGB profile
convert res/%{name}.png -strip res/%{name}.png
for size in 256x256 128x128 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
    convert res/%{name}.png -strip -resize ${size} \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png || true
done
%find_lang %{name} --with-qt
%suse_update_desktop_file net.fasterland.%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/net.fasterland.%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/loc/

%changelog
