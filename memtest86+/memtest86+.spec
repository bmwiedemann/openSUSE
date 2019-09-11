#
# spec file for package memtest86+
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           memtest86+
Version:        5.01
Release:        0
Summary:        Memory Testing Image for x86 Architecture
License:        BSD-3-Clause
Group:          System/Boot
URL:            http://www.memtest.org
Source:         http://www.memtest.org/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         fix-destdir
Patch1:         memtest86+-5.01-no-optimization.patch
Patch2:         memtest86+-5.01-compile-fix.patch
Patch3:         memtest86+-5.01-array-size-fix.patch
Patch4:         memtest86+-gcc5.patch
#!BuildIgnore:  gcc-PIE
Requires(pre):  /sbin/update-bootloader
Requires(pre):  perl
Provides:       lilo:/boot/memtest.bin
Obsoletes:      memtest86 <= 3.2
Provides:       memtest86 > 3.2
ExclusiveArch:  %{ix86} x86_64
%ifarch x86_64
BuildRequires:  glibc-devel-32bit
%endif

%description
Memtest86 is an image that can be booted instead of a real OS. Once booted,
it can be used to test the computer's memory.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make %{?_smp_mflags}

%install
install -Dpm 0644 memtest.bin \
  %{buildroot}/boot/memtest.bin

%post
if [ "$YAST_IS_RUNNING" != instsys -a $1 = 1 -a \
	 -x /sbin/update-bootloader ]; then
	/sbin/update-bootloader --add --image /boot/memtest.bin --name "Memory Test (memtest86+)"
fi
true

%postun
test -x /sbin/update-bootloader && /sbin/update-bootloader --remove --force --image /boot/memtest.bin || true

%files
/boot/memtest.bin
%doc README* changelog FAQ

%changelog
