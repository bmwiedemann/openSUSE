#
# spec file for package stressapptest
#
# Copyright (c) 2023 SUSE LLC
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


Name:           stressapptest
Version:        1.0.9
Release:        0
Summary:        Stressful application test
License:        Apache-2.0
Group:          System/Benchmark
URL:            https://github.com/stressapptest/stressapptest
Source:         https://github.com/stressapptest/stressapptest/archive/v%{version}.tar.gz
Patch0:         reproducible.patch
Patch1:         stressapptest-cstdint.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++

%description
Stressful Application Test (or stressapptest, its unix name) tries to maximize
randomized traffic to memory from processor and I/O, with the intent of
creating a realistic high load situation in order to test the existing
hardware devices in a computer.

%prep
%autosetup -p1

%build
autoreconf -fvi
export CXXFLAGS="%{optflags}"
%configure \
  --disable-silent-rules \
  --disable-default-optimizations \
  --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc NOTICE
%{_bindir}/%{name}
%{_mandir}/man1/stressapptest.1%{?ext_man}

%changelog
