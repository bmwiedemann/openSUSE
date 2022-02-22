#
# spec file for package prosody-community-plugins
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


Name:           prosody-community-modules
Version:        0~hg4900
Release:        0
Summary:        Community and experimental modules not distributed as part of Prosody
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://modules.prosody.im/
Source:         prosody-modules-%version.tar.xz
BuildRequires:  fdupes
Requires:       prosody
Requires:       lua51-zlib

%description
Prosody Community Modules are additional modulse not shipped with the
main Prosody package. These modules are not tested with the main
server and may be in alpha or beta state. All modules shipped here may
require additional configuration by the admin.

%prep
%autosetup -n prosody-modules-%version

%build
# already in base prosody
rm -rf mod_mam

%install
d="%buildroot/%_libdir/prosody/modules"
mkdir -p "$d"
cp -a mod_* "$d/"
rm -r "$d/mod_auth_external_insecure/examples"
find "$d" -type f -name "*.lua" -exec chmod a-x {} +
%fdupes %buildroot/%_prefix

%files
%_libdir/prosody/
%license COPYING
%doc README CONTRIBUTING

%changelog
