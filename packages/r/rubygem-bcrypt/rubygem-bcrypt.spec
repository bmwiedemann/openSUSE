#
# spec file for package rubygem-bcrypt
#
# Copyright (c) 2020 SUSE LLC
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

Name:           rubygem-bcrypt
Version:        3.1.16
Release:        0
%define mod_name bcrypt
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/codahale/bcrypt-ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-bcrypt-rpmlintrc
Source2:        gem2rpm.yml
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
%gem_cleanup

%gem_packages

%changelog
