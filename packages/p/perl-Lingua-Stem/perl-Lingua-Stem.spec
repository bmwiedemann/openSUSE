#
# spec file for package perl-Lingua-Stem
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Lingua-Stem
Version:        2.31
Release:        0
%define cpan_name Lingua-Stem
Summary:        Stemming of words
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SN/SNOWHARE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Lingua::GL::Stemmer)
BuildRequires:  perl(Lingua::PT::Stemmer)
BuildRequires:  perl(Lingua::Stem::Fr) >= 0.02
BuildRequires:  perl(Lingua::Stem::It)
BuildRequires:  perl(Lingua::Stem::Ru)
BuildRequires:  perl(Lingua::Stem::Snowball::Da) >= 1.01
BuildRequires:  perl(Lingua::Stem::Snowball::No) >= 1.00
BuildRequires:  perl(Lingua::Stem::Snowball::Se) >= 1.01
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Text::German)
Requires:       perl(Lingua::GL::Stemmer)
Requires:       perl(Lingua::PT::Stemmer)
Requires:       perl(Lingua::Stem::Fr) >= 0.02
Requires:       perl(Lingua::Stem::It)
Requires:       perl(Lingua::Stem::Ru)
Requires:       perl(Lingua::Stem::Snowball::Da) >= 1.01
Requires:       perl(Lingua::Stem::Snowball::No) >= 1.00
Requires:       perl(Lingua::Stem::Snowball::Se) >= 1.01
Requires:       perl(Text::German)
%{perl_requires}

%description
This routine applies stemming algorithms to its parameters, returning the
stemmed words as appropriate to the selected locale.

You can import some or all of the class methods.

use Lingua::Stem qw (stem clear_stem_cache stem_caching add_exceptions
delete_exceptions get_exceptions set_locale get_locale :all :locale
:exceptions :stem :caching);

 :all        - imports  stem add_exceptions delete_exceptions get_exceptions
               set_locale get_locale
 :stem       - imports  stem
 :caching    - imports  stem_caching clear_stem_cache
 :locale     - imports  set_locale get_locale
 :exceptions - imports  add_exceptions delete_exceptions get_exceptions

Currently supported locales are:

      DA          - Danish
      DE          - German
      EN          - English (also EN-US and EN-UK)
      FR          - French
      GL          - Galician
      IT          - Italian
      NO          - Norwegian
      PT          - Portuguese
      RU          - Russian (also RU-RU and RU-RU.KOI8-R)
      SV          - Swedish

If you have the memory and lots of stemming to do, I *strongly* suggest
using cache level 2 and processing lists in 'big chunks' (long lists) for
best performance.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples GPL_License.txt README
%license Artistic_License.txt LICENSE

%changelog
