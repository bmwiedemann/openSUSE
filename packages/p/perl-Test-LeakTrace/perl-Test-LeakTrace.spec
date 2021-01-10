#
# spec file for package perl-Test-LeakTrace
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Test-LeakTrace
Name:           perl-Test-LeakTrace
Version:        0.17
Release:        0
Summary:        Traces memory leaks
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'Test::LeakTrace' provides several functions that trace memory leaks. This
module scans arenas, the memory allocation system, so it can detect any
leaked SVs in given blocks.

*Leaked SVs* are SVs which are not released after the end of the scope they
have been created. These SVs include global variables and internal caches.
For example, if you call a method in a tracing block, perl might prepare a
cache for the method. Thus, to trace true leaks, 'no_leaks_ok()' and
'leaks_cmp_ok()' executes a block more than once.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes example README

%changelog
