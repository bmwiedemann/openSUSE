#
# spec file for package smemstat
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


Name:           smemstat
Version:        0.02.11
Release:        0
Summary:        Memory usage monitoring tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/ColinIanKing/smemstat
Source:         https://github.com/ColinIanKing/smemstat/archive/refs/tags/V%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncursesw)

%description
Smemstat reports the physical memory usage taking into consideration shared
memory. The tool can either report a current snapshot of memory usage or
periodically dump out any changes in memory.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (smemstat and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} $(pkg-config --cflags ncursesw) -fwhole-program"
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/smemstat
%{_mandir}/man8/smemstat.8%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
