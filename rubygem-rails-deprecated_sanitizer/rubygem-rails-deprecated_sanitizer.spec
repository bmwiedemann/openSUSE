#
# spec file for package rubygem-rails-deprecated_sanitizer
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-rails-deprecated_sanitizer
Version:        1.0.3
Release:        0
%define mod_name rails-deprecated_sanitizer
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} == 1110
%define rb_build_versions ruby21
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/rails/rails-deprecated_sanitizer
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Deprecated sanitizer API extracted from Action View
License:        MIT
Group:          Development/Languages/Ruby

%description
Deprecated sanitizer API extracted from Action View.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md README.md" \
  -f

%gem_packages

%changelog
