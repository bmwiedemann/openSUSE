#
# spec file for package rubygem-dry-configurable
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

Name:           rubygem-dry-configurable
Version:        1.0.1
Release:        0
%define mod_name dry-configurable
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.7.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://dry-rb.org/gems/dry-configurable
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A mixin to add configuration functionality to your classes
License:        MIT
Group:          Development/Languages/Ruby

%description
A mixin to add configuration functionality to your classes.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f

%gem_packages

%changelog
