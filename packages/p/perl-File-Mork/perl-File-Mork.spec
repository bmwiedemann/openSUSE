#
# spec file for package perl-File-Mork
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


%define cpan_name File-Mork
Name:           perl-File-Mork
Version:        0.400.0
Release:        0
# 0.4 -> normalize -> 0.400.0
%define cpan_version 0.4
#Upstream: SUSE-Public-Domain
License:        MIT
Summary:        Module to read Mozilla URL history files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMONW/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Module::Build) >= 0.4
Requires:       perl(HTML::Entities)
Provides:       perl(File::Mork) = %{version}
Provides:       perl(File::Mork::Entry)
%undefine       __perllib_provides
%{perl_requires}

%description
This is a module that can read the Mozilla URL history file -- normally
$HOME/.mozilla/default/*.slt/history.dat -- and extract the id, url, name,
hostname, first visted dat, last visited date and visit count.

To find your history file it might be worth using *Mozilla::Backup* which
has some platform-independent code for finding the profiles of various
Mozilla-isms (including Firefox, Camino, K-Meleon, etc.).

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
%doc Changes examples

%changelog
