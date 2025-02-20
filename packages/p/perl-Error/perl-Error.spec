#
# spec file for package perl-Error
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


%define cpan_name Error
Name:           perl-Error
Version:        0.170.300
Release:        0
# 0.17030 -> normalize -> 0.170.300
%define cpan_version 0.17030
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Error/exception handling in an OO-ish way
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(Test::More) >= 0.88
Provides:       perl(Error) = %{version}
Provides:       perl(Error::Simple) = %{version}
Provides:       perl(Error::WarnDie) = %{version}
Provides:       perl(Error::subs) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The 'Error' package provides two interfaces. Firstly 'Error' provides a
procedural interface to exception handling. Secondly 'Error' is a base
class for errors/exceptions that can either be thrown, for subsequent
catch, or can simply be recorded.

Errors in the class 'Error' should not be thrown directly, but the user
should throw errors from a sub-class of 'Error'.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog Changes examples README
%license LICENSE

%changelog
