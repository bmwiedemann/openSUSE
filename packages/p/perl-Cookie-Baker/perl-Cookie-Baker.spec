#
# spec file for package perl-Cookie-Baker
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


%define cpan_name Cookie-Baker
Name:           perl-Cookie-Baker
Version:        0.120.0
Release:        0
%define cpan_version 0.12
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Cookie string generator / parser
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Time)
BuildRequires:  perl(URI::Escape)
Requires:       perl(URI::Escape)
Provides:       perl(Cookie::Baker) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Cookie::Baker provides simple cookie string generator and parser.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
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
