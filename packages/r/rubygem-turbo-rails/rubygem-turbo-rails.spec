#
# spec file for package rubygem-turbo-rails
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

Name:           rubygem-turbo-rails
Version:        1.3.2
Release:        0
%define mod_name turbo-rails
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.6.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/hotwired/turbo-rails
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        The speed of a single-page web application without having to write
License:        MIT
Group:          Development/Languages/Ruby

%description
The speed of a single-page web application without having to write any
JavaScript.

%prep

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
