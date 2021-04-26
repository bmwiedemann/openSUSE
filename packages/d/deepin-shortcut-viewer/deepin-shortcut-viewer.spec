#
# spec file for package deepin-shortcut-viewer
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           deepin-shortcut-viewer
Version:        5.0.3
Release:        0
Summary:        Deepin Shortcut Viewer
License:        GPL-3.0
URL:            https://github.com/linuxdeepin/deepin-shortcut-viewer
Source0:        https://github.com/linuxdeepin/deepin-shortcut-viewer/archive/%{version}/%{name}-%{version}.tar.gz
Group:          Productivity/Graphics/Viewers
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(dtkwidget)
Provides:       bundled(CuteLogger)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The program displays a shortcut key window when a JSON data is passed.

%prep
%setup -q

%build
%qmake5 PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%qmake5_install

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/%{name}

%changelog
