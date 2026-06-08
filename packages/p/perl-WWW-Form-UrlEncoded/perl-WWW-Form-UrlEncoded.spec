#
# spec file for package perl-WWW-Form-UrlEncoded
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name WWW-Form-UrlEncoded
Name:           perl-WWW-Form-UrlEncoded
Version:        0.260.0
Release:        0
# 0.26 -> normalize -> 0.260.0
%define cpan_version 0.26
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parser and builder for application/x-www-form-urlencoded
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
# MANUAL
#BuildArch:     noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(Module::Build) >= 0.400.500
BuildRequires:  perl(Test::More) >= 0.98
Provides:       perl(WWW::Form::UrlEncoded) = %{version}
Provides:       perl(WWW::Form::UrlEncoded::PP)
%undefine       __perllib_provides
%{perl_requires}

%description
WWW::Form::UrlEncoded provides application/x-www-form-urlencoded parser and
builder. This module aims to have compatibility with other CPAN modules
like HTTP::Body's urlencoded parser.

This module try to use WWW::Form::UrlEncoded::XS by default and fail to it,
use WWW::Form::UrlEncoded::PP instead

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
