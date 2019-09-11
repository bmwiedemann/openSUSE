#
# spec file for package kbackup
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


%bcond_without lang
Name:           kbackup
Version:        19.08.0
Release:        0
Summary:        Backup program based on KDE Frameworks 5
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  karchive-devel
BuildRequires:  kf5-filesystem
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
# Needed for 42.3
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
%if 0%{?sle_version} < 120300
BuildRequires:  gcc6-c++
%else
BuildRequires:  gcc7-c++
%endif
%endif

%description
kbackup is a backup program based on KDE Frameworks 5. It allows backing
folders and files up and setting profiles to exclude or include directories
or files from the backup. It can save to both local files or remote locations.
Although GUI based, it also offers an automated, GUI-less mode.

%lang_package

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
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --with-qt --all-name
    %{kf5_find_htmldocs}
  %endif

%files
%license COPYING
%doc README
%{_kf5_bindir}/kbackup
%{_kf5_applicationsdir}/org.kde.kbackup.desktop
%dir %{_kf5_kxmlguidir}/kbackup
%{_kf5_kxmlguidir}/kbackup/kbackupui.rc
%{_kf5_appstreamdir}/org.kde.kbackup.appdata.xml
%{_kf5_iconsdir}/hicolor/*/*/
%{_datadir}/mime/packages/kbackup.xml
%doc %lang(en) %{_kf5_htmldir}/en/kbackup

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
