#
# spec file for package perl-XML-XSLT
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


Name:           perl-XML-XSLT
BuildRequires:  perl-XML-DOM perl-XML-Parser perl-libwww-perl
BuildRequires:  perl-macros
Version:        0.48
Release:        180
Requires:       perl-XML-Parser perl-XML-DOM perl-libwww-perl perl-URI perl-XML-RegExp
AutoReqProv:    on
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Url:            http://cpan.org/modules/by-module/XML/
Summary:        Perl module XML::XSLT
Source:         XML-XSLT-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
This is a Perl module to parse XSL Transformational sheets.



Authors:
--------
    Geert Josten <gjosten@sci.kun.nl>
    Egon Willighagen <egonw@sci.kun.nl>

%prep
%setup -n XML-XSLT-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}
make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist
chmod 755 examples
chmod 644 README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc ChangeLog README examples
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/*
%{perl_vendorarch}/auto/XML/XSLT/
%{_bindir}/*

%changelog
