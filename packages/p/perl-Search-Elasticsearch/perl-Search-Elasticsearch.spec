#
# spec file for package perl-Search-Elasticsearch
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


%define cpan_name Search-Elasticsearch
Name:           perl-Search-Elasticsearch
Version:        8.120.0
Release:        0
%define cpan_version 8.12
#Upstream:  This is free software, licensed under: The Apache License, Version 2.0, January 2004
License:        Apache-2.0
Summary:        The official client for Elasticsearch
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EZ/EZIMUEL/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Any::URI::Escape)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Tiny) >= 0.076
BuildRequires:  perl(IO::Compress::Deflate)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(JSON::MaybeXS) >= 1.002002
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Log::Any) >= 1.02
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::Callback) >= 0.09
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.001000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Package::Stash) >= 0.34
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::SharedFork)
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
Provides:       perl(Search::Elasticsearch) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0)
Provides:       perl(Search::Elasticsearch::Client::8_0::Bulk) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Autoscaling) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::CCR) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Cat) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Cluster) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Connector) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::ConnectorSyncJob) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::DanglingIndices) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Enrich) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Eql) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Esql) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Features) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Fleet) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Graph) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::ILM) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Indices) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Inference) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Ingest) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::License) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Logstash) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::ML) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Migration) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Monitoring) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Nodes) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Profiling) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::QueryRuleset) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Rollup) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::SQL) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::SSL) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::SearchApplication) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::SearchableSnapshots) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Security) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Shutdown) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Simulate) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Slm) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Snapshot) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Synonyms) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Tasks) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::TextStructure) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Transform) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::Watcher) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Direct::XPack) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Role::API) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Role::Bulk) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Role::Scroll) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::Scroll) = %{version}
Provides:       perl(Search::Elasticsearch::Client::8_0::TestServer) = %{version}
Provides:       perl(Search::Elasticsearch::Cxn::Factory) = %{version}
Provides:       perl(Search::Elasticsearch::Cxn::HTTPTiny) = %{version}
Provides:       perl(Search::Elasticsearch::Cxn::LWP) = %{version}
Provides:       perl(Search::Elasticsearch::CxnPool::Sniff) = %{version}
Provides:       perl(Search::Elasticsearch::CxnPool::Static) = %{version}
Provides:       perl(Search::Elasticsearch::CxnPool::Static::NoPing) = %{version}
Provides:       perl(Search::Elasticsearch::Error) = %{version}
Provides:       perl(Search::Elasticsearch::Logger::LogAny) = %{version}
Provides:       perl(Search::Elasticsearch::Role::API) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Client) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Client::Direct) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Cxn) = %{version}
Provides:       perl(Search::Elasticsearch::Role::CxnPool) = %{version}
Provides:       perl(Search::Elasticsearch::Role::CxnPool::Sniff) = %{version}
Provides:       perl(Search::Elasticsearch::Role::CxnPool::Static) = %{version}
Provides:       perl(Search::Elasticsearch::Role::CxnPool::Static::NoPing) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Is_Sync) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Logger) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Serializer) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Serializer::JSON) = %{version}
Provides:       perl(Search::Elasticsearch::Role::Transport) = %{version}
Provides:       perl(Search::Elasticsearch::Serializer::JSON) = %{version}
Provides:       perl(Search::Elasticsearch::Serializer::JSON::Cpanel) = %{version}
Provides:       perl(Search::Elasticsearch::Serializer::JSON::PP) = %{version}
Provides:       perl(Search::Elasticsearch::Serializer::JSON::XS) = %{version}
Provides:       perl(Search::Elasticsearch::TestServer) = %{version}
Provides:       perl(Search::Elasticsearch::Transport) = %{version}
Provides:       perl(Search::Elasticsearch::Util) = %{version}
%define         __perllib_provides /bin/true
Recommends:     perl(IO::Socket::IP) >= 0.37
Recommends:     perl(URI::Escape::XS)
%{perl_requires}

%description
Search::Elasticsearch is the official Perl client for Elasticsearch,
supported by at http://elastic.co. Elasticsearch itself is a flexible and
powerful open source, distributed real-time search and analytics engine for
the cloud. You can read more about it on at http://www.elastic.co.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%license LICENSE

%changelog
