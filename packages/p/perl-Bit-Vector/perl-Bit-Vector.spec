#
# spec file for package perl-Bit-Vector
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Bit-Vector
Name:           perl-Bit-Vector
Version:        7.400.0
Release:        0
# 7.4 -> normalize -> 7.400.0
%define cpan_version 7.4
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Bit::Vector Perl module
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STBEY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Bit-Vector-7.1.diff
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan) >= 5.300
BuildRequires:  perl(Storable) >= 2.21
Requires:       perl(Carp::Clan) >= 5.300
Requires:       perl(Storable) >= 2.21
Provides:       perl(Bit::Vector) = %{version}
Provides:       perl(Bit::Vector::Overload) = %{version}
Provides:       perl(Bit::Vector::String) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -N

%patch -P0

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
%doc CHANGES.txt CREDITS.txt examples GNU_GPL.txt GNU_LGPL.txt README.txt
%license Artistic.txt

%changelog
