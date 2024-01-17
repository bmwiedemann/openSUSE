#
# spec file for package perl-Class-ISA
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



Name:           perl-Class-ISA
Version:        0.36
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Class-ISA
Summary:        report the search path for a class's ISA tree
Url:            http://search.cpan.org/dist/Class-ISA/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Suppose you have a class (like Food::Fish::Fishstick) that is derived, via
its @ISA, from one or more superclasses (as Food::Fish::Fishstick is from
Food::Fish, Life::Fungus, and Chemicals), and some of those superclasses
may themselves each be derived, via its @ISA, from one or more superclasses
(as above).

When, then, you call a method in that class ($fishstick->calories), Perl
first searches there for that method, but if it's not there, it goes
searching in its superclasses, and so on, in a depth-first (or maybe
"height-first" is the word) search. In the above example, it'd first look
in Food::Fish, then Food, then Matter, then Life::Fungus, then Life, then
Chemicals.

This library, Class::ISA, provides functions that return that list -- the
list (in order) of names of classes Perl would search to find a method,
with no duplicates.

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
%doc ChangeLog README

%changelog
