#
# spec file for package kmousetool
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
Name:           kmousetool
Version:        19.08.1
Release:        0
Summary:        Automatic Mouse Click
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kdelibs4support-devel
BuildRequires:  knotifications-devel
BuildRequires:  oxygen-icon-theme-large
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  sbl
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.3.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
Provides:       kmousetool5 = %{version}
Obsoletes:      kmousetool5 < %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Clicks the mouse for you, reducing hand strain.

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
  %suse_update_desktop_file org.kde.kmousetool   Utility Accessibility

%files
%license COPYING COPYING.DOC
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/*.desktop
%{_kf5_bindir}/kmousetool
%{_kf5_iconsdir}/hicolor/*/*/*.png
%{_kf5_mandir}/man1/kmousetool*
%{_kf5_sharedir}/kmousetool/
%{_kf5_appstreamdir}/org.kde.kmousetool.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
