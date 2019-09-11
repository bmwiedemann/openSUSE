#
# spec file for package ohpc
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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
%include %{_sourcedir}/OHPC_macros
Summary:   OpenHPC compatibility environment setup
Name:      ohpc
Version:   1.2
Release:   1
License:   BSD-3-Clause
Group:     Productivity/Clustering/Computing
URL:       https://github.com/openhpc/ohpc
BuildArch: noarch
Source0:   OHPC_macros
Source1:   LICENSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires: sed
Requires:  lua-lmod

%description
Provide rpm macros for compatibility with the OpenHPC project

%prep

%build
cp %{S:1} .

%install
mkdir -p  %{buildroot}/%{_sysconfdir}/rpm
sed -e "s#global ##" -e "s#^%%debug_package.*##" < %{S:0}  > %{buildroot}/%{_sysconfdir}/rpm/macros.ohpc

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/rpm/macros.ohpc
%doc LICENSE

%changelog
