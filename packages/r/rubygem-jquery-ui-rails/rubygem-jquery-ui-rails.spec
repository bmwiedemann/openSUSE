#
# spec file for package rubygem-jquery-ui-rails
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-jquery-ui-rails
Version:        6.0.1
Release:        0
%define mod_name jquery-ui-rails
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/joliss/jquery-ui-rails
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        jQuery UI packaged for the Rails asset pipeline
License:        MIT
Group:          Development/Languages/Ruby

%description
jQuery UI's JavaScript, CSS, and image files packaged for the Rails 3.1+ asset
pipeline.

%prep

%build

%install
%gem_install \
  --doc-files="History.md License.txt README.md" \
  -f

%gem_packages

%changelog
