#
# spec file for package dt
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


Name:           dt
Version:        18.32
Release:        0
Summary:        Generic data test program
License:        MIT
Group:          System/Filesystems
URL:            http://www.scsifaq.org/RMiller_Tools/dt.html
Source:         http://dl.dropboxusercontent.com/u/32363629/Datatest/dt-source-v%{version}.tar.gz
Patch0:         dt-manpage.patch
Patch1:         dt-wformat-security.patch
Patch2:         dt-default-source-define.patch

%description
dt is a generic data test program used to verify proper operation of
peripherals, file systems, device drivers, or any data stream supported
by the operating system.  In its simplest mode of operation, dt writes
and then verifys its default data pattern, then displays performance
statisics and other test parameters before exiting.  Since verification
of data is performed, dt can be thought of as a generic diagnostic tool.

%prep
%setup -q -n dt.v%{version}
%patch0
%patch1
%patch2

%build
export CFLAGS="%{optflags} -I.. -DAIO -DFIFO -DMMAP -D__linux__ -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -DTHREADS -DSCSI"
export LDFLAGS="-Wl,--no-undefined -Wl,-z,now"
mkdir build
cd build
make %{?_smp_mflags} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" -f ../Makefile.linux VPATH=.. OS=linux

%install
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -Dpm 0755 build/dt \
  %{buildroot}/%{_bindir}/dt
install -Dpm 0644 Documentation/dt.man  \
  %{buildroot}/%{_mandir}/man1/dt.1
install -pm 0755 Scripts/dt? \
  %{buildroot}%{_datadir}/%{name}
install -pm 0644 data/pattern_* \
  %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%{_bindir}/dt
%{_datadir}/%{name}
%{_mandir}/man1/dt.1%{?ext_man}

%changelog
