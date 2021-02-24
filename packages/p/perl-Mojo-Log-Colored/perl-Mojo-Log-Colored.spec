#
# spec file for package perl-Mojo-Log-Colored
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Mojo-Log-Colored
Name:           perl-Mojo-Log-Colored
Version:        0.04
Release:        0
Summary:        Colored Mojo logging
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMBABQUE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Mojolicious) >= 5.00
BuildRequires:  perl(Term::ANSIColor) >= 3.00
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Mojolicious) >= 5.00
Requires:       perl(Term::ANSIColor) >= 3.00
%{perl_requires}

%description
Mojo::Log::Colored is a logger for Mojolicious with colored output for the
terminal. It lets you define colors for each log level based on
Term::ANSIColor and comes with sensible default colors. The full lines in
the log will be colored.

Since this inherits from Mojo::Log you can still give it a 'file', but the
output would also be colored. That does not make a lot of sense, so you
don't want to do that. Use this for development, not production.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes minil.toml README.md
%license LICENSE

%changelog
