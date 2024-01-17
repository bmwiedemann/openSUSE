#
# spec file for package perl-MooseX-Role-Parameterized
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-MooseX-Role-Parameterized
Version:        1.11
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
%define cpan_name MooseX-Role-Parameterized
Summary:        Moose roles with composition parameters
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 2.0300
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean) >= 0.19
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 2.0300
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Meta::Role)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util)
Requires:       perl(namespace::autoclean)
Requires:       perl(namespace::clean) >= 0.19
%{perl_requires}

%description
Your parameterized role consists of two new things: parameter declarations
and a 'role' block.

Parameters are declared using the parameter keyword which very much
resembles Moose/has. You can use any option that Moose/has accepts. The
default value for the 'is' option is 'ro' as that's a very common case. Use
'is => 'bare'' if you want no accessor. These parameters will get their
values when the consuming class (or role) uses Moose/with. A parameter
object will be constructed with these values, and passed to the 'role'
block.

The 'role' block then uses the usual Moose::Role keywords to build up a
role. You can shift off the parameter object to inspect what the consuming
class provided as parameters. You use the parameters to customize your role
however you wish.

There are many possible implementations for parameterized roles (hopefully
with a consistent enough API); I believe this to be the easiest and most
flexible design. Coincidentally, Pugs originally had an eerily similar
design.

See MooseX::Role::Parameterized::Extending for some tips on how to extend
this module.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
