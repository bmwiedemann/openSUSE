#
# spec file for package perl-Net-Ident
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Net-Ident
Name:           perl-Net-Ident
Version:        1.310.0
Release:        0
# 1.31 -> normalize -> 1.310.0
%define cpan_version 1.31
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Lookup the username on the remote end of a TCP/IP connection
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Net::Ident) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
You can either use the simple interface, which does one ident lookup at a
time, or use the asynchronous interface to perform (possibly) many
simultaneous lookups, or simply continue serving other things while the
lookup is proceeding.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc AI_POLICY.md Changes README.md

%changelog
