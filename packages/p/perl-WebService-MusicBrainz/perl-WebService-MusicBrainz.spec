#
# spec file for package perl-WebService-MusicBrainz
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


%define cpan_name WebService-MusicBrainz
Name:           perl-WebService-MusicBrainz
Version:        1.0.6
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Web service API to MusicBrainz database
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BF/BFAIST/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Mojolicious) >= 7.13
Requires:       perl(Mojolicious) >= 7.13
%{perl_requires}

%description
API to search the musicbrainz.org database

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
# MANUAL no testing (needs network)
#./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md

%changelog
