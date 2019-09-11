#
# spec file for package imv
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           imv
Version:        3.1.2
Release:        0
Summary:        Image viewer for X11/Wayland
License:        MIT AND GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/eXeC64/imv
Source:         https://github.com/eXeC64/imv/archive/v%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  freeimage-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  libpng16-devel
BuildRequires:  librsvg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(fontconfig)

%description
imv is a command line image viewer intended for use with tiling window managers.

%prep
%setup -q

%build
make %{?_smp_mflags} \
    PREFIX="%{_prefix}"

%install
%make_install \
    PREFIX="%{_prefix}"

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}*
%{_sysconfdir}/%{name}_config

%changelog
