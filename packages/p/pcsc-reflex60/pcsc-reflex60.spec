#
# spec file for package pcsc-reflex60 (Version 2.2.0)
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


Name:           pcsc-reflex60
Version:        2.2.0
Release:        135
Group:          Productivity/Security
License:        BSD-3-Clause
Url:            http://musclecard.com/sourcedrivers.html
Summary:        PCSC driver for Schlumberger Reflex 60 smartcard readers
Source0:        slb_rf60-drv-%{version}.tar.bz2
Patch0:         slb_rf60-drv-%{version}-cflags.diff
Patch1:         slb_rf60-drv-%{version}-prototypes.diff
Patch2:         slb_rf60-drv-%{version}-uninitialized.diff
Patch3:         slb_rf60-drv-%{version}-fmt.diff
Patch4:         slb_rf60-drv-%{version}-ldflags.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pcsc-lite
%define ifddir %{_libdir}/readers

%description
This package contains a driver for the Reflex 62 and Reflex 64 smart
card readers produced by Schlumberger.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.


%prep
%autosetup -p0 -n slb_rf60

%build
make %{?jobs:-j%jobs} lib COPTS="$RPM_OPT_FLAGS -Wno-unused" LD="gcc $LDFLAGS"

%install
install -d $RPM_BUILD_ROOT%{ifddir}/
install -m755 libslb_rf60.so $RPM_BUILD_ROOT%{ifddir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES CREDITS LICENSE README
%{ifddir}/

%changelog
* Wed Jun 17 2009 sbrabec@suse.cz
- Use correct tool for linking.
* Wed Apr 08 2009 sbrabec@suse.cz
- Require pcsc-lite.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Jan 03 2006 mjancar@suse.cz
- move to separate source package
* Mon Jan 02 2006 stark@suse.de
- removed obsolete hotplug stuff for cyberjack
- Updated pcsc-lite to version 1.2.9-beta9
- Updated CCID driver to 0.9.4
- Updated GemPC driver to 1.0.0
- package pkgconfig files to be able to build drivers outside
  the package
* Tue Dec 20 2005 ro@suse.de
- removed unpackaged man-page symlinks
* Tue Nov 29 2005 ro@suse.de
- remove keeper from nfb (unused)
* Mon Oct 10 2005 stark@suse.de
- Updated towitoko driver to 2.0.7 and install USB bundle
* Wed Sep 21 2005 stark@suse.de
- Repackaged CCID as bundle for USB usage (#116497)
* Tue Sep 20 2005 stark@suse.de
- handle old reader.conf in upgrade case
- compile with -fno-strict-aliasing
- fixed missing return in ctapi-cyberjack
* Sat Sep 17 2005 stark@suse.de
- Updated pcsc-lite to version 1.2.9beta8 (#116497)
  * use /etc/reader.conf.d/
  * adapted init script to create /etc/reader.conf
- Updated cyberjack driver to version 2.0.9
  * use rpath for cyberjack tools
- Updated ccid driver to version 0.9.3 (#116497)
- Use RPM_OPT_FLAGS everywhere
- Fixed serious compiler warnings
* Mon Sep 05 2005 skh@suse.de
- fix off-by-one error in hotplug_libusb.c [#112964]
* Mon Aug 29 2005 skh@suse.de
- Remove unnecessary files from pcsc-acr38 again [#112927]
* Mon Aug 29 2005 skh@suse.de
- package ACR38 driver in correct bundle format [#112927]
- remove orphaned /var/run/pcscd.pub when necessary [#112928]
- update ACR38u driver to version 100705 to fix crash when reader
  is plugged in [#112964]
* Tue Aug 16 2005 skh@suse.de
- Updated ACR38u driver to version 100703
* Tue Jul 26 2005 okir@suse.de
- Added ACR38u driver
* Tue Jul 26 2005 okir@suse.de
- Updated description in init script (#79287)
* Thu Jun 16 2005 meissner@suse.de
- use RPM_OPT_FLAGS in 1 more driver
- added includes to avoid implict declaration of memcpy and similar.
* Mon Apr 18 2005 ro@suse.de
- make it build with gcc-4
* Thu Mar 17 2005 okir@suse.de
- Disable support for extended-apdus, it eats 32MB of memory (#73629)
* Thu Mar 10 2005 okir@suse.de
- Fix default search location for USB bundles
* Fri Jan 21 2005 okir@suse.de
- Updated to latest upstream version
- Updated several drivers
- Added CCID driver
- Provide a more informative readers.conf file (#42620)
* Thu Jan 20 2005 ro@suse.de
- drop subpackage gpr400
* Wed Apr 28 2004 ro@suse.de
- compile formaticc with no-strict-aliasing
- fix unused return type in musclecard.c
* Wed Mar 31 2004 okir@suse.de
- Properly install testpcsc, formaticc (#37625)
- Build towitoko driver with --enable-win32-com
* Thu Mar 18 2004 okir@suse.de
- cyberjack apps installed in /bin should be executable (#36409)
* Sat Jan 10 2004 adrian@suse.de
- add %%run_ldconfig
* Tue Aug 05 2003 mge@suse.de
- merge ctapi-cyberjack into pcsc-lite: two additional
  packages are created: ctapi-cyberjack and pcsc-cyberjack
* Thu Jun 26 2003 ro@suse.de
- remove unpackaged files from buildroot
- added directories to filelist
* Fri Nov 29 2002 okir@suse.de
- added -fPIC when building eToken driver
* Fri Nov 29 2002 okir@suse.de
- Updated to latest upstream version
- Included driver for Aladdin eToken PRO
- More GNU auto#*@! headaches
- Various minor fixes
* Wed Aug 28 2002 okir@suse.de
- Moved shared objects to /usr/lib64 on ppc64/s390x (#18421)
* Mon Aug 05 2002 olh@suse.de
- fix initscript, Should-start: setserial hotplug
* Fri Aug 02 2002 okir@suse.de
- added PreReq for insserv_and_fillup
* Wed Jul 31 2002 okir@suse.de
- fixed build problem on s390x (force aclocal.m4 regen)
* Wed Jun 26 2002 ro@suse.de
- use -fPIC when building a shared lib
* Wed Jun 12 2002 okir@suse.de
- fix for bug #15051 (hey, it's a palindrome bug:):
  missing %%doc DRIVERS file; misc silly binaries moved
  out of /usr/bin
* Tue Apr 30 2002 okir@suse.de
- Fixed build problem introduced by previous patch
* Tue Apr 30 2002 okir@suse.de
- updated to latest upstream version
- added drivers for these readers: Towitoko, Schlumberger Reflex 6x,
  Gemplus GPR 400, GemPlus GemPC 410/430
* Tue Apr 09 2002 ro@suse.de
- fixed for latest automake/autoconf
* Wed Feb 13 2002 stark@suse.de
- spec-file cleanup
- LSB compliant init-script
* Mon Jan 14 2002 ro@suse.de
- removed START_PCSCD
* Wed Nov 14 2001 ro@suse.de
- call aclocal
* Sun Aug 26 2001 mge@suse.de
- updated to 1.0.0Beta
- fixed /etc/init.d/pcscd status-handling (bug #9069)
* Thu Jun 07 2001 ro@suse.de
- fix broken Makefile.am
* Mon Apr 23 2001 mge@suse.de
- update to 0.9.1
* Thu Apr 19 2001 mge@suse.de
- created package
