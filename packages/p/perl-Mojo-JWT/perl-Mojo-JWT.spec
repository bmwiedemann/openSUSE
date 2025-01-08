#
# spec file for package perl-Mojo-JWT
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


%define cpan_name Mojo-JWT
Name:           perl-Mojo-JWT
Version:        1.10.0
Release:        0
# 1.01 -> normalize -> 1.10.0
%define cpan_version 1.01
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        JSON Web Token the Mojo way
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JB/JBERGER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CryptX) >= 0.029
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Mojolicious) >= 5.00
Requires:       perl(CryptX) >= 0.029
Requires:       perl(Mojolicious) >= 5.00
Provides:       perl(Mojo::JWT) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
JSON Web Token is described in https://tools.ietf.org/html/rfc7519.
Mojo::JWT implements that standard with an API that should feel familiar to
Mojolicious users (though of course it is useful elsewhere). Indeed, JWT is
much like Mojolicious::Sessions except that the result is a url-safe text
string rather than a cookie.

In JWT, the primary payload is called the 'claims', and a few claims are
reserved, as seen in the IETF document. The header and the claims are
signed when stringified to guard against tampering. Note that while signed,
the data is not encrypted, so don't use it to send secrets over clear
channels.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes metamerge.json README
%license LICENSE

%changelog
