#
# spec file for package rubygem-rspec-mocks-3_5
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

Name:           rubygem-rspec-mocks-3_5
Version:        3.5.0
Release:        0
%define mod_name rspec-mocks
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -3_5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 1.8.7}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
Url:            https://github.com/rspec/rspec-mocks
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        RSpecs test double framework, with support for stubbing and mocking
License:        MIT
Group:          Development/Languages/Ruby

%description
rspec-mocks is a test-double framework for rspec with support for method stubs, fakes, and message expectations on generated test-doubles and real objects alike.
%prep

%build

%install
%gem_install \
  --doc-files="Changelog.md LICENSE.md README.md" \
  -f

%gem_packages

%changelog
