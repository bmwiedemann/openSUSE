#
# spec file for package poxml
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           poxml
Version:        22.12.0
Release:        0
Summary:        Tools for translating DocBook XML files with Gettext
License:        GPL-2.0-only AND GFDL-1.2-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  antlr
BuildRequires:  antlr-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Xml)

%description
This is a collection of tools that facilitate translating DocBook XML
files using Gettext message files (PO files).

%package -n kde-l10n-devel
Summary:        Tools for translating DocBook XML files with Gettext
Recommends:     %{name}-lang
Obsoletes:      kde4-l10n-devel < %{version}
Provides:       kde4-l10n-devel = %{version}
Provides:       %{name} = %{version}

%description -n kde-l10n-devel
This is a collection of tools that facilitate translating DocBook XML
files using Gettext message files (PO files).

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
%cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n kde-l10n-devel -p /sbin/ldconfig
%postun -n kde-l10n-devel -p /sbin/ldconfig

%files -n kde-l10n-devel
%license COPYING*
%{_kf5_bindir}/po2xml
%{_kf5_bindir}/split2po
%{_kf5_bindir}/swappo
%{_kf5_bindir}/xml2pot
%{_kf5_mandir}/man1/*.*%{ext_man}

%files lang -f %{name}.lang

%changelog
