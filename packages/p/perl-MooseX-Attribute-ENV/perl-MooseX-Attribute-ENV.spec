#
# spec file for package perl-MooseX-Attribute-ENV
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


Name:           perl-MooseX-Attribute-ENV
Version:        0.02
Release:        0
%define cpan_name MooseX-Attribute-ENV
Summary:        Set default of an attribute to a value from %ENV
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Attribute-ENV/
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.48
Requires:       perl(Moose) >= 0.48
%{perl_requires}

%description
This is a Moose attribute trait that you use when you want the default
value for an attribute to be populated from the %ENV hash. So, for example
if you have set the environment variable USERNAME = 'John' you can do:

	package MyApp::MyClass;

	use Moose;
	use MooseX::Attribute::ENV;

	has 'username' => (is=>'ro', traits=>['ENV']);

	package main;

	my $myclass = MyApp::MyClass->new();

	print $myclass->username; # STDOUT => 'John';

This is basically similar functionality to something like:

	has 'attr' => (
		is=>'ro',
		default=> sub {
			$ENV{uc 'attr'};
		},
	);

but this module has a few other features that offer merit, as well as being
a simple enough attribute trait that I hope it can serve as a learning
tool.

If the named key isn't found in %ENV, then defaults will execute as normal.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
%doc Changes README

%changelog
