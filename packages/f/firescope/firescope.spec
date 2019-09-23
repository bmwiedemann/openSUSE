#
# spec file for package firescope
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           firescope
Version:        0.2
Release:        0
Summary:        Read linux kernel logs over firewire
License:        GPL-2.0+
Group:          System/Monitoring
Url:            ftp://firstfloor.org/pub/ak/firescope/
Source:         http://ftp.suse.com/pub/people/ak/firescope/%{name}-%{version}.tar.bz2
Source1:        COPYING.GPLv2
Patch0:         firescope-fix-uninitialised
BuildRequires:  gcc
BuildRequires:  libraw1394-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%ifarch x86_64
BuildRequires:  gcc-32bit
BuildRequires:  glibc-32bit
BuildRequires:  glibc-devel-32bit
BuildRequires:  libraw1394-devel-32bit
%endif

%description
Firescope allows to read remote kernel memory over a firewire
connection.  On x86-64 it is normally used to read the kernel log
buffer.

%prep
%setup -q
%patch0 -p1

%build
# disable as-needed to fix build
export SUSE_ASNEEDED=0
RPM_OPT_FLAGS="%{optflags} -fno-strict-aliasing"
make CC="gcc" CFLAGS="%{optflags}" firescope %{?_smp_mflags}
%ifarch x86_64
make CC="gcc" CFLAGS="%{optflags}" firescope32 %{?_smp_mflags}
%endif
cp %{SOURCE1} COPYING

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 firescope %{buildroot}/%{_bindir}
%ifarch x86_64
install -m 755 firescope32 %{buildroot}/%{_bindir}
%endif
install -m 644 firescope.1 %{buildroot}%{_mandir}/man1

%files
%defattr(-, root, root)
%doc QUICKSTART CHANGES COPYING
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}*

%changelog
