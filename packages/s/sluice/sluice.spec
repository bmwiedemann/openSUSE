#
# spec file for package sluice
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           sluice
Version:        0.02.08
Release:        0
Summary:        Rate limiting data piping tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://kernel.ubuntu.com/~cking/sluice/
Source:         http://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

%description
Sluice reads from standard input and write to standard output at a specified
data rate. This can be useful for benchmarking and exercising I/O streaming at
desired throughput rates.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%{_bindir}/sluice
%{_mandir}/man1/sluice.1%{?ext_man}

%changelog
