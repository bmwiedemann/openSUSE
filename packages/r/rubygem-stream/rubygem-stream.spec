#
# spec file for package rubygem-stream
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


%define mod_name stream
%define mod_full_name %{mod_name}-%{version}
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-stream
Version:        0.5.5
Release:        0
Summary:        stream - Extended External Iterators
License:        Ruby
Group:          Development/Languages/Ruby
URL:            https://github.com/monora/stream
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5

%description
Module Stream defines an interface for external iterators.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE README.rdoc" \
  -f

%gem_packages

%changelog
