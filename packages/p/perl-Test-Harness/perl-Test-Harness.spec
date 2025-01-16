#
# spec file for package perl-Test-Harness
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


%define cpan_name Test-Harness
Name:           perl-Test-Harness
Version:        3.50
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Run Perl standard test scripts with statistics
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Although, for historical reasons, the Test::Harness distribution takes its
name from this module it now exists only to provide TAP::Harness with an
interface that is somewhat backwards compatible with Test::Harness 2.xx. If
you're writing new code consider using TAP::Harness directly instead.

Emulation is provided for 'runtests' and 'execute_tests' but the pluggable
'Straps' interface that previous versions of Test::Harness supported is not
reproduced here. Straps is now available as a stand alone module:
Test::Harness::Straps.

See TAP::Parser, TAP::Harness for the main documentation for this
distribution.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
chmod a+x t/source_tests/source.sh t/source_tests/source_args.sh
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
mv %buildroot/usr/bin/prove %buildroot/usr/bin/prove-cpan
mv %buildroot/usr/share/man/man1/prove.1 %buildroot/usr/share/man/man1/prove-cpan.1
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Changes-2.64 examples MANIFEST.CUMMULATIVE README

%changelog
