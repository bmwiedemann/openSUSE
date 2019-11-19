#
# spec file for package gpars
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           gpars
Version:        1.2.1
Release:        0
Summary:        Groovy Parallel Systems
License:        Apache-2.0 AND SUSE-Public-Domain
URL:            http://gpars.codehaus.org
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         0001-JSR-166.patch
Patch1:         0002-Enable-XMvn-local-mode.patch
Patch2:         0003-Port-build-script-to-current-gradle.patch
Patch3:         gpars-1.2.1-port-to-netty-3.10.6.patch
BuildRequires:  gradle-local
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.codehaus.jcsp:jcsp)
BuildRequires:  mvn(org.codehaus.jsr166-mirror:extra166y)
BuildRequires:  mvn(org.jboss.netty:netty:3)
BuildRequires:  mvn(org.multiverse:multiverse-core)
Obsoletes:      %{name}-bootstrap
BuildConflicts: java-devel >= 9
#!BuildRequires: gradle-bootstrap groovy-bootstrap
BuildArch:      noarch

%description
The GPars framework offers Java developers intuitive and safe ways to
handle Java or Groovy tasks concurrently. Leveraging the enormous
flexibility of the Groovy programming language and building on proven
Java technologies, we aim to make concurrent programming for
multi-core hardware intuitive, robust and enjoyable.

GPars is a multi-paradigm concurrency framework, offering several
mutually cooperating high-level concurrency abstractions, such as
Dataflow operators, Promises, CSP, Actors, Asynchronous Functions,
Agents and Parallel Collections.

%prep
%setup -q
cp %{SOURCE1} .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{gradle_build} -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE-2.0.txt

%changelog
