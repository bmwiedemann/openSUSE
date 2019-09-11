#
# spec file for package perl-Mojolicious-Plugin-CHI
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Mojolicious-Plugin-CHI
Version:        0.20
Release:        0
%define cpan_name Mojolicious-Plugin-CHI
Summary:        Use CHI Caches in Mojolicious
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKRON/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CHI) >= 0.58
BuildRequires:  perl(Digest::JHash) >= 0.05
BuildRequires:  perl(Mojolicious) >= 4.77
BuildRequires:  perl(Test::Memory::Cycle) >= 1.06
BuildRequires:  perl(Test::Output) >= 1
Requires:       perl(CHI) >= 0.58
Requires:       perl(Digest::JHash) >= 0.05
Requires:       perl(Mojolicious) >= 4.77
%{perl_requires}

%description
Mojolicious::Plugin::CHI is a simple plugin to work with CHI caches within
Mojolicious.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes
%license LICENSE

%changelog
