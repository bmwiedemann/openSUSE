#
# spec file for package perl-Expect
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Expect
Name:           perl-Expect
Version:        1.380.0
Release:        0
# 1.38 -> normalize -> 1.380.0
%define cpan_version 1.38
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Automate interactions with command line programs that expose a text term[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JACOBY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Expect.diff
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(IO::Pty) >= 1.11
BuildRequires:  perl(IO::Tty) >= 1.11
BuildRequires:  perl(Test::More) >= 1.00
Requires:       perl(IO::Pty) >= 1.11
Requires:       perl(IO::Tty) >= 1.11
Provides:       perl(Expect) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
See an explanation of at http://code-maven.com/expect

The Expect module is a successor of Comm.pl and a descendent of Chat.pl. It
more closely resembles the Tcl Expect language than its predecessors. It
does not contain any of the networking code found in Comm.pl. I suspect
this would be obsolete anyway given the advent of IO::Socket and external
tools such as netcat.

Expect.pm is an attempt to have more of a switch() & case feeling to make
decision processing more fluid. Three separate types of debugging have been
implemented to make code production easier.

It is possible to interconnect multiple file handles (and processes) much
like Tcl's Expect. An attempt was made to enable all the features of Tcl's
Expect without forcing Tcl on the victim programmer :-) .

Please, before you consider using Expect, read the FAQs about "I want to
automate password entry for su/ssh/scp/rsh/..." and "I want to use Expect
to automate [anything with a buzzword]..."

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README.md
%license LICENSE

%changelog
