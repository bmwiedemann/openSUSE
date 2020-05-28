#
# spec file for package supertux2
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


%define _name   supertux
Name:           supertux2
Version:        0.6.2
Release:        0
Summary:        Jump'n run game
License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND GPL-2.0-or-later AND GPL-1.0-only
Group:          Amusements/Games/Action/Arcade
URL:            https://supertux.github.io/
Source:         https://github.com/SuperTux/supertux/releases/download/v%{version}/SuperTux-v%{version}-Source.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libphysfs-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(raqm)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
#!BuildIgnore:  gcc-PIE
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_system-devel

%description
SuperTux is a classic 2D jump'n run sidescroller game in a similar
style like the original SuperMario games.

%prep
%setup -q -n SuperTux-v%{version}-Source
# Use supertux2.png filename to not conflict with supertux package.
for res in png xpm; do
    cp -f data/images/engine/icons/{%{_name},%{name}}.$res
done
sed -i 's/%{_name}.\(png\|xpm\)/%{name}.\1/g' CMakeLists.txt
sed -i 's|^\(Icon=\).*$|\1%{name}|' %{name}.desktop

%build
%cmake \
  -DINSTALL_SUBDIR_BIN="$(realpath --relative-to=%{_prefix} %{_bindir})"            \
  -DINSTALL_SUBDIR_SHARE="$(realpath --relative-to=%{_prefix} %{_datadir})/%{name}" \
  -DINSTALL_SUBDIR_DOC="$(realpath --relative-to=%{_prefix} %{_docdir})/%{name}" \
  -DENABLE_BOOST_STATIC_LIBS=OFF
make %{?_smp_mflags}

%install
%cmake_install
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL.md
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE.txt
%suse_update_desktop_file %{name}
%fdupes %{buildroot}

%files
%doc README.md NEWS.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%attr(755,root,root) %{_datadir}/%{name}/sounds/normalize.sh
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
