#
# spec file for package container-suseconnect
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


%global project     container-suseconnect
%global import_path github.com/SUSE/%{project}
%global zypp_path   %{_prefix}/lib/zypp/plugins
%global zypp_services %{zypp_path}/services
%global zypp_urlresolver %{zypp_path}/urlresolver
Name:           %{project}
Version:        2.4.0
Release:        0
Summary:        Provides access to repositories inside containers
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://%{import_path}
Source0:        %{project}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        container-suseconnect-rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  libzypp > 9.34
Requires:       libzypp > 9.34
%{go_provides}
%{go_exclusivearch}

%description
container-suseconnect gives access to package repositories inside containers
using the host machine entitlements.

%prep
%setup -q -n %{project}-%{version} -a1

%build
%{goprep} %{import_path}
%{gobuild} cmd/container-suseconnect

%install
%{goinstall}
%{gofilelist}
mkdir -p %{buildroot}/%{zypp_services}
mkdir -p %{buildroot}/%{zypp_urlresolver}
ln -s %{_bindir}/%{project} %{buildroot}/%{zypp_services}/%{project}-zypp
ln -s %{_bindir}/%{project} %{buildroot}/%{zypp_urlresolver}/susecloud

%files -f file.lst
%doc README.md
%license LICENSE
%{_bindir}/%{project}
%{zypp_services}/%{project}-zypp
%{zypp_urlresolver}/susecloud

%changelog
