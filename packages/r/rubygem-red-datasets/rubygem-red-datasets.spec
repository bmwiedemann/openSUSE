#
# spec file for package rubygem-red-datasets
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

Name:           rubygem-red-datasets
Version:        0.1.5
Release:        0
%define mod_name red-datasets
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/red-data-tools/red-datasets
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Red Datasets provides classes that provide common datasets such as
License:        MIT
Group:          Development/Languages/Ruby

%description
You can use datasets easily because you can access each dataset with multiple
ways such as `#each` and Apache Arrow Record Batch.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
