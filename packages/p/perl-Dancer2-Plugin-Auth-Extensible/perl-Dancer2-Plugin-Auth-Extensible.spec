#
# spec file for package perl-Dancer2-Plugin-Auth-Extensible
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Dancer2-Plugin-Auth-Extensible
Version:        0.709
Release:        0
%define cpan_name Dancer2-Plugin-Auth-Extensible
Summary:        Extensible authentication framework for Dancer2 apps
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABEVERLEY/%{cpan_name}-%{version}.tar.gz
Patch0:         remove-env-perl.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::SaltedHash)
BuildRequires:  perl(Dancer2) >= 0.204000
BuildRequires:  perl(Dancer2::Core::Types)
BuildRequires:  perl(Dancer2::FileUtils)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Dancer2::Template::Tiny)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::Share)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(HTTP::BrowserDetect)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.000000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Tiny) >= 0.016
BuildRequires:  perl(Plack) >= 1.0029
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Session::Token)
BuildRequires:  perl(Test::Deep) >= 0.114
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockDateTime)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(YAML)
BuildRequires:  perl(namespace::clean)
Requires:       perl-base = %{perl_version}
Requires:       perl(Crypt::SaltedHash)
Requires:       perl(Dancer2) >= 0.204000
Requires:       perl(Dancer2::Core::Types)
Requires:       perl(Dancer2::FileUtils)
Requires:       perl(Dancer2::Plugin)
Requires:       perl(Dancer2::Template::Tiny)
Requires:       perl(File::Share)
Requires:       perl(HTTP::BrowserDetect)
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 2.000000
Requires:       perl(Moo::Role)
Requires:       perl(Plack) >= 1.0029
Requires:       perl(Session::Token)
Requires:       perl(Try::Tiny)
Requires:       perl(URI::Escape)
Requires:       perl(YAML)
Requires:       perl(namespace::clean)
%{perl_requires}


%description
A user authentication and authorisation framework plugin for Dancer2 apps.

Makes it easy to require a user to be logged in to access certain routes,
provides role-based access control, and supports various authentication
methods/sources (config file, database, Unix system users, etc).

Designed to support multiple authentication realms and to be as extensible
as possible, and to make secure password handling easy. The base class for
auth providers makes handling 'RFC2307'-style hashed passwords really
simple, so you have no excuse for storing plain-text passwords. A simple
script called *dancer2-generate-crypted-password* to generate RFC2307-style
hashed passwords is included, or you can use Crypt::SaltedHash yourself to
do so, or use the 'slappasswd' utility if you have it installed.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes example ignore.txt README

%changelog
