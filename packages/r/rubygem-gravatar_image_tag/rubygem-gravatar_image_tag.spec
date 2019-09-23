#
# spec file for package rubygem-gravatar_image_tag
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

Name:           rubygem-gravatar_image_tag
Version:        1.2.0
Release:        0
%define mod_name gravatar_image_tag
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://github.com/mdeering/gravatar_image_tag
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        A configurable and documented Rails view helper for adding gravatars
License:        MIT
Group:          Development/Languages/Ruby

%description
A configurable and documented Rails view helper for adding gravatars into your
Rails application.

%prep

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE" \
  -f

%gem_packages

%changelog
