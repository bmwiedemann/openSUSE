#
# spec file for package forkstat
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


Name:           forkstat
Version:        0.02.14
Release:        0
Summary:        Process fork/exec/exit monitoring tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://kernel.ubuntu.com/~cking/forkstat/
Source:         https://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.xz

%description
Forkstat monitors process fork(), exec() and exit() activity. It is useful for
monitoring system behaviour and to track down rogue processes that are spawning
off processes and potentially abusing the system.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(forkstat:bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%{_bindir}/forkstat
%{_mandir}/man8/forkstat.8%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
