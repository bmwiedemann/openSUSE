#
# spec file for package autobench
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           autobench
Version:        2.1.2
Release:        0
Summary:        Simple Perl script for automating the process of benchmarking a web server
License:        GPL-2.0-only
Url:            http://www.xenoclast.org/autobench
Source0:        http://www.xenoclast.org/autobench/downloads/%{name}-%{version}.tar.gz
Source1:        http://www.xenoclast.org/autobench/downloads/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  perl
Requires:       gawk
Requires:       gnuplot
Requires:       httperf
Requires:       perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Autobench is a simple Perl script for automating the process of benchmarking
a web server (or for conducting a comparative test of two different web
servers). The script is a wrapper around  httperf. Autobench runs httperf a
number of times against each host, increasing the number of requested
connections per second on each iteration, and extracts the significant data
from the httperf output, delivering a CSV or TSV format file which can be
imported directly into a spreadsheet for analysis/graphing.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make \
  install \
	PREFIX=%{buildroot} \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man1
# deleting harcoded path to the build root
sed -i '/MASTER_CONFIG/s/"\([^"]*\)"/"\/etc\/autobench.conf"/' %{buildroot}%{_bindir}/autobench

%files
%defattr(-,root,root)
%doc ChangeLog README
%config %{_sysconfdir}/autobench.conf
%{_bindir}/autobench
%{_bindir}/autobench_admin
%{_bindir}/autobenchd
%{_bindir}/bench2graph
%{_bindir}/crfile
%{_bindir}/sesslog
%{_mandir}/man1/autobench.1%{ext_man}
%{_mandir}/man1/autobench_admin.1%{ext_man}
%{_mandir}/man1/autobenchd.1%{ext_man}
%{_mandir}/man1/bench2graph.1%{ext_man}
%{_mandir}/man1/crfile.1%{ext_man}
%{_mandir}/man1/sesslog.1%{ext_man}

%changelog
