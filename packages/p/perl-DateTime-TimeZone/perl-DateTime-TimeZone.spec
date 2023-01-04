#
# spec file for package perl-DateTime-TimeZone
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name DateTime-TimeZone
Name:           perl-DateTime-TimeZone
Version:        2.57
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Time zone object base class and factory
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Singleton) >= 1.03
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
Requires:       perl(Class::Singleton) >= 1.03
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Runtime)
Requires:       perl(Params::ValidationCompiler) >= 0.13
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(Specio::Library::String)
Requires:       perl(Try::Tiny)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent)
%{perl_requires}

%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

Note that without the DateTime module, this module does not do much. It's
primary interface is through a DateTime object, and most users will not
need to directly use 'DateTime::TimeZone' methods.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
