#
# spec file for package perl-Test-Class-Most
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


Name:           perl-Test-Class-Most
Version:        0.08
Release:        0
%define cpan_name Test-Class-Most
Summary:        Test Classes the easy way
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Class-Most/
Source:         http://www.cpan.org/authors/id/O/OV/OVID/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.4
BuildRequires:  perl(Test::Class) >= 0.38
BuildRequires:  perl(Test::Most) >= 0.31
Requires:       perl(Test::Class) >= 0.38
Requires:       perl(Test::Most) >= 0.31
%{perl_requires}

%description
When people write test classes with the excellent 'Test::Class', you often
see the following at the top of the code:

  package Some::Test::Class;

  use strict;
  use warnings;
  use base 'My::Test::Class';
  use Test::More;
  use Test::Exception;

  # and then the tests ...

That's a lot of boilerplate and I don't like boilerplate. So now you can do
this:

  use Test::Class::Most parent => 'My::Test::Class';

That automatically imports the strict manpage and the warnings manpage for
you. It also gives you all of the testing goodness from the Test::Most
manpage.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
