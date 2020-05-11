#
# spec file for package rubygem-gettext
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

Name:           rubygem-gettext
Version:        3.3.5
Release:        0
%define mod_name gettext
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://ruby-gettext.github.io/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Gettext is a pure Ruby libary and tools to localize messages
License:        Ruby OR LGPL-3.0-or-later
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Gettext is a GNU gettext-like program for Ruby.
The catalog file(po-file) is same format with GNU gettext.
So you can use GNU gettext tools for maintaining.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="README.md" \
  -f

%gem_packages

%changelog
