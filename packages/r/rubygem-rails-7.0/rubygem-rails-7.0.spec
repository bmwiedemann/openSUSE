#
# spec file for package rubygem-rails-7.0
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

Name:           rubygem-rails-7.0
Version:        7.0.8.4
Release:        0
%define mod_name rails
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -7.0
# MANUAL
BuildRequires:  ruby-common >= 3.2.1

#!BuildIgnore: ruby3.1-rubygem-sprockets-3.7
BuildRequires:  %{rubygem activejob >= 7.0}
BuildRequires:  %{rubygem activemodel:7.0}
BuildRequires:  %{rubygem railties:7.0}

# keep in sync with below
BuildRequires:  %{rubygem puma:5}
BuildRequires:  %{rubygem bootsnap}
BuildRequires:  %{rubygem importmap-rails}
BuildRequires:  %{rubygem jbuilder}
BuildRequires:  %{rubygem sprockets-rails}
BuildRequires:  %{rubygem sqlite3:1 >= 1.4}
BuildRequires:  %{rubygem stimulus-rails}
BuildRequires:  %{rubygem turbo-rails}
BuildRequires:  %{rubygem web-console }

# It says 3.0, but to avoid any question for the 3.7 we
# still have in Factory, let's go newer
BuildRequires:  %{rubygem sprockets > 3.8}
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.7.0}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://rubyonrails.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Full-stack web application framework
License:        MIT

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.

%prep

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
