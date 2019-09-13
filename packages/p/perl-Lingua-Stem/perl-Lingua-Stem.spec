#
# spec file for package perl-Lingua-Stem
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Lingua-Stem
Version:        0.84
Release:        0
%define cpan_name Lingua-Stem
Summary:        Stemming of words in various languages
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-Stem/
Source:         http://www.cpan.org/authors/id/S/SN/SNOWHARE/%{cpan_name}-%{version}.tar.gz
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
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Artistic_License.txt Changes examples GPL_License.txt LICENSE README

%changelog
