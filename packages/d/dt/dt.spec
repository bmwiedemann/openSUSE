#
# spec file for package dt
#
# Copyright (c) 2021 SUSE LLC
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


Name:           dt
Version:        23.28
Release:        0
Summary:        Generic data test program
License:        MIT
Group:          System/Filesystems
URL:            https://github.com/RobinTMiller/dt
Source:         dt-%{version}.tar.xz
# PATCH-FIX-UPSTREAM dt-manpage.patch -- https://github.com/RobinTMiller/dt/issues/4
Patch0:         dt-manpage.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(uuid)

%description
dt is a generic data test program used to verify proper operation of
peripherals, file systems, device drivers, or any data stream supported
by the operating system.  In its simplest mode of operation, dt writes
and then verifys its default data pattern, then displays performance
statisics and other test parameters before exiting.  Since verification
of data is performed, dt can be thought of as a generic diagnostic tool.

%prep
%setup -q
%patch0

%build
CFLAGS=$(pkg-config --cflags uuid)
export CFLAGS="%{optflags} $CFLAGS -I.. -DAIO -DFIFO -DMMAP -D__linux__ -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -DTHREADS -DSCSI"
export LIBS=$(pkg-config --libs uuid)
export LDFLAGS="-Wl,--no-undefined -Wl,-z,now"
mkdir build
cd build
make %{?_smp_mflags} \
  LIBS="$LIBS" \
  CFLAGS="$CFLAGS" \
  LDFLAGS="$LDFLAGS" \
  -f ../Makefile.linux \
  VPATH=.. OS=linux

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
