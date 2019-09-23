#
# spec file for package changelog-generator-data
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild

Name:           changelog-generator-data
Version:        1.0.0
Release:        0
License:        MIT
Summary:        Data to be consumed by containement-rpm-docker
Url:            http://git.suse.de/?p=docker/containment-rpm-docker.git
Group:          System/Management
Source1:        old.packages.x86_64
Source2:        old.packages.s390x
Source3:        old.packages.ppc64le
Source4:        old.packages.aarch64
Source5:        old.changes.x86_64
Source6:        old.changes.s390x
Source7:        old.changes.ppc64le
Source8:        old.changes.aarch64
Requires:       rubygem(changelog_generator)
BuildRequires:  filesystem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Files required to dynamically generate the new changelog file of the Docker
image RPM.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE4} %{buildroot}/%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE5} %{buildroot}/%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE6} %{buildroot}/%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE7} %{buildroot}/%{_datadir}/changelog-generator-data/
install -m 644 %{SOURCE8} %{buildroot}/%{_datadir}/changelog-generator-data/

%files
%defattr(-,root,root)
/%{_datadir}/changelog-generator-data/

%changelog
