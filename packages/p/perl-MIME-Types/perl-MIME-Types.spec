#
# spec file for package perl-MIME-Types
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        2.300.0
Release:        0
# 2.30 -> normalize -> 2.300.0
%define cpan_version 2.30
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Definition of MIME types
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1
Provides:       perl(MIME::Type) = %{version}
Provides:       perl(MIME::Types) = %{version}
Provides:       perl(MojoX::MIME::Types) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
"MIME Type" is the old name for "Media Type". This module dates from 1999,
and name changes are painful, so we stuck with the original name.

Media types are used in many applications (for instance as part of e-mail
and HTTP traffic) to indicate the type of content which is transmitted. or
expected. Read at https://www.rfc-editor.org/rfc/rfc6838 (registrations)
and at https://www.rfc-editor.org/rfc/rfc9694 (top-levels) for the
specification.

Sometimes detailed knowledge about a mime-type is need, however this module
only knows about the file-name extensions which relate to some filetype. It
can also be used to produce the right format: types which are not
registered at IANA need to use 'x-' prefixes.

This object administers a huge list of known mime-types, combined from
various sources. For instance, it contains *all IANA* types and the
knowledge of Apache. Probably the most complete table on the net!

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc ChangeLog README.md

%changelog
