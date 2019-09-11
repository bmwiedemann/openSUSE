#
# spec file for package perl-Unicode-Map8
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Unicode-Map8
Version:        0.13
Release:        0
%define cpan_name Unicode-Map8
Summary:        Mapping table between 8-bit chars and Unicode
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Unicode-Map8/
Source:         http://www.cpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Unicode::String) >= 2
Requires:       perl(Unicode::String) >= 2
%{perl_requires}
# MANUAL BEGIN
Patch0:         Unicode-Map8-%{version}-type.diff
Patch1:         Unicode-Map8-%{version}-declaration.diff
# MANUAL END

%description
The Unicode::Map8 class implements efficient mapping tables between
8-bit character sets and 16-bit character sets like Unicode. The tables
are efficient both in terms of space allocated and translation speed.
The 16-bit strings are assumed to use network byte order.

%prep
%setup -n Unicode-Map8-%{version}
%patch0
%patch1

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
%doc Changes diff_iso make_rfc1345_maps make_unicd_maps map8_bin2txt map8_txt2bin README rfc1345.txt umap

%changelog
