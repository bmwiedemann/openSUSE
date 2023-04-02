#
# spec file for package jupyter
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


%define plainpython python
%define skip_python2 1
Name:           jupyter
Version:        1.0.0
Release:        0
Summary:        Metapackage to install all the Jupyter components in one go
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter/jupyter-%{version}.tar.gz
Source1:        https://buildmedia.readthedocs.org/media/pdf/jupyter/latest/jupyter.pdf
Source2:        https://buildmedia.readthedocs.org/media/htmlzip/jupyter/latest/jupyter.zip
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipywidgets}
#BuildRequires:  %%{python_module jupyter-client}
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module jupyter_console}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module qtconsole}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-ipykernel
Requires:       python-ipywidgets
# current notebook 6.5 requires jupyter-client < 8
#Requires:       python-jupyter-client
Requires:       python-jupyter-core
Requires:       python-jupyter_console
Requires:       python-nbconvert
Requires:       python-notebook
Requires:       python-qtconsole
Requires:       %plainpython(abi) = %{python_version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter = %{version}-%{release}
Obsoletes:      jupyter < %{version}-%{release}
%endif
BuildArch:      noarch
%python_subpackages

%description
Jupyter is an environment for interactive computing in multiple languages.
It includes a console, a browser-based notebook format, and support for
dozens of languages through the use of language-specific kernels.

Jupyter is an evolution and modularization of the IPython project, separating
out the python3-specific parts from the language-agnostic parts.

This package pulls in the main Jupyter system, including the notebook,
qtconsole, and the IPython kernel.  Additional components and kernels
can be installed separately.

%package        -n jupyter-doc
Summary:        HTML documentation for %{name}
Group:          Development/Languages/Python
Provides:       %{name}-doc-html = %{version}-%{release}
Provides:       %{name}-doc-pdf = %{version}-%{release}
Provides:       %{python_module %{name}-doc = %{version}-%{release}}
Provides:       %{python_module %{name}-doc-html = %{version}-%{release}}
Provides:       %{python_module %{name}-doc-pdf = %{version}-%{release}}
Obsoletes:      %{name}-doc-html < %{version}-%{release}
Obsoletes:      %{name}-doc-pdf < %{version}-%{release}
Obsoletes:      %{python_module %{name}-doc-html < %{version}-%{release}}
Obsoletes:      %{python_module %{name}-doc-pdf < %{version}-%{release}}

%description    -n jupyter-doc
Documentation and help files for %{name}.

%prep
%setup -q -n jupyter-%{version}
unzip %{SOURCE2} -d docs
mv docs/jupyter-* docs/html
rm docs/html/.buildinfo

%build
%python_build

%install
%python_install

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}

cp %{SOURCE1} %{buildroot}%{_docdir}/%{name}/
cp -r docs/html %{buildroot}%{_docdir}/%{name}/

%fdupes %{buildroot}%{_docdir}/%{name}/

%files %python_files
%license LICENSE
%doc README.md
%{python_sitelib}/jupyter-%{version}*-info
# This is provided by jupyter_core now
%exclude %{python_sitelib}/jupyter.py*
%pycache_only %exclude %{python_sitelib}/__pycache__/

%files -n jupyter-doc
%license LICENSE
%doc README.md
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/jupyter.pdf

%changelog
