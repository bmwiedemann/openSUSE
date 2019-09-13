#
# spec file for package rubygem-securecompare
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

Name:           rubygem-securecompare
Version:        1.0.0
Release:        0
%define mod_name securecompare
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 1.9.3}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/samuelkadolph/securecompare
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        securecompare is a gem that implements a constant time string
License:        MIT
Group:          Development/Languages/Ruby

%description
securecompare borrows the secure_compare private method from
ActiveSupport::MessageVerifier which lets you do safely compare strings
without being vulnerable to timing attacks. Useful for Basic HTTP
Authentication in your rack/rails application.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
