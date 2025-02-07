#
# spec file for package perl-Convert-UUlib
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Convert-UUlib
Name:           perl-Convert-UUlib
Version:        1.800.0
Release:        0
# 1.8 -> normalize -> 1.800.0
%define cpan_version 1.8
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        GPL-1.0-or-later
Summary:        Decode uu/xx/b64/mime/yenc/etc-encoded data from a massive number of files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(common::sense) >= 3.740
Requires:       perl(common::sense) >= 3.740
Provides:       perl(Convert::UUlib) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
Provides:       p_conulb
Obsoletes:      p_conulb
# MANUAL END

%description
This module started as an interface to the uulib/uudeview library by Frank
Pilhofer that can be used to decode all kinds of usenet (and other) binary
messages.

After upstream abondoned the project, th library was continuously bugfixed
and improved in this module, with major focuses on security fixes,
correctness and speed (that does not mean that this library is considered
safe with untrusted data, but it surely is safer than the poriginal
uudeview).

Read the file doc/library.pdf from the distribution for in-depth
information about the C-library used in this interface, and the rest of
this document and especially the non-trivial decoder program at the end.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes doc example-decoder README
%license COPYING COPYING.Artistic COPYING.GNU

%changelog
