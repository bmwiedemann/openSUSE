#
# spec file for package rubygem-dry-core
#
# Copyright (c) 2025 SUSE LLC
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

Name:           rubygem-dry-core
Version:        1.1.0
Release:        0
%define mod_name dry-core
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 3.1.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://dry-rb.org/gems/dry-core
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        dry-core-1.1.0.gem.sha256
Source2:        gem2rpm.yml
Summary:        A toolset of small support modules used throughout the dry-rb
License:        MIT

%description
A toolset of small support modules used throughout the dry-rb ecosystem.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f

%gem_packages

%changelog
