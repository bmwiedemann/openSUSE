#
# spec file for package rubygem-gssapi
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

Name:           rubygem-gssapi
Version:        1.3.0
Release:        0
%define mod_name gssapi
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 1.8.7}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
Url:            http://github.com/zenchild/gssapi
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A FFI wrapper around the system GSSAPI library
License:        MIT
Group:          Development/Languages/Ruby

%description
A FFI wrapper around the system GSSAPI library. Please make sure and read
the
Yard docs or standard GSSAPI documentation if you have any questions.
There is also a class called GSSAPI::Simple that wraps many of the common
features
used for GSSAPI.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING Changelog.md README.md" \
  -f

%gem_packages

%changelog
