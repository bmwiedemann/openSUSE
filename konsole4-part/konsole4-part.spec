#
# spec file for package konsole4-part
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           konsole4-part
Version:        4.14.3
Release:        0
Summary:        KDE Terminal
License:        GPL-2.0+
Group:          System/X11/Terminals
Url:            http://www.kde.org/
Source0:        konsole-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libkde4-devel
BuildRequires:  libkonq-devel >= %version
BuildRequires:  xz
BuildRequires:  pkgconfig(libxklavier)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde4_runtime_requires

%description
Konsole is a terminal emulator for the K Desktop Environment.
This package provides KPart of the Konsole application.

%prep
%setup -q -n konsole-%{version}

%build
  %cmake_kde4 -d build
  %make_jobs

%install
  pushd build
  %kde4_makeinstall
  popd
  %fdupes -s %{buildroot} 
  rm %{buildroot}%_kde4_applicationsdir/konsole.desktop
  rm %{buildroot}%_kde4_bindir/konsole
  rm %{buildroot}%_kde4_bindir/konsoleprofile
  rm -rf %{buildroot}%_kde4_htmldir/en/konsole/
  %kde_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING README
%_kde4_libdir/*.so
%_kde4_modulesdir/*.so
%_kde4_appsdir/kconf_update/
%_kde4_appsdir/konsole/
%_kde4_servicesdir/*.desktop
%_kde4_servicesdir/ServiceMenus/*.desktop
%_kde4_servicetypes/*.desktop

%changelog
