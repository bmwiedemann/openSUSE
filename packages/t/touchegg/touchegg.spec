#
# spec file for package touchegg
#
# Copyright (c) 2022 SUSE LLC
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


Name:           touchegg
Version:        2.0.15
Release:        0
Summary:        A multitouch gesture recogniser for GNU/Linux
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://github.com/JoseExposito/touchegg
Source:         https://github.com/JoseExposito/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         harden_touchegg.service.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  cmake(pugixml)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
Obsoletes:      %{name}-gui

%description
Touchegg is an app that runs in the background and transforms the
gestures you make on your touchpad or touchscreen into visible
actions in your desktop.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.conf
%{_sysconfdir}/xdg/autostart/%{name}.desktop

%changelog
