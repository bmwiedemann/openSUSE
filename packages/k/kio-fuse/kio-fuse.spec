#
# spec file for package kio-fuse
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        5.1.1
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
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
# Older versions have a bug in chown error reporting
BuildRequires:  cmake(KF6KIO) >= 6.19
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  pkgconfig(fuse3)
Requires:       fuse3
# For %%check
BuildRequires:  kio-extras
BuildRequires:  /usr/bin/dbus-run-session
# While kio itself can make use of this, it's most likely used through dolphin
Supplements:    dolphin

%description
kio-fuse is a daemon which makes KIO URLs accessible to KIO unaware
applications using FUSE.

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_TESTING=ON -DBUILD_WITH_QT6=ON
%kf6_build

%install
%kf6_install

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
%{_kf6_sharedir}/dbus-1/services/org.kde.KIOFuse.service
%{_libexecdir}/kio-fuse
%{_tmpfilesdir}/kio-fuse-tmpfiles.conf
%{_userunitdir}/kio-fuse.service

%changelog
