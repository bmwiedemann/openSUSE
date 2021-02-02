#
# spec file for package local-npm-registry
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           local-npm-registry
Version:        0.0.2
Release:        0
Summary:        Localhost-only version of NPM registry
License:        GPL-3.0-or-later
Url:            https://github.com/openSUSE/npm-localhost-proxy
Source:         https://github.com/openSUSE/npm-localhost-proxy/releases/download/v%{version}/local_npm_registry-v%{version}.tar.gz
Requires:       npm-default
BuildArch:      noarch

%description
localhost-only npm registry serves NPM packages on localhost
address allowing running of "npm install" in a non-networked
environment

%prep
%autosetup -p1 -n local_npm_registry-v%{version}

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
cp -r dist node_modules %{buildroot}%{_datadir}/%{name}
cat > %{buildroot}%{_bindir}/local-npm-registry << EOF
#!/bin/sh

if [ "x$QUILT_COMMAND" = "xsetup" ]
then
        echo "Run in setup mode. 'npm install' skipped. Run 'npm ci' manually."
        cp "$RPM_SOURCE_DIR/package-lock.json" .
        exit 0
fi

exec %{_bindir}/node %{_datadir}/%{name}/dist/ "\$@"
EOF

%files
%defattr(-,root,root)
%license COPYING
%doc README.md
%attr(755,root,root) %{_bindir}/local-npm-registry
%{_datadir}/%{name}

%changelog

