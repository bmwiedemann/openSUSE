#
# spec file for package kdesdk-kioslaves
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without released
%define rname kdesdk-kio
Name:           kdesdk-kioslaves
Version:        22.12.1
Release:        0
Summary:        KDE SDK KIO slaves
License:        GPL-2.0-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Core)

%description
This package contains additional KIO slaves.

%lang_package -n kio_perldoc

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang kio5_perldoc kio_perldoc.lang

%package -n kio_perldoc
Summary:        KDE KIO-Slave to browse Perl documentation
Recommends:     perl-doc
# for users of the unstable repo
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n kio_perldoc
This KDE KIO slave allows to browse the Perl documentation.

%files -n kio_perldoc
%license COPYING
%dir %{_kf5_sharedir}/kio_perldoc
%{_kf5_plugindir}/kf5/kio/perldoc.so
%{_kf5_sharedir}/kio_perldoc/pod2html.pl

%files -n kio_perldoc-lang -f kio_perldoc.lang

%changelog
