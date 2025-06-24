#
# spec file for package perl-App-Nopaste
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


%define cpan_name App-Nopaste
Name:           perl-App-Nopaste
Version:        1.13.0
Release:        0
# 1.013 -> normalize -> 1.13.0
%define cpan_version 1.013
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Easy access to any pastebin
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        SusePaste.pm
Source2:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
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
BuildRequires:  perl(namespace::clean) >= 0.190
BuildRequires:  perl(parent)
Requires:       perl(Class::Load)
Requires:       perl(Getopt::Long::Descriptive)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Module::Pluggable)
Requires:       perl(Module::Runtime)
Requires:       perl(Path::Tiny)
Requires:       perl(URI::Escape)
Requires:       perl(WWW::Mechanize)
Requires:       perl(namespace::clean) >= 0.190
Requires:       perl(parent)
Provides:       perl(App::Nopaste) = %{version}
Provides:       perl(App::Nopaste::Command) = %{version}
Provides:       perl(App::Nopaste::Service) = %{version}
Provides:       perl(App::Nopaste::Service::Codepeek) = %{version}
Provides:       perl(App::Nopaste::Service::Debian) = %{version}
Provides:       perl(App::Nopaste::Service::Gist) = %{version}
Provides:       perl(App::Nopaste::Service::GitLab) = %{version}
Provides:       perl(App::Nopaste::Service::Mojopaste) = %{version}
Provides:       perl(App::Nopaste::Service::PastebinCom) = %{version}
Provides:       perl(App::Nopaste::Service::Pastie) = %{version}
Provides:       perl(App::Nopaste::Service::Shadowcat) = %{version}
Provides:       perl(App::Nopaste::Service::Snitch) = %{version}
Provides:       perl(App::Nopaste::Service::Ubuntu) = %{version}
Provides:       perl(App::Nopaste::Service::ssh) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Browser::Open)
Recommends:     perl(Clipboard)
Recommends:     perl(WWW::Pastebin::PastebinCom::Create) >= 1.3
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
%__install -m 0644 "%{SOURCE1}" lib/App/Nopaste/Service/
# MANUAL END

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
