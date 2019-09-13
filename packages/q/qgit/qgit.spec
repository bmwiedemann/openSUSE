#
# spec file for package qgit
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


Name:           qgit
Version:        2.8
Release:        0
Summary:        Graphical Git Repository Viewer
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
Url:            https://github.com/tibirna/qgit
Source:         https://github.com/tibirna/qgit/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.11
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.5.0
Requires:       git-core >= 1.4.0

%description
QGit is a git GUI viewer built on Qt/C++.

With qgit you will be able to browse revisions history, view patch
content and changed files, graphically following different development
branches.

Features

- View revisions, diffs, files history, files annotation, archive tree.

- Commit changes visually cherry picking modified files.

- Apply or format patch series from selected commits, drag and drop
commits between two instances of qgit.

- Associate commands sequences, scripts and anything else executable to
a custom action. Actions can be run from menu and corresponding output
is grabbed by a terminal window.

- qgit implements a GUI for the most common StGIT commands like push/pop
and apply/format patches. You can also create new patches or refresh
current top one using the same semantics of git commit,  i.e. cherry
picking single modified files.

%prep
%setup -q -n qgit-qgit-%{version}

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license COPYING.rtf
%doc README
%{_bindir}/qgit
%{_datadir}/applications/qgit.desktop
%{_datadir}/icons/hicolor/48x48/apps/qgit.png
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/qgit.appdata.xml

%changelog
