#
# spec file for package rfbplaymacro (Version 0.2.2)
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


Name:           rfbplaymacro
Url:            http://cyberelk.net/tim/rfbplaymacro/
License:        GPL-2.0+
Group:          System/X11/Utilities
#Requires:     xforms
AutoReqProv:    on
Version:        0.2.2
Release:        30
Summary:        Replays VNC macros
Source:         http://cyberelk.net/tim/data/rfbplaymacro/stable/%name-%version.tar.bz2
#Patch:        %name-%version.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
rfbplaymacro replays VNC macros as created by rfbproxy to a VNC server.



Authors:
--------
    Tim Waugh <twaugh@redhat.com>

%prep
%setup
#%patch

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README AUTHORS COPYING test.rfm
/usr/bin/rfbplaymacro

%changelog
* Fri May 09 2008 mfabian@suse.de
- bnc#388222: update to 0.2.2
  • src/rfbplaymacro.c (connect_to_server): Use protocol 3.3.
  • src/rfbplaymacro.c: Made more tolerant of bad input files, and
  of servers requesting passwords when none has been specified.
  • test.rfm: New file, created by Ralf Mueller.
  • README: Updated.
  • src/rfbplaymacro.c (main): Accept 'password' in the input file.
  Spotted by Ralf Mueller.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sat Jan 10 2004 adrian@suse.de
- add %%defattr
* Mon Jun 16 2003 coolo@suse.de
- use BuildRoot
* Tue Jul 09 2002 uli@suse.de
- update -> 0.2.0 (VNC authentication support)
* Wed Apr 17 2002 uli@suse.de
- initial package
