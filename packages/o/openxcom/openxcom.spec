#
# spec file for package openxcom
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


Name:           openxcom
Version:        1.0.0.1592170963.8ae998af3
Release:        0
Summary:        An open source reimplementation of the original X-Com game
License:        GPL-3.0-only
URL:            https://openxcom.org/
Source:         OpenXcom-%{version}.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook2X
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(SDL_gfx)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(yaml-cpp) >= 0.5

%description
OpenXcom is an open-source clone of the original UFO: Enemy Unknown
(X-Com: UFO Defense in USA), licensed under the GPL and written in C++ / SDL.

The goal of the project is to bring back the tried and true feel of the original
with none of the issues. All the same graphics, sound and gameplay with a brand
new codebase written from scratch.

User is required to have original gamedata (possible to obtain from e.g. Steam)
installed to ~/.local/share/openxcom/data/

%package doc
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}

%description doc
Documentation files for %{name} game.

%prep
%setup -q -n OpenXcom-%{version}

chmod -x LICENSE.txt
sed -i \
	-e 's:HTML_TIMESTAMP         = YES:HTML_TIMESTAMP         = NO:g' \
	docs/Doxyfile.in
dos2unix *.txt

%build
autoreconf -fvi
%configure \
	--disable-werror \
	--disable-silent-rules \
	--with-docs --docdir="%{_docdir}/%{name}"
%make_build

%install
%make_install
pushd %{buildroot}%{_datadir}/pixmaps/
ln -s openxcom_wide.svg openxcom.svg
popd
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE.txt
%doc README.md CHANGELOG.txt
%{_datadir}/applications/openxcom.desktop
%{_mandir}/man6/openxcom.6%{?ext_man}
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/
%{_docdir}/%{name}/*.txt
%{_bindir}/%{name}
%dir %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/html/

%files doc
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/html
%{_docdir}/%{name}/html/*

%changelog
