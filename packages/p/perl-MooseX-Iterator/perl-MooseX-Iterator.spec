#
# spec file for package perl-MooseX-Iterator
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


Name:           perl-MooseX-Iterator
Version:        0.11
Release:        0
%define cpan_name MooseX-Iterator
Summary:        Iterate over collections
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Iterator/
Source0:        https://cpan.metacpan.org/authors/id/R/RL/RLB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.86
Requires:       perl(Moose) >= 0.86
%{perl_requires}

%description
This is an attempt to add smalltalk-like streams to Moose. It currently
works with ArrayRefs and HashRefs.

* next

The next method provides the next item in the colletion.

  For arrays it returns the element of the array
  
  For hashs it returns a pair as a hashref with the keys: key and value

* has_next

The has_next method is a boolean method that is true if there is another
item in the colletion after the current item. and falue if there isn't.

* peek

The peek method returns the next item without moving the state of the
iterator forward. It returns undef if it is at the end of the collection.

* reset

Resets the cursor, so you can iterate through the elements again.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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

%changelog
