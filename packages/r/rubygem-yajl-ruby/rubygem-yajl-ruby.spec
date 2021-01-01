#
# spec file for package rubygem-yajl-ruby
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

Name:           rubygem-yajl-ruby
Version:        1.4.1
Release:        0
%define mod_name yajl-ruby
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 1.8.6}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            http://github.com/brianmario/yajl-ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-yajl-ruby-rpmlintrc
Source2:        gem2rpm.yml
# MANUAL
Patch0:         silence-gcc-warnings.patch
# /MANUAL
Summary:        Ruby C bindings to the excellent Yajl JSON stream-based parser
License:        MIT AND BSD-3-Clause
Group:          Development/Languages/Ruby

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
