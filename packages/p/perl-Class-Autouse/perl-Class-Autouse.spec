#
# spec file for package perl-Class-Autouse
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Class-Autouse
Name:           perl-Class-Autouse
Version:        2.20.0
Release:        0
# 2.02 -> normalize -> 2.20.0
%define cpan_version 2.02
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Run-time load a class the first time you call a method in it
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(prefork)
Requires:       perl(prefork)
Provides:       perl(Class::Autouse) = %{version}
Provides:       perl(Class::Autouse::Parent) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
*Class::Autouse* is a runtime class loader that allows you to specify
classes that will only load when a method of that class is called.

For large classes or class trees that might not be used during the running
of a program, such as Date::Manip, this can save you large amounts of
memory, and decrease the script load time a great deal.

*Class::Autouse* also provides a number of "unsafe" features for runtime
generation of classes and implementation of syntactic sugar. These features
make use of (evil) UNIVERSAL::AUTOLOAD hooking, and are implemented in this
class because these hooks can only be done by a one module, and
Class::Autouse serves as a useful place to centralise this kind of evil :)

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
