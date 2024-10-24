#
# spec file for package rubygem-pdf-reader
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

Name:           rubygem-pdf-reader
Version:        2.12.0
Release:        0
%define mod_name pdf-reader
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/yob/pdf-reader
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A library for accessing the content of PDF files
License:        MIT
PreReq:         update-alternatives

%description
The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
