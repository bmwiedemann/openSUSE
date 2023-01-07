#
# spec file for package kross-interpreters
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
Name:           kross-interpreters
Version:        22.12.1
Release:        0
Summary:        Diverse bindings for KROSS
License:        LGPL-2.1-or-later
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  ruby-devel
BuildRequires:  xz
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
The kross interpreter for Ruby

%package -n kross-ruby
Summary:        Ruby Bindings for kross

%description -n kross-ruby
The Ruby bindings which can be used with KROSS

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files -n kross-ruby
%license COPYING
%{_kf5_plugindir}/krossruby.so

%changelog
