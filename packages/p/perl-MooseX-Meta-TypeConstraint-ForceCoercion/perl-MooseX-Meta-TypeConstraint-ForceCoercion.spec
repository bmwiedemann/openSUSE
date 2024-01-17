# vim: set sw=4 ts=4 et nu:
#
# spec file for package perl-MooseX-Meta-TypeConstraint-ForceCoercion
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
Name:           perl-MooseX-Meta-TypeConstraint-ForceCoercion
Version:        0.01
Release:        0
Summary:        Force coercion when validating type constraints
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/MooseX-Meta-TypeConstraint-ForceCoercion-%{version}.tar.gz
Url:            http://search.cpan.org/dist/MooseX-Meta-TypeConstraint-ForceCoercion
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(namespace::autoclean)
Requires:       perl(Moose)
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description
This class allows to wrap any "Moose::Meta::TypeConstraint" in a way that
will force coercion of the value when checking or validating a value
against it.

%prep
%setup -q -n "MooseX-Meta-TypeConstraint-ForceCoercion-%{version}"
%__sed -i '/^auto_install/d' Makefile.PL

%build
%__perl Makefile.PL PREFIX="%{_prefix}"
%__make %{?jobs:-j%{jobs}}

%install
%perl_make_install
%perl_process_packlist

%check
%__make test

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%dir %{perl_vendorlib}/MooseX
%dir %{perl_vendorlib}/MooseX/Meta
%dir %{perl_vendorlib}/MooseX/Meta/TypeConstraint
%{perl_vendorlib}/MooseX/Meta/TypeConstraint/ForceCoercion.pm
%doc %{perl_man3dir}/MooseX::Meta::TypeConstraint::ForceCoercion.%{perl_man3ext}%{ext_man}

%changelog
