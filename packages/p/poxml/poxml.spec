#
# spec file for package poxml
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           poxml
Version:        24.12.1
Release:        0
Summary:        Tools for translating DocBook XML files with Gettext
License:        GPL-2.0-only AND GFDL-1.2-only
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  antlr
BuildRequires:  antlr-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  gettext-devel
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
This is a collection of tools that facilitate translating DocBook XML
files using Gettext message files (PO files).

%package -n kde-l10n-devel
Summary:        Tools for translating DocBook XML files with Gettext
Recommends:     poxml-lang
Obsoletes:      kde4-l10n-devel < %{version}
Provides:       kde4-l10n-devel = %{version}
Provides:       poxml = %{version}

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
%cmake_kf6 -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n kde-l10n-devel

%files -n kde-l10n-devel
%license COPYING*
%{_kf6_bindir}/po2xml
%{_kf6_bindir}/split2po
%{_kf6_bindir}/swappo
%{_kf6_bindir}/xml2pot
%{_kf6_mandir}/man1/*.*%{ext_man}

%files lang -f %{name}.lang

%changelog
