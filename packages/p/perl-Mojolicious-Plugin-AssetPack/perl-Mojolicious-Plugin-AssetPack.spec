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
Version:        2.150.0
Release:        0
# 2.15 -> normalize -> 2.150.0
%define cpan_version 2.15
License:        Artistic-2.0
Summary:        Compress and convert CSS, Less, Sass, JavaScript and CoffeeScript files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which) >= 1.21
BuildRequires:  perl(IPC::Run3) >= 0.048
BuildRequires:  perl(Mojolicious) >= 9.340
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::Which) >= 1.21
Requires:       perl(IPC::Run3) >= 0.048
Requires:       perl(Mojolicious) >= 9.340
Provides:       perl(Mojolicious::Plugin::AssetPack) = %{version}
Provides:       perl(Mojolicious::Plugin::AssetPack::Asset)
Provides:       perl(Mojolicious::Plugin::AssetPack::Asset::Null)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::CoffeeScript)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Combine)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Css)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Favicon)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Fetch)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::JavaScript)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Jpeg)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Less)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Png)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Riotjs)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::RollupJs)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Sass)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::TypeScript)
Provides:       perl(Mojolicious::Plugin::AssetPack::Pipe::Vuejs)
Provides:       perl(Mojolicious::Plugin::AssetPack::Store)
Provides:       perl(Mojolicious::Plugin::AssetPack::Util)
Provides:       perl(Mojolicious::Plugin::AssetPack::Util::_chdir)
%undefine       __perllib_provides
%{perl_requires}

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
%doc Changes examples README.md
%license LICENSE

%changelog
