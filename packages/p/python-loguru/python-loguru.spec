#
# spec file for package python-loguru
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-loguru
Version:        0.7.3
Release:        0
Summary:        Python logging component with a simple interface
License:        MIT
URL:            https://github.com/Delgan/loguru
Source:         https://github.com/Delgan/loguru/archive/refs/tags/%{version}.tar.gz#/loguru-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support newer mypy than upstream
Patch0:         support-new-mypy.patch
# PATCH-FIX-UPSTREAM gh#Delgan/loguru#84023e2bd8339de95250470f422f096edcb8f7b7
Patch1:         support-python314.patch
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mypy-plugins}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-colorama
BuildArch:      noarch

%python_subpackages

%description
Python logging component providing a single object
which dispatches log messages to configured handlers.

%prep
%autosetup -p1 -n loguru-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -v tests/test_type_hinting.py
export LANG=en_US.UTF-8
if [ $(getconf LONG_BIT) = 32 ]; then
  # Threads have different references on 32-bit
  donttest=" or (test_log_formatters and thread and not thread.name)"
fi
%pytest -k "not (donttestexprprefixdummy $donttest)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/loguru
%{python_sitelib}/loguru-%{version}.dist-info

%changelog
