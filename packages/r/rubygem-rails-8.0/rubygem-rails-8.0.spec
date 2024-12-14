#
# spec file for package rubygem-rails-8.0
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

Name:           rubygem-rails-8.0
Version:        8.0.0
Release:        0
%define mod_name rails
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -8.0
# MANUAL
BuildRequires:  %{rubygem activesupport = 8.0.0}
BuildRequires:  %{rubygem actionpack = 8.0.0}
BuildRequires:  %{rubygem actionview = 8.0.0}
BuildRequires:  %{rubygem activemodel = 8.0.0}
BuildRequires:  %{rubygem activerecord = 8.0.0}
BuildRequires:  %{rubygem actionmailer = 8.0.0}
BuildRequires:  %{rubygem activejob = 8.0.0}
BuildRequires:  %{rubygem actioncable = 8.0.0}
BuildRequires:  %{rubygem activestorage = 8.0.0}
BuildRequires:  %{rubygem actionmailbox = 8.0.0}
BuildRequires:  %{rubygem actiontext = 8.0.0}
BuildRequires:  %{rubygem railties = 8.0.0}
BuildRequires:  %{rubygem bundler >= 1.15.0}

# help scheduler
BuildRequires:  %{rubygem rack-session >= 2}
BuildRequires:  %{rubygem mail >= 2.8.1}
BuildRequires:  %{rubygem mini_mime >= 1.1.5}

%bcond_with ensure_default_gemfile_works
%if %{with ensure_default_gemfile_works}
# keep in sync with below
BuildRequires:  %{rubygem propshaft}
BuildRequires:  %{rubygem sqlite3 >= 2.1}
BuildRequires:  %{rubygem puma >= 6.0}
BuildRequires:  %{rubygem importmap-rails}
BuildRequires:  %{rubygem jsbundling-rails}
BuildRequires:  %{rubygem turbo-rails}
BuildRequires:  %{rubygem stimulus-rails}
BuildRequires:  %{rubygem jbuilder >= 2.13}
BuildRequires:  %{rubygem solid_cable}
BuildRequires:  %{rubygem solid_cache}
BuildRequires:  %{rubygem solid_queue}
BuildRequires:  %{rubygem bootsnap}
BuildRequires:  %{rubygem kamal}
# BuildRequires:  %{rubygem thruster}
BuildRequires:  %{rubygem debug}
BuildRequires:  %{rubygem brakeman}
BuildRequires:  %{rubygem web-console}
BuildRequires:  %{rubygem rack-mini-profiler}
BuildRequires:  %{rubygem redis >= 5.0}

BuildRequires:  %{rubygem redis:5 >= 5.0.0}
BuildRequires:  %{rubygem kredis}
BuildRequires:  %{rubygem bcrypt:3.1 >= 3.1.7}
BuildRequires:  %{rubygem image_processing:1 >= 1.2}
BuildRequires:  %{rubygem rack-cors}
# BuildRequires:  %{rubygem rubocop-rails-omakase}

# help the scheduler
BuildRequires:  %{rubygem net-ssh >= 6.1}
BuildRequires:  %{rubygem mysql2:0 >= 0.5}
BuildRequires:  %{rubygem pg:1 >= 1.1}
%endif
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 3.2.0}
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
  --no-rdoc --no-ri \
  --doc-files="MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
