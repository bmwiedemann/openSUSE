#
# spec file for package perl-UUID
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


%define cpan_name UUID
Name:           perl-UUID
Version:        0.310.0
Release:        0
%define cpan_version 0.31
License:        Artistic-2.0
Summary:        DCE compatible Universally Unique Identifier library for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Devel::CheckLib) >= 1.14
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
Provides:       perl(UUID) = 0.310.0
%define         __perllib_provides /bin/true
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
Environment (DCE) utility uuidgen.

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
%doc Changes README
%license LICENSE

%changelog
