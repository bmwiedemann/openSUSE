#
# spec file for package rubygem-rack-test-0_6
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           rubygem-rack-test-0_6
Version:        0.6.3
Release:        0
%define mod_name rack-test
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -0_6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://github.com/brynary/rack-test
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Simple testing API built on Rack
License:        MIT
Group:          Development/Languages/Ruby

%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on. Most of its initial functionality is an extraction of Merb 1.0's
request helpers feature.

%prep

%build

%install
%gem_install \
  --doc-files="History.txt MIT-LICENSE.txt README.rdoc" \
  -f

%gem_packages

%changelog
