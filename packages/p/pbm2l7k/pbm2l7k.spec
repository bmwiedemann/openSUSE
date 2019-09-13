#
# spec file for package pbm2l7k (Version 990321)
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


Name:           pbm2l7k
License:        GPL-2.0+
Group:          Hardware/Printing
Provides:       lexmark7000linux
AutoReqProv:    on
Version:        990321
Release:        929
Summary:        Driver for Lexmark Printers 7000, 7200, and 5700
Source:         lexmark7000linux-990321.tar.gz
Patch:          lexmark7k.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A driver for Lexmark printers 7000, 7200, and 5700. This driver
translates PBM (Portable Bitmap) into the printer protocol for the
Lexmark printers 7000, 7200, and 5700.



Authors:
--------
    Henryk Paluch <paluch@bimbo.fjfi.cvut.cz>

%prep
%setup -n lexmark7k -c -T -a 0
%patch

%build
make 

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc lexmark7000linux-990321.lsm lexmarkprotocol.txt
%doc README stairs.pbm stairsb.prn stairsc.prn
/usr/bin/pbm2l7k
/usr/share/pbm2l7k/

%changelog
* Fri May 26 2006 schwab@suse.de
- Use RPM_OPT_FLAGS.
- Don't strip binaries.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jun 25 2004 hmacht@suse.de
- building as non-root user
* Tue May 27 2003 coolo@suse.de
- use BuildRoot
* Wed Sep 18 2002 ro@suse.de
- removed bogus self-provides
* Thu Dec 14 2000 werner@suse.de
- Group tag
* Thu Jun 08 2000 ro@suse.de
- specfile fixed
* Wed Jun 07 2000 ro@suse.de
- doc relocation
* Wed Dec 01 1999 werner@suse.de
- Fix bug in option handling
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Fri Jun 18 1999 werner@suse.de
- New package: pbm to lexmark (7000, 7200, and 5700)
