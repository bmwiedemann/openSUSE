#
# spec file for package perl-Passwd-Keyring-Gnome
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Passwd-Keyring-Gnome
Version:        1.0000
Release:        0
%define cpan_name Passwd-Keyring-Gnome
Summary:        Password storage implementation based on GNOME Keyring
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ME/MEKK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.120000
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build) >= 0.360000
BuildRequires:  perl(Pod::Markdown) >= 2.0
BuildRequires:  perl(Pod::Readme) >= 1.001002
BuildRequires:  perl(Test::Pod::Coverage) >= 1.0
Requires:       perl(File::ShareDir) >= 1.00
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libgnome-keyring-devel
# MANUAL END

%description
Password storage implementation based on GNOME Keyring.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes example README README.md

%changelog
