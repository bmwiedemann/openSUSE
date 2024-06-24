#
# spec file for package rubygem-locale
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

Name:           rubygem-locale
Version:        2.1.4
Release:        0
%define mod_name locale
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/ruby-gettext/locale
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby-Locale is the pure ruby library which provides basic APIs for
License:        Ruby AND LGPL-3.0-or-later

%description
Ruby-Locale is the pure ruby library which provides basic APIs for
localization.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING ChangeLog README.rdoc" \
  -f

%gem_packages

%changelog
