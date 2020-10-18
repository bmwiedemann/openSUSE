#
# spec file for package rubygem-activesupport-6.0
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

Name:           rubygem-activesupport-6.0
Version:        6.0.3.4
Release:        0
%define mod_name activesupport
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -6.0
# MANUAL
%if 0%{?suse_version} && 0%{?suse_version} < 1500
%define rb_build_versions       ruby26
%define rb_build_ruby_abis      ruby:2.6.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
URL:            https://rubyonrails.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A toolkit of support libraries and Ruby core extensions extracted
License:        MIT
Group:          Development/Languages/Ruby

%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md MIT-LICENSE README.rdoc" \
  -f

%gem_packages

%changelog
