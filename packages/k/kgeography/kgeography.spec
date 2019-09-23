#
# spec file for package kgeography
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
Name:           kgeography
Version:        19.08.1
Release:        0
Summary:        Geography Trainer
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Other
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
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kservice-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KGeography is a geography learning program.

%if %{with lang}
%lang_package
%endif

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
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/kgeography/
%{_kf5_applicationsdir}/org.kde.kgeography.desktop
%{_kf5_appsdir}/kgeography/
%{_kf5_bindir}/kgeography
%{_kf5_configkcfgdir}/kgeography.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/kgeography.*
%{_kf5_kxmlguidir}/kgeography/
%{_kf5_appstreamdir}/org.kde.kgeography.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%dir %{_kf5_sharedir}/locale/fi/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/fr/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/ja/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/pl/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/uk/LC_SCRIPTS
%dir %{_kf5_sharedir}/locale/ml/LC_SCRIPTS
%lang (fi) %{_kf5_sharedir}/locale/fi/LC_SCRIPTS/kgeography
%lang (fr) %{_kf5_sharedir}/locale/fr/LC_SCRIPTS/kgeography
%lang (ja) %{_kf5_sharedir}/locale/ja/LC_SCRIPTS/kgeography
%lang (pl) %{_kf5_sharedir}/locale/pl/LC_SCRIPTS/kgeography
%lang (uk) %{_kf5_sharedir}/locale/uk/LC_SCRIPTS/kgeography
%lang (ml) %{_kf5_sharedir}/locale/ml/LC_SCRIPTS/kgeography
%endif

%changelog
