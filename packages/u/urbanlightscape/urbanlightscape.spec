#
# spec file for package urbanlightscape
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           urbanlightscape
Version:        1.4.0
Release:        0
Summary:        Improve Lighting, Correct Exposure, Add Synthetic Light to Photos
License:        GPL-2.0+
Group:          Productivity/Graphics/Bitmap Editors
Url:            http://www.indii.org/software/urbanlightscape
Source0:        http://www.indii.org/files/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        http://www.indii.org/images/%{name}_128.png
BuildRequires:  ImageMagick
BuildRequires:  bc
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel >= 3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Appliaction heavily depends on SSE, which is Intel specific feature
ExclusiveArch:  %{ix86} x86_64

%description
Urban Lightscape is a photo filter for exposure correction,
localized brightness adjustments, dodging and burning, and the
introduction of synthetic lighting to a photo. A simple
"double-click-and-drag" paradigm is used to place control points on
a photo, and clever edge detection localises and interpolates
lightness adjustments around and between these points. Results are
rapid, with additional controls for more subtle refinements.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -msse2"
%configure --disable-assert
make %{?_smp_mflags}

%install
%make_install
# Create desktop file.
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Urban Lightscape
GenericName=Correct Exposure, Lighting, Brightness
GenericName[ru]=Коррекция экспозиции, яркости, света
Type=Application
Exec=urbanlightscape %f
Icon=urbanlightscape
Categories=Graphics;Photography;
Comment=Improve lighting, Correct Exposure, Add Synthetic Light to Photos
Comment[ru]=Коррекция экспозиции, яркости, света
StartupNotify=true
Terminal=false
MimeType=image/gif;image/jpeg;image/png;image/tiff;image/x-bmp;image/x-portable-pixmap;image/x-pcx;image/x-targa;image/x-xpm;
EOF
install -Dm 0644 %{name}.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install icons of various sizes.
install -Dm 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for size in 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    convert -strip -resize ${size} %{SOURCE1} \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done
%suse_update_desktop_file %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%changelog
