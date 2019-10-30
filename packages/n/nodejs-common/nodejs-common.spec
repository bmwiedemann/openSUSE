#
# spec file for package nodejs-common
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


###########################################################
#
#   WARNING! WARNING! WARNING! WARNING! WARNING! WARNING!
#
# This spec file is generated from a template hosted at
# https://github.com/AdamMajer/nodejs-packaging
#
###########################################################

Name:           nodejs-common
Version:        3.0
Release:        0
Summary:        Common files for the NodeJS ecosystem
License:        MIT
Group:          Development/Languages/NodeJS
Url:            https://github.com/AdamMajer/nodejs-packaging
Source1:        node.c
Source2:        LICENSE
Requires:       nodejs
Conflicts:      nodejs4 < 4.8.4
Conflicts:      nodejs6 < 6.11.1
Conflicts:      nodejs7 < 7.10.1
Conflicts:      nodejs8 < 8.1.4
BuildRequires:  gcc

%description
Common NodeJS files that allow recursive invocation of Node executable
while retaining the same codestream version.

%prep
%build
cp %{S:2} .
gcc ${RPM_OPT_FLAGS} -o node %{S:1}

%install
install -D -m 0755 node %{buildroot}%{_bindir}/node
ln node %{buildroot}%{_bindir}/npm
ln node %{buildroot}%{_bindir}/npx

%files
%license LICENSE
%{_bindir}/node
%{_bindir}/npm
%{_bindir}/npx

%changelog
