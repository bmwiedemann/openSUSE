#
# spec file for package perl-App-Nopaste
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


Name:           perl-App-Nopaste
Version:        1.013
Release:        0
%define cpan_name App-Nopaste
Summary:        Easy access to any pastebin
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        SusePaste.pm
Source2:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(parent)
Requires:       perl(Browser::Open)
Requires:       perl(Class::Load)
Requires:       perl(Getopt::Long::Descriptive)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Module::Pluggable)
Requires:       perl(Module::Runtime)
Requires:       perl(Path::Tiny)
Requires:       perl(URI::Escape)
Requires:       perl(WWW::Mechanize)
Requires:       perl(namespace::clean) >= 0.19
Requires:       perl(parent)
Recommends:     perl(Browser::Open)
Recommends:     perl(Clipboard)
Recommends:     perl(WWW::Pastebin::PastebinCom::Create) >= 1.003
%{perl_requires}

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the name
nopaste).

Each pastebin is slightly different. When one pastebin goes down (I'm
looking at you, http://paste.husk.org), then you have to find a new one.
And if you usually use a script to publish text, then it's too much hassle.

This module aims to smooth out the differences between pastebins, and
provides redundancy: if one site doesn't work, it just tries a different
one.

It's also modular: you only need to put on CPAN a
App::Nopaste::Service::Foo module and anyone can begin using it.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
%__install -m 0644 "%{SOURCE1}" lib/App/Nopaste/Service/
# MANUAL END

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
