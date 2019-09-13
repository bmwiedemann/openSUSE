#
# spec file for package perl-MooseX-Params-Validate
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


Name:           perl-MooseX-Params-Validate
Version:        0.21
Release:        0
%define cpan_name MooseX-Params-Validate
Summary:        an extension of Params::Validate using Moose's types
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Params-Validate/
Source:         http://www.cpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Caller)
BuildRequires:  perl(Moose) >= 2.1200
BuildRequires:  perl(Moose::Exception)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Params::Validate) >= 1.15
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Devel::Caller)
Requires:       perl(Moose) >= 2.1200
Requires:       perl(Moose::Exception)
Requires:       perl(Moose::Util)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(Params::Validate) >= 1.15
Requires:       perl(Sub::Exporter)
%{perl_requires}

%description
This module fills a gap in Moose by adding method parameter validation to
Moose. This is just one of many developing options, it should not be
considered the "official" one by any means though.

You might also want to explore 'MooseX::Method::Signatures' and
'MooseX::Declare'.

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
%doc Changes LICENSE README.md

%changelog
