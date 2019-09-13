#
# spec file for package tintii
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


Name:           tintii
Version:        2.10.0
Release:        0
Summary:        Selective Colour Photo Filter
License:        GPL-2.0
Group:          Productivity/Graphics/Bitmap Editors
Url:            http://www.indii.org/software/tintii
Source0:        http://www.indii.org/files/tint/releases/%{name}-%{version}.tar.gz
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

%description
tintii takes full colour photos and processes them into black and white
with some select regions highlighted in colour. The technique is known
as colour popping or selective colouring.

%prep
%setup -q

%build
%configure --disable-assert
make %{?_smp_mflags}

%install
%make_install
# Create desktop file.
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=tintii
GenericName=Selective Colour Photo Filter
GenericName[ru]=Избирательный фильтр цветов фотографий
Type=Application
Exec=tintii %f
Icon=tintii
Categories=Graphics;Photography;
Comment=Selective processing colour photos into black and white
Comment[ru]=Избирательное преобразование цветных фотографий в чёрно-белые
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
