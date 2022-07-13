#
# spec file for package perl-MIME-tools
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


%define cpan_name MIME-tools
Name:           perl-MIME-tools
Version:        5.510
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tools to manipulate MIME messages
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSKOLL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(Mail::Field) >= 1.05
BuildRequires:  perl(Mail::Header) >= 1.01
BuildRequires:  perl(Mail::Internet) >= 1.0203
BuildRequires:  perl(Test::Deep)
Requires:       perl(File::Temp) >= 0.18
Requires:       perl(Mail::Field) >= 1.05
Requires:       perl(Mail::Header) >= 1.01
Requires:       perl(Mail::Internet) >= 1.0203
Recommends:     perl(Convert::BinHex)
%{perl_requires}

%description
Tools to manipulate MIME messages

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc ChangeLog examples README
%license COPYING

%changelog
