#
# spec file for package python-docformatter
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-docformatter
Version:        1.3.1
Release:        0
Summary:        Utility to re-format docstrings per PEP 257
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/myint/docformatter
Source:         https://files.pythonhosted.org/packages/source/d/docformatter/docformatter-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-untokenize
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module untokenize}
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
%setup -q -n docformatter-%{version}
sed -i -e '/^#!\//, 1d' docformatter.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/docformatter
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative docformatter

%postun
%python_uninstall_alternative docformatter

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%python_alternative %{_bindir}/docformatter
%{python_sitelib}/*

%changelog
