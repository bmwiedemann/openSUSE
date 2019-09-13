#
# spec file for package rungetty
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


Name:           rungetty
Version:        1.2
Release:        0
Summary:        Minimal Getty for Virtual Consoles 
License:        GPL-2.0+
Group:          System/Base
Provides:       sysvinit:/sbin/mingetty
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2

%description
rungetty might be the getty you were looking for when you want to run any
program, not just login. If a different program than login is used it usually
is run as nobody:nogroup, or the user/group specified on the commandline.
rungetty can even be configured to autologin, under certain circumstances.
See the manual page for more information.

You have to change some lines in /etc/inittab for having any effect after
installing the package.  rungetty is based on mingetty and therefore not
suitable for serial use.

%prep
%setup -q

%build
make RPM_OPT_FLAGS="%optflags -D_FILE_OFFSET_BITS=64" DEFTERM=linux

%install
mkdir -p %buildroot{/sbin,%{_mandir}/man8}
# make install MANPATH=%buildroot/%{_mandir} DESTDIR=%buildroot
install -m 755 rungetty %buildroot/sbin/
install -m 644 rungetty.8 %buildroot/%{_mandir}/man8/

%files
%defattr(-,root,root,755)
%doc %{_mandir}/man8/rungetty.8.gz
/sbin/rungetty

%changelog
