#
# spec file for package perl-Stream-Buffered
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Stream-Buffered
Name:           perl-Stream-Buffered
Version:        0.30.0
Release:        0
# 0.03 -> normalize -> 0.30.0
%define cpan_version 0.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Temporary buffer to save bytes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::File) >= 1.14
Requires:       perl(IO::File) >= 1.14
Provides:       perl(Stream::Buffered) = %{version}
Provides:       perl(Stream::Buffered::Auto)
Provides:       perl(Stream::Buffered::File)
Provides:       perl(Stream::Buffered::PerlIO)
%undefine       __perllib_provides
%{perl_requires}

%description
Stream::Buffered is a buffer class to store arbitrary length of byte
strings and then get a seekable filehandle once everything is buffered. It
uses PerlIO and/or temporary file to save the buffer depending on the
length of the size.

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
%doc Changes README
%license LICENSE

%changelog
