#
# spec file for package perl-Expect
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Expect
Version:        1.35
Release:        0
%define cpan_name Expect
Summary:        Automate Interactions with Command Line Programs That Expose a Text Term[cut]
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Expect/
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JACOBY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Expect.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Pty) >= 1.11
BuildRequires:  perl(IO::Tty) >= 1.11
BuildRequires:  perl(Test::More) >= 1.00
Requires:       perl(IO::Pty) >= 1.11
Requires:       perl(IO::Tty) >= 1.11
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README.md
%license LICENSE

%changelog
