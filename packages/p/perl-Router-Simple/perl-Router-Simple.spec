#
# spec file for package perl-Router-Simple
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Router-Simple
Name:           perl-Router-Simple
Version:        0.180.0
Release:        0
# 0.18 -> normalize -> 0.180.0
%define cpan_version 0.18
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple HTTP router
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Lite) >= 0.50
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.35
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(parent)
Requires:       perl(Class::Accessor::Lite) >= 0.50
Requires:       perl(parent)
Provides:       perl(Router::Simple) = %{version}
Provides:       perl(Router::Simple::Declare)
Provides:       perl(Router::Simple::Route)
Provides:       perl(Router::Simple::SubMapper)
%undefine       __perllib_provides
%{perl_requires}

%description
Router::Simple is a simple router class.

Its main purpose is to serve as a dispatcher for web applications.

Router::Simple can match against PSGI '$env' directly, which means it's
easy to use with PSGI supporting web frameworks.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
