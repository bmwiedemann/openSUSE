#
# spec file for package perl-Dancer2-Plugin-WebSocket
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


%define cpan_name Dancer2-Plugin-WebSocket
Name:           perl-Dancer2-Plugin-WebSocket
Version:        0.3.1
Release:        0
Summary:        Add a websocket interface to your Dancers app
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Plack::App::WebSocket)
BuildRequires:  perl(Set::Tiny)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Dancer2::Plugin)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Moo)
Requires:       perl(Moo::Role)
Requires:       perl(Plack::App::WebSocket)
Requires:       perl(Set::Tiny)
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
'Dancer2::Plugin::WebSocket' provides an interface to Plack::App::WebSocket
and allows to interact with the webSocket connections within the Dancer
app.

Plack::App::WebSocket, and thus this plugin, requires a plack server that
supports the psgi _streaming_, _nonblocking_ and _io_. Twiggy is the most
popular server fitting the bill.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc AUTHOR_PLEDGE Changes CODE_OF_CONDUCT.md CONTRIBUTORS doap.xml example README.mkdn
%license LICENSE

%changelog
