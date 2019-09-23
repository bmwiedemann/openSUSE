#
# spec file for package perl-MooseX-Role-TraitConstructor
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

Name:           perl-MooseX-Role-TraitConstructor
Version:        0.01
Release:        0
%define cpan_name MooseX-Role-TraitConstructor
Summary:        A wrapper for C<new> that can accept a
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Role-TraitConstructor/
Source:         http://www.cpan.org/authors/id/N/NU/NUFFIN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.40
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::use::ok)
#BuildRequires: perl(Moose::Role)
#BuildRequires: perl(MooseX::Role::TraitConstructor)
#BuildRequires: perl(ok)
Requires:       perl(Moose) >= 0.40
Requires:       perl(Test::Exception)
Requires:       perl(Test::use::ok)
%{perl_requires}

%description
This role allows you to easily accept a 'traits' argument (or another name)
into your constructor, which will easily mix roles into an anonymous class
before construction, much like the Moose::Meta::Attribute manpage does.

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

%changelog
