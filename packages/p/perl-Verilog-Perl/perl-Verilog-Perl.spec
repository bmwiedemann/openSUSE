#
# spec file for package perl-Verilog-Perl
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Verilog-Perl
Name:           perl-Verilog-Perl
Version:        3.480
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Verilog language utilities and parsing
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/W/WS/WSNYDER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Pod::Usage) >= 1.34
Requires:       perl(Pod::Usage) >= 1.34
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
# MANUAL END

%description
Verilog language utilities and parsing

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
%doc Changes README vhier vpassert vppreproc vrename vsplitmodule
%license COPYING

%changelog
