#
# spec file for package perl-MooseX-Types-LoadableClass
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


Name:           perl-MooseX-Types-LoadableClass
Version:        0.015
Release:        0
%define cpan_name MooseX-Types-LoadableClass
Summary:        ClassName type constraint with coercion to load the class
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Types-LoadableClass/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean) >= 0.19
Requires:       perl(Module::Runtime)
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
    use Moose::Util::TypeConstraints;

    my $tc = subtype as ClassName;
    coerce $tc, from Str, via { Class::Load::load_class($_); $_ };

I've written those three lines of code quite a lot of times, in quite a lot
of places.

Now I don't have to.

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
%doc Changes CONTRIBUTING LICENCE README

%changelog
