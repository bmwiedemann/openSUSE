#
# spec file for package perl-Web-MREST-CLI
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Web-MREST-CLI
Name:           perl-Web-MREST-CLI
Version:        0.284
Release:        0
Summary:        CLI components for Web::MEST-based applications
License:        BSD-3-Clause
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        Web-MREST-CLI-0.284.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::CELL) >= 0.205
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::https) >= 6.04
BuildRequires:  perl(LWP::UserAgent) >= 6.05
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI::Escape)
Requires:       perl(App::CELL) >= 0.205
Requires:       perl(File::HomeDir)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(HTTP::Request::Common)
Requires:       perl(JSON)
Requires:       perl(LWP::Protocol::https) >= 6.04
Requires:       perl(LWP::UserAgent) >= 6.05
Requires:       perl(Log::Any::Adapter)
Requires:       perl(Params::Validate)
Requires:       perl(Test::Deep)
Requires:       perl(Try::Tiny)
Requires:       perl(URI::Escape)
%{perl_requires}

%description
Top-level module of the Web::MREST::CLI distribution. Exports some
"generalized" functions that are used internally and might also be useful
for writing CLI clients in general.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.rst
%license LICENSE

%changelog
