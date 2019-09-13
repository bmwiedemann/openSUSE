#
# spec file for package rubygem-haml
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-haml
Version:        5.1.1
Release:        0
%define mod_name haml
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            http://haml.info/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        An elegant, structured (X)HTML/XML templating engine
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Haml (HTML Abstraction Markup Language) is a layer on top of HTML or XML
that's
designed to express the structure of documents in a non-repetitive, elegant,
and
easy way by using indentation rather than closing tags and allowing Ruby to be
embedded with ease. It was originally envisioned as a plugin for Ruby on
Rails,
but it can function as a stand-alone templating engine.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
