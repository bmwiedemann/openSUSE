#
# spec file for package mailcommon
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


%define kf5_version 5.58.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           mailcommon
Version:        19.08.3
Release:        0
Summary:        Base KDE PIM library for mail-handling applications
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-mime-devel
BuildRequires:  akonadi-server-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdesignerplugin-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kmailtransport-devel >= %{_kapp_version}
BuildRequires:  kmime-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdepim-devel
BuildRequires:  mailimporter-devel >= %{_kapp_version}
BuildRequires:  messagelib-devel >= %{_kapp_version}
BuildRequires:  phonon4qt5-devel
BuildRequires:  pimcommon-devel
BuildRequires:  pkgconfig
BuildRequires:  syntax-highlighting-devel
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(Qt5DBus) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.10.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.10.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
Recommends:     %{name}-lang

%description
The mailcommon library is a KDE PIM project to provide a
framework to build applications which handle e-mail.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build

%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%package -n libKF5MailCommon5
Summary:        Common Mail library for kdepim
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}

%description -n libKF5MailCommon5
This package provides the mailcommon library, a base KDE PIM library
to build email-handling applications.

%post -n libKF5MailCommon5 -p /sbin/ldconfig
%postun -n libKF5MailCommon5 -p /sbin/ldconfig

%package devel
Summary:        Development package for mailcommon
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       akonadi-mime-devel
Requires:       akonadi-server-devel
Requires:       kcompletion-devel
Requires:       libKF5MailCommon5 = %{version}
Requires:       libkdepim-devel
Requires:       messagelib-devel
Requires:       pimcommon-devel

%description devel
This package contains the development headers for the mailcommon library.

%files
%license COPYING*
%{_kf5_debugdir}/mailcommon.categories
%{_kf5_debugdir}/mailcommon.renamecategories

%files devel
%license COPYING*
%dir %{_kf5_plugindir}/designer
%{_kf5_includedir}/MailCommon/
%{_kf5_includedir}/mailcommon/
%{_kf5_includedir}/mailcommon_version.h
%{_kf5_libdir}/cmake/KF5MailCommon/
%{_kf5_libdir}/libKF5MailCommon.so
%{_kf5_mkspecsdir}/qt_MailCommon.pri
%{_kf5_plugindir}/designer/mailcommonwidgets.so

%files -n libKF5MailCommon5
%license COPYING*
%{_libdir}/libKF5MailCommon.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
