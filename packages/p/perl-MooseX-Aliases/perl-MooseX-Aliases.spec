#
# spec file for package perl-MooseX-Aliases
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-Aliases
Version:        0.11
Release:        0
%define cpan_name MooseX-Aliases
Summary:        easy aliasing of methods and attributes in Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Aliases/
Source:         http://www.cpan.org/authors/id/D/DO/DOY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 2.0000
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.88
#BuildRequires: perl(Foo)
#BuildRequires: perl(MooseX::Aliases)
#BuildRequires: perl(MyApp::Role)
#BuildRequires: perl(MyTest)
#BuildRequires: perl(MyTestRole)
#BuildRequires: perl(Parent)
Requires:       perl(Moose) >= 2.0000
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
%{perl_requires}

%description
The MooseX::Aliases module will allow you to quickly alias methods in
Moose. It provides an alias parameter for 'has()' to generate aliased
accessors as well as the standard ones. Attributes can also be initialized
in the constructor via their aliased names.

You can create more than one alias at once by passing a arrayref:

    has ip_addr => (
        alias => [ qw(ipAddr ip) ],
    );

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
%doc Changes LICENSE README

%changelog
