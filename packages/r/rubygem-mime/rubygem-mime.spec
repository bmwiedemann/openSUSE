#
# spec file for package rubygem-mime
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


%define mod_name mime
%define mod_full_name %{mod_name}-%{version}
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-mime
Version:        0.4.4
Release:        0
Summary:        Multipurpose Internet Mail Extensions (MIME) Library
License:        ISC
Group:          Development/Languages/Ruby
URL:            https://ecentryx.com/gems/mime
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5

%description
A library for building RFC compliant Multipurpose Internet Mail Extensions
(MIME) messages. It can be used to construct standardized MIME messages for
use
in client/server communications, such as Internet mail or HTTP
multipart/form-data transactions.

%prep

%build

%install
%gem_install \
  --doc-files="README.rdoc" \
  -f

%gem_packages

%changelog
