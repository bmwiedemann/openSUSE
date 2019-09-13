#
# spec file for package jupyter
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


Name:           jupyter
Version:        1.0.0
Release:        0
Summary:        Environment for interactive computing
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter/jupyter-%{version}.tar.gz
Source1:        https://buildmedia.readthedocs.org/media/pdf/jupyter/latest/jupyter.pdf
Source2:        https://buildmedia.readthedocs.org/media/htmlzip/jupyter/latest/jupyter.zip
BuildRequires:  fdupes
BuildRequires:  jupyter-ipykernel
BuildRequires:  jupyter-ipywidgets
BuildRequires:  jupyter-jupyter_console
BuildRequires:  jupyter-jupyter_core
BuildRequires:  jupyter-nbconvert
BuildRequires:  jupyter-notebook
BuildRequires:  jupyter-qtconsole
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  unzip
Requires:       jupyter-jupyter_core
Recommends:     jupyter-ipykernel
Recommends:     jupyter-ipywidgets
Recommends:     jupyter-jupyter_console
Recommends:     jupyter-nbconvert
Recommends:     jupyter-notebook
Recommends:     jupyter-qtconsole
Provides:       python3-jupyter = %{version}
Obsoletes:      python3-jupyter <= %{version}
BuildArch:      noarch

%description
Jupyter is an environment for interactive computing in multiple languages.
It includes a console, a browser-based notebook format, and support for
dozens of languages through the use of language-specific kernels.

Jupyter is an evolution and modularization of the IPython project, separating
out the python3-specific parts from the language-agnostic parts.

This package pulls in the main Jupyter system, including the notebook,
qtconsole, and the IPython kernel.  Additional components and kernels
can be installed separately.

%package        doc
Summary:        HTML documentation for %{name}
Group:          Development/Languages/Python
Provides:       %{name}-doc-pdf = %{version}
Provides:       %{name}-doc-html = %{version}
Provides:       %{python_module %{name}-doc = %{version}}
Provides:       %{python_module %{name}-doc-pdf = %{version}}
Provides:       %{python_module %{name}-doc-html = %{version}}
# Change from <= to < when (and if) there is a next release after 1.0.0
Obsoletes:      %{name}-doc-pdf <= %{version}
Obsoletes:      %{name}-doc-html <= %{version}
Obsoletes:      %{python_module %{name}-doc-pdf <= %{version}}
Obsoletes:      %{python_module %{name}-doc-html <= %{version}}

%description    doc
Documentation and help files for %{name}.

%prep
%setup -q -n jupyter-%{version}
unzip %{SOURCE2} -d docs
mv docs/jupyter-* docs/html
rm docs/html/.buildinfo

%build
%python3_build

%install
%python3_install

# This is provided by jupyter_core now
rm -f %{buildroot}%{python3_sitelib}/jupyter.py*
rm -rf %{buildroot}%{python3_sitelib}/__pycache__/

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}

cp %{SOURCE1} %{buildroot}%{_docdir}/%{name}/
cp -r docs/html %{buildroot}%{_docdir}/%{name}/

%fdupes %{buildroot}%{_docdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/jupyter-%{version}-py*.egg-info

%files doc
%license LICENSE
%doc README.md
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/jupyter.pdf

%changelog
