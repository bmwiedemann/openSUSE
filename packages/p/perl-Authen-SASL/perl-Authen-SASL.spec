#
# spec file for package perl-Authen-SASL
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


Name:           perl-Authen-SASL
Version:        2.16
Release:        0
%define cpan_name Authen-SASL
Summary:        SASL Authentication framework
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Authen-SASL/
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBARR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl526.path
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::HMAC_MD5)
Requires:       perl(Digest::HMAC_MD5)
Recommends:     perl(GSSAPI)
%{perl_requires}

%description
SASL is a generic mechanism for authentication used by several network
protocols. *Authen::SASL* provides an implementation framework that all
protocols should be able to share.

The framework allows different implementations of the connection class to
be plugged in. At the time of writing there were two such plugins.

* Authen::SASL::Perl

This module implements several mechanisms and is implemented entirely in
Perl.

* Authen::SASL::XS

This module uses the Cyrus SASL C-library (both version 1 and 2 are
supported).

* Authen::SASL::Cyrus

This module is the predecessor to Authen::SASL::XS. It is reccomended to
use Authen::SASL::XS

By default the order in which these plugins are selected is
Authen::SASL::XS, Authen::SASL::Cyrus and then Authen::SASL::Perl.

If you want to change it or want to specifically use one implementation
only simply do

 use Authen::SASL qw(Perl);

or if you have another plugin module that supports the Authen::SASL API

 use Authen::SASL qw(My::SASL::Plugin);

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

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
%doc api.txt Changes compat_pl example_pl

%changelog
