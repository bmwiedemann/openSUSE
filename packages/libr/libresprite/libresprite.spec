#
# spec file for package libresprite
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


Name:           libresprite
Version:        1.1
Release:        0
Summary:        Animated sprite editor & pixel art tool
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Graphics/Bitmap Editors
Source:         LibreSprite-%{version}.tar.bz2
URL:            https://libresprite.github.io/
BuildRequires:  cmake >= 3.4
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  fdupes
BuildRequires:  giflib-devel >= 5.1.0
BuildRequires:  glibc-devel
BuildRequires:  googletest-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  nodejs-devel-default
BuildRequires:  shared-mime-info
BuildRequires:  tinyxml-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(duktape)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(lua5.3)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  pkgconfig(x11)

%description
LibreSprite is an open source program to create animated sprites
for websites and games.

%prep
%autosetup -p1 -n LibreSprite-%{version}

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
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%{_datadir}/metainfo/io.github.libresprite.%{name}.metainfo.xml
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/aseprite.xml
%{_datadir}/thumbnailers/
%{_datadir}/icons/hicolor/

%changelog
