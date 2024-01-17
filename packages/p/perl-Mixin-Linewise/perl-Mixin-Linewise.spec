#
# spec file for package perl-Mixin-Linewise
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


%define cpan_name Mixin-Linewise
Name:           perl-Mixin-Linewise
Version:        0.111
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Write your linewise code for handles; this does the rest
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(PerlIO::utf8_strict)
Requires:       perl(Sub::Exporter)
%{perl_requires}

%description
It's boring to deal with opening files for IO, converting strings to
handle-like objects, and all that. With Mixin::Linewise::Readers and
Mixin::Linewise::Writers, you can just write a method to handle handles,
and methods for handling strings and filenames are added for you.

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
