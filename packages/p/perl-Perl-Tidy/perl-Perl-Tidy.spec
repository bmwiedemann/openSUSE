#
# spec file for package perl-Perl-Tidy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Perl-Tidy
Version:        20190601
Release:        0
#Upstream: GPL-1.0-or-later
%define cpan_name Perl-Tidy
Summary:        Parses and beautifies perl source
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHANCOCK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc BUGS.md CHANGES.md docs examples pm2pl README.md
%license COPYING

%changelog
