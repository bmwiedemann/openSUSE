#
# spec file for package perl-IO-Compress
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


%define cpan_name IO-Compress
Name:           perl-IO-Compress
Version:        2.213.0
Release:        0
# 2.213 -> normalize -> 2.213.0
%define cpan_version 2.213
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        IO Interface to compressed data files/buffers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Bzip2) >= 2.213
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.213
Requires:       perl(Compress::Raw::Bzip2) >= 2.213
Requires:       perl(Compress::Raw::Zlib) >= 2.213
Provides:       perl(Compress::Zlib) = 2.213
Provides:       perl(File::GlobMapper) = 1.001
Provides:       perl(IO::Compress) = %{version}
Provides:       perl(IO::Compress::Adapter::Bzip2) = 2.213
Provides:       perl(IO::Compress::Adapter::Deflate) = 2.213
Provides:       perl(IO::Compress::Adapter::Identity) = 2.213
Provides:       perl(IO::Compress::Base) = 2.213
Provides:       perl(IO::Compress::Base::Common) = 2.213
Provides:       perl(IO::Compress::Bzip2) = 2.213
Provides:       perl(IO::Compress::Deflate) = 2.213
Provides:       perl(IO::Compress::Gzip) = 2.213
Provides:       perl(IO::Compress::Gzip::Constants) = 2.213
Provides:       perl(IO::Compress::RawDeflate) = 2.213
Provides:       perl(IO::Compress::Zip) = 2.213
Provides:       perl(IO::Compress::Zip::Constants) = 2.213
Provides:       perl(IO::Compress::Zlib::Constants) = 2.213
Provides:       perl(IO::Compress::Zlib::Extra) = 2.213
Provides:       perl(IO::Uncompress::Adapter::Bunzip2) = 2.213
Provides:       perl(IO::Uncompress::Adapter::Identity) = 2.213
Provides:       perl(IO::Uncompress::Adapter::Inflate) = 2.213
Provides:       perl(IO::Uncompress::AnyInflate) = 2.213
Provides:       perl(IO::Uncompress::AnyUncompress) = 2.213
Provides:       perl(IO::Uncompress::Base) = 2.213
Provides:       perl(IO::Uncompress::Bunzip2) = 2.213
Provides:       perl(IO::Uncompress::Gunzip) = 2.213
Provides:       perl(IO::Uncompress::Inflate) = 2.213
Provides:       perl(IO::Uncompress::RawInflate) = 2.213
Provides:       perl(IO::Uncompress::Unzip) = 2.213
Provides:       perl(U64)
Provides:       perl(Zlib::OldDeflate)
Provides:       perl(Zlib::OldInflate)
%undefine       __perllib_provides
%{perl_requires}

%description
This is a stub module. It contains no code.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
# Avoid file conflicts with perl core
mv %{buildroot}/usr/bin/streamzip %{buildroot}/usr/bin/streamzip-%{version}
mv %{buildroot}/usr/bin/zipdetails %{buildroot}/usr/bin/zipdetails-%{version}
mv %{buildroot}/usr/share/man/man1/streamzip.1 %{buildroot}/usr/share/man/man1/streamzip-%{version}.1
mv %{buildroot}/usr/share/man/man1/zipdetails.1 %{buildroot}/usr/share/man/man1/zipdetails-%{version}.1
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README

%changelog
