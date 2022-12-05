#
# spec file for package bff
#
# Copyright (c) 2022 SUSE LLC
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


Name:           bff
Version:        1.0.7
Release:        0
Summary:        Moderately-optimizing Brainfuck interpreter
License:        BSD-3-Clause
Group:          Development/Languages/Other
URL:            https://swapped.cc/bff
Source:         https://github.com/apankrat/bff/archive/v%{version}/%{name}-%{version}.tar.gz

%description
Moderately-optimizing (tm) Brainfuck interpreter

%package samples
Summary:        Samples of code written in Brainfuck
Group:          Development/Languages/Other
BuildArch:      noarch

%description samples
Some examples of programs written in Brainfuck.

%prep
%setup -q

%build
gcc %{optflags} -DNDEBUG bff.c -o bff

%install
install -D -m 755 bff %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/bff-samples
install -m 644 samples/* %{buildroot}%{_datadir}/bff-samples

%files
%doc README.md
%{_bindir}/%{name}

%files samples
%{_datadir}/bff-samples

%changelog
