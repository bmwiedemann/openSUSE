#
# spec file for package perl-Devel-TakeHashArgs
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


%define cpan_name Devel-TakeHashArgs
Name:           perl-Devel-TakeHashArgs
Version:        0.6.0
Release:        0
# 0.006 -> normalize -> 0.6.0
%define cpan_version 0.006
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Make a hash from @_ and set defaults in subs while checking that all man[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
Provides:       perl(Devel::TakeHashArgs) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The module is a short utility I made after being sick and tired of writing
redundant code to make a hash out of args when they are passed as key/value
pairs including setting their defaults and checking for mandatory
arguments.

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
%doc Changes examples README
%license LICENSE

%changelog
