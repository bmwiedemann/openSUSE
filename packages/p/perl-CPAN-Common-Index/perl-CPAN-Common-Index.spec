#
# spec file for package perl-CPAN-Common-Index
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-CPAN-Common-Index
Version:        0.010
Release:        0
%define cpan_name CPAN-Common-Index
Summary:        Common library for searching CPAN modules, authors and distributions
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Search::Dict) >= 1.07
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Tie::Handle::SkipHeader)
BuildRequires:  perl(URI)
BuildRequires:  perl(parent)
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta::YAML)
Requires:       perl(Class::Tiny)
Requires:       perl(File::Fetch)
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(HTTP::Tiny)
Requires:       perl(Module::Load)
Requires:       perl(Search::Dict) >= 1.07
Requires:       perl(Tie::Handle::SkipHeader)
Requires:       perl(URI)
Requires:       perl(parent)
Recommends:     perl(IO::Uncompress::Gunzip)
%{perl_requires}

%description
This module provides a common library for working with a variety of CPAN
index services. It is intentionally minimalist, trying to use as few
non-core modules as possible.

The 'CPAN::Common::Index' module is an abstract base class that defines a
common API. Individual backends deliver the API for a particular index.

As shown in the SYNOPSIS, one interesting application is multiplexing --
using different index backends, querying each in turn, and returning the
first result.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.mkdn examples README Todo
%license LICENSE

%changelog
