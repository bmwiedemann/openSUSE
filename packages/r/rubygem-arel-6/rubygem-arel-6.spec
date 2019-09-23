#
# spec file for package rubygem-arel-6
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-arel-6
Version:        6.0.4
Release:        0
%define mod_name arel
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/rails/arel
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Arel Really Exasperates Logicians
License:        MIT
Group:          Development/Languages/Ruby

%description
Arel Really Exasperates Logicians
Arel is a SQL AST manager for Ruby. It
1. Simplifies the generation of complex SQL queries
2. Adapts to various RDBMSes
It is intended to be a framework framework; that is, you can build your own
ORM
with it, focusing on innovative object and collection modeling as opposed to
database compatibility and query generation.

%prep

%build

%install
%gem_install \
  --doc-files="History.txt MIT-LICENSE.txt README.markdown" \
  -f

%gem_packages

%changelog
