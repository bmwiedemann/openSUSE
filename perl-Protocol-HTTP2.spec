#
# spec file for package perl-Protocol-HTTP2
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Protocol-HTTP2
Version:        1.10
Release:        0
%define cpan_name Protocol-HTTP2
Summary:        HTTP/2 protocol implementation (RFC 7540)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        Protocol-HTTP2-1.10.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(MIME::Base64) >= 3.11
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Net::SSLeay) >= 1.45
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::TCP)
Requires:       perl(MIME::Base64) >= 3.11
%{perl_requires}

%description
Protocol::HTTP2 is HTTP/2 protocol implementation (at
https://tools.ietf.org/html/rfc7540) with stateful decoders/encoders of
HTTP/2 frames. You may use this module to implement your own HTTP/2
client/server/intermediate on top of your favorite event loop over plain or
tls socket (see examples).

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes examples README.md
%license LICENSE

%changelog
