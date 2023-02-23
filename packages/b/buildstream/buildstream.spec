#
# spec file for package buildstream
#
# Copyright (c) 2023 SUSE LLC
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


Name:           buildstream
Version:        1.6.9
Release:        0
Summary:        A framework for modelling build pipelines in YAML
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            https://buildstream.build/
Source0:        https://github.com/apache/buildstream/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  bubblewrap
BuildRequires:  fdupes
BuildRequires:  python3-base >= 3.7
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  typelib-1_0-OSTree-1_0
Requires:       bubblewrap
Requires:       python3-base >= 3.7
Requires:       python3-click
Requires:       python3-gobject
Requires:       python3-grpcio >= 1.34
Requires:       python3-psutil
Requires:       python3-ruamel.yaml >= 0.16
Requires:       typelib-1_0-OSTree-1_0

BuildArch:      noarch

%description
BuildStream is a flexible and extensible framework for the modelling of
build and CI pipelines in a declarative YAML format, written in python.

%prep
%autosetup -p1
# Fix the shebang
find -type f -exec sed -i 's|/usr/bin/env python3|%{_bindir}/python3|' {} \;
# https://github.com/apache/buildstream/commit/b27b592a64a7050a205fa17c807fac193990b2a7
sed -i 's:pytest-runner::' setup.py

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%license COPYING
%doc HACKING.rst MAINTAINERS NEWS README.rst
%{_bindir}/bst
%{_bindir}/bst-artifact-server
%{_datadir}/bash-completion/completions/bst
%{python3_sitelib}/BuildStream-*-py3.*.egg-info
%{python3_sitelib}/buildstream
%{_mandir}/man1/bst*%{ext_man}

%changelog
