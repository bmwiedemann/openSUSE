#
# spec file for package vnote
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           vnote
Version:        3.20.1
Release:        0
Summary:        A Vim-inspired note-taking application, especially for Markdown
License:        LGPL-3.0-only
Group:          Productivity/Text/Editors
URL:            https://github.com/tamlok/vnote
Source0:        https://github.com/tamlok/vnote/archive/v%{version}.tar.gz#/vnote-%{version}.tar.gz
Source1:        vtextedit.tar.xz
Source2:        QHotkey.tar.xz
# PATCH-FIX-UPSTREAM 0001-fix-build-with-cmake-4.patch -- Fix build with CMake 4
Patch0:         0001-fix-build-with-cmake-4.patch
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
Provides:       bundled(vtextedit)
Requires:       qt6-sql-sqlite
# vnote doesn't install development files, moving the bundled library to a separate package isn't useful
Obsoletes:      libVTextEdit1 < 3.20.1
ExclusiveArch:  %{x86_64} aarch64 riscv64

%description
VNote is a note-taking application, designed especially for Markdown.
VNote provides both note management and Markdown edit experience.

%prep
%autosetup -p1
cd libs
rmdir QHotkey vtextedit
/usr/lib/rpm/rpmuncompress -x %{SOURCE1}
/usr/lib/rpm/rpmuncompress -x %{SOURCE2}
cd ..

# Useless and broken
sed -i '/Packaging.cmake/d' src/CMakeLists.txt

# Use a less generic location for translations
sed -i 's#app:translations#app:vnote/translations#' src/main.cpp

%build
%cmake_qt6 -DCMAKE_SKIP_RPATH:BOOL=TRUE

%qt6_build

%install
%qt6_install

# Move translations to a less generic location
mkdir -p %{buildroot}%{_datadir}/vnote
mv %{buildroot}%{_datadir}/translations %{buildroot}%{_datadir}/vnote/translations

%ldconfig_scriptlets

%files
%license COPYING.LESSER
%doc README.md changes.md
%{_bindir}/vnote
%{_datadir}/applications/vnote.desktop
%{_datadir}/icons/hicolor
%{_datadir}/vnote_extra.rcc
%{_datadir}/vnote/
%{_libdir}/libVTextEdit.so

%changelog
