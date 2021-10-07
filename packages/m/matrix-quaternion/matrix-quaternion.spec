#
# spec file for package matrix-quaternion
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.0.95.1
Release:        0
Summary:        QT Matrix client
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/quotient-im/Quaternion
Source0:        https://github.com/quotient-im/Quaternion/archive/%{version}/matrix-quaternion-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Olm)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(QtOlm)
BuildRequires:  cmake(Quotient) >= 0.6.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       %{name}-lang
Conflicts:      matrix-quaternion-git
Provides:       matrix-quaternion = %{version}
Provides:       matrix-quaternion-git = %{version}
Provides:       quaternion = %{version}
Provides:       quaternion-git = %{version}

%description
Quaternion is a desktop IM client for the Matrix protocol using QT.

%lang_package

%prep
%setup -q -n Quaternion-%{version}

%build
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
%license COPYING
%doc README.md
%{_bindir}/quaternion
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*
%dir %{_datadir}/Quotient
%dir %{_datadir}/Quotient/quaternion

%files lang
%{_datadir}/Quotient/quaternion/translations/

%changelog
