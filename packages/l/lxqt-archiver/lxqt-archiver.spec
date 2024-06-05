#
# spec file for package lxqt-archiver
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


Name:           lxqt-archiver
Version:        1.0.0
Release:        0
Summary:        LXQt File Archiver
License:        GPL-2.0-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-archiver
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fm-qt6)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache)
Recommends:     %{name}-lang = %{version}-%{release}
Requires:       bsdtar
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils

%description
A simple & lightweight Qt file archiver. The core I/O functions are ported
from Engrampa (a Gnome File Roller fork). This is only a front-end (a
graphical interface) to archiving programs like tar and zip.

%lang_package

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%license LICENSE

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
