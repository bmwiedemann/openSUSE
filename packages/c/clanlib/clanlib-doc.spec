#
# spec file for package clanlib-doc
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define clan_ver 2.3

Name:           clanlib-doc
Summary:        A Portable Interface for Writing Games
License:        Zlib
Group:          Documentation/HTML
BuildArch:      noarch
Version:        2.3.6
Release:        0
Url:            http://www.clanlib.org/
Source:         ClanLib-%{version}.tgz
BuildRequires:  Mesa-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  alsa-devel
BuildRequires:  clanlib-devel = %{version}
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz
#needed for png output of documentation
BuildRequires:  graphviz-gnome
BuildRequires:  libjpeg-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxslt
BuildRequires:  pcre-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ClanLib delivers a platform-independent interface for writing games.

%package -n     clanlib-examples
Summary:        A Portable Interface for Writing Games
Group:          Documentation/Other
Requires:       clanlib = %{version}
Requires:       clanlib-devel = %{version}
BuildArch:      noarch

%description -n  clanlib-examples
ClanLib delivers a platform-independent interface for writing games.

%prep
%setup -q -n ClanLib-%{version}

%build
find Examples -name \*.sln -o -name \*.vcproj -o -name \*.vcxproj\* | xargs rm -f
dos2unix Examples/Game/SpritesRTS/resources.xml Examples/Database/SQL/Database/create_database.sql \
	Examples/3D/Chess3D/Resources/Sponza/readme.txt Examples/3D/Chess3D/Resources/skybox_fragment.glsl \
	Examples/Game/Pacman/pacman.xml Examples/3D/Chess3D/Resources/skybox_vertex.glsl \
	Examples/Game/TileMap/README.txt \
	Examples/3D/Clan3D/Resources/teapot.dae \
	Examples/Game/TileMap/Resources/tileset.txt

%configure --with-pic --disable-static --enable-docs
make %{?_smp_mflags} html

%install
make DESTDIR=%{buildroot} install-html
mkdir -p %{buildroot}%{_datadir}/doc/clanlib-%{clan_ver}
cp -a Examples %{buildroot}%{_datadir}/doc/clanlib-%{clan_ver}
%fdupes %{buildroot}%{_datadir}/doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%{_datadir}/doc/clanlib-%{clan_ver}/
%exclude %{_datadir}/doc/clanlib-%{clan_ver}/Examples

%files -n clanlib-examples
%defattr(-, root, root)
%{_datadir}/doc/clanlib-%{clan_ver}/Examples

%changelog
