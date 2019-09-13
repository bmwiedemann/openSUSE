#
# spec file for package python-nbformat
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-nbformat
Version:        4.4.0
%define doc_ver 4.4.0
Release:        0
Summary:        The Jupyter Notebook format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/nbformat
Source:         https://files.pythonhosted.org/packages/source/n/nbformat/nbformat-%{version}.tar.gz
Source1:        https://buildmedia.readthedocs.org/media/pdf/nbformat/%{doc_ver}/nbformat.pdf
Source2:        https://buildmedia.readthedocs.org/media/htmlzip/nbformat/%{doc_ver}/nbformat.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jsonschema > 2.5.0}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module traitlets >= 4.1}
# /SECTION
Requires:       jupyter-nbformat = %{version}
Requires:       python-ipython_genutils
Requires:       python-jsonschema > 2.5.0
Requires:       python-jupyter_core
Requires:       python-traitlets >= 4.1
Provides:       python-jupyter_nbformat = %{version}
# Change <= to < with next release after 4.4
Obsoletes:      python-jupyter_nbformat <= %{version}
BuildArch:      noarch
%python_subpackages

%description
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.

This package provides the python interface.

%package     -n jupyter-nbformat
Summary:        The Jupyter Notebook format
Requires:       jupyter-jupyter_core
Requires:       python3-nbformat = %{version}
# uncomment with next release after 4.4:
# Conflicts:      python3-jupyter_nbformat <= 4.5

%description -n jupyter-nbformat
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.

This package provides the jupyter components.

%package     -n jupyter-nbformat-doc
Summary:        Documentation for the Jupyter Notebook format
Requires:       jupyter-nbformat = %{version}
Provides:       python-jupyter_nbformat-doc = %{version}
Obsoletes:      python-jupyter_nbformat-doc <= %{version}
Provides:       %{python_module jupyter_nbformat-doc = %{version}}
Obsoletes:      %{python_module jupyter_nbformat-doc <= %{version}}
Provides:       %{python_module nbformat-doc = %{version}}
Provides:       python-nbformat-html = %{version}
Provides:       python-nbformat-pdf = %{version}
Obsoletes:      python-nbformat-html < %{version}
Obsoletes:      python-nbformat-pdf < %{version}

%description -n jupyter-nbformat-doc
This package contains documentation and help files for the Jupyter
Notebook format

%prep
%setup -q -n nbformat-%{version}
unzip %{SOURCE2} -d docs
mv docs/nbformat-* docs/html
rm docs/html/.buildinfo

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_docdir}/jupyter-nbformat

cp %{SOURCE1} %{buildroot}%{_docdir}/jupyter-nbformat/
cp -r docs/html %{buildroot}%{_docdir}/jupyter-nbformat/

%fdupes %{buildroot}%{_docdir}/jupyter-nbformat/

%check
%pytest -k "not TestNotary and not SQLiteSignatureStoreTests"

%files %{python_files}
%license COPYING.md
%doc README.md
%{python_sitelib}/nbformat-%{version}-py*.egg-info
%{python_sitelib}/nbformat/
# Move this to jupyter-nbformat with next release (after 4.4)
%python3_only %{_bindir}/jupyter-trust

%files -n jupyter-nbformat
%license COPYING.md

%files -n jupyter-nbformat-doc
%license COPYING.md
%{_docdir}/jupyter-nbformat/

%changelog
