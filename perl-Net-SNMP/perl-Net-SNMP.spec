#
# spec file for package perl-Net-SNMP
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Net-SNMP
%define         cpan_name Net-SNMP
Summary:        Object oriented interface to SNMP
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Version:        6.0.1
Release:        0
Url:            http://search.cpan.org/dist/Net-SNMP/
#Source:         http://www.cpan.org/modules/by-module/Net/Net-SNMP-v%{version}.tar.gz
Source:         %{cpan_name}-v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
# MANUAL
BuildRequires:  netcfg
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::DES) >= 2.03
BuildRequires:  perl(Crypt::Rijndael) >= 1.02
BuildRequires:  perl(Digest::HMAC) >= 1.00
BuildRequires:  perl(Digest::MD5) >= 2.11
BuildRequires:  perl(Digest::SHA1) >= 1.02
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Socket6) >= 0.23
Requires:       perl(Carp)
Requires:       perl(Crypt::DES) >= 2.03
Requires:       perl(Crypt::Rijndael) >= 1.02
Requires:       perl(Digest::HMAC) >= 1.00
Requires:       perl(Digest::MD5) >= 2.11
Requires:       perl(Digest::SHA1) >= 1.02
Requires:       perl(Errno)
Requires:       perl(Exporter)
Requires:       perl(IO::Socket)
Requires:       perl(Socket6) >= 0.23

%description
The Net::SNMP module abstracts the intricate details of the Simple
Network Management Protocol by providing a high level programming
interface to the protocol. Each Net::SNMP object provides a one-to-one
mapping between a Perl object and a remote SNMP agent or manager. Once an
object is created, it can be used to perform the basic protocol exchange
actions defined by SNMP.

Authors:
--------
    David M. Town <dtown@fore.com>

%prep
%setup -q -n %{cpan_name}-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes LICENSE README examples

%changelog
