#
# spec file for package perl-Business-ISBN-Data
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


%define cpan_name Business-ISBN-Data
Name:           perl-Business-ISBN-Data
Version:        20240614.1.0
Release:        0
# 20240614.001 -> normalize -> 20240614.1.0
%define cpan_version 20240614.001
License:        Artistic-2.0
Summary:        Data pack for Business::ISBN
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::More) >= 1
Provides:       perl(Business::ISBN::Data) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
You don't need to load this module yourself in most cases. Business::ISBN
will load it when it loads. You must use Business::ISBN 3.005 or later
because the data structure changed slightly to fix a bug with ISBN13
prefixes.

These data are generated from the _RangeMessage.xml_ file provided by the
ISBN Agency. The distributed version matches the date in the version for
this module. You can retrieve this yourself at
https://www.isbn-international.org/range_file_generation. This file is
included as part of the distribution and should be installed at
_~lib/Business/ISBN/Data/RangeMessage.xml_.

If you want to use a different _RangeMessage.xml_ file, you can set the
'ISBN_RANGE_MESSAGE' environment variable to the alternate location before
you load 'Business::ISBN'. This way, you can use the latest (or even
earlier) data without having to install something new or wait for an update
to this module.

If the default _RangeMessage.xml_ or your alternate one is not available,
the module falls back to data included in _Data.pm_. However, that data are
likely to be older. If it does not find that file, it looks for
_RangeMessage.xml_ in the current directory.

The data are in '%Business::ISBN::country_data' (although the "country"
part is historical). If you want to see where the data are from, check
'$Business::ISBN::country_data{_source}'.

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
%doc Changes examples
%license LICENSE

%changelog
