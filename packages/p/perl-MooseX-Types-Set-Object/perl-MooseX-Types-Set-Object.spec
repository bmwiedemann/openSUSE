#
# spec file for package perl-MooseX-Types-Set-Object
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


Name:           perl-MooseX-Types-Set-Object
Version:        0.05
Release:        0
%define cpan_name MooseX-Types-Set-Object
Summary:        Set::Object type with coercions and stuff
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Types-Set-Object/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.007
BuildRequires:  perl(Moose) >= 0.50
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Set::Object)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(ok)
Requires:       perl(Moose) >= 0.50
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(Set::Object)
%{perl_requires}

%description
This module provides a Moose type constraint (see the
Moose::Util::TypeConstraints manpage, the MooseX::Types manpage). Note that
this constraint and its coercions are *global*, not simply limited to the
scope that imported it -- in this way it acts like a regular the Moose
manpage type constraint, rather than one from the MooseX::Types manpage.

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
