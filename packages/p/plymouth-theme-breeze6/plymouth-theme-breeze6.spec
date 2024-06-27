#
# spec file for package plymouth-theme-breeze6
#
# Copyright (c) 2024 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%if 0%{?is_opensuse}
%define _distro_logo os
%define _distro_name openSUSE
%else
%define _distro_logo plasma
%endif

%if 0%{?suse_version} == 1500
%define _distro_version Leap
%else
%if 0%{?is_opensuse} && !0%{?sle_version}
%define _distro_version Tumbleweed
%else
BuildRequires:  fix-version-checks-in-here
%endif
%endif

%define kf6_version 6.2.0

%define rname breeze-plymouth

%bcond_without released
Name:           plymouth-theme-breeze6
Version:        6.1.1
Release:        0
Summary:        Plymouth "Breeze" theme
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  plymouth-devel
Requires:       plymouth-plugin-breeze = %{version}
Requires:       plymouth-plugin-label-ft
Requires(post): plymouth-scripts
Provides:       plymouth-theme-breeze = %{version}
Obsoletes:      plymouth-theme-breeze < %{version}

%description
This package contains the "breeze" boot splash theme for Plymouth.

%package -n plymouth-plugin-breeze
Summary:        Plymouth "breeze" plugin
Provides:       plymouth-theme-breeze-plugin-breeze = %{version}
Obsoletes:      plymouth-theme-breeze-plugin-breeze < %{version}

%description -n plymouth-plugin-breeze
This package contains the "breeze" boot splash plugin for Plymouth.
It features an extensible, scriptable boot splash language that simplifies
the process of designing custom boot splash themes.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DDISTRO_NAME=%{_distro_name} \
  -DDISTRO_VERSION=%{_distro_version} \
  -DDISTRO_LOGO=%{_distro_logo}

%kf6_build

%install
%kf6_install

%files
%license LICENSES/*
%{_datadir}/plymouth/themes/breeze*/

%files -n plymouth-plugin-breeze
%license LICENSES/*
%{_libdir}/plymouth/breeze-text.so

%changelog
