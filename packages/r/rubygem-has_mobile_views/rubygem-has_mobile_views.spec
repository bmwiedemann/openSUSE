#
# spec file for package rubygem-has_mobile_views
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


Name:           rubygem-has_mobile_views
Version:        0.0.3
Release:        0
%define mod_name has_mobile_views
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://github.com/openSUSE/has_mobile_views
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        A Rails plugin which allows for rendering special templates for
License:        MIT
Group:          Development/Languages/Ruby

%description
This Rails plugin allows for rendering special templates for mobile
devices, using the existing views and partials as a fallback.

%prep

%build

%install
%gem_install \
  --doc-files="README.md" \
  -f

%gem_packages

%changelog
