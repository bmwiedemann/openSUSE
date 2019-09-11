#
# spec file for package perl-Text-CharWidth
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-Text-CharWidth
License:        Artistic-1.0
Group:          System/I18n/Japanese
AutoReqProv:    on
Summary:        Get number of occupied columns of a string on terminal
Version:        0.04
Release:        83
Url:            http://search.cpan.org/~kubota/Text-CharWidth-0.04/CharWidth.pm
Source0:        http://search.cpan.org/CPAN/authors/id/K/KU/KUBOTA/Text-CharWidth-0.04.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Get number of occupied columns of a string on terminal



Authors:
--------
    &#20037;&#20445;&#30000; &#26234;&#24195; (Tomohiro KUBOTA) <kubota@debian.org>

%prep
%setup -n Text-CharWidth-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%{perl_vendorlib}/*/Text/
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/CharWidth
%{_mandir}/man?/*
%doc Changes README

%changelog
