#
# spec file for package perl-PerlIO-gzip
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-PerlIO-gzip
Version:        0.20
Release:        0
%define cpan_name PerlIO-gzip
Summary:        Perl extension to provide a PerlIO layer to gzip/gunzip
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/PerlIO-gzip/
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  zlib-devel
# MANUAL END

%description
PerlIO::gzip provides a PerlIO layer that manipulates files in the format
used by the 'gzip' program. Compression and Decompression are implemented,
but not together. If you attempt to open a file for reading and writing the
open will fail.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
