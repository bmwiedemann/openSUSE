#
# spec file for package perl-Apache2-AuthCookieDBI
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Apache2-AuthCookieDBI
Version:        2.18
Release:        0
%define cpan_name Apache2-AuthCookieDBI
Summary:        An AuthCookie module backed by a DBI database
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATISSE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Apache2::AuthCookie) >= 3.08
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(Crypt::CBC) >= 2.13
BuildRequires:  perl(DBI) >= 1.4
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Digest::SHA) >= 5.47
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(mod_perl2) >= 1.999022
Requires:       perl(Apache2::AuthCookie) >= 3.08
Requires:       perl(Apache2::Const)
Requires:       perl(Apache2::RequestRec)
Requires:       perl(Apache2::ServerUtil)
Requires:       perl(Crypt::CBC) >= 2.13
Requires:       perl(DBI) >= 1.4
Requires:       perl(Date::Calc)
Requires:       perl(mod_perl2) >= 1.999022
Recommends:     perl(Digest::SHA) >= 5.47
%{perl_requires}

%description
This module is an authentication handler that uses the basic mechanism
provided by Apache2::AuthCookie with a DBI database for ticket-based
protection. It is based on two tokens being provided, a username and
password, which can be any strings (there are no illegal characters for
either). The username is used to set the remote user as if Basic
Authentication was used.

On an attempt to access a protected location without a valid cookie being
provided, the module prints an HTML login form (produced by a CGI or any
other handler; this can be a static file if you want to always send people
to the same entry page when they log in). This login form has fields for
username and password. On submitting it, the username and password are
looked up in the DBI database. The supplied password is checked against the
password in the database; the password in the database can be plaintext, or
a crypt() or md5_hex() checksum of the password. If this succeeds, the user
is issued a ticket. This ticket contains the username, an issue time, an
expire time, and an MD5 checksum of those and a secret key for the server.
It can optionally be encrypted before returning it to the client in the
cookie; encryption is only useful for preventing the client from seeing the
expire time. If you wish to protect passwords in transport, use an
SSL-encrypted connection. The ticket is given in a cookie that the browser
stores.

After a login the user is redirected to the location they originally wished
to view (or to a fixed page if the login "script" was really a static
file).

On this access and any subsequent attempt to access a protected document,
the browser returns the ticket to the server. The server unencrypts it if
encrypted tickets are enabled, then extracts the username, issue time,
expire time and checksum. A new checksum is calculated of the username,
issue time, expire time and the secret key again; if it agrees with the
checksum that the client supplied, we know that the data has not been
tampered with. We next check that the expire time has not passed. If not,
the ticket is still good, so we set the username.

Authorization checks then check that any "require valid-user" or "require
user jacob" settings are passed. Finally, if a "require group foo"
directive was given, the module will look up the username in a groups
database and check that the user is a member of one of the groups listed.
If all these checks pass, the document requested is displayed.

If a ticket has expired or is otherwise invalid it is cleared in the
browser and the login form is shown again.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes generic_reg_auth_scheme.txt README schema.sql techspec.txt
%license LICENSE

%changelog
