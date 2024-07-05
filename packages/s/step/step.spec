#
# spec file for package step
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           step
Version:        24.05.2
Release:        0
Summary:        An interactive physics simulator
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/step
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Plotting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(eigen3) >= 3.2.2
BuildRequires:  pkgconfig(gsl)
# Disabled with Qt6 builds
# BuildRequires:  pkgconfig(libqalculate)
Obsoletes:      step5 < %{version}
Provides:       step5 = %{version}

%description
Step is an interactive physical simulator. The user first places some
bodies on the scene, add some forces such as gravity or springs. When
the simulation is run, Step shows how the scene will evolve according
to the laws of physics. Every property of bodies/forces in the
experiment may be changed, even during simulation.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name --with-qt

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc AUTHORS ChangeLog README
%doc %lang(en) %{_kf6_htmldir}/en/step/
%{_kf6_applicationsdir}/org.kde.step.desktop
%{_kf6_appstreamdir}/org.kde.step.appdata.xml
%{_kf6_bindir}/step
%{_kf6_configkcfgdir}/step.kcfg
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_knsrcfilesdir}/step.knsrc
%{_kf6_sharedir}/mime/packages/org.kde.step.xml
%{_kf6_sharedir}/step/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/step/
# Not detected by find-lang.sh
%dir %{_kf6_sharedir}/locale/nn/LC_SCRIPTS/
%dir %{_kf6_sharedir}/locale/nn/LC_SCRIPTS/step
%lang(nn) %{_kf6_sharedir}/locale/nn/LC_SCRIPTS/step/step.js

%changelog
