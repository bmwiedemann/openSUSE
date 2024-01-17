#
# spec file for package perl-Net-DBus
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


Name:           perl-Net-DBus
Version:        1.2.0
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
%define cpan_name Net-DBus
Summary:        Perl extension for the DBus message system
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANBERR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::Twig)
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
the Net::DBus::Service and Net::DBus::Object modules are of most relevance,
or are client consumers, in which case Net::DBus::RemoteService and
Net::DBus::RemoteObject are of most relevance.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS Changes examples README
%license LICENSE

%changelog
