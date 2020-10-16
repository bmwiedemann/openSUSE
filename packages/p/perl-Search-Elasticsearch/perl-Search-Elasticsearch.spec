#
# spec file for package perl-Search-Elasticsearch
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


Name:           perl-Search-Elasticsearch
Version:        7.30
Release:        0
#Upstream:  This is free software, licensed under: The Apache License, Version 2.0, January 2004
%define cpan_name Search-Elasticsearch
Summary:        The official client for Elasticsearch
License:        Apache-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EZ/EZIMUEL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Any::URI::Escape)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Tiny) >= 0.076
BuildRequires:  perl(IO::Compress::Deflate)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(JSON::MaybeXS) >= 1.002002
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Log::Any) >= 1.02
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.001000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Package::Stash) >= 0.34
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(namespace::clean)
Requires:       perl(Any::URI::Escape)
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Tiny) >= 0.076
Requires:       perl(IO::Compress::Deflate)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(JSON::MaybeXS) >= 1.002002
Requires:       perl(JSON::PP)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Log::Any) >= 1.02
Requires:       perl(Log::Any::Adapter)
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 2.001000
Requires:       perl(Moo::Role)
Requires:       perl(Net::IP)
Requires:       perl(Package::Stash) >= 0.34
Requires:       perl(Sub::Exporter)
Requires:       perl(Try::Tiny)
Requires:       perl(URI)
Requires:       perl(namespace::clean)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Log::Any::Adapter::Callback)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::SharedFork)
# MANUAL END

%description
Search::Elasticsearch is the official Perl client for Elasticsearch,
supported by at http://elastic.co. Elasticsearch itself is a flexible and
powerful open source, distributed real-time search and analytics engine for
the cloud. You can read more about it on at http://www.elastic.co.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
