#
# spec file for package perl-Proc-Fork
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Proc-Fork
Version:        0.806
Release:        0
%define cpan_name Proc-Fork
Summary:        Simple, Intuitive Interface to the Fork() System Call
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Proc-Fork/
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Tidy)
Requires:       perl(Exporter::Tidy)
%{perl_requires}

%description
This module provides an intuitive, Perl-ish way to write forking programs
by letting you use blocks to illustrate which code section executes in
which fork. The code for the parent, child, retry handler and error handler
are grouped together in a "fork block". The clauses may appear in any
order, but they must be consecutive (without any other statements in
between).

All four clauses need not be specified. If the retry clause is omitted,
only one fork will be attempted. If the error clause is omitted the program
will die with a simple message if it can't retry. If the parent or child
clause is omitted, the respective (parent or child) process will start
execution after the final clause. So if one or the other only has to do
some simple action, you need only specify that one. For example:

 # spawn off a child process to do some simple processing
 run_fork { child {
     exec '/bin/ls', '-l';
     die "Couldn't exec ls: $!\n";
 } };
 # Parent will continue execution from here
 # ...

If the code in any of the clauses does not die or exit, it will continue
execution after the fork block.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
