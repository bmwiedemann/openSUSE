#
# spec file for package clanlib
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define clan_ver 4.2
Name:           clanlib
Version:        4.2.0
Release:        0
Summary:        A Portable Interface for Writing Games
License:        Zlib
Group:          System/Libraries
URL:            https://github.com/sphair/ClanLib
Source:         %{URL}/archive/refs/tags/v%{version}.tar.gz#/ClanLib-%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  graphviz-gnome
BuildRequires:  libXinerama-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif

%description
ClanLib delivers a platform-independent interface for writing games.

%package        devel
Summary:        A portable interface for writing games
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}
#wants compiler intrinsics in installed headers
Requires:       c++_compiler
Requires:       pkgconfig(alsa)
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(x11)

%description    devel
ClanLib delivers a platform independent interface to write games with.

%package        doc
Summary:        A Portable Interface for Writing Games
Group:          Documentation/HTML
Suggests:       clanlib-devel = %{version}
BuildArch:      noarch

%description doc
ClanLib delivers a platform-independent interface for writing games.

%package        examples
Summary:        A Portable Interface for Writing Games
Group:          Documentation/Other
Requires:       clanlib = %{version}
Requires:       clanlib-devel = %{version}
BuildArch:      noarch

%description examples
ClanLib delivers a platform-independent interface for writing games.

%prep
%autosetup -n ClanLib-%{version}

%build
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-12"
export CXX="g++-12"
%endif
# Remove IDE files
find Examples -name \*.sln -o -name \*.vcproj -o -name \*.vcxproj\* | xargs rm -vf
# Fix line ending
find Examples -name \*.props -exec dos2unix \{\} +
# Configure
autoreconf -fiv
%configure --with-pic --disable-static --enable-docs
%make_build
%make_build html

%install
%make_install
make DESTDIR=%{buildroot} install-html
# Install examples
mkdir -p %{buildroot}%{_datadir}/doc/clanlib-%{clan_ver}
cp -a Examples %{buildroot}%{_datadir}/doc/clanlib-%{clan_ver}
%fdupes %{buildroot}%{_datadir}/doc

find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc CREDITS README
%{_libdir}/libclan*.so.*

%files devel
%doc CODING_STYLE
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libclan*.so

%files doc
%{_datadir}/doc/clanlib-%{clan_ver}/
%exclude %{_datadir}/doc/clanlib-%{clan_ver}/Examples

%files examples
%{_datadir}/doc/clanlib-%{clan_ver}/Examples

%changelog
