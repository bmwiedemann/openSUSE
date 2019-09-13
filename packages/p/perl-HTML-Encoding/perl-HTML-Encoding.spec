#
# spec file for package perl-HTML-Encoding
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


Name:           perl-HTML-Encoding
Version:        0.61
Release:        0
Summary:        Determine the encoding of HTML/XML/XHTML documents
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Encoding/
Source0:        http://www.cpan.org/authors/id/B/BJ/BJOERN/HTML-Encoding-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-HTML-Parser
BuildRequires:  perl-libwww-perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
HTML::Encoding helps to determine the encoding of HTML and XML/XHTML
documents.

%prep
%setup -q -n HTML-Encoding-%{version}
find . -type f | xargs chmod -c -x
find . -type f | xargs %{__perl} -pi -e 's/\r//g'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(- ,root, root)
%doc Changes README
%dir %{perl_vendorlib}/HTML
%{perl_vendorlib}/HTML/Encoding.pm
%dir %{perl_vendorarch}/auto/HTML
%{perl_vendorarch}/auto/HTML/Encoding
%{_mandir}/man3/HTML::Encoding*.gz

%changelog
