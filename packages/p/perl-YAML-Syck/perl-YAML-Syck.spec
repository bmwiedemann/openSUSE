#
# spec file for package perl-YAML-Syck
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


%define cpan_name YAML-Syck
Name:           perl-YAML-Syck
Version:        1.360.0
Release:        0
# 1.36 -> normalize -> 1.360.0
%define cpan_version 1.36
License:        MIT
Summary:        Perl YAML loader and dumper
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(JSON::Syck) = %{version}
Provides:       perl(YAML::Dumper::Syck)
Provides:       perl(YAML::Loader::Syck)
Provides:       perl(YAML::Syck) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides a Perl interface to the *libsyck* data serialization
library. It exports the 'Dump' and 'Load' functions for converting Perl
data structures to YAML strings, and the other way around.

*NOTE*: If you are working with other language's YAML/Syck bindings (such
as Ruby), please set '$YAML::Syck::ImplicitTyping' to '1' before calling
the 'Load'/'Dump' functions. The default setting is for preserving
backward-compatibility with 'YAML.pm'.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
# https://github.com/cpan-authors/YAML-Syck/issues/61
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags} -DI_STDLIB -DI_STRING -std=gnu11"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes COMPATIBILITY README.md
%license COPYING

%changelog
