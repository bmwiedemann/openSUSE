#
# spec file for package rubygem-bcrypt-ruby
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


Name:           rubygem-bcrypt-ruby
Version:        3.1.5
Release:        0
%define mod_name bcrypt-ruby
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/codahale/bcrypt-ruby
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        OpenBSD's bcrypt() password hashing algorithm
License:        MIT
Group:          Development/Languages/Ruby

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project
for hashing passwords. The bcrypt Ruby gem provides a simple wrapper for
safely handling
passwords.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG COPYING README.md" \
  -f

%gem_packages

%changelog
