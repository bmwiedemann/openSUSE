#
# spec file for package rubygem-actionmailer-8.0
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

Name:           rubygem-actionmailer-8.0
Version:        8.0.0.1
Release:        0
%define mod_name actionmailer
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -8.0
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 3.2.0}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://rubyonrails.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Email composition and delivery framework (part of Rails)
License:        MIT

%description
Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%prep

%build

%install
%gem_install \
  --no-rdoc --no-ri \
  --doc-files="CHANGELOG.md MIT-LICENSE README.rdoc" \
  -f

%gem_packages

%changelog
