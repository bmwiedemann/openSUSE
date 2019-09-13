#
# spec file for package perl-POSIX-strftime-Compiler
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-POSIX-strftime-Compiler
Version:        0.41
Release:        0
%define cpan_name POSIX-strftime-Compiler
Summary:        GNU C library compatible strftime for loggers and servers
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/POSIX-strftime-Compiler/
Source:         http://www.cpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Test::More) >= 0.98
%{perl_requires}
# MANUAL
BuildRequires:  timezone

%description
POSIX::strftime::Compiler provides GNU C library compatible strftime(3).
But this module will not affected by the system locale. This feature is
useful when you want to write loggers, servers and portable applications.

For generate same result strings on any locale, POSIX::strftime::Compiler
wraps POSIX::strftime and converts some format characters to perl code

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes cpanfile LICENSE minil.toml README.md

%changelog
