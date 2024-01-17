#
# spec file for package perl-HTTP-Tinyish
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


%define cpan_name HTTP-Tinyish
Name:           perl-HTTP-Tinyish
Version:        0.18
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        HTTP::Tiny compatible HTTP client wrappers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which)
BuildRequires:  perl(HTTP::Tiny) >= 0.055
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(File::Which)
Requires:       perl(HTTP::Tiny) >= 0.055
Requires:       perl(IPC::Run3)
Requires:       perl(parent)
%{perl_requires}

%description
HTTP::Tinyish is a wrapper module for HTTP client modules LWP, HTTP::Tiny
and HTTP client software 'curl' and 'wget'.

It provides an API compatible to HTTP::Tiny, and the implementation has
been extracted out of App::cpanminus. This module can be useful in a
restrictive environment where you need to be able to download CPAN modules
without an HTTPS support in built-in HTTP library.

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
