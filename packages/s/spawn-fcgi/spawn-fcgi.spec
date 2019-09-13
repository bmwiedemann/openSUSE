#
# spec file for package spawn-fcgi
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           spawn-fcgi
Version:        1.6.4
Release:        0
Summary:        Spawn FastCGI applications independent of the webserver
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
%define pkg_version %{version}
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
Url:            http://redmine.lighttpd.net/projects/spawn-fcgi/
Source:         http://www.lighttpd.net/download/spawn-fcgi-%{version}.tar.bz2
#

%description
spawn-fcgi is used to spawn FastCGI applications independent of the webserver.

Authors:
---------
    Jan Kneschke
    Stefan Buehler

%prep
%setup

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/spawn-fcgi
%{_mandir}/man1/spawn-fcgi.1*

%changelog
