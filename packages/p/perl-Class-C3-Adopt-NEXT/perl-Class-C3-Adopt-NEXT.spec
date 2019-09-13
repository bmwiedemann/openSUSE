#
# spec file for package perl-Class-C3-Adopt-NEXT
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


Name:           perl-Class-C3-Adopt-NEXT
Version:        0.14
Release:        0
%define cpan_name Class-C3-Adopt-NEXT
Summary:        Make Next Suck Less
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-C3-Adopt-NEXT/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Test::Exception) >= 0.270000
Requires:       perl(List::Util) >= 1.33
Requires:       perl(MRO::Compat)
%{perl_requires}

%description
the NEXT manpage was a good solution a few years ago, but isn't any more.
It's slow, and the order in which it re-dispatches methods appears random
at times. It also encourages bad programming practices, as you end up with
code to re-dispatch methods when all you really wanted to do was run some
code before or after a method fired.

However, if you have a large application, then weaning yourself off 'NEXT'
isn't easy.

This module is intended as a drop-in replacement for NEXT, supporting the
same interface, but using the Class::C3 manpage to do the hard work. You
can then write new code without 'NEXT', and migrate individual source files
to use 'Class::C3' or method modifiers as appropriate, at whatever pace
you're comfortable with.

%prep
%setup -q -n %{cpan_name}-%{version}

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
