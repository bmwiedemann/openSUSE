#
# spec file for package rubygem-packaging_rake_tasks
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


Name:           rubygem-packaging_rake_tasks
Version:        1.4.11
Release:        0
%define mod_name packaging_rake_tasks
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Suggests:       %{rubygem parallel}
URL:            http://github.org/openSUSE/packaging_tasks
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Rake tasks providing tasks to package project in git and integration
License:        LGPL-2.1-only
Group:          Development/Languages/Ruby

%description
Rake tasks to allow easy packaging ruby projects in git for Build Service or
other packaging service.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING" \
  -f

%gem_packages

%changelog
