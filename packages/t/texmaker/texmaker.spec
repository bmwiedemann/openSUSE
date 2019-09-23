#
# spec file for package texmaker
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


Name:           texmaker
Version:        5.0.3
Release:        0
Summary:        LaTeX editor
License:        GPL-2.0-only AND BSD-3-Clause
Group:          Productivity/Publishing/TeX/Frontends
Url:            http://www.xm1math.net/texmaker/
Source:         http://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-private-headers-devel >= 5.7
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
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
%setup -q

%build
QTDIR=%{_libdir}/qt5
PATH=$QTDIR/bin:$PATH
LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH
DYLD_LIBRARY_PATH=$QTDIR/lib:$DYLD_LIBRARY_PATH
export QTDIR PATH LD_LIBRARY_PATH DYLD_LIBRARY_PATH
PREFIX=%{_prefix}

find ./ -name ".qmake.stash" -delete -print
%qmake5 METAINFODIR="%{_datadir}/metainfo" -unix texmaker.pro
%make_jobs

%install
%qmake5_install
%fdupes %{buildroot}%{_datadir}/%{name}/

%files
%doc utilities/AUTHORS utilities/COPYING utilities/CHANGELOG.txt
%{_bindir}/texmaker
%{_datadir}/applications/texmaker.desktop
%{_datadir}/pixmaps/texmaker.png
%{_datadir}/texmaker/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
