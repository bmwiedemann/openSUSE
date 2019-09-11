#
# spec file for package perl-Devel-Trace
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Devel-Trace
Version:        0.12
Release:        0
#Upstream:  Devel::Trace 0.11 and its source code are hereby placed in the public domain.
%define cpan_name Devel-Trace
Summary:        Print out each line before it is executed (like C<sh -x>)
License:        SUSE-Public-Domain
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-Trace/
Source0:        http://www.cpan.org/authors/id/M/MJ/MJD/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes README sample

%changelog
