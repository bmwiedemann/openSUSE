#
# spec file for package perl-Test-NoWarnings
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


Name:           perl-Test-NoWarnings
Version:        1.04
Release:        0
#Upstream: SUSE-Public-Domain
%define cpan_name Test-NoWarnings
Summary:        Make sure you didn't emit any warnings while testing
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-NoWarnings/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Builder) >= 0.86
BuildRequires:  perl(Test::Tester) >= 0.107
Requires:       perl(Test::Builder) >= 0.86
%{perl_requires}

%description
In general, your tests shouldn't produce warnings. This modules causes any
warnings to be captured and stored. It automatically adds an extra test
that will run when your script ends to check that there were no warnings.
If there were any warings, the test will give a "not ok" and diagnostics of
where, when and what the warning was, including a stack trace of what was
going on when the it occurred.

If some of your tests *are supposed to* produce warnings then you should be
capturing and checking them with the Test::Warn manpage, that way the
Test::NoWarnings manpage will not see them and so not complain.

The test is run by an 'END' block in Test::NoWarnings. It will not be run
when any forked children exit.

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
%doc Changes LICENSE README

%changelog
