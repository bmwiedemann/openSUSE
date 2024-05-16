#
# spec file for package perl-ExtUtils-Config
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name ExtUtils-Config
Name:           perl-ExtUtils-Config
Version:        0.9.0
Release:        0
# 0.009 -> normalize -> 0.9.0
%define cpan_version 0.009
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Wrapper for perl's configuration
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
Provides:       perl(ExtUtils::Config) = %{version}
Provides:       perl(ExtUtils::Config::MakeMaker) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
ExtUtils::Config is an abstraction around the %Config hash. By itself it is
not a particularly interesting module by any measure, however it ties
together a family of modern toolchain modules.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
