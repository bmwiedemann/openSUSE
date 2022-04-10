#
# spec file for package delayacct-utils
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Name:           delayacct-utils
Version:        %{version}
Release:        0
Summary:        Delay Accounting Utilities
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://www.kernel.org/
Source0:        delayacct-utils.tar.bz2
Patch0:         delayacct-utils-nl.patch
BuildRequires:  kernel-devel
BuildRequires:  kernel-source

%description
Delay accounting allows the administrator to track the time an
application spends waiting on disk I/O, swap I/O and CPU scheduling.
This can help pin-point resource shortages in a system configuration.

%package rebuild
Summary:        Empty package to ensure rebuilding delayacct-utils in OBS
Group:          System/Monitoring
%requires_eq    kernel-source

%description rebuild
This is empty package that ensures delayacct-utils is rebuilt every time
kernel-default is rebuilt in OBS.

There is no reason to install this package.

%prep
%setup -q -n %{name}
%patch0 -p1
mkdir -p linux
%if 0%{?suse_version} <= 1220
cp %{_prefix}/src/linux/include/linux/taskstats.h linux/taskstats.h
%else
cp %{_prefix}/src/linux/include/uapi/linux/taskstats.h linux/taskstats.h
%endif
if [ -f %{_prefix}/src/linux/Documentation/accounting/getdelays.c ]; then
	cp %{_prefix}/src/linux/Documentation/accounting/getdelays.c .
fi
if [ -f %{_prefix}/src/linux/tools/accounting/getdelays.c ]; then
	cp %{_prefix}/src/linux/tools/accounting/getdelays.c .
fi

%build
%make_build CCOPT="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -m 555 getdelays %{buildroot}%{_bindir}
install -m 444 getdelays.1 %{buildroot}%{_mandir}/man1

%files
%license COPYING
%doc README
%attr(555,root,root) %{_bindir}/getdelays
%attr(444,root,root) %{_mandir}/man?/*

%files rebuild
%license COPYING

%changelog
