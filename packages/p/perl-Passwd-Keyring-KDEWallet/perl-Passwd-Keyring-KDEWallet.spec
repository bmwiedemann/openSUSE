#
# spec file for package perl-Passwd-Keyring-KDEWallet
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


%define cpan_name Passwd-Keyring-KDEWallet
Name:           perl-Passwd-Keyring-KDEWallet
Version:        1.0001
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Password storage implementation based on KDE Wallet
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ME/MEKK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         0001-FIX-kwalletd6.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build) >= 0.360000
BuildRequires:  perl(Net::DBus)
BuildRequires:  perl(Pod::Markdown) >= 2.0
BuildRequires:  perl(Pod::Readme) >= 1.001002
BuildRequires:  perl(Proc::SyncExec) >= 1.01
BuildRequires:  perl(Test::Pod::Coverage) >= 1.0
BuildRequires:  perl(Try::Tiny)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Net::DBus)
Requires:       perl(Proc::SyncExec) >= 1.01
Requires:       perl(Try::Tiny)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(File::Which)
# MANUAL END

%description
Password storage implementation based on KDE Wallet.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes example README README.md

%changelog
