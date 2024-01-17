#
# spec file for package perl-Authen-SASL-Cyrus
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Authen-SASL-Cyrus
BuildRequires:  cyrus-sasl-devel
BuildRequires:  perl-Authen-SASL
BuildRequires:  perl-macros
Version:        0.13
Release:        0
Requires:       perl-Authen-SASL
Url:            http://www.cpan.org/modules/by-module/Authen/
Summary:        SASL Authentication Framework - Cyrus Plugin
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Source0:        http://www.cpan.org/modules/by-module/Authen/Authen-SASL-Cyrus-%{version}.tar.gz
Patch0:         Authen-SASL-Cyrus-0.12.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
SASL is a generic mechanism for authentication used by several network
protocols.

Authen::SASL::Cyrus is a plug-in for the Authen::SASL module and
provides an implementation framework that all protocols should be able
to share.

The XS framework makes calls to the existing libsasl.so shared library
to perform SASL client connection functionality, including loading
existing shared library mechanisms.

%prep
%setup -n Authen-SASL-Cyrus-%{version}
%patch0 -p0

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
make %{?_smp_mflags}
#make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%files
%defattr(-, root, root)
%doc CHANGES
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/Authen
%dir %{perl_vendorarch}/Authen/SASL
%{perl_vendorarch}/Authen/SASL/Cyrus*
%dir %{perl_vendorarch}/auto/Authen
%dir %{perl_vendorarch}/auto/Authen/SASL
%{perl_vendorarch}/auto/Authen/SASL/Cyrus*

%changelog
