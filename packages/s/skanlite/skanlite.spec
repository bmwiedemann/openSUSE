#
# spec file for package skanlite
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           skanlite
Version:        2.1.0.1
Release:        0
Summary:        Image Scanner Application
License:        LGPL-2.1+
Group:          Hardware/Scanner
Url:            https://www.kde.org/applications/graphics/skanlite/
Source0:        http://download.kde.org/stable/%{name}/2.1/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libksane-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang = %{version}
Obsoletes:      %{name}-doc < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Skanlite is an image scanner application by KDE.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%find_lang %{name} --all-name
# Fix rpmlint warning "script-without-shebang"
chmod 644 %{buildroot}%{_kf5_applicationsdir}/org.kde.skanlite.desktop

%files
%defattr(-,root,root,-)
%license src/COPYING
%doc src/TODO
%{_kf5_applicationsdir}/org.kde.skanlite.desktop
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.skanlite.appdata.xml
%{_kf5_bindir}/skanlite
%doc %{_kf5_htmldir}/en/

%files lang -f %{name}.lang
%defattr(-,root,root)
%doc %{_kf5_htmldir}
%exclude %{_kf5_htmldir}/en/

%changelog
