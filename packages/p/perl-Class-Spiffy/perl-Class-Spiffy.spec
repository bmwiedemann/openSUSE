#
# spec file for package perl-Class-Spiffy
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


Name:           perl-Class-Spiffy
Version:        0.15
Release:        0
%define cpan_name Class-Spiffy
Summary:        Spiffy Framework with No Source Filtering
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Spiffy/
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
"Class::Spiffy" is a framework and methodology for doing object oriented
(OO) programming in Perl. Class::Spiffy combines the best parts of
Exporter.pm, base.pm, mixin.pm and SUPER.pm into one magic foundation
class. It attempts to fix all the nits and warts of traditional Perl OO, in
a clean, straightforward and (perhaps someday) standard way.

Class::Spiffy borrows ideas from other OO languages like Python, Ruby, Java
and Perl 6. It also adds a few tricks of its own.

If you take a look on CPAN, there are a ton of OO related modules. When
starting a new project, you need to pick the set of modules that makes most
sense, and then you need to use those modules in each of your classes.
Class::Spiffy, on the other hand, has everything you'll probably need in
one module, and you only need to use it once in one of your classes. If you
make Class::Spiffy the base class of the basest class in your project,
Class::Spiffy will automatically pass all of its magic to all of your
subclasses. You may eventually forget that you're even using it!

%prep
%setup -q -n %{cpan_name}-%{version}
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
