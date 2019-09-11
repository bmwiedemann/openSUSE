#
# spec file for package perl-X500-DN
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


Name:           perl-X500-DN
BuildRequires:  perl-Parse-RecDescent
BuildRequires:  perl-macros
Requires:       perl-Parse-RecDescent
Summary:        Provides an interface for RFC 2253 style DN strings
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Version:        0.29
Release:        0
Url:            http://search.cpan.org/dist/X500-DN/
Source:         http://www.cpan.org/authors/id/R/RJ/RJOOP/X500-DN-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch1:         version-string-fix2.diff
%{perl_requires}
Patch:          version-string-fix.diff
Patch2:         X500-DN-dont_set_skip_to_undef.patch

%description
X500::DN Provides a pure perl parser and formatter for RFC 2253 style
DN strings.



Authors:
--------
    Robert Joop <yaph-020416@timesink.de>

%prep
%setup -n X500-DN-%{version}
%patch
%patch1
%patch2 -p1
# ---------------------------------------------------------------------------

%build
perl Makefile.PL
make %{?_smp_mflags}
# ---------------------------------------------------------------------------

%check
make test

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
make DESTDIR=$RPM_BUILD_ROOT \
	 INSTALLMAN3DIR=$RPM_BUILD_ROOT/%{_mandir}/man3 \
	 install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%{perl_vendorarch}/auto/X500
%dir %{perl_vendorlib}/X500
%{perl_vendorlib}/X500/RDN.pod
%{perl_vendorlib}/X500/RDN.pm
%{perl_vendorlib}/X500/DN.pod
%{perl_vendorlib}/X500/DN.pm
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*

%changelog
