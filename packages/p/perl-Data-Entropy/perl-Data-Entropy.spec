#
# spec file for package perl-Data-Entropy
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


%define cpan_name Data-Entropy
Name:           perl-Data-Entropy
Version:        0.8.0
Release:        0
# 0.008 -> normalize -> 0.8.0
%define cpan_version 0.008
#Upstream:  <zefram@fysh.org>
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Entropy (randomness) management
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom) >= 0.360
BuildRequires:  perl(Data::Float) >= 0.8.0
BuildRequires:  perl(HTTP::Lite) >= 2.2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
Requires:       perl(Crypt::Rijndael)
Requires:       perl(Crypt::URandom) >= 0.360
Requires:       perl(Data::Float) >= 0.8.0
Requires:       perl(HTTP::Lite) >= 2.2
Requires:       perl(Module::Build)
Requires:       perl(Params::Classify)
Requires:       perl(parent)
Provides:       perl(Data::Entropy) = %{version}
Provides:       perl(Data::Entropy::Algorithms) = %{version}
Provides:       perl(Data::Entropy::RawSource::CryptCounter) = %{version}
Provides:       perl(Data::Entropy::RawSource::Local) = %{version}
Provides:       perl(Data::Entropy::RawSource::RandomOrg) = %{version}
Provides:       perl(Data::Entropy::RawSource::RandomnumbersInfo) = %{version}
Provides:       perl(Data::Entropy::Source) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module maintains a concept of a current selection of entropy source.
Algorithms that require entropy, such as those in
Data::Entropy::Algorithms, can use the source nominated by this module,
avoiding the need for entropy source objects to be explicitly passed
around. This is convenient because usually one entropy source will be used
for an entire program run and so an explicit entropy source parameter would
rarely vary. There is also a default entropy source, avoiding the need to
explicitly configure a source at all.

If nothing is done to set a source then it defaults to the use of Rijndael
(AES) in counter mode (see Data::Entropy::RawSource::CryptCounter and
Crypt::Rijndael), keyed using Crypt::URandom.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README SECURITY.md

%changelog
