#
# spec file for package perl-Plack-App-WebSocket
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Plack-App-WebSocket
Version:        0.08
Release:        0
%define cpan_name Plack-App-WebSocket
Summary:        WebSocket server as a PSGI application
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Plack-App-WebSocket/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::WebSocket::Client) >= 0.20
BuildRequires:  perl(AnyEvent::WebSocket::Server) >= 0.06
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Module::Build::Prereqs::FromCPANfile) >= 0.02
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Plack::Component)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Protocol::WebSocket)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(parent)
BuildRequires:  perl(Cookie::Baker)
BuildRequires:  perl(HTTP::Headers::Fast)
Requires:       perl(AnyEvent)
Requires:       perl(AnyEvent::WebSocket::Server) >= 0.06
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(Plack::Component)
Requires:       perl(Plack::Response)
Requires:       perl(Try::Tiny)
Requires:       perl(parent)
Provides:       perl(Plack::App::WebSocket)
%{perl_requires}

%description
This module is a PSGI application that creates an endpoint for WebSocket
connections.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes

%changelog
