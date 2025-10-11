#
# spec file for package perl-HTTP-Headers-Fast
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name HTTP-Headers-Fast
Name:           perl-HTTP-Headers-Fast
Version:        0.220.0
Release:        0
# 0.22 -> normalize -> 0.220.0
%define cpan_version 0.22
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Faster implementation of HTTP::Headers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.35
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Requires)
Requires:       perl(HTTP::Date)
Provides:       perl(HTTP::Headers::Fast) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
HTTP::Headers::Fast is a perl class for parsing/writing HTTP headers.

The interface is same as HTTP::Headers.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
