#
# spec file for package kdialog
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
Name:           kdialog
Version:        19.08.0
Release:        0
Summary:        KDE version of xdialog
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kdelibs4support-devel >= 5.7.0
BuildRequires:  kf5-filesystem
BuildRequires:  kio-devel >= 5.7.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2.0
Recommends:     %{name}-lang

%description
KDialog can be used to show nice dialog boxes from shell scripts.

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

%files
%license COPYING*
%doc README
%{_kf5_bindir}/kdialog
%{_kf5_bindir}/kdialog_progress_helper
%{_kf5_dbusinterfacesdir}/org.kde.kdialog.ProgressDialog.xml
%{_kf5_appstreamdir}/org.kde.kdialog.metainfo.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
