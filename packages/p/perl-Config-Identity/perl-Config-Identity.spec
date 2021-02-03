#
# spec file for package perl-Config-Identity
#
# Copyright (c) 2021 SUSE LLC
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


Name:           perl-Config-Identity
Version:        0.0019
Release:        0
%define cpan_name Config-Identity
Summary:        Load (and optionally decrypt via GnuPG) user/pass identity information
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Test::Deep)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Which)
Requires:       perl(IPC::Run)
%{perl_requires}

%description
Config::Identity is a tool for loading (and optionally decrypting via
GnuPG) user/pass identity information

For GitHub API access, an identity is a 'login'/'token' pair

For PAUSE access, an identity is a 'user'/'password' pair

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
