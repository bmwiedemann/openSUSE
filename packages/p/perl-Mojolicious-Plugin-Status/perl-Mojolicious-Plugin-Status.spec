#
# spec file for package perl-Mojolicious-Plugin-Status
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Mojolicious-Plugin-Status
Name:           perl-Mojolicious-Plugin-Status
Version:        1.17
Release:        0
Summary:        Mojolicious server status
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(File::Map)
BuildRequires:  perl(File::Temp) >= 0.2308
BuildRequires:  perl(Mojolicious) >= 9.11
BuildRequires:  perl(Sereal)
Requires:       perl(BSD::Resource)
Requires:       perl(File::Map)
Requires:       perl(File::Temp) >= 0.2308
Requires:       perl(Mojolicious) >= 9.11
Requires:       perl(Sereal)
%{perl_requires}

%description
Mojolicious::Plugin::Status is a Mojolicious plugin providing a server
status ui for Mojo::Server::Daemon and Mojo::Server::Prefork. Note that
this module is *EXPERIMENTAL* and should therefore only be used for
debugging purposes.

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
%doc Changes examples README.md
%license LICENSE

%changelog
