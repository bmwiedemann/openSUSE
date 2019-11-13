#
# spec file for package kde-print-manager
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 24.9.90 Raymond Wooninck <tittiatcoke@gmail.com>
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


%define rname print-manager
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kde-print-manager
Version:        19.08.3
Release:        0
Summary:        A print manager for KDE
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cups
BuildRequires:  cups-backends
BuildRequires:  cups-client
BuildRequires:  cups-devel
BuildRequires:  cups-pk-helper
BuildRequires:  extra-cmake-modules
BuildRequires:  kcmutils-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  knotifications-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  pkgconfig
BuildRequires:  plasma-framework-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang
Conflicts:      kde4-print-manager
Obsoletes:      kde4-print-manager < %{version}
Obsoletes:      print-manager5 < %{version}
Provides:       print-manager5 = %{version}
Provides:       dbus(com.redhat.NewPrinterNotification)

%description
This project is a replacement for the previous printing management of KDE.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build -- -DCUPS_INCLUDE_DIR=%{_includedir}/cups
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif
  %suse_update_desktop_file -r org.kde.PrintQueue  Utility  DesktopUtility
  %suse_update_desktop_file -r org.kde.kde-add-printer  Utility  DesktopUtility

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README
%dir %{_kf5_appstreamdir}/
%dir %{_kf5_plasmadir}
%dir %{_kf5_plasmadir}/plasmoids
%{_kf5_applicationsdir}/org.kde.kde-add-printer.desktop
%{_kf5_applicationsdir}/org.kde.ConfigurePrinter.desktop
%{_kf5_applicationsdir}/org.kde.PrintQueue.desktop
%{_kf5_appstreamdir}/org.kde.plasma.printmanager.appdata.xml
%{_kf5_bindir}/configure-printer
%{_kf5_bindir}/kde-add-printer
%{_kf5_bindir}/kde-print-queue
%{_kf5_libdir}/libkcupslib.so*
%{_kf5_notifydir}/printmanager.notifyrc
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.printmanager/
%{_kf5_plugindir}/kcm_printer_manager.so
%{_kf5_plugindir}/kded_printmanager.so
%{_kf5_qmldir}/org/kde/plasma/printmanager/
%{_kf5_servicesdir}/kcm_printer_manager.desktop
%{_kf5_servicesdir}/kded/
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.printmanager.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
