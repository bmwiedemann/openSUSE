#
# spec file for package rubygem-loofah
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

Name:           rubygem-loofah
Version:        2.7.0
Release:        0
%define mod_name loofah
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/flavorjones/loofah
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        HTML/XML manipulation and sanitization based on Nokogiri
License:        MIT
Group:          Development/Languages/Ruby

%description
Loofah is a general library for manipulating and transforming HTML/XML documents and fragments.
It's built on top of Nokogiri and libxml2, so it's fast and has a nice API.

Loofah excels at HTML sanitization (XSS prevention). It includes some nice HTML sanitizers,
which are based on HTML5lib's whitelist, so it most likely won't make your codes less secure.
%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md MIT-LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
