#
# spec file for package perl-URI
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name URI
Name:           perl-URI
Version:        5.09
Release:        0
Summary:        Uniform Resource Identifiers (absolute and relative)
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
This module implements the 'URI' class. Objects of this class represent
"Uniform Resource Identifier references" as specified in RFC 2396 (and
updated by RFC 2732).

A Uniform Resource Identifier is a compact string of characters that
identifies an abstract or physical resource. A Uniform Resource Identifier
can be further classified as either a Uniform Resource Locator (URL) or a
Uniform Resource Name (URN). The distinction between URL and URN does not
matter to the 'URI' class interface. A "URI-reference" is a URI that may
have additional information attached in the form of a fragment identifier.

An absolute URI reference consists of three parts: a _scheme_, a
_scheme-specific part_ and a _fragment_ identifier. A subset of URI
references share a common syntax for hierarchical namespaces. For these,
the scheme-specific part is further broken down into _authority_, _path_
and _query_ components. These URIs can also take the form of relative URI
references, where the scheme (and usually also the authority) component is
missing, but implied by the context of the URI reference. The three forms
of URI reference syntax are summarized as follows:

  <scheme>:<scheme-specific-part>#<fragment>
  <scheme>://<authority><path>?<query>#<fragment>
  <path>?<query>#<fragment>

The components into which a URI reference can be divided depend on the
_scheme_. The 'URI' class provides methods to get and set the individual
components. The methods available for a specific 'URI' object depend on the
scheme.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md README uri-test
%license LICENSE

%changelog
