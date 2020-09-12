#
# spec file for package cpustat
#
# Copyright (c) 2020 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           cpustat
Version:        0.02.12
Release:        0
Summary:        Periodic cpu utilization statistics
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://kernel.ubuntu.com/~cking/cpustat/
Source:         https://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  ncurses-devel

%description
cpustat periodically reports the current CPU utilization of running tasks and
can optionally report per CPU and per task utilization statistics at the end
of a run.
cpustat has been designed and optimized to use a minimal amount of CPU cycles
to monitor a system hence it is a light weight alternative to traditional
process monitoring tools such as top.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (cpustat and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_sbindir}/cpustat
%{_mandir}/man8/cpustat.8%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
