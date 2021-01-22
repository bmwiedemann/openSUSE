#
# spec file for package perl-Business-ISBN
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Business-ISBN
Name:           perl-Business-ISBN
Version:        3.006
Release:        0
Summary:        Work with International Standard Book Numbers
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Business::ISBN::Data) >= 20191107
BuildRequires:  perl(Test::More) >= 1
Requires:       perl(Business::ISBN::Data) >= 20191107
%{perl_requires}

%description
This modules handles International Standard Book Numbers, including ISBN-10
and ISBN-13.

The data come from Business::ISBN::Data, which means you can update the
data separately from the code. Also, you can use Business::ISBN::Data with
whatever _RangeMessage.xml_ you like if you have updated data. See that
module for details.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc bad-isbn13s.txt bad-isbns.txt Changes examples isbn13s.txt isbns.txt
%license LICENSE

%changelog
