#
# spec file for package converseen
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.9.7.2
Release:        0
Summary:        Batch Image Conversion Tool
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Convertors
URL:            http://converseen.fasterland.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
cp -p README.md README
chmod -x README COPYING

%build
%cmake
make %{?_smp_mflags} VERBOSE=1

%install
# Create desktop file because the original one is incorrect.
cat > res/%{name}.desktop << EOF
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
rm -rf \
    %{buildroot}%{_datadir}/kde4/ \
    %{buildroot}%{_datadir}/kservices5/ \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png
# strip incorrect sRGB profile
convert res/%{name}.png -strip res/%{name}.png
for size in 256x256 128x128 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
    convert res/%{name}.png -strip -resize ${size} \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png || true
done
%find_lang %{name} --with-qt
%suse_update_desktop_file %{name}

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%if 0%{?suse_version} && 0%{?suse_version} < 1320
%dir %{_datadir}/appdata/
%endif
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/loc/

%changelog
