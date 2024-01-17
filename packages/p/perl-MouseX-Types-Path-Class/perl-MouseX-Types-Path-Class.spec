#
# spec file for package perl-MouseX-Types-Path-Class
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


Name:           perl-MouseX-Types-Path-Class
Version:        0.07
Release:        0
%define cpan_name MouseX-Types-Path-Class
Summary:        Path::Class type library for Mouse
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MouseX-Types-Path-Class/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mouse) >= 0.39
BuildRequires:  perl(MouseX::Types) >= 0.02
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::UseAllModules)
Requires:       perl(Mouse) >= 0.39
Requires:       perl(MouseX::Types) >= 0.02
Requires:       perl(Path::Class)
Recommends:     perl(MouseX::Getopt) >= 0.2200
%{perl_requires}

%description
MouseX::Types::Path::Class creates common Mouse types, coercions and option
specifications useful for dealing with Path::Class objects as Mouse
attributes.

Coercions (see Mouse::Util::TypeConstraints) are made from both 'Str' and
'ArrayRef' to both Path::Class::Dir and Path::Class::File objects. If you
have MouseX::Getopt installed, the Getopt option type ("=s") will be added
for both Path::Class::Dir and Path::Class::File.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
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
%doc Changes README README.mkdn

%changelog
