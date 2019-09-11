#
# spec file for package rubygem-ci_reporter
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           rubygem-ci_reporter
Version:        2.0.0
Release:        0
%define mod_name ci_reporter
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/ci-reporter/ci_reporter
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Connects Ruby test frameworks to CI systems via JUnit reports
License:        MIT
Group:          Development/Languages/Ruby

%description
CI::Reporter is an add-on to Ruby testing frameworks that allows you to
generate XML reports of your test runs. The resulting files can be read by a
continuous integration system that understands Ant's JUnit report format.

%prep

%build

%install
%gem_install \
  --doc-files="History.txt LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
