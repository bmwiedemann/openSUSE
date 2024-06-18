#
# spec file for package perl-Mojolicious-Plugin-AssetPack
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


%define cpan_name Mojolicious-Plugin-AssetPack
Name:           perl-Mojolicious-Plugin-AssetPack
Version:        2.14
Release:        0
License:        Artistic-2.0
Summary:        Compress and convert CSS, Less, Sass, JavaScript and CoffeeScript files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-UPSTREAM https://github.com/mojolicious/mojo-assetpack/pull/149
Patch0:         mojolicious-deprecate-spurt.patch
# PATCH-FIX-UPSTREAM https://github.com/mojolicious/mojo-assetpack/pull/150
Patch1:         sass-trace.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which) >= 1.21
BuildRequires:  perl(IPC::Run3) >= 0.048
BuildRequires:  perl(Mojolicious) >= 9.0
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::Which) >= 1.21
Requires:       perl(IPC::Run3) >= 0.048
Requires:       perl(Mojolicious) >= 9.0
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Mojolicious) >= 9.34
Requires:       perl(Mojolicious) >= 9.34
# MANUAL END

%description
Mojolicious::Plugin::AssetPack is a Mojolicious plugin for processing
static assets. The idea is that JavaScript and CSS files should be served
as one minified file to save bandwidth and roundtrip time to the server.

There are many external tools for doing this, but integrating them with
Mojolicious can be a struggle: You want to serve the source files directly
while developing, but a minified version in production. This assetpack
plugin will handle all of that automatically for you.

Your application creates and refers to an asset by its topic (virtual asset
name). The process of building actual assets from their components is
delegated to "pipe objects".

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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
%doc Changes examples README.md
%license LICENSE

%changelog
