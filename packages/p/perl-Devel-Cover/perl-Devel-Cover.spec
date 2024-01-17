#
# spec file for package perl-Devel-Cover
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Devel-Cover
Name:           perl-Devel-Cover
Version:        1.40
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Code coverage metrics for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJCJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Entities) >= 3.69
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(HTML::Entities) >= 3.69
Recommends:     perl(Browser::Open)
Recommends:     perl(Capture::Tiny)
Recommends:     perl(Class::XSAccessor)
Recommends:     perl(HTML::Parser)
Recommends:     perl(JSON::MaybeXS) >= 1.003003
Recommends:     perl(Moo)
Recommends:     perl(PPI::HTML) >= 1.07
Recommends:     perl(Parallel::Iterator)
Recommends:     perl(Perl::Tidy) >= 20060719
Recommends:     perl(Pod::Coverage) >= 0.06
Recommends:     perl(Pod::Coverage::CountParents)
Recommends:     perl(Sereal::Decoder)
Recommends:     perl(Sereal::Encoder)
Recommends:     perl(Template) >= 2.00
Recommends:     perl(Test::Differences)
Recommends:     perl(namespace::clean)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl-B-Debug
Requires:       perl-B-Debug
# MANUAL END

%description
This module provides code coverage metrics for Perl. Code coverage metrics
describe how thoroughly tests exercise code. By using Devel::Cover you can
discover areas of code not exercised by your tests and determine which
tests to create to increase coverage. Code coverage can be considered an
indirect measure of quality.

Devel::Cover is now quite stable and provides many of the features to be
expected in a useful coverage tool.

Statement, branch, condition, subroutine, and pod coverage information is
reported. Statement and subroutine coverage data should be accurate. Branch
and condition coverage data should be mostly accurate too, although not
always what one might initially expect. Pod coverage comes from
Pod::Coverage. If Pod::Coverage::CountParents is available it will be used
instead.

The _cover_ program can be used to generate coverage reports. Devel::Cover
ships with a number of reports including various types of HTML output,
textual reports, a report to display missing coverage in the same format as
compilation errors and a report to display coverage information within the
Vim editor.

It is possible to add annotations to reports, for example you can add a
column to an HTML report showing who last changed a line, as determined by
git blame. Some annotation modules are shipped with Devel::Cover and you
can easily create your own.

The _gcov2perl_ program can be used to convert gcov files to 'Devel::Cover'
databases. This allows you to display your C or XS code coverage together
with your Perl coverage, or to use any of the Devel::Cover reports to
display your C coverage data.

Code coverage data are collected by replacing perl ops with functions which
count how many times the ops are executed. These data are then mapped back
to reality using the B compiler modules. There is also a statement
profiling facility which should not be relied on. For proper profiling use
Devel::NYTProf. Previous versions of Devel::Cover collected coverage data
by replacing perl's runops function. It is still possible to switch to that
mode of operation, but this now gets little testing and will probably be
removed soon. You probably don't care about any of this.

The most appropriate mailing list on which to discuss this module would be
perl-qa. See http://lists.perl.org/list/perl-qa.html.

The Devel::Cover repository can be found at
http://github.com/pjcj/Devel--Cover. This is also where problems should be
reported.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes Contributors docs README.md
%license LICENCE

%changelog
