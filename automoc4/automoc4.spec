#
# spec file for package automoc4
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Url:            http://www.kde.org

Name:           automoc4
BuildRequires:  cmake
BuildRequires:  kde4-filesystem
BuildRequires:  libqt4-devel
Version:        0.9.88
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        CMake automatic MOC Generation
License:        MIT
Group:          Development/Tools/Building
Source0:        http://download.kde.org/stable/%{name}/%{version}/%name-%version.tar.bz2
Requires:       libqt4 >= %(rpm -q --queryformat '%%{VERSION}' libqt4)

%description
automoc4 is a tool to add rules for generating Qt moc files
automatically to projects that use CMake as the buildsystem.

%prep
%setup -q

%build
  %cmake_kde4 -d build
  %make_jobs

%install
  cd build
  make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
/usr/bin/automoc4
%_libdir/automoc4

%changelog
