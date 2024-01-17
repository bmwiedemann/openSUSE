#
# spec file for package rubygem-mixlib-cli
#
# Copyright (c) 2020 SUSE LLC
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

Name:           rubygem-mixlib-cli
Version:        2.1.8
Release:        0
%define mod_name mixlib-cli
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.4}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/chef/mixlib-cli
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A simple mixin for CLI interfaces, including option parsing
License:        Apache-2.0
Group:          Development/Languages/Ruby

%description
A simple mixin for CLI interfaces, including option parsing.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE" \
  -f

%gem_packages

%changelog
