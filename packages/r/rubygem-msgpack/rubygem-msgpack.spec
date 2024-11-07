#
# spec file for package rubygem-msgpack
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

Name:           rubygem-msgpack
Version:        1.7.3
Release:        0
%define mod_name msgpack
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{rubydevel >= 2.5}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            http://msgpack.org/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Source2:        rubygem-msgpack-rpmlintrc
Source3:        gem2rpm.yml
Summary:        MessagePack, a binary-based efficient data interchange format
License:        Apache-2.0

%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.

%prep

%build

%install
%gem_install \
  --doc-files="ChangeLog LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
