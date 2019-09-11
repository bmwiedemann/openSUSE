#
# spec file for package kwordquiz
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
Name:           kwordquiz
Version:        19.08.1
Release:        0
Summary:        Vocabulary Trainer
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Language
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkeduvocdocument-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang

%description
A flashcard and vocabulary learning program.

%lang_package

%prep
%setup -q

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %fdupes -s %{buildroot}

%files
%dir %{_kf5_appstreamdir}
%license COPYING*
%doc AUTHORS README
%config %{_kf5_configdir}/kwordquiz.knsrc
%doc %lang(en) %{_kf5_htmldir}/en/kwordquiz/
%{_kf5_applicationsdir}/org.kde.kwordquiz.desktop
%{_kf5_appsdir}/kwordquiz/
%{_kf5_appstreamdir}/org.kde.kwordquiz.appdata.xml
%{_kf5_bindir}/kwordquiz
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/kwordquiz.*
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-kwordquiz.png
%{_kf5_sharedir}/knotifications5/
%{_kf5_kxmlguidir}/kwordquiz/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
