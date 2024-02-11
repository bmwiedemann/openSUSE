#
# spec file for package fortio
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           fortio
Version:        1.63.3
Release:        0
Summary:        Load testing library, command line tool, advanced echo server and web UI
License:        Apache-2.0
URL:            https://github.com/fortio/fortio
Source:         fortio-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.21

%description
Fortio (Φορτίο) started as, and is, Istio's load testing tool and now graduated to be its own project.

Fortio is also used by, among others, Meshery

Fortio runs at a specified query per second (qps) and records an histogram of execution time and calculates percentiles (e.g. p99 ie the response time such as 99% of the requests take less than that number (in seconds, SI unit)). It can run for a set duration, for a fixed number of calls, or until interrupted (at a constant target QPS, or max speed/load per connection/thread).

The name fortio comes from greek φορτίο which means load/burden.

Fortio is a fast, small (3Mb docker image, minimal dependencies), reusable, embeddable go library as well as a command line tool and server process, the server includes a simple web UI and REST API to trigger run and see graphical representation of the results (both a single latency graph and a multiple results comparative min, max, avg, qps and percentiles graphs).

Fortio also includes a set of server side features (similar to httpbin) to help debugging and testing: request echo back including headers, adding latency or error codes with a probability distribution, tcp echoing, tcp proxying, http fan out/scatter and gather proxy server, GRPC echo/health in addition to http, etc...

%prep
%autosetup -p1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X fortio.org/fortio/version.version=%{version}" \
   -o bin/fortio

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
