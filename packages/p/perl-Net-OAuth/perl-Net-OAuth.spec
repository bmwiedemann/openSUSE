#
# spec file for package perl-Net-OAuth
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Net-OAuth
Version:        0.28
Release:        0
%define cpan_name Net-OAuth
Summary:        OAuth 1.0 for Perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-OAuth/
Source:         http://www.cpan.org/authors/id/K/KG/KGRENNAN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor) >= 0.31
BuildRequires:  perl(Class::Data::Inheritable) >= 0.06
BuildRequires:  perl(Digest::HMAC_SHA1) >= 1.01
BuildRequires:  perl(Digest::SHA) >= 5.47
BuildRequires:  perl(Digest::SHA1) >= 2.12
BuildRequires:  perl(Encode) >= 2.35
BuildRequires:  perl(LWP::UserAgent) >= 1
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(Test::More) >= 0.66
BuildRequires:  perl(Test::Warn) >= 0.21
BuildRequires:  perl(URI::Escape) >= 3.28
#BuildRequires: perl(Class::Accessor::Fast)
#BuildRequires: perl(Net::OAuth)
#BuildRequires: perl(Net::OAuth::AccessToken)
#BuildRequires: perl(Net::OAuth::AccessTokenRequest)
#BuildRequires: perl(Net::OAuth::Message)
#BuildRequires: perl(Net::OAuth::ProtectedResourceRequest)
#BuildRequires: perl(Net::OAuth::Request)
#BuildRequires: perl(Net::OAuth::RequestTokenRequest)
#BuildRequires: perl(Net::OAuth::RequestTokenResponse)
#BuildRequires: perl(Net::OAuth::Response)
#BuildRequires: perl(Net::OAuth::UserAuthResponse)
#BuildRequires: perl(URI)
#BuildRequires: perl(URI::QueryParam)
Requires:       perl(Class::Accessor) >= 0.31
Requires:       perl(Class::Data::Inheritable) >= 0.06
Requires:       perl(Digest::HMAC_SHA1) >= 1.01
Requires:       perl(Digest::SHA) >= 5.47
Requires:       perl(Digest::SHA1) >= 2.12
Requires:       perl(Encode) >= 2.35
Requires:       perl(LWP::UserAgent) >= 1
Requires:       perl(URI::Escape) >= 3.28
%{perl_requires}

%description
OAuth 1.0 for Perl

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes demo README

%changelog
