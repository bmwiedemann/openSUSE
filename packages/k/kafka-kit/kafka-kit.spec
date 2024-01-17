#
# spec file for package kafka-kit
#
# Copyright (c) 2022 SUSE LLC
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


Name:           kafka-kit
Version:        2.1.0
Release:        0
Summary:        Build-time dependency of project "kafka"
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/SilvioMoioli/tetra
# This tarball needs to be generated from the source tarball shipped with the
# matching kafka package using Tetra (ruby2.2-rubygem-tetra). You will find
# detailed instructions for generating it in README.updating. This is neccessary
# due to Kafka's Gradle based build process downloading dependencies at build
# time. Tetra will keep track of these downloaded dependencies and generate a
# tarball containing all of them. This tarball is then used to allow the same
# build to run in an offline manner in OBS (where there is no Internet
# connectivity).
Source0:        %{name}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        README.updating
Patch0:         kafka-kit-port-py3-runant.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64
BuildRequires:  fdupes
BuildRequires:  xz
BuildRequires:  zip
# https://www.virustotal.com/en/file/3a8dc4a12ab9f3607a1a2097bbab0150c947ad6719d8f1bb6d5b47d0fb0c4779/analysis/1491457251/
#!BuildIgnore: post-build-checks-malwarescan
Provides:       tetra-kit
Conflicts:      otherproviders(tetra-kit)

%description
This package has been automatically created by tetra in order to
satisfy build time dependencies of Java packages.
It should not be used except for rebuilding other packages,
thus it should never be installed on end users' systems.

%prep
%setup -q -n kit
%patch0 -p1

%build
# nothing to do, precompiled by design
# avoid log4j security bugs by removing classes
#zip error: Nothing to do! (./kit/apache-ant-1.9.7/lib/ant-apache-log4j.jar)
#zip error: Nothing to do! (./kit/gradle-5.1/lib/log4j-over-slf4j-1.7.25.jar)
zip -q -d gradle/caches/modules-2/files-2.1/log4j/log4j/1.2.17/5af35056b4d257e4b64b9e8069c0746e8b08629f/log4j-1.2.17.jar org/apache/logging/log4j/core/lookup/JndiLookup.class org/apache/log4j/net/JMSAppender.class org/apache/log4j/jdbc/JDBCAppender.class org/apache/log4j/net/JMSSink.class org/apache/log4j/chainsaw"*"
#zip error: Nothing to do! (./kit/gradle/caches/modules-2/files-2.1/org.slf4j/slf4j-log4j12/1.7.25/110cefe2df103412849d72ef7a67e4e91e4266b4/slf4j-log4j12-1.7.25.jar)

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
install -d -m 0755 %{buildroot}%{_datadir}/tetra/
cp -a * %{buildroot}%{_datadir}/tetra/
%fdupes %{buildroot}%{_datadir}/tetra/

%files
%defattr(-,root,root)
%{_datadir}/tetra/

%changelog
