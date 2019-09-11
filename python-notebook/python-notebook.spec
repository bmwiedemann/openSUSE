#
# spec file for package python-notebook
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
%define doc_ver 5.7.6
Name:           python-notebook
Version:        5.7.8
Release:        0
Summary:        Jupyter Notebook interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/notebook
Source0:        https://files.pythonhosted.org/packages/source/n/notebook/notebook-%{version}.tar.gz
Source1:        https://media.readthedocs.org/pdf/jupyter-notebook/%{doc_ver}/jupyter-notebook.pdf
Source2:        https://media.readthedocs.org/htmlzip/jupyter-notebook/%{doc_ver}/jupyter-notebook.zip
Source100:      python-notebook-rpmlintrc
BuildRequires:  %{python_module jupyter_core >= 4.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-notebook = %{version}
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-ipykernel
Requires:       python-ipython_genutils
Requires:       python-jupyter_client >= 5.2.0
Requires:       python-jupyter_core >= 4.4.0
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-prometheus_client
Requires:       python-terminado >= 0.8.1
Requires:       python-tornado >= 4
Requires:       python-traitlets >= 4.2.1
Recommends:     python-ipywidgets
Suggests:       %{name}-latex
Provides:       python-jupyter_notebook = %{version}
Obsoletes:      python-jupyter_notebook < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Send2Trash}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter_client >= 5.2.0}
BuildRequires:  %{python_module jupyter_core >= 4.4.0}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module nose-exclude}
BuildRequires:  %{python_module nose_warnings_filters}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module prometheus_client}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module terminado >= 0.8.1}
BuildRequires:  %{python_module tornado >= 4}
BuildRequires:  %{python_module traitlets >= 4.2.1}
# /SECTION
# SECTION Python 2.7 test requirements
BuildRequires:  python-ipaddress
BuildRequires:  python-mock
# /SECTION
%ifpython2
Requires:       python-ipaddress
%endif
%python_subpackages

%description
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package provides the python interface.

%package        lang
# FIXME: consider using %%lang_package macro
Summary:        Translations for the Jupyter Notebook
Group:          System/Localization
Requires:       python-notebook = %{version}
Provides:       python-jupyter_notebook-lang = %{version}
Provides:       python-notebook-lang-all = %{version}
Obsoletes:      python-jupyter_notebook-lang < %{version}
Requires:       jupyter-notebook-lang = %{version}

%description    lang
Provides translations for the Jupyter notebook.

This package provides the Python module translations.

%package     -n jupyter-notebook
Summary:        Jupyter Notebook interface
Group:          Development/Languages/Python
Requires:       jupyter-ipykernel
Requires:       jupyter-jupyter_client >= 5.2.0
Requires:       jupyter-jupyter_core >= 4.4.0
Requires:       jupyter-nbconvert
Requires:       jupyter-nbformat
Requires:       jupyter-notebook-filesystem
Requires:       python3-notebook = %{version}
Conflicts:      python3-jupyter_notebook < 5.7.8

%description -n jupyter-notebook
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package provides the jupyter components.

%package     -n jupyter-notebook-lang
Summary:        Translations for the Jupyter Notebook
Group:          System/Localization
Requires:       jupyter-notebook = %{version}
Requires:       python3-notebook-lang = %{version}
Provides:       jupyter-notebook-lang-all = %{version}

%description -n jupyter-notebook-lang
Provides translations for the Jupyter notebook.

This package provides the jupyter component translations.

%package     -n jupyter-notebook-latex
Summary:        LaTeX support for the Jupyter Notebook
Group:          Development/Languages/Python
Requires:       jupyter-nbconvert-latex
Requires:       jupyter-notebook = %{version}
Provides:       %{python_module jupyter_notebook-latex = %{version}}
Provides:       %{python_module notebook-latex = %{version}}
Obsoletes:      %{python_module jupyter_notebook-latex < %{version}}

%description -n jupyter-notebook-latex
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package pulls in the LaTeX dependencies for the Jupyter Notebook.

%package     -n jupyter-notebook-doc
Summary:        Documentation for Jupyter's notebook
Group:          Documentation/Other
Provides:       %{python_module jupyter_notebook-doc = %{version}}
Provides:       %{python_module notebook-doc = %{version}}
Obsoletes:      %{python_module jupyter_notebook-doc < %{version}}

%description -n jupyter-notebook-doc
Documentation and help files for Jupyter's notebook.

%prep
%setup -q -n notebook-%{version}
unzip %{SOURCE2} -d docs
mv docs/jupyter-notebook-* docs/html
rm docs/html/.buildinfo
%fdupes docs/html/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp docs/resources/icon_512x512.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/JupyterNotebook.svg

for x in 16 24 32 48 64 128 256 512 ; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/
    cp docs/resources/ipynb.iconset/icon_${x}x${x}.png %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/JupyterNotebook.png
done

mkdir -p %{buildroot}%{_docdir}/jupyter-notebook/

cp -r %{SOURCE1} %{buildroot}%{_docdir}/jupyter-notebook/
cp -r docs/html %{buildroot}%{_docdir}/jupyter-notebook/

%fdupes %{buildroot}%{_docdir}/jupyter-notebook/html/

%check
export LANG=en_US.UTF-8
%python_expand nosetests-%{$python_bin_suffix} --exclude-dir notebook/tests/selenium

%files %{python_files}
%doc README.md
%license COPYING.md
%{python_sitelib}/notebook-*-py*.egg-info
%{python_sitelib}/notebook/
%exclude %{python_sitelib}/notebook/i18n/*/

%files %{python_files lang}
%license COPYING.md
%lang(fr_FR) %{python_sitelib}/notebook/i18n/fr_FR/
%lang(zh_CN) %{python_sitelib}/notebook/i18n/zh_CN/

%files -n jupyter-notebook
%license COPYING.md
%{_bindir}/jupyter-bundlerextension
%{_bindir}/jupyter-nbextension
%{_bindir}/jupyter-notebook
%{_bindir}/jupyter-serverextension
%{_datadir}/icons/hicolor/*/apps/JupyterNotebook.*

%files -n jupyter-notebook-lang
%license COPYING.md

%files -n jupyter-notebook-latex
%license COPYING.md

%files -n jupyter-notebook-doc
%license COPYING.md
%dir %{_docdir}/jupyter-notebook/
%{_docdir}/jupyter-notebook/jupyter-notebook.pdf
%{_docdir}/jupyter-notebook/html/

%changelog
