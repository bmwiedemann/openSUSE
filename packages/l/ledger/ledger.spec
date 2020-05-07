#
# spec file for package ledger
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


Name:           ledger
Version:        3.2.0
Release:        0
Summary:        Double-entry accounting system with a command-line reporting interface
License:        BSD-3-Clause
Group:          Productivity/Office/Finance
URL:            https://github.com/ledger/ledger
Source:         https://github.com/ledger/ledger/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  mpfr-devel
BuildRequires:  python3
BuildRequires:  utfcpp-devel
Patch0:         ledger-cmakelists.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ledger is a powerful, double-entry accounting system that is accessed
from the UNIX command-line. This may put off some users, since there is
no flashy UI, but for those who want unparalleled reporting access to
their data there are few alternatives.

%prep
%setup -q
%patch0  -p1
%build
%cmake -DBUILD_LIBRARY=OFF
make %{?_smp_mflags}

%install
%cmake_install
install -m 644 -D contrib/ledger-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/ledger.sh

%files
%defattr(-,root,root)
%license LICENSE.md
%doc README.md
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/ledger
%{_datadir}/bash-completion/completions/ledger.sh

%changelog
