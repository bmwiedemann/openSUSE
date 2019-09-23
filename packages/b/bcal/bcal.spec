#
# spec file for package bcal
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Dilawar Singh <dilawar.s.rajput@gmail.com>
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


Name:           bcal
Summary:        Command-line utility for storage conversions and calculations
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            http://www.github.com/jarun/bcal
Version:        2.1
Release:        0
Source0:        https://github.com/jarun/bcal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM bcal-2.1_gcc9.patch
Patch0:         bcal-2.1_gcc9.patch
BuildRequires:  readline-devel
ExcludeArch:    %ix86 %arm %ppc

%description
bcal (Byte CALculator) is a command-line utility for storage, hardware and
firmware developers who deal with storage-specific numerical calculations,
expressions, unit conversions or address calculations frequently. If you are one
and cannot calculate the hex address offset for (512 - 16) MiB immediately, or
the value when the 43rd bit of a 64-bit address is set, bcal is for you.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} DOCDIR=%{buildroot}/%{_prefix}/share/doc/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%dir %{_prefix}/share/doc/bcal
%{_prefix}/share/doc/bcal/README.md

%changelog
