#
# spec file for package wm-icons
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           wm-icons
Version:        0.4.0
Release:        0
Summary:        Window Manager Icons, themable icon distribution
License:        GPL-2.0+
Group:          System/X11/Icons
Url:            http://wm-icons.sourceforge.net/
Source0:        http://download.sourceforge.net/wm-icons/wm-icons-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Window Manager Icons is an efficient icon distribution designed to
be standardized and configurable.  Includes several themed icon sets,
scripts, and configurations for several window managers.



Authors:
--------
    Mikhael Goikhman <migo@homemail.com>
    Olivier Chapuis <olivier.chapuis@free.fr>

%prep
%setup 
find . -type d | xargs chmod 755

%build
%if %suse_version > 1010
%define prefix /usr
%else
%define prefix /usr/X11R6
%endif
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --enable-all-sets
make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} mandir=$RPM_BUILD_ROOT%{_mandir} ROOT_PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%doc doc/FAQ doc/README.3dpixmaps doc/README.martys doc/README.penguins
%doc doc/icons.lst doc/wm-icons.lsm
%{prefix}/bin/*
%{prefix}/share/wm-icons
%{prefix}/share/icons/wm-icons
%{_mandir}/man?/*

%changelog
