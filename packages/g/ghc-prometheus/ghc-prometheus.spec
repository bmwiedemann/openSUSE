#
# spec file for package ghc-prometheus
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


%global pkg_name prometheus
Name:           ghc-%{pkg_name}
Version:        2.2.2
Release:        0
Summary:        Prometheus Haskell Client
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-atomic-primops-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-warp-devel
ExcludeArch:    %{ix86}

%description
[Prometheus Haskell Client]

A simple and modern, type safe, performance focused, idiomatic Haskell client
for <http://prometheus.io Prometheus> monitoring. Specifically there is no use
of unsafe IO or manual ByteString construction from lists of bytes.
Batteries-included web server.

A key design element of this library is that the RegistryT monad transformer is
only required for registering new time series. Once the time series is
registered, new data samples may just be added in the IO monad.

Note: Version 0.* supports Prometheus v1.0 and version 2.* supports Prometheus
v2.0.

[Usage Example]

> module Example where > > import Control.Monad.IO.Class (liftIO) > import
System.Metrics.Prometheus.Http.Scrape (serveMetricsT) > import
System.Metrics.Prometheus.Concurrent.RegistryT > import
System.Metrics.Prometheus.Metric.Counter (inc) > import
System.Metrics.Prometheus.MetricId > > main :: IO () > main = runRegistryT $ do
> -- Labels can be defined as lists or added to an empty label set >
connectSuccessGauge <- registerGauge "example_connections" (fromList [("login",
"success")]) > connectFailureGauge <- registerGauge "example_connections"
(addLabel "login" "failure" mempty) > connectCounter <- registerCounter
"example_connection_total" mempty > latencyHistogram <- registerHistogram
"example_round_trip_latency_ms" mempty [10, 20..100] > > liftIO $ inc
connectCounter -- increment a counter > > -- [...] pass metric handles to the
rest of the app > > serveMetricsT 8080 ["metrics"] --
http://localhost:8080/metric server >

[Advanced Usage]

A `Registry` and `StateT`-based `RegistryT` are available for unit testing or
generating lists of `[IO a]` actions that can be `sequenced` and returned from
pure code to be applied.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc Example.hs README.md

%changelog
