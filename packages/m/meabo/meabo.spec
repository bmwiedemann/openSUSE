#
# spec file for package meabo
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


Name:           meabo
Version:        1.0+git.20180412
Release:        0
Summary:        Multi-purpose multi-phase micro-benchmark
License:        Apache-2.0
Group:          System/Benchmark
URL:            https://github.com/ARM-software/meabo
Source:         %{name}-%{version}.tar.xz

%description
Meabo is a multi-phased multi-purpose micro-benchmark. It is a highly
configurable tool which can be used for energy efficiency studies, ARM
big.LITTLE Linux scheduler analysis and DVFS studies. It can be used for
other benchmarking as well.

The micro-benchmark is composed of 10 phases that perform various generic
calculations (from memory to compute intensive). None of the compute
kernels are optimized for a specific architecture. The micro-benchmark is
easily extensible, provides performance counter readings (today) and energy
readings (in the future), has multi-core and flexible pinning support, and
allows the user to run each phase in different configurations/

One of the main benefits of this tool is that it is scalable beyond the
aforementioned investigations, and is useful for anyone who would like
to understand system behaviour, whilst running small, simple and
well-understood computational kernels. The level of flexibility built into
the application is an added benefit, as it gives the user full control of
what is being run, where it is run, and whether it's single or
multi-threaded, all within the same run of the application.

%prep
%setup -q

%build
%make_build CC="cc %{optflags} -fcommon"

%install
install -Dpm 0755 %{name}.default \
  %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}

%changelog
