#
# spec file for package fio
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%ifnarch s390x s390 ppc64le ppc64 ppc %{ix86} %{arm}
%bcond_without librbd
%endif
%ifarch x86_64
%bcond_without libpmem
%endif
%ifnarch s390x s390 %{arm}
%bcond_without libnuma
%endif
%bcond_without librdmacm
Name:           fio
Version:        3.37
Release:        0
Summary:        Flexible I/O tester
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            https://git.kernel.dk/?p=fio.git;a=summary
Source:         https://brick.kernel.dk/snaps/fio-%{version}.tar.bz2
BuildRequires:  cunit-devel
BuildRequires:  gtk2-devel
BuildRequires:  libaio-devel
BuildRequires:  libcurl-devel
BuildRequires:  libiscsi-devel
BuildRequires:  libnbd-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
Suggests:       gfio
Suggests:       gnuplot
%if 0%{?is_opensuse}
BuildRequires:  glusterfs-devel
%endif
%if %{with libnuma}
BuildRequires:  libnuma-devel
%endif
%if %{with librbd}
BuildRequires:  librbd-devel
%endif
%if %{with libpmem}
BuildRequires:  libpmem-devel
%endif
%if %{with librdmacm}
BuildRequires:  librdmacm-devel
%endif

%description
fio is an I/O tool meant to be used both for benchmark and stress/hardware
verification. It has support for 4 different types of I/O engines (sync,
mmap, libaio, posixaio), I/O priorities (for newer Linux kernels), rate I/O,
forked or threaded jobs, and much more. It can work on block devices as
well as files. fio accepts job descriptions in a simple-to-understand text
format. Several example job files are included. fio displays all sorts of
I/O performance information, such as completion and submission latencies
(avg/mean/deviation), bandwidth stats, cpu and disk utilization, and more.

%package -n gfio
Summary:        Graphical front end for fio
Group:          System/Benchmark
Requires:       %{name} = %{version}

%description -n gfio
gfio is a gtk based graphical front-end for fio.  It is often installed on the
testers workstation whereas fio would be installed on the server.

%prep
%autosetup -p1

%build
sed -i "s|%{_bindir}/bash|/bin/bash|g" tools/genfio
sed -i "s|-O3|%{optflags}|g" Makefile
# Not autotools configure
./configure \
  --enable-gfio \
  --enable-libiscsi \
  --enable-libnbd \
  --disable-native
%make_build

%install
%make_install \
  prefix="%{_prefix}" \
  mandir="%{_mandir}"

# Drop py2 only tool
rm %{buildroot}%{_bindir}/fio-histo-log-pctiles.py

# fix rpmlint
%python3_fix_shebang

%check
%make_build test

%files
%license COPYING MORAL-LICENSE
%doc README.rst examples
%doc HOWTO.rst REPORTING-BUGS
%doc GFIO-TODO SERVER-TODO STEADYSTATE-TODO
%{_bindir}/fio
%{_bindir}/fiologparser.py
%{_bindir}/fio_generate_plots
%{_bindir}/genfio
%{_bindir}/fio2gnuplot
%{_bindir}/fio-btrace2fio
%{_bindir}/fio-dedupe
%{_bindir}/fio-genzipf
%{_bindir}/fio-verify-state
%{_bindir}/fiologparser_hist.py
%{_bindir}/fio_jsonplus_clat2csv
%{_datadir}/fio
%{_mandir}/man1/fio.1%{?ext_man}
%{_mandir}/man1/fio_generate_plots.1%{?ext_man}
%{_mandir}/man1/fio2gnuplot.1%{?ext_man}
%{_mandir}/man1/fiologparser_hist.py.1%{?ext_man}

%files -n gfio
%{_bindir}/gfio

%changelog
