#
# spec file for package breeze4-style
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


Name:           breeze4-style
Version:        5.17.1
Release:        0
Summary:        Plasma Desktop artwork, styles and assets
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/breeze-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/breeze-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE add-support-for-Q3ListView-to-the-KDE4-style.patch boo#973728 wbauer@tmo.at -- fixes collapse/expand icon in Q3ListView that still may be used by some KDE4 applications (knode e.g.)
Patch0:         add-support-for-Q3ListView-to-the-KDE4-style.patch
BuildRequires:  automoc4
BuildRequires:  cmake >= 2.8.12
BuildRequires:  kde4-filesystem
BuildRequires:  libkde4-devel
BuildRequires:  libqt4-devel
BuildRequires:  libxcb-devel
# This sets the breeze4 style as default in a Plasma environment
Recommends:     kdebase4-workspace-libs
Supplements:    packageand(breeze5-style:libqt4)
%if 0%{?suse_version} > 1500
ExclusiveArch:  do_not_build
%endif

%description
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package contains kde4 backport of new default Plasma 5 style.

%package -n libbreezecommon4-5
Summary:        Library containing support code for the Breeze Qt4 style
Group:          System/Libraries

%description -n libbreezecommon4-5
Library containing support code for the Breeze Qt4 style.

%prep
%setup -q -n breeze-%{version}
%autopatch -p1

%build
  %cmake_kde4 -d build -- -DUSE_KDE4=ON
  %make_jobs

%install
  %kde4_makeinstall -C build

%post   -p /sbin/ldconfig -n libbreezecommon4-5
%postun -p /sbin/ldconfig -n libbreezecommon4-5

%files
%license COPYING*
%{_kde4_modulesdir}/
%{_kde4_appsdir}/

%files -n libbreezecommon4-5
%license COPYING*
%{_libdir}/libbreezecommon4.so.*

%changelog
