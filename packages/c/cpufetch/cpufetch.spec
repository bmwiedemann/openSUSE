#
# spec file for package cpufetch
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Taekyung Kim <gnuykeat.mik@gmail.com>
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


Name:           cpufetch
Version:        1.06
Release:        0
Summary:        CLI CPU information tool written in C
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://github.com/Dr-Noob/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Supports only x86_64, ARM and PowerPC
ExclusiveArch:  %{arm} aarch64 x86_64 ppc ppc64 ppc64le

%description
%{name} is a command-line tool written in C that displays the CPU information
in a clean and beautiful way.

%prep
%setup -q

%build
%set_build_flags
%make_build

%install
%make_install

# "make install" installs the LICENSE file as well
rm %{buildroot}%{_datadir}/licenses/cpufetch-git/LICENSE

%check
# Try running the program to see if it doesn't crash
%{buildroot}%{_bindir}/%{name} --debug

%files
%doc README.md
%license LICENSE
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/%{name}

%changelog
