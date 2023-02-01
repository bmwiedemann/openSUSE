#
# spec file for package perl-Mail-AuthenticationResults
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


%define cpan_name Mail-AuthenticationResults
Name:           perl-Mail-AuthenticationResults
Version:        2.20230112
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Object Oriented Authentication-Results Headers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Test::Exception)
Requires:       perl(Clone)
Requires:       perl(JSON)
%{perl_requires}

%description
Object Oriented Authentication-Results email headers.

This parser copes with most styles of Authentication-Results header seen in
the wild, but is not yet fully RFC7601 compliant

Differences from RFC7601

key/value pairs are parsed when present in the authserv-id section, this is
against RFC but has been seen in headers added by Yahoo!.

Comments added between key/value pairs will be added after them in the data
structures and when stringified.

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
%doc Changes README README.md
%license LICENSE

%changelog
