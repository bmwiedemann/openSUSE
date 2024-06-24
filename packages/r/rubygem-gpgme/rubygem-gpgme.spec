#
# spec file for package rubygem-gpgme
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

Name:           rubygem-gpgme
Version:        2.0.24
Release:        0
%define mod_name gpgme
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  libassuan-devel >= 2.0.2
BuildRequires:  libgpg-error-devel >= 1.8
BuildRequires:  libgpgme-devel >= 1.2.0
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
URL:            http://github.com/ueno/ruby-gpgme
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-gpgme-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Ruby binding of GPGME
License:        LGPL-2.1-or-later

%description
Ruby-GPGME is a Ruby language binding of GPGME (GnuPG
Made Easy). GnuPG Made Easy (GPGME) is a library designed to make access to
GnuPG easier for applications. It provides a High-Level Crypto API for
encryption, decryption, signing, signature verification and key management.

%prep

%build

%install
# MANUAL
export RUBY_GPGME_USE_SYSTEM_LIBRARIES=1
# /MANUAL
%gem_install \
  -f
%gem_cleanup

%gem_packages

%changelog
