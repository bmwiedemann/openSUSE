#
# spec file for package gpick
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


%define appname org.gpick.gpick
Name:           gpick
Version:        0.4
Release:        0
Summary:        Advanced color picker writen in GTK+
License:        BSD-3-Clause
URL:            http://www.gpick.org/
Source0:        https://github.com/thezbyg/gpick/releases/download/v%{version}/%{name}-%{version}.tar.gz

# PATCH-FIX-UPSTREAM gpick-0.4-crash-on-start.patch -- Fix crash on startup when settings are empty
Patch0:         gpick-0.4-crash-on-start.patch
# PATCH-FIX-UPSTREAM gpick-0.4-lua-5.5.patch -- Add support for lua 5.5
Patch1:         gpick-0.4-lua-5.5.patch

BuildRequires:  boost-devel
BuildRequires:  expat
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_test-devel
# hicolor-icon-theme BuildRequires for directory ownership
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake
BuildRequires:  libexpat-devel
BuildRequires:  pkgconfig
BuildRequires:  ragel
BuildRequires:  scons
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lua) >= 5.4

%description
Gpick is a featured color picker with palette creation and modification
tools. It is written in C++ and uses GTK+ toolkit for user interface.

%lang_package

%prep
%autosetup -p1
# Delete external libraries and only use system dependencies to build GPick
rm -rf extern
echo "INTERNAL_EXPAT=False" >> user-config.py
echo "INTERNAL_LUA=False" >> user-config.py
echo "LOCALEDIR=\"%{_datadir}/locale\"" >> user-config.py
echo "%{version}" > .version

%build
%cmake \
	-DCFLAGS="%{optflags} -Wl,--as-needed" \
	-DCXXFLAGS="%%{optflags} -Wl,--as-needed --std=c++17" \
	-DLDFLAGS="%%{optflags} -Wl,--as-needed" \
	-DPREFER_VERSION_FILE=True \
	-DLUA_TYPE="C"

%cmake_build

%install
%cmake_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/mime/packages/%{appname}.xml
%{_datadir}/%{name}/
%{_datadir}/doc/%{name}/
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man1/%{name}.*

%files lang -f %{name}.lang

%changelog
