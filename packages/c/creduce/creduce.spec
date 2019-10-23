#
# spec file for package creduce
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.10.0+git.20191010.8a67e69
Release:        0
Summary:        C-Reduce, a C program reducer
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/csmith-project/creduce
Source:         %{name}-%{version}.tar.xz
Patch0:         llvm9-libs-fix.patch
BuildRequires:  astyle
BuildRequires:  clang9-devel
BuildRequires:  delta
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  indent
BuildRequires:  llvm9-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-Benchmark-Timer
BuildRequires:  perl-Exporter-Lite
BuildRequires:  perl-File-Which
BuildRequires:  perl-Getopt-Tabular
BuildRequires:  perl-Regexp-Common
BuildRequires:  perl-Term-ReadKey
BuildRequires:  zlib-devel
Requires:       astyle
Requires:       clang9-devel
Requires:       delta
Requires:       indent
Requires:       llvm9-devel
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
%patch0 -p1

%build
%configure --libexec=%{_bindir}
%make_build

%install
%make_install

rm %{buildroot}%{_bindir}/topformflat
rm %{buildroot}%{_bindir}/unifdef

%files
%license COPYING
%{_bindir}/creduce
%{_bindir}/clang_delta
%{_bindir}/clex
%{_bindir}/strlex
%{_datadir}/creduce

%changelog
