#
# spec file for package compartm
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


Name:           compartm
Version:        1.1
Release:        0
Summary:        A Wrapper to Securely Run Insecure or Untrusted Programs
License:        GPL-2.0+
Group:          Productivity/Security
Source:         compartment-%version.tar.gz
Patch0:         compartment-%version.diff
Patch1:         compartment-%version-prctl.patch
Patch2:         compartment-%version-nochown.patch
Patch3:         compartment-%version-format.dif
Patch4:         compartment-%version-newcaps.dif
Patch5:         compartment-%version-envp.dif
Patch6:         compartment-%version-va_copy.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Compartment provides all possibilities (chroot, kernel capabilities)
for securely running insecure or untrusted programs. It provides all
necessary options to fine-tune the security tightening process as
needed.



Authors:
--------
    Marc Heuse <marc@suse.de>

%define kversion %(uname -r)

%prep
%setup -n compartment-%version
%patch0 -p1
%patch1 -p1 -b .prctl
%patch2
%patch3
%patch4
%patch5
%patch6

%build
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc README LICENCE CHANGES TODO
%_mandir/man1/compartment.1*
/usr/sbin/compartment

%changelog
