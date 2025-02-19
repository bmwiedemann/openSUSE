#
# spec file for package perl-CommonMark
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


%define cpan_name CommonMark
Name:           perl-CommonMark
Version:        0.310.100
Release:        0
# 0.310100 -> normalize -> 0.310.100
%define cpan_version 0.310100
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Interface to the CommonMark C library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::CheckLib)
Provides:       perl(CommonMark) = %{version}
Provides:       perl(CommonMark::Node)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  cmark-devel >= 0.28.3
Requires:       cmark >= 0.28.3
# MANUAL END

%description
This module is a wrapper around the official CommonMark C library at
https://github.com/commonmark/cmark/. It closely follows the original API.

The main module provides some entry points to parse documents and
convenience functions for node creation. The bulk of features is available
through CommonMark::Node objects of which the parse tree is made.
CommonMark::Iterator is a useful class to walk through the nodes in a tree.
CommonMark::Parser provides a push parser interface.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes
%license LICENSE

%changelog
