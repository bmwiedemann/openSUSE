#
# spec file for package perl-Mail-Sendmail
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define cpan_name Mail-Sendmail
Name:           perl-Mail-Sendmail
Version:        0.80
Release:        0
Summary:        Simple platform independent mailer
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mail-Sendmail/
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(parent)
Requires:       perl(parent)
BuildArch:      noarch
%{perl_requires}

%description
Simple platform independent e-mail from your perl script. Only requires
Perl 5 and a network connection.

Mail::Sendmail takes a hash with the message to send and sends it to your
mail server. It is intended to be very easy to setup and use. See also
"FEATURES" below, and as usual, read this documentation.

There is also a FAQ (see "NOTES").

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
# bsc#1017667 -- Disabled tests sending email when building
# %% {__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README Todo
%license LICENSE

%changelog
