#
# spec file for package esc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%global provider        github
%global provider_tld    com
%global project         mjibson
%global repo            esc
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}

Name:           esc
Version:        0.2.0
Release:        0
Summary:        Embeds files into go programs
License:        MIT
Group:          System/Management
URL:            https://github.com/mjibson/esc
Source0:        %{name}-v%{version}.tar.gz
Source1:	vendor.tar.gz
BuildRequires:  golang(API) >= 1.11
BuildRequires:  golang-packaging
%{go_nostrip}
%{go_provides}

%description
esc embeds files into go programs and provides http.FileSystem interfaces to them.

%prep
%setup -q -n %{name}-v%{version}

tar -zxf %{SOURCE1}

%build
%goprep %{provider_prefix}
%gobuild .

%install
%goinstall

%files
# Binaries
%{_bindir}/esc
# License
%license LICENSE

%changelog
