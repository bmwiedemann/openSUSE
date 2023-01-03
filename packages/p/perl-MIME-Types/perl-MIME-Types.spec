#
# spec file for package perl-MIME-Types
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name MIME-Types
Name:           perl-MIME-Types
Version:        2.24
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Definition of MIME types
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
MIME types are used in many applications (for instance as part of e-mail
and HTTP traffic) to indicate the type of content which is transmitted. or
expected. See RFC2045 at _https://www.ietf.org/rfc/rfc2045.txt_

Sometimes detailed knowledge about a mime-type is need, however this module
only knows about the file-name extensions which relate to some filetype. It
can also be used to produce the right format: types which are not
registered at IANA need to use 'x-' prefixes.

This object administers a huge list of known mime-types, combined from
various sources. For instance, it contains *all IANA* types and the
knowledge of Apache. Probably the most complete table on the net!

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc ChangeLog README README.md

%changelog
