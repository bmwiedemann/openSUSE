#
# spec file for package plymouth-theme-breeze
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Markus S., kamikazow@opensuse.org
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


%if 0%{?is_opensuse}
%define _distro_logo os
%define _distro_name openSUSE
%else
%define _distro_logo plasma
%endif

%if 0%{?suse_version} == 1315 || 0%{?suse_version} == 1500
%define _distro_version Leap
%else
%if 0%{?suse_version} == 1550
%define _distro_version Tumbleweed
%else
BuildRequires:  fix-version-checks-in-here
%endif
%endif

%bcond_without lang
Name:           plymouth-theme-breeze
Version:        5.20.0
Release:        0
Summary:        Plymouth "Breeze" theme
License:        GPL-2.0+
Group:          System/Base
URL:            http://www.kde.org
Source:         breeze-plymouth-%{version}.tar.xz
%if %{with lang}
Source1:        breeze-plymouth-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules >= 1.8.0
BuildRequires:  kf5-filesystem
BuildRequires:  plymouth-devel
Requires:       %{name}-plugin-breeze = %{version}
Requires:       plymouth-plugin-label-ft
Requires(post): plymouth-scripts

%description
This package contains the "breeze" boot splash theme for
Plymouth.

%package plugin-breeze
Summary:        Plymouth "breeze" plugin
Group:          System/Base

%description plugin-breeze
This package contains the "breeze" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%prep
%setup -q -n breeze-plymouth-%{version}

%build
  %cmake_kf5 -d build -- -DDISTRO_NAME=%{_distro_name} -DDISTRO_VERSION=%{_distro_version} -DDISTRO_LOGO=%{_distro_logo}
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license LICENSES/*
%{_datadir}/plymouth/themes/breeze*/

%files plugin-breeze
%license LICENSES/*
%{_libdir}/plymouth/breeze-text.so

%changelog
