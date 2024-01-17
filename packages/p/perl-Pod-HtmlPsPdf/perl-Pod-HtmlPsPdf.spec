#
# spec file for package perl-Pod-HtmlPsPdf (Version 0.04)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Pod-HtmlPsPdf
Version:        0.04
Release:        494
Requires:       html2ps
AutoReqProv:    on
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Url:            http://cpan.org/modules/by-module/Pod
Summary:        Perl module Pod::HtmlPsPdf
Source:         Pod-HtmlPsPdf-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Documentation projects builder in HTML, PS and PDF formats.



Authors:
--------
    Stas Bekman <stas@stason.org>

%prep
%setup -n Pod-HtmlPsPdf-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}
make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist
# move conflicting file
mv $RPM_BUILD_ROOT%{_bindir}/html2ps sample/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes TODO sample
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Pod
%{perl_vendorarch}/auto/Pod
%{_bindir}/*

%changelog
