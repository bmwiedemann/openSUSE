#
# spec file for package rubygem-rails-html-sanitizer
#
# Copyright (c) 2023 SUSE LLC
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

Name:           rubygem-rails-html-sanitizer
Version:        1.6.0
Release:        0
%define mod_name rails-html-sanitizer
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/rails/rails-html-sanitizer
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        HTML sanitization to Rails applications (part of Rails)
License:        MIT
Group:          Development/Languages/Ruby

%description
This gem is responsible for sanitizing HTML fragments in Rails applications.
Specifically, this is the set of sanitizers used to implement the Action View
SanitizerHelper methods sanitize, sanitize_css, strip_tags and strip_links.

Rails HTML Sanitizer is only intended to be used with Rails applications. If
you need similar functionality but aren't using Rails, consider using the
underlying sanitization library Loofah directly.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
