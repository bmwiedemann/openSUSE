#
# spec file for package perl-JSON-MaybeXS
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name JSON-MaybeXS
Name:           perl-JSON-MaybeXS
Version:        1.004005
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cpanel::JSON::XS) >= 2.3310
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs) >= 0.002006
Requires:       perl(Cpanel::JSON::XS) >= 2.3310
Requires:       perl(JSON::PP) >= 2.27300
Recommends:     perl(Cpanel::JSON::XS) >= 2.3310
%{perl_requires}

%description
This module first checks to see if either Cpanel::JSON::XS or JSON::XS (at
at least version 3.0) is already loaded, in which case it uses that module.
Otherwise it tries to load Cpanel::JSON::XS, then JSON::XS, then JSON::PP
in order, and either uses the first module it finds or throws an error.

It then exports the 'encode_json' and 'decode_json' functions from the
loaded module, along with a 'JSON' constant that returns the class name for
calling 'new' on.

If you're writing fresh code rather than replacing JSON.pm usage, you might
want to pass options as constructor args rather than calling mutators, so
we provide our own 'new' method that supports that.

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
%doc Changes README
%license LICENSE

%changelog
