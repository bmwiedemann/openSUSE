#
# spec file for package python-PyYAML
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


%{?sle15_python_module_pythons}
Name:           python-PyYAML
Version:        6.0.1
Release:        0
Summary:        YAML parser and emitter for Python
License:        MIT
URL:            https://github.com/yaml/pyyaml
Source:         https://files.pythonhosted.org/packages/source/P/PyYAML/PyYAML-%{version}.tar.gz
Patch1:         build-with-cython3.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libyaml-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
YAML is a data serialization format designed for human readability
and interaction with scripting languages. PyYAML is a YAML parser
and emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%prep
%autosetup -p1 -n PyYAML-%{version}

%build
export CFLAGS="%{optflags}"
export PYYAML_FORCE_CYTHON=1
%pyproject_wheel
# Fix example permissions.
find examples/ -type f | xargs chmod a-x

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Increase file-descriptor-count for ppc to make tests happy.
%ifarch ppc ppc64 s390 s390x
ulimit -Sn 2048
%endif
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python tests/lib/test_all.py}

%files %{python_files}
%license LICENSE
%doc CHANGES README.md examples/
%{python_sitearch}/yaml
%{python_sitearch}/_yaml
%{python_sitearch}/PyYAML-%{version}.dist-info

%changelog
