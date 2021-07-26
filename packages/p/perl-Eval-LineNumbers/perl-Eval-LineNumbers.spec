#
# spec file for package perl-Eval-LineNumbers
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Eval-LineNumbers
Name:           perl-Eval-LineNumbers
Version:        0.35
Release:        0
#Upstream: LGPL-2.1-or-later
Summary:        Add line numbers to heredoc blocks that contain perl source code
License:        Artistic-2.0 OR LGPL-2.1-only
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.98
%{perl_requires}

%description
Add a '#line "this-file" 392' comment to heredoc/hereis text that is going
to be eval'ed so that error messages will point back to the right place.

Please note: when you embed '\n' in your code, it gets expanded in
double-quote hereis documents so it will mess up your line numbering. Use
'\\n' instead when you can.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc author.yml Changes README
%license LICENSE

%changelog
