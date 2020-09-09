#
# spec file for package re2c
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


Name:           re2c
Version:        2.0.3
Release:        0
Summary:        Tool for generating C-based recognizers from regular expressions
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            https://re2c.org/
Source:         https://github.com/skvadrik/re2c/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  gcc-c++

%description
re2c is a tool for writing fast and flexible lexers. Unlike other such
tools, it concentrates solely on generating efficient code for matching
regular expressions. This makes it suitable for a wide variety of
applications. The generated scanners approach hand-crafted ones in
terms of size and speed.

%prep
%autosetup

%build
%configure
%if 0%{?do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}"
  # do not run profiling in parallel for reproducible builds (boo#1040589 boo#1102408)
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}" check
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CFLAGS="%{optflags}"
%endif

%install
%make_install

%check
make check %{?_smp_mflags}

%files
%license README.md
%doc CHANGELOG
%doc examples/
%{_bindir}/re2c
%{_bindir}/re2go
%{_mandir}/man1/re2c.1%{?ext_man}
%{_mandir}/man1/re2go.1.gz
%dir %{_datadir}/re2c
%dir %{_datadir}/re2c/stdlib
%{_datadir}/re2c/stdlib/unicode_categories.re

%changelog
