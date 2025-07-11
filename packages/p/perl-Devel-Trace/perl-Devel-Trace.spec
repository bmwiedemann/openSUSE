#
# spec file for package perl-Devel-Trace
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Devel-Trace
Name:           perl-Devel-Trace
Version:        0.120.0
Release:        0
# 0.12 -> normalize -> 0.120.0
%define cpan_version 0.12
#Upstream:  Devel::Trace 0.11 and its source code are hereby placed in the public domain.
License:        SUSE-Public-Domain
Summary:        Print out each line before it is executed (like sh -x)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MJ/MJD/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Devel::Trace) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
If you run your program with 'perl -d:Trace program', this module will
print a message to standard error just before each line is executed. For
example, if your program looks like this:

        #!/usr/bin/perl


        print "Statement 1 at line 4\n";
        print "Statement 2 at line 5\n";
        print "Call to sub x returns ", &x(), " at line 6.\n";

        exit 0;


        sub x {
          print "In sub x at line 12.\n";
          return 13;
        }

Then the 'Trace' output will look like this:

        >> ./test:4: print "Statement 1 at line 4\n";
        >> ./test:5: print "Statement 2 at line 5\n";
        >> ./test:6: print "Call to sub x returns ", &x(), " at line 6.\n";
        >> ./test:12:   print "In sub x at line 12.\n";
        >> ./test:13:   return 13;
        >> ./test:8: exit 0;

This is something like the shell's '-x' option.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README sample

%changelog
