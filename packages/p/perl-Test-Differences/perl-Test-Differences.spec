#
# spec file for package perl-Test-Differences
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


#Upstream:  All Rights Reserved. You may use, distribute and modify this software under the terms of the GNU public license, any version, or the Artistic license.
%define cpan_name Test-Differences
Name:           perl-Test-Differences
Version:        0.67
Release:        0
Summary:        Test strings and data structures and show differences if not ok
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.24
BuildRequires:  perl(Data::Dumper) >= 2.126
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Text::Diff) >= 1.43
Requires:       perl(Capture::Tiny) >= 0.24
Requires:       perl(Data::Dumper) >= 2.126
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Text::Diff) >= 1.43
BuildArch:      noarch
%{perl_requires}

%description
When the code you're testing returns multiple lines, records or data
structures and they're just plain wrong, an equivalent to the Unix 'diff'
utility may be just what's needed. Here's output from an example test
script that checks two text documents and then two (trivial) data
structures:

 t/99example....1..3
 not ok 1 - differences in text
 #     Failed test ((eval 2) at line 14)
 #     +---+----------------+----------------+
 #     | Ln|Got             |Expected        |
 #     +---+----------------+----------------+
 #     |  1|this is line 1  |this is line 1  |
 #     *  2|this is line 2  |this is line b  *
 #     |  3|this is line 3  |this is line 3  |
 #     +---+----------------+----------------+
 not ok 2 - differences in whitespace
 #     Failed test ((eval 2) at line 20)
 #     +---+------------------+------------------+
 #     | Ln|Got               |Expected          |
 #     +---+------------------+------------------+
 #     |  1|        indented  |        indented  |
 #     *  2|        indented  |\tindented        *
 #     |  3|        indented  |        indented  |
 #     +---+------------------+------------------+
 not ok 3
 #     Failed test ((eval 2) at line 22)
 #     +----+-------------------------------------+----------------------------+
 #     | Elt|Got                                  |Expected                    |
 #     +----+-------------------------------------+----------------------------+
 #     *   0|bless( [                             |[                           *
 #     *   1|  'Move along, nothing to see here'  |  'Dry, humorless message'  *
 #     *   2|], 'Test::Builder' )                 |]                           *
 #     +----+-------------------------------------+----------------------------+
 # Looks like you failed 3 tests of 3.

eq_or_diff_...() compares two strings or (limited) data structures and
either emits an ok indication or a side-by-side diff. Test::Differences is
designed to be used with Test.pm and with Test::Simple, Test::More, and
other Test::Builder based testing modules. As the SYNOPSIS shows, another
testing module must be used as the basis for your test suite.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
