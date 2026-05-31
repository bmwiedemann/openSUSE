#
# spec file for package pqcverification-zypp-plugin
#
# Copyright (c) 2026 SUSE LLC
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


Name:           pqcverification-zypp-plugin
Summary:        A zypp signature check plugin for verifying pqc repository signatures
License:        GPL-2.0-only
Group:          System/Packages
Version:        1.0
Release:        0
Source0:        pqcverification
Source1:        COPYING
BuildArch:      noarch

Requires:       openssl
Requires:       (openssl >= 3.5 or oqs-provider)

%description
This package contains a plugin for zypp that allows the verification
of post-quantum repository signatures.

The check can be enabled by adding "repo_sigcheck_plugin=pqcverification"
to the repository configuration

%prep

%build
%define _lto_cflags %{nil}
cp %SOURCE1 .

%install
install -m 755 -D %SOURCE0 $RPM_BUILD_ROOT/usr/lib/zypp/plugins/sigcheck/pqcverification

%files
%license COPYING
/usr/lib/zypp

%changelog
