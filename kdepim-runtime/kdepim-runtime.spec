#
# spec file for package kdepim-runtime
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdepim-runtime
Version:        19.08.0
Release:        0
Summary:        Akonadi resources for PIM applications
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-calendar-devel >= %{_kapp_version}
BuildRequires:  akonadi-contact-devel >= %{_kapp_version}
BuildRequires:  akonadi-mime-devel >= %{_kapp_version}
BuildRequires:  akonadi-notes-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules
BuildRequires:  kalarmcal-devel >= %{_kapp_version}
BuildRequires:  kcalcore-devel >= %{_kapp_version}
BuildRequires:  kcalutils-devel >= %{_kapp_version}
BuildRequires:  kcodecs-devel >= %{kf5_version}
BuildRequires:  kconfig-devel >= %{kf5_version}
BuildRequires:  kcontacts-devel >= %{_kapp_version}
BuildRequires:  kdav-devel >= %{_kapp_version}
BuildRequires:  kdelibs4support-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kidentitymanagement-devel >= %{_kapp_version}
BuildRequires:  kimap-devel >= %{_kapp_version}
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  kitemmodels-devel >= %{kf5_version}
BuildRequires:  kmailtransport-devel >= %{_kapp_version}
BuildRequires:  kmbox-devel >= %{_kapp_version}
BuildRequires:  kmime-devel >= %{_kapp_version}
BuildRequires:  knewstuff-devel >= %{kf5_version}
BuildRequires:  knotifyconfig-devel >= %{kf5_version}
BuildRequires:  ktextwidgets-devel >= %{kf5_version}
BuildRequires:  kwallet-devel >= %{kf5_version}
BuildRequires:  kwidgetsaddons-devel >= %{kf5_version}
BuildRequires:  libkgapi-devel >= 1.9.81
BuildRequires:  libkolabxml-devel >= 1.1
BuildRequires:  libxerces-c-devel
BuildRequires:  libxslt-devel
# broken KF5::AkonadiContact, phonon is in interface includes, but private link library
BuildRequires:  phonon4qt5-devel
BuildRequires:  pimcommon-devel >= %{_kapp_version}
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  syndication-devel
BuildRequires:  xz
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  pkgconfig(Qt5DBus) >= 5.5.0
BuildRequires:  pkgconfig(Qt5NetworkAuth) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.5.0
BuildRequires:  pkgconfig(Qt5TextToSpeech) >= 5.7.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.5.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.5.0
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.5.0
Requires:       akonadi-plugin-calendar
Requires:       akonadi-plugin-contacts
Requires:       akonadi-plugin-kalarmcal
Requires:       akonadi-plugin-mime
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     %{name}-lang
Provides:       kio-pimlibs = %{version}
Obsoletes:      kdepim4-runtime < %{version}
Obsoletes:      kio-pimlibs < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif

%description
This package contains the Akonadi resources, agents and plugins needed to
use PIM applications.

%lang_package

%prep
%setup -q -n kdepim-runtime-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}

%make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  rm -rvf %{buildroot}%{_kf5_libdir}/*.so

%post
/sbin/ldconfig
%mime_database_post

%postun
/sbin/ldconfig
%mime_database_postun

%files
%license COPYING*
%{_kf5_debugdir}/kdepim-runtime.categories
%{_kf5_debugdir}/kdepim-runtime.renamecategories
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/
%dir %{_kf5_iconsdir}/hicolor/24x24
%dir %{_kf5_iconsdir}/hicolor/72x72
%dir %{_kf5_iconsdir}/hicolor/96x96
%{_kf5_iconsdir}/hicolor/24x24/apps
%{_kf5_iconsdir}/hicolor/72x72/apps
%{_kf5_iconsdir}/hicolor/96x96/apps
%{_kf5_bindir}/*
%{_kf5_dbusinterfacesdir}/*.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_libdir}/*.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}
%{_kf5_sharedir}/akonadi/
%{_kf5_sharedir}/mime/packages/kdepim-mime.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
