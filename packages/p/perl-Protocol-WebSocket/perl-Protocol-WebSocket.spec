#
# spec file for package perl-Protocol-WebSocket
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Protocol-WebSocket
Version:        0.26
Release:        0
%define cpan_name Protocol-WebSocket
Summary:        WebSocket protocol
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/V/VT/VTI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
Requires:       perl(Digest::SHA)
%{perl_requires}

%description
Client/server WebSocket message and frame parser/constructor. This module
does not provide a WebSocket server or client, but is made for using in
http servers or clients to provide WebSocket support.

Protocol::WebSocket supports the following WebSocket protocol versions:

    draft-ietf-hybi-17 (latest)
    draft-ietf-hybi-10
    draft-ietf-hybi-00 (with HAProxy support)
    draft-hixie-75

By default the latest version is used. The WebSocket version is detected
automatically on the server side. On the client side you have set a
'version' attribute to an appropriate value.

Protocol::WebSocket itself does not contain any code and cannot be used
directly. Instead the following modules should be used:

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples minil.toml README.md util
%license LICENSE

%changelog
