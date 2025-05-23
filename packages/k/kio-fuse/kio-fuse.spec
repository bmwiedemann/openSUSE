#
# spec file for package kio-fuse
#
# Copyright (c) 2023 SUSE LLC
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
Name:           kio-fuse
Version:        5.1.0
Release:        0
Summary:        Access KIO over the regular filesystem
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        kio-fuse.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5KIO) >= 5.96.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(fuse3)
%if 0%{?suse_version} > 1599
BuildRequires:  /usr/bin/dbus-run-session
%endif
Requires:       fuse3
# For %%check
BuildRequires:  kio-extras5
# While kio itself can make use of this, it's most likely used through dolphin
Supplements:    dolphin
# Make sure the protocols in a Plasma 6 session also work via kio-fuse (boo#1226375)
Requires:       (kio-extras5 if kio-extras)

%description
kio-fuse is a daemon which makes KIO URLs accessible to KIO unaware
applications using FUSE.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%if %{pkg_vcmp util-linux >= 2.34}
%check
# The hack below only works with util-linux 3.34+.
# Without working umount, the tests can't work :-(

ret=0
fusermount3 || ret=$?
if [ $ret -eq 126 ] ; then
  # No permission to run fusermount3: boo#1159963
  exit 0
fi

# Hack to make "fusermount3 -u" work in the OBS context
# (https://github.com/openSUSE/obs-build/issues/535)
echo -e '#!/bin/sh\numount $2' >> fusermount3
chmod a+x fusermount3
export PATH=$PWD:$PATH

%ctest
%endif

%files
%license LICENSES/*
%{_kf5_sharedir}/dbus-1/services/org.kde.KIOFuse.service
%{_libexecdir}/kio-fuse
%{_tmpfilesdir}/kio-fuse-tmpfiles.conf
%{_userunitdir}/kio-fuse.service

%changelog
