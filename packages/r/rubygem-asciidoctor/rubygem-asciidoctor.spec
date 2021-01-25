#
# spec file for package rubygem-asciidoctor
#
# Copyright (c) 2021 SUSE LLC
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

Name:           rubygem-asciidoctor
Version:        2.0.12
Release:        0
%define mod_name asciidoctor
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://asciidoctor.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        An implementation of the AsciiDoc text processor and publishing
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
A fast, open source text processor and publishing toolchain for converting
AsciiDoc content to HTML 5, DocBook 5, and other formats.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE" \
  -f

%gem_packages

%changelog
