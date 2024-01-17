#
# spec file for package perl-Encode-EUCJPASCII
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Encode-EUCJPASCII
Version:        0.03
Release:        0
%define cpan_name Encode-EUCJPASCII
Summary:        An eucJP-open mapping
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Encode-EUCJPASCII/
Source:         http://www.cpan.org/authors/id/N/NE/NEZUMI/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides eucJP-ascii, one of eucJP-open mappings, and its
derivative. Following encodings are supported.

  Canonical    Alias                           Description
  --------------------------------------------------------------
  eucJP-ascii                                  eucJP-ascii
               qr/\beuc-?jp(-?open)?(-?19970715)?-?ascii$/i
  x-iso2022jp-ascii                            7-bit counterpart
               qr/\b(x-)?iso-?2022-?jp-?ascii$/i
  --------------------------------------------------------------

*Note*: 'x-iso2022jp-ascii' is unofficial encoding name: It had never been
registered by any standards bodies.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
