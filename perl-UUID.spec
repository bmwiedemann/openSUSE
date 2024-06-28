#
# spec file for package perl-UUID
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


%define cpan_name UUID
Name:           perl-UUID
Version:        0.360.0
Release:        0
# 0.36 -> normalize -> 0.360.0
%define cpan_version 0.36
License:        Artistic-2.0
Summary:        Universally Unique Identifier library for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Devel::CheckLib) >= 1.14
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.06
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version) >= 0.77
Provides:       perl(UUID) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libuuid-devel
# MANUAL END

%description
The UUID library is used to generate unique identifiers for objects that
may be accessible beyond the local system. For instance, they could be used
to generate unique HTTP cookies across multiple web servers without
communication between the servers, and without fear of a name clash.

The generated UUIDs can be reasonably expected to be unique within a
system, and unique across all systems, and are compatible with those
created by the Open Software Foundation (OSF) Distributed Computing
Environment (DCE).

All generated UUIDs are either version 1, 3, 4, 5, 6, or version 7. And all
are variant 1, meaning compliant with the OSF DCE standard as described in
RFC4122.

Versions 6 and 7 are not standardized. They are presented here as proposed
in RFC4122bis, version 14, and may change in the future. RFC4122bis is
noted to replace RFC4122, if approved.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes NOTES README
%license LICENSE

%changelog
