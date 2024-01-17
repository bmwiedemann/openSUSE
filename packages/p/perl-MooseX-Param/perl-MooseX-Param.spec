#
# spec file for package perl-MooseX-Param
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-MooseX-Param
Version:        0.02
Release:        0
%define cpan_name MooseX-Param
Summary:        Simple role to provide a standard param method
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Param/
Source:         http://www.cpan.org/authors/id/S/ST/STEVAN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose) >= 0.32
BuildRequires:  perl(Test::Exception) >= 0.21
#BuildRequires: perl(Moose::Role)
#BuildRequires: perl(MooseX::Param)
Requires:       perl(Moose) >= 0.32
%{perl_requires}

%description
This is a very simple Moose role which provides a the CGI manpage like
'param' method.

I found that I had written this code over and over and over and over again,
and each time it was the same. So I thought, why not put it in a role?

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog README

%changelog
