#
# spec file for package perl-Perl-Tidy
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


%define cpan_name Perl-Tidy
Name:           perl-Perl-Tidy
Version:        20250616.0.0
Release:        0
# 20250616 -> normalize -> 20250616.0.0
%define cpan_version 20250616
#Upstream: GPL-1.0-or-later
License:        GPL-2.0-or-later
Summary:        Indent and reformat perl scripts
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHANCOCK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Perl::Tidy) = %{version}
Provides:       perl(Perl::Tidy::Debugger) = %{version}
Provides:       perl(Perl::Tidy::Diagnostics) = %{version}
Provides:       perl(Perl::Tidy::FileWriter) = %{version}
Provides:       perl(Perl::Tidy::Formatter) = %{version}
Provides:       perl(Perl::Tidy::HtmlWriter) = %{version}
Provides:       perl(Perl::Tidy::IOScalar) = %{version}
Provides:       perl(Perl::Tidy::IOScalarArray) = %{version}
Provides:       perl(Perl::Tidy::IndentationItem) = %{version}
Provides:       perl(Perl::Tidy::Logger) = %{version}
Provides:       perl(Perl::Tidy::Tokenizer) = %{version}
Provides:       perl(Perl::Tidy::VerticalAligner) = %{version}
Provides:       perl(Perl::Tidy::VerticalAligner::Alignment) = %{version}
Provides:       perl(Perl::Tidy::VerticalAligner::Line) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module makes the functionality of the perltidy utility available to
perl scripts. Any or all of the input parameters may be omitted, in which
case the @ARGV array will be used to provide input parameters as described
in the perltidy(1) man page.

For example, the perltidy script is basically just this:

    use Perl::Tidy;
    Perl::Tidy::perltidy();

The call to *perltidy* returns a scalar *$error_flag* which is TRUE if an
error caused premature termination, and FALSE if the process ran to normal
completion. Additional discuss of errors is contained below in the ERROR
HANDLING section.

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
%doc BUGS.md CHANGES.md docs examples pm2pl README.md
%license COPYING

%changelog
