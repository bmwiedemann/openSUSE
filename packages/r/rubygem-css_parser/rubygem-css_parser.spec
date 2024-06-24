#
# spec file for package rubygem-css_parser
#
# Copyright (c) 2024 SUSE LLC
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

Name:           rubygem-css_parser
Version:        1.17.1
Release:        0
%define mod_name css_parser
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.7}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/premailer/css_parser
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby CSS parser
License:        MIT

%description
A set of classes for parsing CSS in Ruby.

%prep

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE" \
  -f

%gem_packages

%changelog
