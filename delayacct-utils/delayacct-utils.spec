#
# spec file for package delayacct-utils
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


Name:           delayacct-utils
BuildRequires:  kernel-source
Summary:        Delay Accounting Utilities
License:        GPL-2.0
Group:          System/Monitoring
%define version %(rpm -q --qf '%%{VERSION}' kernel-devel)
Version:        %version
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  kernel-devel
Source0:        delayacct-utils.tar.bz2
Patch0:         delayacct-utils-nl.patch

%description
Delay accounting allows the administrator to track the time an
application spends waiting on disk I/O, swap I/O and CPU scheduling.
This can help pin-point resource shortages in a system configuration.

%prep
%setup -q -n %name
%patch0 -p1
mkdir -p linux
%if 0%{?suse_version} <= 1220
cp /usr/src/linux/include/linux/taskstats.h linux/taskstats.h
%else
cp /usr/src/linux/include/uapi/linux/taskstats.h linux/taskstats.h
%endif
if [ -f /usr/src/linux/Documentation/accounting/getdelays.c ]; then
	cp /usr/src/linux/Documentation/accounting/getdelays.c .
fi
if [ -f /usr/src/linux/tools/accounting/getdelays.c ]; then
	cp /usr/src/linux/tools/accounting/getdelays.c .
fi

%build
make CCOPT="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%_bindir $RPM_BUILD_ROOT%_mandir/man1
install -m 555 getdelays $RPM_BUILD_ROOT%_bindir
install -m 444 getdelays.1 $RPM_BUILD_ROOT%_mandir/man1

%files
%defattr(444,root,root,755)
%doc README COPYING
%attr(555,root,root) %{_bindir}/getdelays
%attr(444,root,root) %{_mandir}/man?/*

%changelog
