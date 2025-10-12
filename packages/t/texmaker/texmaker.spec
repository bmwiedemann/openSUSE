#
# spec file for package texmaker
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


%if %{?is_opensuse} && 0%{?suse_version} <= 1650
%define gcc_ver 13
%endif


Name:           texmaker
Version:        6.0.1
Release:        0
Summary:        LaTeX editor
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            http://www.xm1math.net/texmaker/
Source:         http://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM CVE-2025-50952.patch bsc#1247798 badshah400@gmail.com -- Guard against 0 offset to nullptr in openjpeg bundled with pdfium
Patch0:         CVE-2025-50952.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-private-devel
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(Qt6Xml)
Requires:       hunspell
Requires:       texlive-collection-latexrecommended
Requires:       web_browser
Requires:       xdg-utils

%description
Texmaker is a LaTeX editor that integrates many tools
needed to develop documents with LaTeX in just one application.

Texmaker includes unicode support, spell checking, auto-completion,
code folding and a built-in PDF viewer with synctex support and
continuous view mode.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_C_COMPILER=gcc%{?gcc_ver:-%{gcc_ver}} \
  -DCMAKE_CXX_COMPILER=g++%{?gcc_ver:-%{gcc_ver}} \
  -DCMAKE_SKIP_RPATH=ON \
	%{nil}
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/%{name}/
# REMOVE DOC FILES PACKAGED ANYWAY USING %%doc
rm %{buildroot}%{_datadir}/%{name}/{AUTHORS,COPYING,CHANGELOG.txt}

%files
%license COPYING 3rdparty/pdfium/LICENSE
%doc datas/CHANGELOG.txt AUTHORS 3rdparty/pdfium/AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
