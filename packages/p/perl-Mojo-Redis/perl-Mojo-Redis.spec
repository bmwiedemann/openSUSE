#
# spec file for package perl-Mojo-Redis
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Mojo-Redis
Version:        3.25
Release:        0
%define cpan_name Mojo-Redis
Summary:        Redis driver based on Mojo::IOLoop
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mojolicious) >= 7.80
BuildRequires:  perl(Protocol::Redis::Faster) >= 0.002
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Mojolicious) >= 7.80
Requires:       perl(Protocol::Redis::Faster) >= 0.002
%{perl_requires}

%description
Mojo::Redis is a Redis driver that use the Mojo::IOLoop, which makes it
integrate easily with the Mojolicious framework.

It tries to mimic the same interface as Mojo::Pg, Mojo::mysql and
Mojo::SQLite, but the methods for talking to the database vary.

This module is in no way compatible with the 1.xx version of Mojo::Redis
and this version also tries to fix a lot of the confusing methods in
Mojo::Redis2 related to pubsub.

This module is currently EXPERIMENTAL, and bad design decisions will be
fixed without warning. Please report at
https://github.com/jhthorsen/mojo-redis/issues if you find this module
useful, annoying or if you simply find bugs. Feedback can also be sent to
'jhthorsen@cpan.org'.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes examples README.md

%changelog
