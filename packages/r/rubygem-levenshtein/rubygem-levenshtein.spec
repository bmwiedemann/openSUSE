#
# spec file for package rubygem-levenshtein
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           rubygem-levenshtein
Version:        0.2.2
Release:        0
%define mod_name levenshtein
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
Url:            http://www.erikveen.dds.nl/levenshtein/index.html
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Calculates the Levenshtein distance between two byte strings
License:        GPL-2.0
Group:          Development/Languages/Ruby

%description
Calculates the Levenshtein distance between two byte strings.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG LICENSE README" \
  -f
%gem_cleanup

%gem_packages

%changelog
