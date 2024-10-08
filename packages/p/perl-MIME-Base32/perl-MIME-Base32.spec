#
# spec file for package perl-MIME-Base32
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name MIME-Base32
Name:           perl-MIME-Base32
Version:        1.303.0
Release:        0
# 1.303 -> normalize -> 1.303.0
%define cpan_version 1.303
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Base32 encoder and decoder
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.9
Provides:       perl(MIME::Base32) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is for encoding/decoding data much the way that MIME::Base64
does.

Prior to version 1.0, MIME::Base32 used the 'base32hex' (or '[0-9A-V]')
encoding and decoding methods by default. If you need to maintain that
behavior, please call 'encode_base32hex' or 'decode_base32hex' functions
directly.

Now, in accordance with at https://tools.ietf.org/html/rfc3548#section-5,
MIME::Base32 uses the 'encode_base32' and 'decode_base32' functions by
default.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes README.md
%license ARTISTIC-1.0 GPL-1 LICENSE

%changelog
