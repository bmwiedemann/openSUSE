#
# spec file for package rubygem-domain_name
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-domain_name
Version:        0.5.20190701
Release:        0
%define mod_name domain_name
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/knu/ruby-domain_name
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Domain Name manipulation library for Ruby
License:        BSD-2-Clause AND BSD-3-Clause AND MPL-2.0
Group:          Development/Languages/Ruby

%description
This is a Domain Name manipulation library for Ruby.
It can also be used for cookie domain validation based on the Public
Suffix List.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
