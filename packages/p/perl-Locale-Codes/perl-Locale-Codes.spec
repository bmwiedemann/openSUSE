#
# spec file for package perl-Locale-Codes
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


%define cpan_name Locale-Codes
Name:           perl-Locale-Codes
Version:        3.790.0
Release:        0
# 3.79 -> normalize -> 3.790.0
%define cpan_version 3.79
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Distribution of modules to handle locale codes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Inter) >= 1.09
Provides:       perl(Locale::Codes) = %{version}
Provides:       perl(Locale::Codes::Constants) = %{version}
Provides:       perl(Locale::Codes::Country) = %{version}
Provides:       perl(Locale::Codes::Country_Codes) = %{version}
Provides:       perl(Locale::Codes::Country_Retired) = %{version}
Provides:       perl(Locale::Codes::Currency) = %{version}
Provides:       perl(Locale::Codes::Currency_Codes) = %{version}
Provides:       perl(Locale::Codes::Currency_Retired) = %{version}
Provides:       perl(Locale::Codes::LangExt) = %{version}
Provides:       perl(Locale::Codes::LangExt_Codes) = %{version}
Provides:       perl(Locale::Codes::LangExt_Retired) = %{version}
Provides:       perl(Locale::Codes::LangFam) = %{version}
Provides:       perl(Locale::Codes::LangFam_Codes) = %{version}
Provides:       perl(Locale::Codes::LangFam_Retired) = %{version}
Provides:       perl(Locale::Codes::LangVar) = %{version}
Provides:       perl(Locale::Codes::LangVar_Codes) = %{version}
Provides:       perl(Locale::Codes::LangVar_Retired) = %{version}
Provides:       perl(Locale::Codes::Language) = %{version}
Provides:       perl(Locale::Codes::Language_Codes) = %{version}
Provides:       perl(Locale::Codes::Language_Retired) = %{version}
Provides:       perl(Locale::Codes::Script) = %{version}
Provides:       perl(Locale::Codes::Script_Codes) = %{version}
Provides:       perl(Locale::Codes::Script_Retired) = %{version}
Provides:       perl(Locale::Country) = %{version}
Provides:       perl(Locale::Currency) = %{version}
Provides:       perl(Locale::Language) = %{version}
Provides:       perl(Locale::Script) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
*Locale-Codes* is a distribution containing a set of modules designed to
work with sets of codes which uniquely identify something. For example,
there are codes associated with different countries, different currencies,
different languages, etc. These sets of codes are typically maintained in
some standard.

This distribution provides a way to work with these lists of codes. Because
the data from the various standards is not available in any sort of
consistent API, access to the lists is not available in any direct fashion.
To compensate for this, the list of codes is stored internally within this
distribution, and the distribution is updated on a regular basis to include
all known codes at that point in time. This does mean that it is necessary
to keep this distribution up-to-date to keep up with the various changes
that are made in the various standards.

Traditionally, a module has been created to work with each type of code
sets. So, there is a module for working with country lists, one for
currency lists, etc. Since version 3.00, all of these individual modules
were written as wrappers around a central module (which was not intended to
be used directly) which did all of the real work.

Starting with version 3.50, the central module was reworked slightly to
provide an object-oriented interface. All of the modules for working with
individual types of code sets were reworked to use the improved OO module,
so the traditional interfaces still work as they always have. As a result,
you are free to use the traditional functional (non-OO) interfaces, or to
use the OO interface and bypass the wrapper modules entirely.

Both methods will be supported in the future, so use the one that is best
suited to your needs.

Within each type, any number of code sets are allowed. For example, sets of
country codes are maintained in several different locations including the
ISO-3166 standard, the IANA, and by the United Nations. The lists of
countries are similar, but not identical. Multiple code sets are supported,
though trying to convert from one code set to another will not always work
since the list of countries is not one-to-one.

All data in all of these modules comes directly from the original standards
(or as close to direct as possible), so it should be up-to-date at the time
of release.

I plan on releasing a new version several times a year to incorporate any
changes made in the standards. However, I don't always know about changes
that occur, so if any of the standards change, and you want a new release
sooner, just email me and I'll get one out.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README README.first
%license LICENSE

%changelog
