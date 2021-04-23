#
# spec file for package rubygem-hashery
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-hashery
Version:        2.1.2
Release:        0
%define mod_name hashery
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://rubyworks.github.com/hashery
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Facets-bread collection of Hash-like classes
License:        BSD-2-Clause
Group:          Development/Languages/Ruby

%description
The Hashery is a tight collection of Hash-like classes. Included among its
many offerings are the auto-sorting Dictionary class, the efficient LRUHash,
the flexible OpenHash and the convenient KeyHash. Nearly every class is a
subclass of the CRUDHash which defines a CRUD model on top of Ruby's standard
Hash making it a snap to subclass and augment to fit any specific use case.

%prep

%build

%install
%gem_install \
  --doc-files="HISTORY.md LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
