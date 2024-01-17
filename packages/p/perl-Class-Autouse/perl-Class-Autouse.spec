#
# spec file for package perl-Class-Autouse
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


Name:           perl-Class-Autouse
Version:        2.01
Release:        0
%define cpan_name Class-Autouse
Summary:        Run-time load a class the first time you call a method in it
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Autouse/
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.17
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
%license LICENSE

%changelog
