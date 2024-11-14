#
# spec file for package nodejs-common
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


###########################################################
#
#   WARNING! WARNING! WARNING! WARNING! WARNING! WARNING!
#
# This spec file is generated from a template hosted at
# https://github.com/AdamMajer/nodejs-packaging
#
###########################################################

%define NODEJS_CURRENT  22
%define NODEJS_LTS      22

%if 0%{?suse_version} > 1500 || 0%{?fedora_version}
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

# SLE-12 variants
%if 0%{?suse_version} < 1500
%define default_node_ver 16
%endif

%if 0%{?suse_version} == 1500

# SLE-15 variants, variation based on SP
%if 0%{?sle_version} >= 150000 && 0%{?sle_version} < 150200
%define default_node_ver 10
%endif

%if 0%{?sle_version} >= 150200 && 0%{?sle_version} < 150300
%define default_node_ver 12
%endif

%if 0%{?sle_version} >= 150300 && 0%{?sle_version} < 150400
%define default_node_ver 14
%endif

%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 150500
%define default_node_ver 16
%endif

%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 150600
%define default_node_ver 18
%endif

%if 0%{?sle_version} >= 150600 && 0%{?sle_version} < 150700
%define default_node_ver 20
%endif

%if 0%{?sle_version} >= 150700
%define default_node_ver 22
%endif

# SLE-15 variants
%endif

%if 0%{?suse_version} == 1600
# SLFO variants
%define default_node_ver %NODEJS_LTS
%endif

# TW
%if 0%{?suse_version} >= 1699
%define default_node_ver %NODEJS_CURRENT
%endif

Name:           nodejs-common
Version:        6.1
Release:        0
Summary:        Common files for the NodeJS ecosystem
License:        MIT
Group:          Development/Languages/NodeJS
URL:            https://github.com/AdamMajer/nodejs-packaging
Source1:        node.c
Source2:        LICENSE
Requires:       nodejs
Conflicts:      nodejs4 < 4.8.4
Conflicts:      nodejs6 < 6.11.1
Conflicts:      nodejs7 < 7.10.1
Conflicts:      nodejs8 < 8.1.4
BuildRequires:  gcc
%if %{with libalternatives}
BuildRequires:  libalternatives-devel
%define libalternatives_cflags -DHAVE_LIBALTERNATIVES_H
%define libalternatives_lflags -lalternatives
%endif

%description
Common NodeJS files that allow recursive invocation of Node executable
while retaining the same codestream version.

%package -n nodejs-default
Summary:        Default version of nodejs
Group:          Development/Languages/NodeJS
Requires:       nodejs%{default_node_ver}
Requires:       nodejs-common
Provides:       nodejs = %default_node_ver
Provides:       nodejs(engine) = %default_node_ver

%description -n nodejs-default
Depends on the most current and recommended version of nodejs for
the current architecture and codestream.

%package -n npm-default
Summary:        Default version of npm
Group:          Development/Languages/NodeJS
Requires:       nodejs-default
Requires:       npm%{default_node_ver}
Provides:       npm = %default_node_ver

%description -n npm-default
Depends on the npm version associated with the current default
version of nodejs for the current architecture and codestream.

%package -n nodejs-devel-default
Summary:        Headers for default version of nodejs
Group:          Development/Languages/NodeJS
Requires:       nodejs%{default_node_ver}-devel
Requires:       npm-default
Provides:       nodejs-devel = %default_node_ver

%description -n nodejs-devel-default
Depends on the most current and up-to-date version of nodejs for
the current architecture and codestream.

%package -n corepack-default
Summary:        Default version of corepack
Group:          Development/Languages/NodeJS
Requires:       corepack%{default_node_ver}
Requires:       npm-default
Provides:       corepack = %default_node_ver

%description -n corepack-default
Depends on the corepack version associated with the current default
version of nodejs for the current architecture and codestream.

%prep

%build
cp %{S:2} .
gcc ${RPM_OPT_FLAGS} %?libalternatives_cflags -o node %{S:1} %?libalternatives_lflags

echo "Default Node version: " %{default_node_ver}

%install
install -D -m 0755 node %{buildroot}%{_bindir}/node
ln node %{buildroot}%{_bindir}/npm
ln node %{buildroot}%{_bindir}/npx
ln node %{buildroot}%{_bindir}/corepack

%files
%license LICENSE
%{_bindir}/node
%{_bindir}/npm
%{_bindir}/npx
%{_bindir}/corepack

%files -n nodejs-default

%files -n npm-default

%files -n nodejs-devel-default

%files -n corepack-default

%changelog
