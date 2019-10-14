#
# spec file for package kmag
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
Name:           kmag
Version:        19.08.2
Release:        0
Summary:        Screen Magnifier
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  sbl
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
Obsoletes:      kmag5 < %{version}
Provides:       kmag5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Magnifies a part of the screen.

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
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kmag      Utility Accessibility

%files
%{_kf5_bindir}/kmag
%{_kf5_applicationsdir}/org.kde.kmag.desktop
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_iconsdir}/hicolor/*/apps/kmag.*
%{_kf5_mandir}//man1/kmag.1*
%{_kf5_sharedir}/kmag/
%{_kf5_appstreamdir}/org.kde.kmag.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
