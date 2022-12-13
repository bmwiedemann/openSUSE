#
# spec file for package rubygem-fluentd
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-fluentd
Version:        1.15.3
Release:        0
%define mod_name fluentd
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.4}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://www.fluentd.org/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-fluentd-rpmlintrc
Source2:        gem2rpm.yml
Source3:        gem2rpm.yml
Summary:        Fluentd event collector
License:        Apache-2.0
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Fluentd is an open source data collector designed to scale and simplify log
management. It can collect, process and ship many kinds of data in near
real-time.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f

%gem_packages

%changelog
