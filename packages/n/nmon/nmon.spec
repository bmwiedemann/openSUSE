#
# spec file for package nmon
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2011-2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           nmon
Version:        16q
Release:        0
Summary:        Performance Monitor
License:        GPL-3.0-only
URL:            https://nmon.sourceforge.io/pmwiki.php
Source0:        https://sourceforge.net/projects/nmon/files/lmon%{version}.c
Source1:        https://www.gnu.org/licenses/gpl-3.0.txt
BuildRequires:  ncurses-devel
Provides:       lmon = %{version}

%description
This systems administrator, tuner, benchmark tool gives you a huge amount of
important performance information in one go. It can output the data in two ways

1. On screen (console, telnet, VNC, putty or X Windows) using curses for low
   CPU impact which is updated once every two seconds. You hit single characters
   on you keyboard to enable/disable the various sorts of data.
   * You can display the CPU, memory, network, disks (mini graphs or numbers),
     file systems, NFS, top processes, resources (Linux version & processors)
     and on Power micro-partition information.
2. Save the data to a comma separated file for analysis and longer term data
   capture.
   * Use this together with nmon Analyser Excel 2000 spreadsheet, which loads
     the nmon output file and automatically creates dozens of graphs ready for
     you to study or write performance reports.
   * Filter this data, add it to a rrd database (using an excellent freely
     available utility called rrdtool). This graphs the data to .gif or .png
     files plus generates the webpage .html file and you can then put the
     graphs directly on a website automatically on AIX with no need of a
     Windows based machine.
   * Directly put the data into a rrd database or other database for your own
     analysis

%prep
%setup -q -T -c %{name}-%{version}

%build
export CFLAGS="%{optflags} \
  -fPIE \
  -D JFS \
  -D GETUSER \
  -D LARGEMEM \
  -D KERNEL_2_6_18 \
  %if !0%{?is_opensuse}
  -D SLES12 \
  %endif
  %{SOURCE0}"
export LDFLAGS="-o nmon \
  -lncurses \
  -lm \
  -Wl,--as-needed \
  -Wl,--no-undefined \
  -Wl,-z,relro,-z,now \
  -pie"
%ifarch ppc ppc64 ppc64le
cc $CFLAGS -D PPC \
  $LDFLAGS
%endif
%ifarch s390x
cc $CFLAGS -D MAINFRAME \
  $LDFLAGS
%endif
%ifarch %{arm} aarch64
cc $CFLAGS -D ARM \
  $LDFLAGS
%endif
%ifarch %{ix86} x86_64
cc $CFLAGS -D X86 \
  $LDFLAGS
%endif

%install
install -Dpm 0755 nmon \
  %{buildroot}%{_bindir}/nmon
ln -s nmon %{buildroot}%{_bindir}/lmon
cp %{SOURCE1} LICENSE.GPL-3.0

%files
%license LICENSE.GPL-3.0
%{_bindir}/nmon
%{_bindir}/lmon

%changelog
