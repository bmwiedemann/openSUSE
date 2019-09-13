#
# spec file for package perl-Net-TFTP
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


Name:           perl-Net-TFTP
Version:        0.1901
Release:        0
%define cpan_name Net-TFTP
Summary:        TFTP Client class
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-TFTP/
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBARR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::MockModule) >= 0.11
BuildRequires:  perl(Test::More) >= 0.8701
BuildRequires:  perl(Test::Warn)
Requires:       perl(Test::MockModule) >= 0.11
Requires:       perl(Test::More) >= 0.8701
Requires:       perl(Test::Warn)
%{perl_requires}

%description
'Net::TFTP' is a class implementing a simple _Trivial File Transfer
Protocol_ client in Perl as described in RFC1350. 'Net::TFTP' also supports
the TFTP Option Extension (as described in RFC2347), with the following
options

 RFC2348 Blocksize Option

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc ChangeLog README

%changelog
