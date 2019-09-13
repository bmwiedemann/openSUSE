#
# spec file for package perl-Net-DBus
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-DBus
Version:        1.1.0
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name Net-DBus
Summary:        Perl extension for the DBus message system
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-DBus/
Source0:        http://www.cpan.org/authors/id/D/DA/DANBERR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::Twig)
Requires:       perl(Test::CPAN::Changes)
Requires:       perl(Test::Pod)
Requires:       perl(Test::Pod::Coverage)
Requires:       perl(XML::Twig)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  dbus-1-devel
BuildRequires:  pkg-config
# MANUAL END

%description
Net::DBus provides a Perl API for the DBus message system. The DBus Perl
interface is currently operating against the 0.32 development version of
DBus, but should work with later versions too, providing the API changes
have not been too drastic.

Users of this package are either typically, service providers in which case
the the Net::DBus::Service manpage and the Net::DBus::Object manpage
modules are of most relevance, or are client consumers, in which case the
Net::DBus::RemoteService manpage and the Net::DBus::RemoteObject manpage
are of most relevance.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS Changes examples LICENSE README

%changelog
