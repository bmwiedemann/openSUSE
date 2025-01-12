#
# spec file for package perl-Module-Pluggable
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Module-Pluggable
Name:           perl-Module-Pluggable
Version:        6.200.0
Release:        0
# 6.2 -> normalize -> 6.200.0
%define cpan_version 6.2
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Automatically give your module the ability to have plugins
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMONW/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Devel::InnerPackage) = 0.4
Provides:       perl(Module::Pluggable) = %{version}
Provides:       perl(Module::Pluggable::Object) = 5.2
%undefine       __perllib_provides
Recommends:     perl(Module::Runtime) >= 0.012
%{perl_requires}

%description
Provides a simple but, hopefully, extensible way of having 'plugins' for
your module. Obviously this isn't going to be the be all and end all of
solutions but it works for me.

Essentially all it does is export a method into your namespace that looks
through a search path for .pm files and turn those into class names.

Optionally it instantiates those classes for you.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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

%changelog
