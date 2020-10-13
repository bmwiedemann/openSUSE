#
# spec file for package krdc
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           krdc
Version:        20.08.2
Release:        0
Summary:        Remote Desktop Connection
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  LibVNCServer-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  freerdp
BuildRequires:  freerdp-devel
BuildRequires:  libssh-devel
BuildRequires:  oxygen5-icon-theme-large
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
Requires:       breeze5-icons
Requires:       freerdp
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Krdc allows to connect to VNC and RDP compatible servers.

%package devel
Summary:        Development files for krdc
Group:          Development/Libraries/KDE
Requires:       krdc = %{version}

%description devel
Development libraries and headers needed to build software using krdc

%lang_package

%prep
%setup -q

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  for i in 128 16 22 32 48 64
  do
     mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/${i}x${i}/apps
     cp %{_kf5_iconsdir}/oxygen/base/${i}x${i}/apps/krdc.png %{buildroot}%{_kf5_iconsdir}/hicolor/${i}x${i}/apps/
  done
  %suse_update_desktop_file -r org.kde.krdc         System   RemoteAccess

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.DOC
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/krdc/
%{_kf5_applicationsdir}/org.kde.krdc.desktop
%{_kf5_bindir}/krdc
%{_kf5_configkcfgdir}/krdc.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/krdc.png
%{_kf5_kxmlguidir}/krdc/
%{_kf5_libdir}/libkrdccore.so.*
%{_kf5_plugindir}/krdc/
%{_kf5_servicesdir}/ServiceMenus/
%{_kf5_servicesdir}/krdc_rdp_config.desktop
%{_kf5_servicesdir}/krdc_vnc_config.desktop
%{_kf5_servicesdir}/rdp.protocol
%{_kf5_servicesdir}/vnc.protocol
%{_kf5_appstreamdir}/org.kde.krdc.appdata.xml

%files devel
%{_includedir}/krdc/
%{_includedir}/krdccore_export.h
%{_kf5_libdir}/libkrdccore.so

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
