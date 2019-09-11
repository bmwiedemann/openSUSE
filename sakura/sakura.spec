#
# spec file for package sakura
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


Name:           sakura
Version:        3.6.0
Release:        0
Summary:        Terminal Emulator based on the VTE Library
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://launchpad.net/sakura
Source:         https://launchpad.net/sakura/trunk/%{version}/+download/sakura-%{version}.tar.bz2
Patch0:         sakura-icon.patch
Patch1:         sakura-fix_pod2man.patch
# to convert SVG to PNG:
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libstdc++-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.20
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vte-2.91) >= 0.38

%description
sakura is a vte-based terminal emulator. It aims to provide a terminal
emulator that only depends on GTK and VTE. It uses a notebook to allow
multiple tabs in the same window.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1
mv terminal-tango.svg sakura.svg
convert -strip sakura.svg sakura.png
# replace hard-coded ICON_DIR
sed -i -r 's|^(\s*#define\s*ICON_DIR\s+").+("\s*)$|\1%{_datadir}/pixmaps\2|g' src/sakura.c

%build
%cmake -DCMAKE_C_FLAGS="%{optflags}"
%make_jobs

%install
%cmake_install
rm -rf "%{buildroot}%{_datadir}/doc"
%find_lang %{name} %{?no_lang_C}

%files
%doc AUTHORS
%license GPL
%{_bindir}/sakura
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man1/sakura.1%{ext_man}

%files lang -f %{name}.lang

%changelog
