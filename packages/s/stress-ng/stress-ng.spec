#
# spec file for package stress-ng
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2015-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           stress-ng
Version:        0.15.01
Release:        0
Summary:        Tool to load and stress a computer
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            https://github.com/ColinIanKing/stress-ng
Source:         https://github.com/ColinIanKing/stress-ng/archive/refs/tags/V%{version}.tar.gz
BuildRequires:  keyutils-devel
BuildRequires:  libaio-devel
BuildRequires:  libapparmor-devel
BuildRequires:  libattr-devel
BuildRequires:  libbsd-devel
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  zlib-devel

%description
stress-ng can stress various subsystems of a computer. It can stress load CPU,
cache, disk, memory, socket and pipe I/O, scheduling and much more. stress-ng
is a re-write of the original stress tool by Amos Waterland but has many
additional features such as specifying the number of bogo operations to run,
execution metrics, a stress verification on memory and compute operations and
considerably more stress mechanisms.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (stress-ng and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for stress-ng.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build

%install
install -D -p -m 0755 stress-ng   \
  %{buildroot}%{_bindir}/stress-ng
install -D -p -m 0644 stress-ng.1 \
  %{buildroot}%{_mandir}/man1/stress-ng.1
install -D -p -m 0644 bash-completion/stress-ng \
  %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/stress-ng
%{_mandir}/man1/stress-ng.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
