#
# spec file for package step
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
Name:           step
Version:        20.08.2
Release:        0
Summary:        An interactive physics simulator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gsl-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libqalculate-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Plotting)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
BuildRequires:  libqt5-linguist-devel
%endif
Recommends:     %{name}-lang

%description
Step is an interactive physical simulator. The user first places some
bodies on the scene, add some forces such as gravity or springs. When
the simulation is run, Step shows how the scene will evolve according
to the laws of physics. Every property of bodies/forces in the
experiment may be changed, even during simulation.

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
    %find_lang %{name} --with-man --all-name --with-qt
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file org.kde.%{name}      X-KDE-Edu-Teaching
  %fdupes -s %{buildroot}

%files
%license COPYING*
%doc AUTHORS ChangeLog README
%doc %lang(en) %{_kf5_htmldir}/en/step/
%config %{_kf5_configdir}/step.knsrc
%dir %{_kf5_appstreamdir}
%dir %{_kf5_configkcfgdir}
%dir %{_kf5_kxmlguidir}/step/
%dir %{_kf5_sharedir}/mime/
%dir %{_kf5_sharedir}/mime/packages
%{_kf5_applicationsdir}/org.kde.step.desktop
%{_kf5_appsdir}/step/
%{_kf5_appstreamdir}/org.kde.step.appdata.xml
%{_kf5_bindir}/step
%{_kf5_configkcfgdir}/step.kcfg
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_sharedir}/mime/packages/org.kde.step.xml
%{_kf5_kxmlguidir}/step/stepui.rc

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%%dir %{_kf5_sharedir}/locale/nn/LC_SCRIPTS/
%%dir %{_kf5_sharedir}/locale/nn/LC_SCRIPTS/step
%lang(nn) %{_kf5_sharedir}/locale/nn/LC_SCRIPTS/step/step.js
%endif

%changelog
