#
# spec file for package rubygem-googleapis-common-protos-types
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


%define mod_name googleapis-common-protos-types
%define mod_full_name %{mod_name}-%{version}
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-googleapis-common-protos-types
Version:        1.4.0
Release:        0
Summary:        Common protocol buffer types used in Google APIs
License:        Apache-2.0
Group:          Development/Languages/Ruby
URL:            https://github.com/googleapis/common-protos-ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{ruby >= 2.6}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5

%description
Common protocol buffer types used by Google APIs.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md README.md" \
  -f

%gem_packages

%changelog
