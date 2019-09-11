#
# spec file for package gource
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


Name:           gource
Version:        0.49
Release:        0
Summary:        Software version control visualization tool
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Visualization/Graph
Url:            http://gource.io/
Source:         https://github.com/acaudwell/Gource/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel >= 0.9.3
BuildRequires:  pkgconfig
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(SDL2_image) >= 2.0
BuildRequires:  pkgconfig(freetype2) >= 9.0.3
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(sdl2) >= 2.0
Requires:       freefont
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
%else
BuildRequires:  boost-devel >= 1.46
%endif

%description
Gource is a software version control visualization tool.

Software projects are displayed by Gource as an animated tree
with the root directory of the project at its centre. Directories
appear as branches with files as leaves. Developers can be seen
working on the tree at the times they contributed to the project.

Currently there is first party support for Git and Mercurial,
and third party (using additional steps) for CVS and SVN.

%prep
%setup -q

%build

%configure \
	--with-tinyxml=yes \
	--enable-ttf-font-dir=%{_datadir}/fonts/truetype
make %{?_smp_mflags}

%install
%make_install

%files
%doc ChangeLog README THANKS
%license COPYING
%{_mandir}/man1/*
%{_bindir}/gource
%{_datadir}/gource/

%changelog
