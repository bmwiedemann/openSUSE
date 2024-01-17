#
# spec file for package texworks
#
# Copyright (c) 2023 SUSE LLC
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


Name:           texworks
Version:        0.6.8
Release:        0
Summary:        TeXshop-like TeX Editor
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            https://www.tug.org/texworks/
Source0:        https://github.com/TeXworks/texworks/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  dbus-1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  libpoppler-devel >= 0.24
BuildRequires:  libpoppler-qt5-devel >= 0.24
BuildRequires:  lua-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  texlive-tex-bin
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
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
Requires:       python

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
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DTW_BUILD_ID="openSUSE" \
       -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=%{_lib} \
       -DWITH_LUA=ON \
       -DWITH_PYTHON=ON \
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

%files plugin-python
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*PythonPlugin.so

%files plugin-lua
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*LuaPlugin.so

%changelog
