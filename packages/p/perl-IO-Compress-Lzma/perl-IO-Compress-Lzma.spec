#
# spec file for package perl-IO-Compress-Lzma
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


Name:           perl-IO-Compress-Lzma
Version:        2.093
Release:        0
%define cpan_name IO-Compress-Lzma
Summary:        Write lzma files/buffers
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Lzma) >= 2.093
BuildRequires:  perl(IO::Compress::Base) >= 2.093
BuildRequires:  perl(IO::Uncompress::Base) >= 2.093
Requires:       perl(Compress::Raw::Lzma) >= 2.093
Requires:       perl(IO::Compress::Base) >= 2.093
Requires:       perl(IO::Uncompress::Base) >= 2.093
%{perl_requires}

%description
This module provides a Perl interface that allows writing lzma compressed
data to files or buffer.

For reading lzma files/buffers, see the companion module
IO::Uncompress::UnLzma.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README

%changelog
