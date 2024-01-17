#
# spec file for package rubygem-rdiscount
#
# Copyright (c) 2022 SUSE LLC
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

Name:           rubygem-rdiscount
Version:        2.2.7
Release:        0
%define mod_name rdiscount
%define mod_full_name %{mod_name}-%{version}
# MANUAL
Conflicts:      ruby = 1.9.2
# Please comment the ruby-devel build requirements that have the "<"
# and ">" operators. Otherwise it won't build.
# This is a manual hack until the != operator for ruby gets correctly
# translated by gem2rpm
BuildRequires:  ruby-devel > 1.9.2
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://dafoster.net/projects/rdiscount/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-rdiscount-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Fast Implementation of Gruber's Markdown in C
License:        BSD-3-Clause
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Fast Implementation of Gruber's Markdown in C.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="COPYING README.markdown" \
  -f
%gem_cleanup

%gem_packages

%changelog
