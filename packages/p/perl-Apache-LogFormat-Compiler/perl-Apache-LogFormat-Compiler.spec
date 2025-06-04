#
# spec file for package perl-Apache-LogFormat-Compiler
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


%define cpan_name Apache-LogFormat-Compiler
Name:           perl-Apache-LogFormat-Compiler
Version:        0.360.0
Release:        0
# 0.36 -> normalize -> 0.360.0
%define cpan_version 0.36
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Compile a log format string to perl-code
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.35
BuildRequires:  perl(POSIX::strftime::Compiler) >= 0.300
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny) >= 0.120
BuildRequires:  perl(URI::Escape) >= 1.600
Requires:       perl(POSIX::strftime::Compiler) >= 0.300
Provides:       perl(Apache::LogFormat::Compiler) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  timezone
# MANUAL END

%description
Compile a log format string to perl-code. For faster generation of
access_log lines.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
