#
# spec file for package perl-Devel-OverloadInfo
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Devel-OverloadInfo
Name:           perl-Devel-OverloadInfo
Version:        0.007
Release:        0
Summary:        Introspect overloaded operators
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Package::Stash) >= 0.14
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
Requires:       perl(MRO::Compat)
Requires:       perl(Package::Stash) >= 0.14
Requires:       perl(Sub::Util) >= 1.40
%{perl_requires}

%description
Devel::OverloadInfo returns information about overloaded operators for a
given class (or object), including where in the inheritance hierarchy the
overloads are declared and where the code implementing them is.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
