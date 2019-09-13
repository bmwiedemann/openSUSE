#
# spec file for package smem
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           smem
Version:        1.4
Release:        0
Summary:        Application memory usage report tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://www.selenic.com/smem/
Source:         https://www.selenic.com/smem/download/%{name}-%{version}.tar.gz
Patch0:         smemcap-fix-build.patch
Requires:       python2

%description
smem is a tool that can give numerous reports on memory usage on Linux
systems. Unlike existing tools, smem can report proportional set size (PSS),
which is a more meaningful representation of the amount of memory used by
libraries and applications in a virtual memory system.

Because large portions of physical memory are typically shared among
multiple applications, the standard measure of memory usage known as
resident set size (RSS) will significantly overestimate memory usage. PSS
instead measures each application's "fair share" of each shared area to give
a realistic measure.

%prep
%setup -q
%patch0 -p1
sed -i 's|%{_bindir}/env python|%{_bindir}/python2|g' smem

%build
gcc %{optflags} -Wall smemcap.c -o smemcap

%install
install -d %{buildroot}/%{_bindir}
install -pm 0755 smem %{buildroot}/%{_bindir}/smem
install -pm 0755 smemcap %{buildroot}/%{_bindir}/smemcap
install -Dpm 0644 smem.8 %{buildroot}/%{_mandir}/man8/smem.8

%files
%license COPYING
%{_bindir}/smem
%{_bindir}/smemcap
%{_mandir}/man8/smem.8%{?ext_man}

%changelog
