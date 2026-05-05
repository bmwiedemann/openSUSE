#
# spec file for package perl-App-AppSpec
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name App-AppSpec
Name:           perl-App-AppSpec
Version:        0.6.0
Release:        0
# 0.006 -> normalize -> 0.6.0
%define cpan_version 0.006
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        App Module ad utilities for appspec tool
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Spec) >= 0.13.0
BuildRequires:  perl(App::Spec::Pod)
BuildRequires:  perl(App::Spec::Run::Cmd)
BuildRequires:  perl(App::Spec::Schema)
BuildRequires:  perl(File::Share)
BuildRequires:  perl(File::ShareDir::Install) >= 0.6
BuildRequires:  perl(JSON::Validator)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo)
BuildRequires:  perl(YAML::PP) >= 0.15.0
Requires:       perl(App::Spec) >= 0.13.0
Requires:       perl(App::Spec::Pod)
Requires:       perl(App::Spec::Run::Cmd)
Requires:       perl(App::Spec::Schema)
Requires:       perl(JSON::Validator)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Moo)
Requires:       perl(YAML::PP) >= 0.15.0
Provides:       perl(App::AppSpec) = %{version}
Provides:       perl(App::AppSpec::Schema::Validator) = %{version}
Provides:       perl(App::AppSpec::Spec) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This is the app class for the appspec command line tool. It contains
utilities for App::Spec files, like generating completion or pod from it.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
