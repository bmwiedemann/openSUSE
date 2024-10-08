#
# spec file for package perl-FCGI-Client
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


%define cpan_name FCGI-Client
Name:           perl-FCGI-Client
Version:        0.90.0
Release:        0
# 0.09 -> normalize -> 0.90.0
%define cpan_version 0.09
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Client library for fastcgi protocol
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Type::Tiny)
Requires:       perl(Moo) >= 2
Requires:       perl(Type::Tiny)
Provides:       perl(FCGI::Client) = %{version}
Provides:       perl(FCGI::Client::Connection)
Provides:       perl(FCGI::Client::Constant)
Provides:       perl(FCGI::Client::Record)
Provides:       perl(FCGI::Client::RecordFactory)
Provides:       perl(FCGI::Client::RecordHeader)
%undefine       __perllib_provides
%{perl_requires}

%description
FCGI::Client is client library for fastcgi protocol.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
