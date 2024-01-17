#
# spec file for package perl-SUPER
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


Name:           perl-SUPER
Version:        1.20190531
Release:        0
%define cpan_name SUPER
Summary:        Control superclass method dispatch
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util) >= 1.20
BuildRequires:  perl(Sub::Identify) >= 0.03
Requires:       perl(Scalar::Util) >= 1.20
Requires:       perl(Sub::Identify) >= 0.03
%{perl_requires}

%description
When subclassing a class, you occasionally want to dispatch control to the
superclass -- at least conditionally and temporarily. The Perl syntax for
calling your superclass is ugly and unwieldy:

    $self->SUPER::method(@_);

especially when compared to its Ruby equivalent:

    super;

It's even worse in that the normal Perl redispatch mechanism only
dispatches to the parent of the class containing the method _at compile
time_. That doesn't work very well for mixins and roles.

This module provides nicer equivalents, along with the universal method
'super' to determine a class' own superclass. This allows you to do things
such as:

    goto &{$_[0]->super('my_method')};

if you don't like wasting precious stack frames.

If you are using roles or mixins or otherwise pulling in methods from other
packages that need to dispatch to their super methods, or if you want to
pass different arguments to the super method, use the 'SUPER()' method:

    $self->SUPER( qw( other arguments here ) );

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
