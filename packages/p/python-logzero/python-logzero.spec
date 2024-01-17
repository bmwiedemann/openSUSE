#
# spec file for package python-logzero
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-logzero
Version:        1.7.0
Release:        0
Summary:        A logging module for Python
License:        MIT
URL:            https://github.com/metachris/logzero
Source:         https://files.pythonhosted.org/packages/source/l/logzero/logzero-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  python3-Sphinx
%python_subpackages

%package -n python-logzero-doc
Summary:        Documentation files for %name

%description
* Logs to console and/or file.
* Pretty formatting, including level-specific colors in the console.
* Robust against str/bytes encoding problems, works with all kinds of character encodings and special characters.
* Heavily inspired by the Tornado web framework.

%description -n python-logzero-doc
Documentation files for %name.

%prep
%setup -q -n logzero-%{version}

%build
%python_build
pushd docs
make html
rm _build/html/.buildinfo
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%pytest

%files %{python_files}
%doc README.md HISTORY.md
%%license LICENSE
%{python_sitelib}/*

%files -n python-logzero-doc
%doc docs/_build/html

%changelog
