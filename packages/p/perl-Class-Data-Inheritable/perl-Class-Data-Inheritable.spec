#
# spec file for package perl-Class-Data-Inheritable
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-Class-Data-Inheritable
%define cpan_name Class-Data-Inheritable
Summary:        Inheritable, overridable class data
Version:        0.08
Release:        59
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Data-Inheritable/
#Source:         http://www.cpan.org/authors/id/T/TM/TMTM/Class-Data-Inheritable-0.08.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Class::Data::Inheritable is for creating accessor/mutators to class data.
That is, if you want to store something about your class as a whole
(instead of about a single object). This data is then inherited by your
subclasses and can be overriden.

For example:

  Pere::Ubu->mk_classdata('Suitcase');

will generate the method Suitcase() in the class Pere::Ubu.

This new method can be used to get and set a piece of class data.

  Pere::Ubu->Suitcase('Red');
  $suitcase = Pere::Ubu->Suitcase;

The interesting part happens when a class inherits from Pere::Ubu:

  package Raygun;
  use base qw(Pere::Ubu);
  
  # Raygun's suitcase is Red.
  $suitcase = Raygun->Suitcase;

Raygun inherits its Suitcase class data from Pere::Ubu.

Inheritance of class data works analogous to method inheritance. As long as
Raygun does not "override" its inherited class data (by using Suitcase() to
set a new value) it will continue to use whatever is set in Pere::Ubu and
inherit further changes:

  # Both Raygun's and Pere::Ubu's suitcases are now Blue
  Pere::Ubu->Suitcase('Blue');

However, should Raygun decide to set its own Suitcase() it has now
"overridden" Pere::Ubu and is on its own, just like if it had overriden a
method:

  # Raygun has an orange suitcase, Pere::Ubu's is still Blue.
  Raygun->Suitcase('Orange');

Now that Raygun has overridden Pere::Ubu futher changes by Pere::Ubu no
longer effect Raygun.

  # Raygun still has an orange suitcase, but Pere::Ubu is using Samsonite.
  Pere::Ubu->Suitcase('Samsonite');

Authors:
--------
     Original code by Damian Conway.
     Maintained by Michael G Schwern until September 2005.
     Now maintained by Tony Bowden.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
### since 11.4 perl_process_packlist
### removes .packlist, perllocal.pod files
%if 0%{?suse_version} > 1130
%perl_process_packlist
%else
# do not perl_process_packlist
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -f $RPM_BUILD_ROOT%perl_archlib/perllocal.pod
%endif
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes README

%changelog
