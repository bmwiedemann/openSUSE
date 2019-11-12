#
# spec file for package dragonplayer
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

%define rname dragon
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           dragonplayer
Version:        19.08.3
Release:        0
Summary:        Multimedia Player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  knotifications-devel
BuildRequires:  kparts-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  solid-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Dragon Player is a simple KDE 4 video player.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file org.kde.dragonplayer   Video

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%config %{_kf5_configdir}/dragonplayerrc
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/*/
%doc %{_kf5_mandir}/man1/dragon.1*
%license COPYING COPYING.DOC
%doc README
%{_kf5_applicationsdir}/org.kde.dragonplayer.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/dragon
%{_kf5_iconsdir}/*/*/*/*.*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/solid/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
