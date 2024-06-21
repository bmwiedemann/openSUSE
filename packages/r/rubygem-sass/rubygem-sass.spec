#
# spec file for package rubygem-sass
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

Name:           rubygem-sass
Version:        3.7.4
Release:        0
%define mod_name sass
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://sass-lang.com/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:         non-numeric.patch
# /MANUAL
Summary:        A powerful but elegant CSS compiler that makes CSS fun again
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Ruby Sass is deprecated! See https://sass-lang.com/ruby-sass for
details.
Sass makes CSS fun again. Sass is an extension of CSS, adding
nested rules, variables, mixins, selector inheritance, and more.
It's translated to well-formatted, standard CSS using the
command line tool or a web-framework plugin.

%prep
%gem_unpack
%patch -P 0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
