#
# spec file for package rubygem-url_safe_base64
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

Name:           rubygem-url_safe_base64
Version:        0.2.2
Release:        0
%define mod_name url_safe_base64
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://github.com/joenoon/url_safe_base64
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Converts strings to/from a slightly modified base64 that contains
License:        MIT
Group:          Development/Languages/Ruby

%description
Converts strings to/from a slightly modified base64 that contains only
url-safe characters.

%prep

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
