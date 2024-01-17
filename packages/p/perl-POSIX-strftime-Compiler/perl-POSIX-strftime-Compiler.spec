#
# spec file for package perl-POSIX-strftime-Compiler
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name POSIX-strftime-Compiler
Name:           perl-POSIX-strftime-Compiler
Version:        0.450.0
Release:        0
%define cpan_version 0.45
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        GNU C library compatible strftime for loggers and servers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Test::More) >= 0.98
Provides:       perl(POSIX::strftime::Compiler) = 0.450.0
%define         __perllib_provides /bin/true
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  timezone
# MANUAL END

%description
POSIX::strftime::Compiler provides GNU C library compatible strftime(3).
But this module will not affected by the system locale. This feature is
useful when you want to write loggers, servers and portable applications.

For generate same result strings on any locale, POSIX::strftime::Compiler
wraps POSIX::strftime and converts some format characters to perl code

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
