#
# spec file for package gource
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


Name:           gource
Version:        0.55
Release:        0
Summary:        Software version control visualization tool
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Visualization/Graph
URL:            https://gource.io/
Source:         https://github.com/acaudwell/Gource/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel >= 0.9.3
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  pkgconfig
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(SDL2_image) >= 2.0
BuildRequires:  pkgconfig(freetype2) >= 9.0.3
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(sdl2) >= 2.0
Requires:       freefont

%description
Gource is a software version control visualization tool.

Software projects are displayed by Gource as an animated tree
with the root directory of the project at its centre. Directories
appear as branches with files as leaves. Developers can be seen
working on the tree at the times they contributed to the project.

Currently there is first party support for Git and Mercurial,
and third party (using additional steps) for CVS and SVN.

%prep
%autosetup -p1

%build
%configure \
	--with-boost-libdir=%{_libdir} \
	--with-tinyxml=yes \
	--enable-ttf-font-dir=%{_datadir}/fonts/truetype
%make_build

%install
%make_install

%files
%doc ChangeLog README.md THANKS
%license COPYING
%{_mandir}/man1/*
%{_bindir}/gource
%{_datadir}/gource/

%changelog
