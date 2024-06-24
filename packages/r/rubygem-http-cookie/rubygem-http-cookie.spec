#
# spec file for package rubygem-http-cookie
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

Name:           rubygem-http-cookie
Version:        1.0.6
Release:        0
%define mod_name http-cookie
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/sparklemotion/http-cookie
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A Ruby library to handle HTTP Cookies based on RFC 6265
License:        MIT

%description
HTTP::Cookie is a Ruby library to handle HTTP Cookies based on RFC 6265.  It
has with security, standards compliance and compatibility in mind, to behave
just the same as today's major web browsers.  It has builtin support for the
legacy cookies.txt and the latest cookies.sqlite formats of Mozilla Firefox,
and its modular API makes it easy to add support for a new backend store.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE.txt README.md" \
  -f
# MANUAL
# drop files from the git repository
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.travis.yml' -o -name '.gitignore' \) | xargs rm
# /MANUAL

%gem_packages

%changelog
