#
# spec file for package perl-Test-Unit
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Unit
Version:        0.25
Release:        0
%define cpan_name Test-Unit
Summary:        The PerlUnit testing framework
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Unit/
Source:         http://www.cpan.org/authors/id/M/MC/MCAST/%{cpan_name}-%{version}.tar.gz
Patch0:         Test-Unit-0.25.diff
Patch1:         Test-Unit_noArrayDefCheck.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inner)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(Error)
Requires:       perl(Class::Inner)
Requires:       perl(Devel::Symdump)
Requires:       perl(Error)
%{perl_requires}

%description
This framework is intended to support unit testing in an object-oriented
development paradigm (with support for inheritance of tests etc.) and is
derived from the JUnit testing framework for Java by Kent Beck and Erich
Gamma. To start learning how to use this framework, see the
Test::Unit::TestCase manpage and the Test::Unit::TestSuite manpage. (There
will also eventually be a tutorial in the Test::Unit::Tutorial manpage.

However 'Test::Unit::Procedural' is the procedural style interface to a
sophisticated unit testing framework for Perl that . Test::Unit is intended
to provide a simpler interface to the framework that is more suitable for
use in a scripting style environment. Therefore, Test::Unit does not
provide much support for an object-oriented approach to unit testing.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS ChangeLog Changes COPYING.Artistic COPYING.GPL-2 doc examples README

%changelog
