#
# spec file for package texworks
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2007-09 by Jonathan Kew.
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


%define __builder ninja
%if 0%{?suse_version} < 1650
# Lua plugin requires GCC >= 8 for filesystem support
%define gcc_ver 9
# Python plugin requires Python >= 3.8
%bcond_with python
%else
%bcond_without python
%endif
Name:           texworks
Version:        0.6.9
Release:        0
Summary:        TeXshop-like TeX Editor
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            https://www.tug.org/texworks/
Source0:        https://github.com/TeXworks/texworks/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM texworks-cmake-find-python.patch gh#TeXworks/texworks#1039 badshah400@gmail.com -- cmake has dropped support for PythonInterp and PythonLibs, use FindPython instead
Patch0:         https://github.com/TeXworks/texworks/commit/dae1586af7a218e9bbe9ce3031a97e8efcac980a.patch#/texworks-cmake-find-python.patch
# PATCH-FIX-UPSTREAM texworks-python-plugin-buildfix.patch gh#/TeXworks/texworks#1038 badshah400@gmail.com -- Fix building the python scripting plugin
Patch1:         https://github.com/TeXworks/texworks/commit/f8962bca2db2cae3183cad201a4726e7726caccb.patch#/texworks-python-plugin-buildfix.patch
BuildRequires:  cmake
BuildRequires:  dbus-1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  libpoppler-devel >= 0.24
BuildRequires:  libpoppler-qt6-devel >= 0.24
BuildRequires:  lua-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
%if %{with python}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
%endif
BuildRequires:  texlive-tex-bin
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
Requires:       dbus-1
Requires:       hunspell
Requires:       poppler-tools
Requires:       texlive-latex

%description
The TeXworks project is a simple TeX front-end program (working
environment) that is modeled on Dick Koch's TeXShop for Mac OS X.

%package plugin-python
Summary:        Plugins to add python scripting to texworks
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python3

%description plugin-python
The TeXworks project is a simple TeX front-end program (working
environment) that is modeled on Dick Koch's TeXShop for Mac OS X.

This package adds python scripting abitilies to TeXworks.

%package plugin-lua
Summary:        Plugins to add python scripting to texworks
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       lua

%description plugin-lua
The TeXworks project is a simple TeX front-end program (working
environment) that is modeled on Dick Koch's TeXShop for Mac OS X.

This package adds lua scripting abitilies to TeXworks.

%prep
%autosetup -p1 -n texworks-release-%{version}

%build
%cmake -DCMAKE_CXX_COMPILER=g++%{?gcc_ver:-%{gcc_ver}} \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DTW_BUILD_ID="openSUSE" \
       -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=%{_lib} \
       -DQT_DEFAULT_MAJOR_VERSION=6 \
       -DWITH_LUA=ON \
       -DWITH_PYTHON=%{?with_python:ON}%{!?with_python:OFF} \
       -DBUILD_SHARED_PLUGINS:BOOL=ON \
       -DTeXworks_DIC_DIR=%{_datadir}/myspell \
       -DTeXworks_PLUGIN_DIR=%{_libdir}/%{name}

%cmake_build

%install
%cmake_install
%suse_update_desktop_file texworks Publishing WordProcessor

# Package doc files using %%doc, remove them here
for i in COPYING README.md NEWS
do
  rm %{buildroot}%{_datadir}/doc/%{name}/${i}
done

%files
%doc README.md NEWS
%license COPYING
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/texworks.appdata.xml
%{_bindir}/texworks
%{_datadir}/applications/texworks.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_mandir}/man1/texworks.1%{?ext_man}

%if %{with python}
%files plugin-python
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*PythonPlugin.so
%endif

%files plugin-lua
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*LuaPlugin.so

%changelog
