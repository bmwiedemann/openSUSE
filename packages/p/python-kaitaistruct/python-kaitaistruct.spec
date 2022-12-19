#
# spec file for package python-kaitaistruct
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


Name:           python-kaitaistruct
Version:        0.10
Release:        0
Summary:        Python library for kaitaistruct
License:        MIT
URL:            https://kaitai.io
Source:         https://files.pythonhosted.org/packages/source/k/kaitaistruct/kaitaistruct-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library implements the Kaitai Struct API for Python.

Kaitai Struct is a declarative language used to describe various binary data
structures, laid out in files or in memory: i.e. binary file formats, network
stream packet formats, etc.

It is similar to Python’s [construct] and [Construct3], but it is
language-agnostic.
The format description is done in YAML-based .ksy format, which then can be
compiled into a wide range of target languages.

%prep
%setup -q -n kaitaistruct-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(0644,root,root,-)
%doc README.md
%license LICENSE
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/kaitaistruct.py*
%{python_sitelib}/kaitaistruct-%{version}*-info

%changelog
