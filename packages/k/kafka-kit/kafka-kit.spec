#
# spec file for package kafka-kit
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kafka-kit
Version:        2.1.0
Release:        0
Summary:        Build-time dependency of project "kafka"
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Url:            https://github.com/SilvioMoioli/tetra
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64
BuildRequires:  fdupes
BuildRequires:  xz
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

%build
# nothing to do, precompiled by design

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
install -d -m 0755 %{buildroot}%{_datadir}/tetra/
cp -a * %{buildroot}%{_datadir}/tetra/
%fdupes %{buildroot}%{_datadir}/tetra/

%files
%defattr(-,root,root)
%{_datadir}/tetra/

%changelog
