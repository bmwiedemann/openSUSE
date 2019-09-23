#
# spec file for package perl-Net-Server
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


Name:           perl-Net-Server
Version:        2.009
Release:        0
%define cpan_name Net-Server
Summary:        Extensible, general Perl server engine
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-Server/
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README
%license LICENSE

%changelog
