#
# spec file for package perl-HTML-RewriteAttributes
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


%define cpan_name HTML-RewriteAttributes
Name:           perl-HTML-RewriteAttributes
Version:        0.60.0
Release:        0
# 0.06 -> normalize -> 0.60.0
%define cpan_version 0.06
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Concise attribute rewriting
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(URI)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::Parser)
Requires:       perl(HTML::Tagset)
Requires:       perl(URI)
Provides:       perl(HTML::RewriteAttributes) = %{version}
Provides:       perl(HTML::RewriteAttributes::Links) = 0.03
Provides:       perl(HTML::RewriteAttributes::Resources) = 0.03
%undefine       __perllib_provides
%{perl_requires}

%description
'HTML::RewriteAttributes' is designed for simple yet powerful HTML
attribute rewriting.

You simply specify a callback to run for each attribute and we do the rest
for you.

This module is designed to be subclassable to make handling special cases
easier. See the source for methods you can override.

See the SYNOPSIS above and included tests in the 't' directory for more
examples.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
