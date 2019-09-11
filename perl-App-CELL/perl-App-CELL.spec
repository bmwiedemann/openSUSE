#
# spec file for package perl-App-CELL
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-App-CELL
Version:        0.222
Release:        0
%define cpan_name App-CELL
Summary:        Configuration, Error-handling, Localization, and Logging
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/App-CELL/
Source0:        App-CELL-0.222.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(File::ShareDir) >= 1
BuildRequires:  perl(File::ShareDir::Install) >= 0.11
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter) >= 0.1
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Date::Format)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Next)
Requires:       perl(File::ShareDir) >= 1
Requires:       perl(Log::Any)
Requires:       perl(Log::Any::Adapter) >= 0.1
Requires:       perl(Params::Validate)
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
This is the top-level module of App::CELL, the Configuration,
Error-handling, Localization, and Logging framework for applications (or
scripts) written in Perl.

For details, read the POD in the App::CELL distro. For an introduction,
read App::CELL::Guide.

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
%doc Changes config LICENSE README.rst WISHLIST

%changelog
