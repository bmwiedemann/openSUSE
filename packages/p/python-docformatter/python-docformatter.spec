#
# spec file for package python-docformatter
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-docformatter
Version:        1.7.8
Release:        0
Summary:        Utility to re-format docstrings per PEP 257
License:        MIT
URL:            https://github.com/myint/docformatter
Source:         https://github.com/PyCQA/docformatter/archive/refs/tags/v%{version}.tar.gz#/docformatter-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Do not require virtualenvs to run the tests
Patch0:         do-not-require-venv.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-charset-normalizer >= 3.0.0
%if %{python_version_nodots} < 311
Requires:       python-tomli >= 2.0.0
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.4.0}
BuildRequires:  %{python_module charset-normalizer >= 3.0.0}
%if %{python_version_nodots} < 311
BuildRequires:  %{python_module tomli >= 2.0.0}
%endif
# /SECTION
%python_subpackages

%description
Docformatter currently automatically formats docstrings to follow a
subset of the PEP 257 conventions. Below are the relevant items quoted
from PEP 257.

- For consistency, always use triple double quotes around docstrings.
- Triple quotes are used even though the string fits on one line.
- Multi-line docstrings consist of a summary line just like a one-line
  docstring, followed by a blank line, followed by a more elaborate
  description.
- The BDFL recommends inserting a blank line between the last paragraph
  in a multi-line docstring and its closing quotes, placing the closing
  quotes on a line by themselves.

docformatter also handles some of the PEP 8 conventions.

- Don't write string literals that rely on significant trailing
  whitespace. Such trailing whitespace is visually indistinguishable
  and some editors (or more recently, reindent.py) will trim them.

%prep
%autosetup -p1 -n docformatter-%{version}
sed -i -e '/^#!\//, 1d' src/docformatter/*.py
chmod -x src/docformatter/__main__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/docformatter
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export BUILDROOT=%{buildroot}
%pytest

%post
%python_install_alternative docformatter

%postun
%python_uninstall_alternative docformatter

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/docformatter
%{python_sitelib}/docformatter
%{python_sitelib}/docformatter-%{version}.dist-info

%changelog
