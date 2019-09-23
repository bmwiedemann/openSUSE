#
# spec file for package uperf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           uperf
Version:        1.0.6
Release:        0
Summary:        Unified Network Performance Tool
License:        GPL-3.0-only
Group:          Productivity/Networking/Diagnostic
URL:            http://www.uperf.org/
Source0:        https://github.com/uperf/uperf/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         uperf-openssl-1_1.patch
# PATCH-FIX-UPSTREAM https://github.com/uperf/uperf/pull/13
Patch1:         reproducible.patch
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel

%description
uperf is a network performance tool that supports modelling and replay of
various networking patterns. uperf was developed by the Performance
Applications Engineering group at Sun Microsystems and is released under the
GNU General Public License Version 3.

uperf represents the next generation benchmarking tools (like filebench) where
instead of running a fixed benchmark or workload, a description (or model) of
the workload is provided and the tool generates the load according to the
model. By distilling the benchmark or workload into a model, you can now do
various things like change the scale of the workload, change different
parameters, change protocols, etc and analyse the effect of these changes on
your model. You can also study the effect of interleaving CPU activity, or
think times or the use of SSL instead of TCP among many other things.

Some of the questions you could answer using uperf are
* Bandwidth and latency (unidirectional and bi-directional) with different
  protocols like TCP, UDP, SCTP, SSL
* Connection setup and teardown scalability for different protocols
* Effect of noise on ongoing network connections
* Does it matter if I use processes instead of threads to do network
  communication?
* What is the L2 cache miss rate for connection setup?
* Understand TCP, UDP, SCTP, SSL performance under a variety of conditions
and much more!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
  --datadir="%{_datadir}/%{name}" \
  --enable-cpc \
  --enable-netstat \
  --enable-udp \
  --enable-ssl \
  --enable-sctp
make %{?_smp_mflags}

%install
%make_install
chmod 0644 AUTHORS ChangeLog COPYING NEWS README *.pem

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/uperf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xml

%changelog
