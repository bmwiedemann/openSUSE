#
# spec file for package perl-Compress-Raw-Lzma
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Compress-Raw-Lzma
Name:           perl-Compress-Raw-Lzma
Version:        2.204
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Low-Level Interface to lzma compression library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  xz
BuildRequires:  xz-devel
# MANUAL END

%description
'Compress::Raw::Lzma' provides an interface to the in-memory
compression/uncompression functions from the lzma compression library.

Although the primary purpose for the existence of 'Compress::Raw::Lzma' is
for use by the 'IO::Compress::Lzma', 'IO::Uncompress::UnLzma',
'IO::Compress::Xz' and 'IO::Uncompress::UnXz' modules, it can be used on
its own for simple compression/uncompression tasks.

There are two functions, called 'code' and 'flush', used in all the
compression and uncompression interfaces defined in this module. By default
both of these functions overwrites any data stored in its output buffer
parameter. If you want to compress/uncompress to a single buffer, and have
'code' and 'flush' append to that buffer, enable the 'AppendOutput' option
when you create the compression/decompression object.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README

%changelog
