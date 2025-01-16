#
# spec file for package perl-Compress-Raw-Bzip2
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


%define cpan_name Compress-Raw-Bzip2
Name:           perl-Compress-Raw-Bzip2
Version:        2.213
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND BSD-3-Clause
Summary:        Low-Level Interface to bzip2 compression library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'Compress::Raw::Bzip2' provides an interface to the in-memory
compression/uncompression functions from the bzip2 compression library.

Although the primary purpose for the existence of 'Compress::Raw::Bzip2' is
for use by the 'IO::Compress::Bzip2' and 'IO::Compress::Bunzip2' modules,
it can be used on its own for simple compression/uncompression tasks.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
