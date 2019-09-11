#
# spec file for package tkirc (Version 2.46)
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


Name:           tkirc
License:        GPL-2.0+
Group:          Productivity/Networking/IRC
Requires:       tk /usr/bin/epic
AutoReqProv:    on
Version:        2.46
Release:        387
Summary:        A graphical IRC client
Source:         %name%version.tar.bz2
Patch:          tkirc.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tkirc is a graphical frontend for the ircII or epic textmode IRC
clients. It is written in Tcl/Tk and thus can be greatly configured,
customized and extended.

Documentation can be found under /usr/share/doc/packages/tkirc/README
and the directory /usr/share/doc/packages/tkirc/.tkirc2 contains
configuration examples, that can be copied over to one's home
directory.



Authors:
--------
    Andreas Gelhausen <atte@gecko.North.DE>

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_SCRIPT install -m755
%define INSTALL_DATA install -m644

%prep
%setup -n tkirc2
%patch

%build

%install
    %INSTALL_DIR $RPM_BUILD_ROOT/usr/bin
    %INSTALL_SCRIPT tkirc2 $RPM_BUILD_ROOT/usr/bin
    ln -sf tkirc2 $RPM_BUILD_ROOT/usr/bin/tkirc

%files
%defattr(-,root,root)
/usr/bin/tkirc2
/usr/bin/tkirc
%doc CHANGES
%doc COPYING
%doc README
%doc .tkirc2

%changelog
* Wed Jan 24 2007 ro@suse.de
- move from /usr/X11R6 to /usr
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Feb 24 2004 hmacht@suse.de
- building as non-root
* Thu May 23 2002 max@suse.de
- New version 2.46.
- Patched to use epic instead of ircii.
- Using Buildroot now.
* Wed Apr 11 2001 max@suse.de
- Added Group: Applications/Networking
- Added Buildarchitectures: noarch
- changed path to wish
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Mar 18 1998 max@suse.de
- new version: 1.202
* Tue Oct 28 1997 max@suse.de
- added tkirc as a new package
