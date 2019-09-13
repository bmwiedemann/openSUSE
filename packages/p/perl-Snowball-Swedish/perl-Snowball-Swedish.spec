#
# spec file for package perl-Snowball-Swedish
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



Name:           perl-Snowball-Swedish
Version:        1.2
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Snowball-Swedish
Summary:        Porters stemming algorithm for swedish.
Url:            http://search.cpan.org/dist/Snowball-Swedish/
Group:          Development/Libraries/Perl
Source:         Snowball-Swedish-1.2.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
#BuildRequires: perl(Lingua::Stem::Snowball::Se)
#BuildRequires: perl(Test::Pod::Coverage)
%{perl_requires}

%description
Porters stemming algorithm for swedish.

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
%doc Changes examples LICENSE README

%changelog
