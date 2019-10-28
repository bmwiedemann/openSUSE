#
# spec file for package krfb
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           krfb
Version:        19.08.2
Release:        0
Summary:        Screen sharing using the VNC/RFB protocol
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  LibVNCServer-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdnssd-framework-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  knotifications-devel
BuildRequires:  kwallet-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  xcb-util-image-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
# Needed for 42.3
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
%if 0%{?sle_version} < 120300
BuildRequires:  gcc6-c++
%else
BuildRequires:  gcc7-c++
%endif
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
VNC-compatible server to share KDE desktops.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%if 0%{?suse_version} < 1330
  # It does not build with the default compiler (GCC 4.8) on Leap 42.x
  %if 0%{?sle_version} < 120300
    export CC=gcc-6
    export CXX=g++-6
  %else
    export CC=gcc-7
    export CXX=g++-7
  %endif
%endif
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kf5 -d build -- -DBUILD_EXPERIMENTAL_TUBES_SUPPORT="on"
  make %{?_smp_mflags}

%install
  %make_install -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.krfb         System   RemoteAccess

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/krfb/
%{_kf5_applicationsdir}/org.kde.krfb.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/krfb
%{_kf5_iconsdir}/hicolor/*/apps/krfb.*
%{_kf5_libdir}/libkrfbprivate.so*
%{_kf5_plugindir}/krfb/
%{_kf5_servicetypesdir}/krfb-framebuffer*.desktop
%{_kf5_servicetypesdir}/krfb-events.desktop
%{_kf5_sharedir}/krfb/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
