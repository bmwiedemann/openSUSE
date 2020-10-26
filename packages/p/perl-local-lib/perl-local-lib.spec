#
# spec file for package perl-local-lib
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


Name:           perl-local-lib
Version:        2.000024
Release:        0
%define cpan_name local-lib
Summary:        Create and use a local lib/ for perl modules with PERL5LIB
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        perl-homedir.sh
Source2:        perl-homedir.csh
Source3:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN) >= 1.82
BuildRequires:  perl(ExtUtils::Install) >= 1.43
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.00
BuildRequires:  perl(Module::Build) >= 0.360000
Requires:       perl(CPAN) >= 1.82
Requires:       perl(ExtUtils::Install) >= 1.43
Requires:       perl(ExtUtils::MakeMaker) >= 7.00
Requires:       perl(Module::Build) >= 0.360000
%{perl_requires}

%description
This module provides a quick, convenient way of bootstrapping a user-local
Perl module library located within the user's home directory. It also
constructs and prints out for the user the list of environment variables
using the syntax appropriate for the user's current shell (as specified by
the 'SHELL' environment variable), suitable for directly adding to one's
shell configuration file.

More generally, local::lib allows for the bootstrapping and usage of a
directory containing Perl modules outside of Perl's '@INC'. This makes it
easier to ship an application with an app-specific copy of a Perl module,
or collection of modules. Useful in cases like when an upstream maintainer
hasn't applied a patch to a module of theirs that you need for your
application.

On import, local::lib sets the following environment variables to
appropriate values:

* PERL_MB_OPT

* PERL_MM_OPT

* PERL5LIB

* PATH

* PERL_LOCAL_LIB_ROOT

When possible, these will be appended to instead of overwritten entirely.

These values are then available for reference by any code after import.

%package -n perl-homedir
Summary:        Per-user Perl local::lib setup
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}-%{release}
Requires:       /usr/bin/cpan

%description -n perl-homedir
perl-homedir configures the system to automatically create a ~/perl5
directory in each user's $HOME on user login.  This allows each user to
install and CPAN packages via the CPAN to their $HOME, with no additional
configuration or privliges, and without installing them system-wide.

If you want your users to be able to install and use their own Perl modules,
install this package.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
%__install -d "%{buildroot}%{_sysconfdir}/profile.d"
%__install -m0644 "%{SOURCE1}" "%{SOURCE2}" "%{buildroot}%{_sysconfdir}/profile.d/"
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%files -n perl-homedir
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/profile.d/*

%changelog
