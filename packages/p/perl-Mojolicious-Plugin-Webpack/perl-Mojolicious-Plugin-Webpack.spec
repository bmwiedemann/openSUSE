#
# spec file for package perl-Mojolicious-Plugin-Webpack
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


%define cpan_name Mojolicious-Plugin-Webpack
Name:           perl-Mojolicious-Plugin-Webpack
Version:        1.02
Release:        0
License:        Artistic-2.0
Summary:        Mojolicious ♥ Webpack
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::chdir) >= 0.10
BuildRequires:  perl(Mojolicious) >= 8.00
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::chdir) >= 0.10
Requires:       perl(Mojolicious) >= 8.00
%{perl_requires}

%description
Mojolicious::Plugin::Webpack is a Mojolicious plugin to make it easier to
work with https://webpack.js.org/ or https://rollupjs.org/. This plugin
will...

* 1.

Generate a minimal 'package.json' and a Webpack or Rollup config file.
Doing this manually is possible, but it can be quite time consuming to
figure out all the bits and pieces if you are not already familiar with
Webpack.

* 2.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes example

%changelog
