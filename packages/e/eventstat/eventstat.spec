#
# spec file for package eventstat
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           eventstat
Version:        0.04.12
Release:        0
Summary:        Kernel event states monitoring tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://kernel.ubuntu.com/~cking/eventstat/
Source:         https://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
Eventstat periodically dumps out the current kernel event state.It keeps track
of current events and outputs the change in events on each output update.
The tool requires sudo to run since it needs to write to /proc/timer_stats to
start and stop the event monitoring.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
BuildRequires:  bash-completion
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (eventstat and bash-completion)
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
%{_bindir}/eventstat
%{_mandir}/man8/eventstat.8%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
