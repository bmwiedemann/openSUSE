#
# spec file for package perl-Compress-Bzip2
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Compress-Bzip2
Version:        2.27
Release:        0
%define cpan_name Compress-Bzip2
Summary:        Interface to Bzip2 compression library
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Compress::Raw::Bzip2) >= 2.060
Recommends:     perl(Compress::Zlib) >= 1.19
Recommends:     perl(IO::Compress::Bzip2) >= 2.060
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libbz2-devel
Requires:       bzip2
# MANUAL END

%description
The _Compress::Bzip2_ module provides a Perl interface to the *bzip2*
compression library (see AUTHOR for details about where to get _Bzip2_). A
relevant subset of the functionality provided by _bzip2_ is available in
_Compress::Bzip2_.

All string parameters can either be a scalar or a scalar reference.

The module can be split into two general areas of functionality, namely
in-memory compression/decompression and read/write access to _bzip2_ files.
Each of these areas will be discussed separately below.

*NOTE*

_Compress::Bzip2_ is just a simple _bzip2_ binding, comparable to the old
Compress::Zlib library. It is not well integrated into PerlIO, use the
preferred IO::Compress::Bzip2 instead.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ANNOUNCE Changes NEWS README.md
%license COPYING

%changelog
