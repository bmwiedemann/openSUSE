#
# spec file for package perl-Sub-Name
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


%define cpan_name Sub-Name
Name:           perl-Sub-Name
Version:        0.280.0
Release:        0
# 0.28 -> normalize -> 0.280.0
%define cpan_version 0.28
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        (Re)name a sub
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Sub::Name) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Devel::CheckBin)
# MANUAL END

%description
This module has only one function, which is also exported by default:

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
