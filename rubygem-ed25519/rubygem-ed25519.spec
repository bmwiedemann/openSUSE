#
# spec file for package rubygem-ed25519
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-ed25519
Version:        1.2.4
Release:        0
%define mod_name ed25519
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/crypto-rb/ed25519
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-ed25519-rpmlintrc
Source2:        gem2rpm.yml
Summary:        An efficient digital signature library providing the Ed25519
License:        MIT
Group:          Development/Languages/Ruby

%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGES.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
