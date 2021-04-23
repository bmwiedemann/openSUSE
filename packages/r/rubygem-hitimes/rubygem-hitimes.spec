#
# spec file for package rubygem-hitimes
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

Name:           rubygem-hitimes
Version:        2.0.0
Release:        0
%define mod_name hitimes
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.2.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
URL:            http://github.com/copiousfreetime/hitimes
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-hitimes-rpmlintrc
Source2:        gem2rpm.yml
Summary:        A fast, high resolution timer library for recording peformance
License:        ISC
Group:          Development/Languages/Ruby

%description
A fast, high resolution timer library for recording peformance metrics. *
(http://github.com/copiousfreetime/hitimes) *
(http://github.com/copiousfreetime/hitimes) * email jeremy at copiousfreetime
dot org * `git clone url git://github.com/copiousfreetime/hitimes.git`.

%prep

%build

%install
%gem_install \
  --doc-files="HISTORY.md LICENSE README.md" \
  -f

%gem_packages

%changelog
