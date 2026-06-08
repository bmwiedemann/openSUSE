#
# spec file for package perl-Class-ReturnValue
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Class-ReturnValue
Name:           perl-Class-ReturnValue
Version:        0.550.0
Release:        0
# 0.55 -> normalize -> 0.550.0
%define cpan_version 0.55
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Smart return value object
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JESSE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::StackTrace)
Requires:       perl(Devel::StackTrace)
Provides:       perl(Class::ReturnValue) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Class::ReturnValue is a "clever" return value object that can allow code
calling your routine to expect: a boolean value (did it fail) or a list
(what are the return values)

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
