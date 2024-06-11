#
# spec file for package qps
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


Name:           qps
Version:        2.9.0
Release:        0
Summary:        Visual Process Manager
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/lxqt/qps
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(lxqt) >= 2.0.0

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them. It
displays some general system information, and many details about current
processes.

%lang_package

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}
%suse_update_desktop_file -r %{name} System Monitor

%find_lang %{name} --with-qt

%files
%doc CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/metainfo/org.lxqt.Qps.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%license COPYING

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
