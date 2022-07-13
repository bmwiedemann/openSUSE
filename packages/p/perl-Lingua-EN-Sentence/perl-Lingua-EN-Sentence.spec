#
# spec file for package perl-Lingua-EN-Sentence
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


%define cpan_name Lingua-EN-Sentence
Name:           perl-Lingua-EN-Sentence
Version:        0.33
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Split text into sentences
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.380000
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(warnings) >= 1.06
Requires:       perl(warnings) >= 1.06
%{perl_requires}

%description
The 'Lingua::EN::Sentence' module contains the function get_sentences,
which splits text into its constituent sentences, based on a regular
expression and a list of abbreviations (built in and given).

Certain well know exceptions, such as abbreviations, may cause incorrect
segmentations. But some of them are already integrated into this code and
are being taken care of. Still, if you see that there are words causing the
get_sentences function to fail, you can add those to the module, so it
notices them. Note that abbreviations are case sensitive, so 'Mrs.' is
recognised but not 'mrs.'

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README
%license LICENCE

%changelog
