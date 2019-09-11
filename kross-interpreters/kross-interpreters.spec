#
# spec file for package kross-interpreters
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kross-interpreters
Version:        19.08.0
Release:        0
Summary:        Diverse bindings for KROSS
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kdelibs4support-devel
BuildRequires:  kross-devel >= 5.11.0
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
The kross interpreters for Ruby, Python and Java

%package -n kross-python
Summary:        Python Bindings for kross
Group:          Development/Libraries/KDE

%description -n kross-python
The Python bindings which can be used with KROSS

%package -n kross-ruby
Summary:        Ruby Bindings for kross
Group:          Development/Libraries/KDE

%description -n kross-ruby
The Ruby bindings which can be used with KROSS

%package -n kross-java
Summary:        Java Bindings for kross
Group:          Development/Libraries/KDE

%description -n kross-java
The Java bindings which can be used with KROSS

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  #make DESTDIR=%{buildroot} install

%files -n kross-python
%license COPYING
%{_kf5_plugindir}/krosspython.so

%changelog
