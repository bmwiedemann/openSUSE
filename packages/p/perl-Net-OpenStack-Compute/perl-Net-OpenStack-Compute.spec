#
# spec file for package perl-Net-OpenStack-Compute
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Net-OpenStack-Compute
Version:        1.1200
Release:        0
%define cpan_name Net-OpenStack-Compute
Summary:        Bindings for the OpenStack Compute API
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-OpenStack-Compute/
Source:         http://www.cpan.org/authors/id/I/IR/IRONCAMEL/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Rad)
BuildRequires:  perl(App::Rad::Plugin::MoreHelp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::Most)
#BuildRequires: perl(Moose::Role)
#BuildRequires: perl(Net::OpenStack::Compute)
#BuildRequires: perl(Net::OpenStack::Compute::AuthRole)
Requires:       perl(App::Rad)
Requires:       perl(App::Rad::Plugin::MoreHelp)
Requires:       perl(HTTP::Request)
Requires:       perl(JSON)
Requires:       perl(LWP)
Requires:       perl(Moose)
Requires:       perl(Test::Most)
%{perl_requires}

%description
This class is an interface to the OpenStack Compute API. Also see the the
oscompute manpage command line tool.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc CHANGES LICENSE README

%changelog
