#
# spec file for package perl-Scalar-List-Utils
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


%define cpan_name Scalar-List-Utils
Name:           perl-Scalar-List-Utils
Version:        1.680.0
Release:        0
# 1.68 -> normalize -> 1.680.0
%define cpan_version 1.68
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Common Scalar and List utility subroutines
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(List::Util) = 1.68
Provides:       perl(List::Util::XS) = 1.68
Provides:       perl(Scalar::List::Utils) = %{version}
Provides:       perl(Scalar::Util) = 1.68
Provides:       perl(Sub::Util) = 1.68
%undefine       __perllib_provides
%{perl_requires}

%description
'Scalar::List::Utils' does nothing on its own. It is packaged with several
useful modules.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
