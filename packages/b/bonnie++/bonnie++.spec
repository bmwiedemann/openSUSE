#
# spec file for package bonnie++
#
# Copyright (c) 2020 SUSE LLC
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


Name:           bonnie++
Version:        1.98
Release:        0
Summary:        A Bonnie-Like File System Benchmark
License:        MIT
URL:            https://www.coker.com.au/bonnie++/
Source:         https://www.coker.com.au/bonnie++/bonnie++-%{version}.tgz
# PATCH-FIX-UPSTREAM bonnie++-1.96-makefile.patch -- fixes make install
Patch0:         bonnie++-1.96-makefile.patch
BuildRequires:  gcc-c++

%description
Bonnie++ is a benchmark suite aimed at performing a number of simple
hard drive and file system performance tests.

%prep
%setup -q
%patch0

%build
%configure \
  --disable-stripping
%make_build clean
%make_build MORECFLAGS="%{optflags}"

%install
%make_install

%files
%doc README-2.00 README.txt
%{_bindir}/bon_csv2html
%{_bindir}/bon_csv2txt
%{_bindir}/generate_randfile
%{_sbindir}/bonnie++
%{_sbindir}/getc_putc
%{_sbindir}/getc_putc_helper
%{_sbindir}/zcav
%{_mandir}/man1/bon_csv2html.1%{?ext_man}
%{_mandir}/man1/bon_csv2txt.1%{?ext_man}
%{_mandir}/man1/generate_randfile.1%{?ext_man}
%{_mandir}/man8/bonnie++.8%{?ext_man}
%{_mandir}/man8/getc_putc.8%{?ext_man}
%{_mandir}/man8/zcav.8%{?ext_man}

%changelog
