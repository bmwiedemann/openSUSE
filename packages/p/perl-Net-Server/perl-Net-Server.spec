#
# spec file for package perl-Net-Server
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Net-Server
Name:           perl-Net-Server
Version:        2.013
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Extensible Perl internet server
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'Net::Server' is an extensible, generic Perl server engine.

'Net::Server' attempts to be a generic server as in 'Net::Daemon' and
'NetServer::Generic'. It includes with it the ability to run as an inetd
process ('Net::Server::INET'), a single connection server ('Net::Server' or
'Net::Server::Single'), a forking server ('Net::Server::Fork'), a
preforking server which maintains a constant number of preforked children
('Net::Server::PreForkSimple'), or as a managed preforking server which
maintains the number of children based on server load
('Net::Server::PreFork'). In all but the inetd type, the server provides
the ability to connect to one or to multiple server ports.

The additional server types are made possible via "personalities" or sub
classes of the 'Net::Server'. By moving the multiple types of servers out
of the main 'Net::Server' class, the 'Net::Server' concept is easily
extended to other types (in the near future, we would like to add a
"Thread" personality).

'Net::Server' borrows several concepts from the Apache Webserver.
'Net::Server' uses "hooks" to allow custom servers such as SMTP, HTTP,
POP3, etc. to be layered over the base 'Net::Server' class. In addition the
'Net::Server::PreFork' class borrows concepts of min_start_servers,
max_servers, and min_waiting servers. 'Net::Server::PreFork' also uses the
concept of an flock serialized accept when accepting on multiple ports
(PreFork can choose between flock, IPC::Semaphore, and pipe to control
serialization).

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
%doc Changes examples README
%license LICENSE

%changelog
