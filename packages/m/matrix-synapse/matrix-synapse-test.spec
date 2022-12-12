#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


# synapse only supports python >= 3.5, which is not available on pre-15 Leap.
# However, future versions of matrix-synapse will no longer support python2 and
# continued use of python2 is not recommended, so we only use the primary
# python3 flavor. As a result, at no point do we have two versions of the
# matrix-synapse package.

# Disable debug packages since we're not installing anything.
%define debug_package %{nil}

%define         pkgname matrix-synapse
Name:           %{pkgname}-test
Version:        1.73.0
Release:        0
Summary:        Test package for %{pkgname}
License:        Apache-2.0
BuildRequires:  %{pkgname} == %{version}

%description
.

%prep
touch %{_sourcedir}/%{pkgname}

%build

%install

%check

# Following tests disabled which would need to be run as 'synapse' user which
# we can not do easily (or at all) within RPM
# Generate a sample config.
#python3 -m synapse.app.homeserver \
#	--generate-config \
#	--server localhost \
#	--config-path dummy-homeserver.yaml \
#	--report-stats no

# Start synapse and try to register a user (basic smoke-test).
# register_new_matrix_user doesn't seem to work inside check so we have to
# manually run the module.
#synctl start dummy-homeserver.yaml
#sleep 2s
#python3 -m synapse._scripts.register_new_matrix_user \
#	http://localhost:8008 \
#	--config dummy-homeserver.yaml \
#	--admin --user opensuse --password opensuse
#synctl stop dummy-homeserver.yaml

%changelog
