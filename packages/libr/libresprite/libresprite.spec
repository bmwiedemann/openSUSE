#
# spec file for package aseprite
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           libresprite
Version:        1.0
Release:        0
Summary:        Animated sprite editor & pixel art tool
License:        GPL-2.0+ and MIT
Group:          Productivity/Graphics/Bitmap Editors
Source:         LibreSprite-%{version}.tar.bz2
Url:            https://libresprite.github.io/
BuildRequires:  cmake >= 3.4
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  giflib-devel >= 5.1.0
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  libjpeg-devel
BuildRequires:  googletest-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libpng)
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(lua5.3)
BuildRequires:  nodejs-devel-default
BuildRequires:  pkgconfig(duktape)
BuildRequires:  pkgconfig(libwebp)

%description
LibreSprite is an open source program to create animated sprites
for websites and games.

%prep
%setup -q -n LibreSprite-%{version}

%build
%cmake .. -DWITH_DESKTOP_INTEGRATION=ON \
%if 0%{?suse_version} <= 1500
          -DCMAKE_CXX_COMPILER=g++-10 \
%endif
          -DWITH_QT_THUMBNAILER=OFF \
          -DWITH_WEBP_SUPPORT=ON

make %{?_smp_mflags}

%install
%cmake_install

install -m0644 -D data/icons/ase16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m0644 -D data/icons/ase32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m0644 -D data/icons/ase48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m0644 -D data/icons/ase64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%doc README.md LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/aseprite.xml
%{_datadir}/thumbnailers/
%{_datadir}/icons/hicolor/

%changelog
