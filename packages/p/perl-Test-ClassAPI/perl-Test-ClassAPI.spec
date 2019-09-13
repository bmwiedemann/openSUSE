#
# spec file for package perl-Test-ClassAPI
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


Name:           perl-Test-ClassAPI
Version:        1.07
Release:        0
%define cpan_name Test-ClassAPI
Summary:        Provides basic first-pass API testing for large class trees
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-ClassAPI/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inspector) >= 1.12
BuildRequires:  perl(Config::Tiny) >= 2.00
BuildRequires:  perl(Params::Util) >= 1.00
Requires:       perl(Class::Inspector) >= 1.12
Requires:       perl(Config::Tiny) >= 2.00
Requires:       perl(Params::Util) >= 1.00
%{perl_requires}

%description
For many APIs with large numbers of classes, it can be very useful to be
able to do a quick once-over to make sure that classes, methods, and
inheritance is correct, before doing more comprehensive testing. This
module aims to provide such a capability.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
