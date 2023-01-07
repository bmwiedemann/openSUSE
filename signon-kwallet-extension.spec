#
# spec file for package signon-kwallet-extension
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
Name:           signon-kwallet-extension
Version:        22.12.1
Release:        0
Summary:        KWallet integration for signon framework
License:        GPL-2.0-or-later
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  signon-plugins-devel
BuildRequires:  signond-libs-devel
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
# This is very important - the default in signon is to save tokens in plaintext
# in a sqlite database...
Supplements:    signond

%description
KWallet integration for signon framework.

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license COPYING
%dir %{_kf5_libdir}/signon/extensions
%{_kf5_libdir}/signon/extensions/libkeyring-kwallet.so*

%changelog
