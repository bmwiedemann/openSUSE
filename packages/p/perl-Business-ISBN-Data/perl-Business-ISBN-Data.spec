#
# spec file for package perl-Business-ISBN-Data
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Business-ISBN-Data
Version:        20191107
Release:        0
%define cpan_name Business-ISBN-Data
Summary:        Data pack for Business::ISBN
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.95
%{perl_requires}

%description
You don't need to load this module yourself in most cases. 'Business::ISBN'
will load it when it loads.

These data are generated from the _RangeMessage.xml_ file provided by the
ISBN Agency. You can retrieve this yourself at
https://www.isbn-international.org/range_file_generation. This file is
included as part of the distribution and should be installed at
_~lib/Business/ISBN/Data/RangeMessage.xml_.

If you want to use a different _RangeMessage.xml_ file, you can set the
'ISBN_RANGE_MESSAGE' environment variable to the alternate location before
you load 'Business::ISBN'. This way, you can use the latest (or even
earlier) data without having to install something new or wait for an update
to this module.

If the default _RangeMessage.xml_ or your alternate one is not available,
the module falls back to data included in _Data.pm_. However, that data is
likely to be older data. If it does not find that file, it looks for
_RangeMessage.xml_ in the current directory.

The data are in '%Business::ISBN::country_data' (although the "country"
part is historical). If you want to see where the data are from, check
'$Business::ISBN::country_data{_source}'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples
%license LICENSE

%changelog
