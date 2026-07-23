#
# spec file for package perl-XML-Bare
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name XML-Bare
Name:           perl-XML-Bare
Version:        0.53
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Minimal XML parser / schema checker / pretty-printer using C internally
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CODECHILD/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
# PATCH-FIX-UPSTREAM https://github.com/nanoscopic/perl-XML-Bare/pull/2
Patch0:         CVE-2026-13401-r1.patch
# PATCH-FIX-UPSTREAM https://github.com/nanoscopic/perl-XML-Bare/pull/1
Patch1:         CVE-2026-57074-r1.patch
Patch2:         fix-pointers.diff
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
%{perl_requires}

%description
This module is a 'Bare' XML parser. It is implemented in C. The parser
itself is a simple state engine that is less than 500 lines of C. The
parser builds a C struct tree from input text. That C struct tree is
converted to a Perl hash by a Perl function that makes basic calls back to
the C to go through the nodes sequentially.

The parser itself will only cease parsing if it encounters tags that are
not closed properly. All other inputs will parse, even invalid inputs. To
allowing checking for validity, a schema checker is included in the module
as well.

The schema format is custom and is meant to be as simple as possible. It is
based loosely around the way multiplicity is handled in Perl regular
expressions.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README

%changelog
