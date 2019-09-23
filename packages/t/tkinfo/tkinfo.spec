#
# spec file for package tkinfo (Version 2.8)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           tkinfo
Url:            http://math-www.uni-paderborn.de/~axel/tkinfo/
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/Texinfo
Version:        2.8
Release:        134
Summary:        Viewer for info-files
Source:         %name-%version.tar.bz2
Patch0:         tkinfo.patch
Patch1:         tkinfo-alias.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
TkInfo is a tk script to read GNU "info" files and display them. TkInfo
can be used stand-alone (via WISH) or embedded within an application to
provide integrated, online help.



Authors:
--------
    Axel Boldt <boldt@math.ucsb.edu>

%prep
%setup
%patch0
%patch1

%build

%install
mkdir -p %buildroot/usr/bin
install -m 755 tkinfo %buildroot/usr/bin
mkdir -p %buildroot%_mandir/man1
install -m 644 tkinfo.1 %buildroot%_mandir/man1

%files
%defattr(-,root,root)
%doc README
%doc %_mandir/*/*
/usr/bin/tkinfo

%changelog
