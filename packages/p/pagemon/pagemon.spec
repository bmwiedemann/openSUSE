#
# spec file for package pagemon
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


Name:           pagemon
Version:        0.02.00
Release:        0
Summary:        Interactive memory/page monitoring tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/ColinIanKing/pagemon
Source:         https://github.com/ColinIanKing/pagemon/archive/refs/tags/V%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
pagemon is a ncurses based interactive memory/page monitoring tool
allowing one to browse the memory map of an active running process
on Linux.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (pagemon and bash-completion)
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
%{_sbindir}/pagemon
%{_mandir}/man8/pagemon.8%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
