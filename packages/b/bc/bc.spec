#
# spec file for package bc
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           bc
Version:        1.08.2
Release:        0
Summary:        GNU Command Line Calculator
License:        GFDL-1.2-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.gnu.org/software/bc/
Source0:        https://ftp.gnu.org/gnu/bc/bc-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/bc/bc-%{version}.tar.gz.sig
# from https://src.fedoraproject.org/rpms/bc/blob/rawhide/f/kevin_pizzini.asc
Source2:        %{name}.keyring
BuildRequires:  bison
BuildRequires:  ed
BuildRequires:  flex
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(readline)

%description
bc is an interpreter that supports numbers of arbitrary precision and
the interactive execution of statements. The syntax has some
similarities to the C programming language. A standard math library is
available through command line options. When used, the math library is
read in before any other input files. bc then reads in all other files
from the command line, evaluating their contents. Then bc reads from
standard input (usually the keyboard).

The dc program is also included. dc is a calculator that supports
reverse-polish notation and allows unlimited precision arithmetic.
Macros can also be defined. Normally, dc reads from standard input but
can also read in files specified on the command line. A calculator with
reverse-polish notation saves numbers to a stack. Arguments to
mathematical operations (operands) are "pushed" onto the stack until
the next operator is read in, which "pops" its arguments off the stack
and "pushes" its results back onto the stack.

%prep
%autosetup -p1

%build
%configure \
  --with-readline \
  --without-libedit
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc NEWS README FAQ
%{_bindir}/bc
%{_bindir}/dc
%{_infodir}/bc.info%{?ext_info}
%{_infodir}/dc.info%{?ext_info}
%{_mandir}/man1/bc.1%{?ext_man}
%{_mandir}/man1/dc.1%{?ext_man}

%changelog
