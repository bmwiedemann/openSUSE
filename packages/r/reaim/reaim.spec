#
# spec file for package reaim
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


Name:           reaim
Version:        7.0.1.13
Release:        0
Summary:        A tool to benchmark overall system performance
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://sourceforge.net/projects/re-aim-7
Source0:        http://sourceforge.net/projects/re-aim-7/files/re-aim/%{version}/osdl-aim-%{version}.tar.gz
Source1:        %{name}.changes
Patch0:         bugfixes.patch
Patch1:         fix-aio.patch
Patch2:         fix-defaults.patch
Patch3:         fix-tst_sig.patch
Patch4:         fix-abs-paths.patch
Patch6:         fix-diskdir.patch
Patch8:         fix-pipe_test.patch
Patch9:         c_macro_problem.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libaio-devel
BuildRequires:  libtool

%description
This tool benchmarks overall system speed by mixing measurements of
file system speed and execution speed under VM and CPU pressure.

%prep
%autosetup -n osdl-aim-7 -p1

%build
autoreconf -fiv
%configure
%make_build CFLAGS="%{optflags} -lm -ffloat-store -fcommon -D_GNU_SOURCE -DSHARED_OFILE"

%install
# install wants to be interactive
%make_install ||:

%files
%license COPYING
%doc NEWS README AUTHORS
%{_bindir}/reaim
%{_datadir}/reaim

%changelog
