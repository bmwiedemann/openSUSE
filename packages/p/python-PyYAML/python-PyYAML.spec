#
# spec file for package python-PyYAML
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-PyYAML
Version:        6.0
Release:        0
Summary:        YAML parser and emitter for Python
License:        MIT
URL:            https://github.com/yaml/pyyaml
Source:         https://files.pythonhosted.org/packages/source/P/PyYAML/PyYAML-%{version}.tar.gz
Patch0:         setuptools.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools}
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
%setup -q -n PyYAML-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build
# Fix example permissions.
find examples/ -type f | xargs chmod a-x

%install
%python_install
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
%{python_sitearch}/PyYAML-%{version}*-info

%changelog
