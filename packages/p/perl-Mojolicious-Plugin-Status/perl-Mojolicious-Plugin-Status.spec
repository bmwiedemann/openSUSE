#
# spec file for package perl-Mojolicious-Plugin-Status
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Mojolicious-Plugin-Status
Version:        1.0
Release:        0
%define cpan_name Mojolicious-Plugin-Status
Summary:        Mojolicious server status
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mojolicious-Plugin-Status/
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(IPC::ShareLite)
BuildRequires:  perl(Mojolicious) >= 7.88
BuildRequires:  perl(Sereal)
Requires:       perl(BSD::Resource)
Requires:       perl(IPC::ShareLite)
Requires:       perl(Mojolicious) >= 7.88
Requires:       perl(Sereal)
%{perl_requires}

%description
Mojolicious::Plugin::Status is a Mojolicious plugin providing a server
status ui for Mojo::Server::Daemon and Mojo::Server::Prefork. Very useful
for debugging.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README.md
%license LICENSE

%changelog
