#
# spec file for package perl-aliased
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


Name:           perl-aliased
Version:        0.34
Release:        0
%define cpan_name aliased
Summary:        Use shorter versions of class names
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/aliased/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
%{perl_requires}

%description
'aliased' is simple in concept but is a rather handy module. It loads the
class you specify and exports into your namespace a subroutine that returns
the class name. You can explicitly alias the class to another name or, if
you prefer, you can do so implicitly. In the latter case, the name of the
subroutine is the last part of the class name. Thus, it does something
similar to the following:

  #use aliased 'Some::Annoyingly::Long::Module::Name::Customer';

  use Some::Annoyingly::Long::Module::Name::Customer;
  sub Customer {
    return 'Some::Annoyingly::Long::Module::Name::Customer';
  }
  my $cust = Customer->new;

This module is useful if you prefer a shorter name for a class. It's also
handy if a class has been renamed.

(Some may object to the term "aliasing" because we're not aliasing one
namespace to another, but it's a handy term. Just keep in mind that this is
done with a subroutine and not with typeglobs and weird namespace munging.)

Note that this is *only* for 'use'ing OO modules. You cannot use this to
load procedural modules. See the the Why OO Only? manpage section. Also,
don't let the version number fool you. This code is ridiculously simple and
is just fine for most use.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENSE README

%changelog
