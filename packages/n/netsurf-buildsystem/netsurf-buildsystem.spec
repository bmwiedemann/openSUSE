#
# spec file for package netsurf-buildsystem
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


%define src_name buildsystem
Name:           netsurf-buildsystem
Version:        1.1
Release:        0
Summary:        Makefiles shared by NetSurf projects
License:        MIT
Group:          Development/Tools
Url:            http://www.netsurf-browser.org/
Source:         http://download.netsurf-browser.org/libs/releases/%{src_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
%{name} contains makefiles shared by NetSurf projects.

%prep
%setup -q -n %{src_name}-%{version}

%build

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%defattr(-,root,root)
%doc COPYING README
%{_datadir}/%{name}

%changelog
