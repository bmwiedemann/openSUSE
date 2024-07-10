#
# spec file for package gpick
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


%define appname org.gpick.gpick
Name:           gpick
Version:        0.3
Release:        0
Summary:        Advanced color picker writen in GTK+
License:        BSD-3-Clause
Group:          Productivity/Graphics/Visualization/Other
URL:            http://www.gpick.org/
Source0:        https://github.com/thezbyg/gpick/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        copyright
# PATCH-FIX-UPSTREAM fix-boost-184.patch gh#thezbyg/gpick#227 smolsheep@opensuse.org -- Fix builds with boost
Patch1:         fix-boost-184.patch
# PATCH-FIX-UPSTREAM fix-version-check.patch gh#thezbyg/gpick#215 smolsheep@opensuse.org -- Fix path in build
Patch2:         fix-version-check.patch
# PATCH-FIX-UPSTREAM import-missing-scons.patch gh#thezbyg/gpick#216 smolsheep@opensuse.org -- Fix import of SCons
Patch3:         import-missing-scons.patch
# PATCH-FIX-UPSTREAM revert-cpp-lua.patch gh#thezbyg/gpick#217 smolsheep@opensuse.org -- Don't use nonexistant lua-c++
Patch4:         revert-cpp-lua.patch
BuildRequires:  boost-devel
BuildRequires:  expat
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
# hicolor-icon-theme BuildRequires for directory ownership
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake
BuildRequires:  libexpat-devel
BuildRequires:  pkgconfig
BuildRequires:  ragel
BuildRequires:  scons
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lua) >= 5.3

%description
Gpick is a featured color picker with palette creation and modification
tools. It is written in C++ and uses GTK+ toolkit for user interface.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%cmake
%cmake_build

%check
./build/tests

%install
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%cmake_install
%if 0%{?suse_version}
%suse_update_desktop_file %{appname} Viewer
%endif
# Install copyright file. This file was given to me by the author/upstream.
cp %{SOURCE1} COPYRIGHT
%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%if 0%{?fedora_version}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%defattr(-,root,root)
%doc COPYRIGHT
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
