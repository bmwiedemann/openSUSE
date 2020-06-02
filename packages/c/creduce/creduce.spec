#
# spec file for package creduce
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


Name:           creduce
Version:        2.10.0+git.20200420.d83cbda
Release:        0
Summary:        C-Reduce, a C program reducer
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/csmith-project/creduce
Source:         %{name}-%{version}.tar.xz
Patch0:         llvm9-libs-fix.patch
Patch2:         binary-search-location.patch
Patch3:         port-to-llvm10.patch
Patch4:         std-cpp14.patch
BuildRequires:  astyle
BuildRequires:  clang10-devel
BuildRequires:  delta
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  indent
BuildRequires:  llvm10-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-Benchmark-Timer
BuildRequires:  perl-Exporter-Lite
BuildRequires:  perl-File-Which
BuildRequires:  perl-Getopt-Tabular
BuildRequires:  perl-Regexp-Common
BuildRequires:  perl-Term-ReadKey
Requires:       astyle
Requires:       clang10
Requires:       delta
Requires:       indent
Requires:       llvm10
Requires:       perl-Benchmark-Timer
Requires:       perl-Exporter-Lite
Requires:       perl-File-Which
Requires:       perl-Getopt-Tabular
Requires:       perl-Regexp-Common
Requires:       perl-Term-ReadKey
Requires:       unifdef

%description

C-Reduce is a tool that takes a large C or C++ program that has a
property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ program that has the same
property.  It is intended for use by people who discover and report
bugs in compilers and other tools that process C/C++ code.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

rm %{buildroot}%{_libexecdir}/topformflat
rm %{buildroot}%{_libexecdir}/unifdef

%files
%license COPYING
%{_bindir}/creduce
%{_libexecdir}/clang_delta
%{_libexecdir}/clex
%{_libexecdir}/strlex
%{_datadir}/creduce

%changelog
