#
# spec file for package buildstream
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


Name:           buildstream
Version:        2.4.0
Release:        0
Summary:        A framework for modelling build pipelines in YAML
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            https://buildstream.build/
Source0:        https://github.com/apache/buildstream/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  bubblewrap
BuildRequires:  fdupes
BuildRequires:  python3-Cython
BuildRequires:  python3-base >= 3.7
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  typelib-1_0-OSTree-1_0
Requires:       bubblewrap
Requires:       python3-Jinja2
Requires:       python3-base >= 3.7
Requires:       python3-click
Requires:       python3-gobject
Requires:       python3-grpcio >= 1.34
Requires:       python3-pluginbase
Requires:       python3-protobuf
Requires:       python3-psutil
Requires:       python3-ruamel.yaml >= 0.16
Requires:       python3-ruamel.yaml.clib
Requires:       python3-setuptools
Requires:       python3-ujson
Requires:       typelib-1_0-OSTree-1_0
#Requires:       python3-pyroaring

%description
BuildStream is a flexible and extensible framework for the modelling of
build and CI pipelines in a declarative YAML format, written in python.

%prep
%autosetup -p1
# Fix the shebang
find -type f -exec sed -i 's|/usr/bin/env python3|%{_bindir}/python3|' {} \;

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitearch}

%files
%license LICENSE
%doc COMMITTERS.rst CONTRIBUTING.rst NEWS NOTICE README.rst
%{_bindir}/bst
%{_datadir}/bash-completion/completions/bst
%{python3_sitearch}/BuildStream-*-py3.*.egg-info
%{python3_sitearch}/buildstream
%{_mandir}/man1/bst*%{ext_man}

%changelog
