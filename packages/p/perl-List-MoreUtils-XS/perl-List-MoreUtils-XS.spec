#
# spec file for package perl-List-MoreUtils-XS
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


Name:           perl-List-MoreUtils-XS
Version:        0.430
Release:        0
#Upstream: Apache-2.0
%define cpan_name List-MoreUtils-XS
Summary:        Provide compiled List::MoreUtils functions
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND Apache-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(XSLoader) >= 0.22
Requires:       perl(XSLoader) >= 0.22
%{perl_requires}

%description
List::MoreUtils::XS is a backend for List::MoreUtils. Even if it's possible
(because of user wishes) to have it practically independent from
List::MoreUtils, it technically depend on 'List::MoreUtils'. Since it's
only a backend, the API is not public and can change without any warning.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes GPL-1 MAINTAINER.md README.md
%license ARTISTIC-1.0 LICENSE

%changelog
