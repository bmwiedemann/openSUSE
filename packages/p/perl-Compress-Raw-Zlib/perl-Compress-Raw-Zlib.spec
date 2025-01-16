#
# spec file for package perl-Compress-Raw-Zlib
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


%define cpan_name Compress-Raw-Zlib
Name:           perl-Compress-Raw-Zlib
Version:        2.213
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND Zlib
Summary:        Perl interface to zlib/zlib-ng compression libraries
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The _Compress::Raw::Zlib_ module provides a Perl interface to the _zlib_ or
_zlib-ng_ compression libraries (see SEE ALSO for details about where to
get _zlib_ or _zlib-ng_).

In the text below all references to _zlib_ are also applicable to _zlib-ng_
unless otherwise stated.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes examples README

%changelog
