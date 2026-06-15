#
# spec file for package perl-Dancer2-Plugin-REST
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


%define cpan_name Dancer2-Plugin-REST
Name:           perl-Dancer2-Plugin-REST
Version:        1.30.0
Release:        0
# 1.03 -> normalize -> 1.30.0
%define cpan_version 1.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Plugin for writing RESTful apps with Dancer2
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Dancer2) >= 0.203
BuildRequires:  perl(Dancer2::Core::HTTP) >= 0.203
BuildRequires:  perl(Dancer2::Core::Request)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Dancer2::Serializer::Mutable)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test2::Bundle::More)
BuildRequires:  perl(Test::Requires)
Requires:       perl(Dancer2) >= 0.203
Requires:       perl(Dancer2::Core::HTTP) >= 0.203
Requires:       perl(Dancer2::Plugin)
Requires:       perl(Dancer2::Serializer::Mutable)
Requires:       perl(Moo)
Provides:       perl(Dancer2::Plugin::REST) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This plugin helps you write a RESTful webservice with Dancer2.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md doap.xml README README.mkdn SECURITY.md
%license LICENSE

%changelog
