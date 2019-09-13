#
# spec file for package perl-HTTP-Negotiate
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-HTTP-Negotiate
Version:        6.01
Release:        0
%define cpan_name HTTP-Negotiate
Summary:        choose a variant to serve
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTTP-Negotiate/
Source:         http://www.cpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Headers) >= 6
#BuildRequires: perl(HTTP::Negotiate)
#BuildRequires: perl(HTTP::Request)
Requires:       perl(HTTP::Headers) >= 6
%{perl_requires}

%description
This module provides a complete implementation of the HTTP content
negotiation algorithm specified in _draft-ietf-http-v11-spec-00.ps_ chapter
12. Content negotiation allows for the selection of a preferred content
representation based upon attributes of the negotiable variants and the
value of the various Accept* header fields in the request.

The variants are ordered by preference by calling the function choose().

The first parameter is reference to an array of the variants to choose
among. Each element in this array is an array with the values [$id, $qs,
$content_type, $content_encoding, $charset, $content_language,
$content_length] whose meanings are described below. The $content_encoding
and $content_language can be either a single scalar value or an array
reference if there are several values.

The second optional parameter is either a HTTP::Headers or a HTTP::Request
object which is searched for "Accept*" headers. If this parameter is
missing, then the accept specification is initialized from the CGI
environment variables HTTP_ACCEPT, HTTP_ACCEPT_CHARSET,
HTTP_ACCEPT_ENCODING and HTTP_ACCEPT_LANGUAGE.

In an array context, choose() returns a list of [variant identifier,
calculated quality, size] tuples. The values are sorted by quality, highest
quality first. If the calculated quality is the same for two variants, then
they are sorted by size (smallest first). _E.g._:

  (['var1', 1, 2000], ['var2', 0.3, 512], ['var3', 0.3, 1024]);

Note that also zero quality variants are included in the return list even
if these should never be served to the client.

In a scalar context, it returns the identifier of the variant with the
highest score or 'undef' if none have non-zero quality.

If the $HTTP::Negotiate::DEBUG variable is set to TRUE, then a lot of noise
is generated on STDOUT during evaluation of choose().

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
%doc Changes README

%changelog
