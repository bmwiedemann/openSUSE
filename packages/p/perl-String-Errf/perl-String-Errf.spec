#
# spec file for package perl-String-Errf
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


%define cpan_name String-Errf
Name:           perl-String-Errf
Version:        0.009
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple sprintf-like dialect
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(String::Formatter) >= 0.102081
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(autodie)
BuildRequires:  perl(parent)
Requires:       perl(Params::Util)
Requires:       perl(String::Formatter) >= 0.102081
Requires:       perl(Sub::Exporter)
Requires:       perl(Time::Piece)
Requires:       perl(parent)
%{perl_requires}

%description
String::Errf provides 'errf', a simple string formatter that works
something like 'sprintf'. It is implemented using String::Formatter and
Sub::Exporter. Their documentation may be useful in understanding or
extending String::Errf. The 'errf' subroutine is only available when
imported. Calling String::Errf::errf will not do what you want.

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
