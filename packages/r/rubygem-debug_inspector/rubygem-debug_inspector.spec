#
# spec file for package rubygem-debug_inspector
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-debug_inspector
Version:        0.0.3
Release:        0
%define mod_name debug_inspector
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/banister/debug_inspector
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A Ruby wrapper for the MRI 2.0 debug_inspector API
License:        MIT
Group:          Development/Languages/Ruby

%description
A Ruby wrapper for the MRI 2.0 debug_inspector API.

%prep

%build

%install
%gem_install \
  --doc-files="README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
