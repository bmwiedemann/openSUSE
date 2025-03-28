#
# spec file for package perl-Future-IO
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


%define cpan_name Future-IO
Name:           perl-Future-IO
Version:        0.160.0
Release:        0
# 0.16 -> normalize -> 0.160.0
%define cpan_version 0.16
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Future-returning IO methods
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Future)
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Struct::Dumb)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::ExpectAndCheck) >= 0.60.0
BuildRequires:  perl(Test::Future::IO::Impl)
Requires:       perl(Future)
Requires:       perl(Struct::Dumb)
Provides:       perl(Future::IO) = %{version}
Provides:       perl(Future::IO::ImplBase) = %{version}
Provides:       perl(Future::IO::System) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This package provides a few basic methods that behave similarly to the
same-named core perl functions relating to IO operations, but yield their
results asynchronously via Future instances.

This is provided primarily as a decoupling mechanism, to allow modules to
be written that perform IO in an asynchronous manner to depend directly on
this, while allowing asynchronous event systems to provide an
implementation of these operations.

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
%doc Changes README
%license LICENSE

%changelog
