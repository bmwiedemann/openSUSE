#
# spec file for package kdesdk-kioslaves
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
%define rname kdesdk-kio
Name:           kdesdk-kioslaves
Version:        24.05.1
Release:        0
Summary:        KDE SDK KIO slaves
License:        GPL-2.0-only
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}

%description
This package contains additional KIO slaves.

%lang_package -n kio_perldoc

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang kio6_perldoc kio_perldoc.lang

%package -n kio_perldoc
Summary:        KDE KIO-Slave to browse Perl documentation
Recommends:     perl-doc

%description -n kio_perldoc
This KDE KIO slave allows to browse the Perl documentation.

%files -n kio_perldoc
%license COPYING
%dir %{_kf6_sharedir}/kio_perldoc
%{_kf6_plugindir}/kf6/kio/perldoc.so
%{_kf6_sharedir}/kio_perldoc/pod2html.pl

%files -n kio_perldoc-lang -f kio_perldoc.lang

%changelog
