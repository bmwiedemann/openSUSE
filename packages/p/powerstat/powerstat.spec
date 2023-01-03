#
# spec file for package powerstat
#
# Copyright (c) 2023 SUSE LLC
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


Name:           powerstat
Version:        0.02.28
Release:        0
Summary:        Laptop power measuring tool
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/ColinIanKing/powerstat
Source:         https://github.com/ColinIanKing/powerstat/archive/refs/tags/V%{version}.tar.gz

%description
Powerstat measures the power consumption of a mobile PC that has a battery
power source. The output is like vmstat but also shows power consumption
statistics. At the end of a run, powerstat will calculate the average,
standard deviation and min/max of the gathered data.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
BuildRequires:  bash-completion
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (powerstat and bash-completion)
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
%doc README.md
%{_bindir}/powerstat
%{_mandir}/man8/powerstat.8%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
