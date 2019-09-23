#
# spec file for package vacation
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vacation
Version:        1.2.7.1
Release:        0
Summary:        A way to automatically reply to incoming e-mail
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Utilities
Url:            http://vacation.sf.net/
Source:         http://downloads.sf.net/vacation/%name-%version.tar.gz
Patch0:         vacation-%{version}.diff
Patch1:         vacation-%{version}.multiple-vacationmsg_files.diff
Patch3:         vacation-%{version}.strip.diff
# PATCH-FIX-UPSTREAM bsc#944326 - long From: header (two lines) not handled correctly
Patch4:         0001-Patch-to-handle-long-folded-headers-from-Zdenek-Havr.patch
# PATCH-FIX-SUSE Also handle junkfilter based on procmail
Patch5:         vacation-%{version}-junkfilter.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gdbm-devel

%description
This program answers your e-mail when you are lying on the beach.

Documentation: man vacation



Authors:
--------
    Sean F Rima <sean.rima@tcob1.uklinux.net>
    Eric P. Allman
    Harald Milz <hm@seneca.muc.de>

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4
%patch5

%build
# %ifarch ia64 x86_64 s390x ppc64
# # neededforbuild  gdbm-32bit gdbm-devel-32bit glibc-devel-32bit
#    RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -m32"
#%endif
    chmod -R u+w,g+r,o+r .
    make %{?jobs:-j%jobs} clobber
    make %{?jobs:-j%jobs}

%install
# %ifarch ia64 x86_64 s390x ppc64
# # neededforbuild  gdbm-32bit gdbm-devel-32bit glibc-devel-32bit
#     RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -m32"
# %endif
    mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT%{_mandir}/man{1,5}
    make install MANDIR=$RPM_BUILD_ROOT%{_mandir}/man BINDIR=$RPM_BUILD_ROOT/usr/bin
    rm -f $RPM_BUILD_ROOT%{_mandir}/man5/forward.5
    echo '.so man5/aliases.5' > $RPM_BUILD_ROOT%{_mandir}/man5/forward.5
    chmod 0444 $RPM_BUILD_ROOT%{_mandir}/man5/forward.5

%clean
    rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING ChangeLog README
/usr/bin/vacation
/usr/bin/vaclook
%{_mandir}/man1/vacation.1.gz
%{_mandir}/man1/vaclook.1.gz
%{_mandir}/man5/forward.5.gz

%changelog
