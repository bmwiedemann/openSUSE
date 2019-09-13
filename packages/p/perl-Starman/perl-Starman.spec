#
# spec file for package perl-Starman
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


Name:           perl-Starman
Version:        0.4015
Release:        0
%define cpan_name Starman
Summary:        High-performance preforking PSGI/Plack web server
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Parser::XS)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Net::Server) >= 2.007
BuildRequires:  perl(Plack) >= 0.9971
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP) >= 2.00
BuildRequires:  perl(parent)
Requires:       perl(Data::Dump)
Requires:       perl(HTTP::Date)
Requires:       perl(HTTP::Parser::XS)
Requires:       perl(HTTP::Status)
Requires:       perl(Net::Server) >= 2.007
Requires:       perl(Plack) >= 0.9971
Requires:       perl(Test::TCP) >= 2.00
Requires:       perl(parent)
%{perl_requires}

%description
Starman is a PSGI perl web server that has unique features such as:

* High Performance

Uses the fast XS/C HTTP header parser

* Preforking

Spawns workers preforked like most high performance UNIX servers do.
Starman also reaps dead children and automatically restarts the worker
pool.

* Signals

Supports 'HUP' for graceful worker restarts, and 'TTIN'/'TTOU' to
dynamically increase or decrease the number of worker processes, as well as
'QUIT' to gracefully shutdown the worker processes.

* Superdaemon aware

Supports Server::Starter for hot deploy and graceful restarts.

* Multiple interfaces and UNIX Domain Socket support

Able to listen on multiple interfaces including UNIX sockets.

* Small memory footprint

Preloading the applications with '--preload-app' command line option
enables copy-on-write friendly memory management. Also, the minimum memory
usage Starman requires for the master process is 7MB and children (workers)
is less than 3.0MB.

* PSGI compatible

Can run any PSGI applications and frameworks

* HTTP/1.1 support

Supports chunked requests and responses, keep-alive and pipeline requests.

* UNIX only

This server does not support Win32.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README script
%license LICENSE

%changelog
