#
# spec file for package kio-stash
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without lang
Name:           kio-stash
Version:        1.0
Release:        0
Summary:        KIO slave for stashing temporary files
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source:         http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(KF5Config) >= 5.22.0
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     %{name}-lang
%if %{with lang}
%lang_package
%endif

%description
This KIO slave can be used to stash files in a virtual
folder temporarily. It requires use of a KIO-compatible
file manager, like dolphin.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
  # There are no translations yet
  echo > %{name}.lang
  #%%find_lang kio_stash %%{name}.lang
  #%%kf5_find_htmldocs
  %endif

%files
%defattr(-,root,root)
%doc COPYING README.md
%{_kf5_dbusinterfacesdir}/org.kde.kio.StashNotifier.xml
%{_kf5_plugindir}/kf5/
%{_kf5_appstreamdir}/org.kde.filestash.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%defattr(-,root,root,-)
%endif

%changelog
