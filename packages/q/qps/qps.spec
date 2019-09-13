#
# spec file for package qps
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


Name:           qps
Version:        1.10.20
Release:        0
Summary:        Visual Process Manager
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Monitoring
URL:            https://github.com/lxqt/qps/
Source0:        https://github.com/lxqt/qps/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  lxqt-build-tools-devel >= 0.6.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xrender)

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them. It
displays some general system information, and many details about current
processes.

%lang_package

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file -r %{name} System Monitor

%find_lang %{name} --with-qt

%files
%doc CHANGELOG README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_mandir}/man?/%{name}.?%{ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/qps/
%{_datadir}/qps/translations/

%changelog
