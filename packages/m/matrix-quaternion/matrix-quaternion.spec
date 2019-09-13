#
# spec file for package matrix-quaternion
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


Name:           matrix-quaternion
Version:        0.0.9.4
Release:        0
Summary:        QT Matrix client
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/QMatrixClient/Quaternion
Source0:        https://github.com/QMatrixClient/Quaternion/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(QMatrixClient) >= 0.5.1
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       %{name}-lang
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
# upstream use instead Qt5Core, Qt5Gui, Qt5Network, Qt5Quick, Qt5Widgets:
# BuildRequires:  libqt5-qtdeclarative-devel libqt5-qtquickcontrols

%description
Quaternion is a desktop IM client for the Matrix protocol using QT.

%lang_package

%prep
%setup -q -n Quaternion-%{version}

%build
%if 0%{?suse_version} < 1500
export CC="gcc-7"
export CXX="g++-7"
%endif
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%cmake
%make_jobs

%install
%cmake_install

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} < 1500
%postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_bindir}/quaternion
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*
%dir %{_datadir}/QMatrixClient/quaternion

%files lang
%{_datadir}/QMatrixClient/quaternion/translations/

%changelog
