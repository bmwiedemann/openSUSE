#
# spec file for package python-notebook
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
BuildArch:      noarch
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-notebook%{psuffix}
Version:        6.2.0
Release:        0
Summary:        Jupyter Notebook interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/notebook
Source0:        https://files.pythonhosted.org/packages/source/n/notebook/notebook-%{version}.tar.gz
Source100:      python-notebook-rpmlintrc
BuildRequires:  %{python_module jupyter-core >= 4.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       jupyter-notebook = %{version}
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-argon2-cffi
Requires:       python-ipykernel
Requires:       python-ipython_genutils
Requires:       python-jupyter-client >= 5.3.4
Requires:       python-jupyter-core >= 4.6.1
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-prometheus_client
Requires:       python-pyzmq >= 17
Requires:       python-terminado >= 0.8.3
Requires:       python-tornado >= 6.1
Requires:       python-traitlets >= 4.2.1
Recommends:     python-ipywidgets
Suggests:       %{name}-latex
Provides:       python-jupyter_notebook = %{version}
Obsoletes:      python-jupyter_notebook < %{version}
%if !%{with test}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jupyter-notebook-filesystem
%endif
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Send2Trash}
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module attrs >= 17.4.0}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter-client >= 5.3.4}
BuildRequires:  %{python_module jupyter-core >= 4.6.1}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module nbval}
# Some dependency loop involving the jupyter-notebook subpackage could pull in an old version otherwise!
BuildRequires:  %{python_module notebook = %{version}}
BuildRequires:  %{python_module prometheus_client}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module requests-unixsocket}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module terminado >= 0.8.3}
BuildRequires:  %{python_module tornado >= 6.1}
BuildRequires:  %{python_module traitlets >= 4.2.1}
%ifnarch %{ix86}
# pandoc package disabled build for ix86
BuildRequires:  pandoc
%endif
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

%description    lang
Provides translations for the Jupyter notebook.

This package provides the Python module translations.

%package     -n jupyter-notebook
Summary:        Jupyter Notebook interface
Group:          Development/Languages/Python
Requires:       jupyter-ipykernel
Requires:       jupyter-jupyter-client >= 5.3.4
Requires:       jupyter-jupyter-core >= 4.6.1
Requires:       jupyter-nbconvert
Requires:       jupyter-nbformat
Requires:       jupyter-notebook-filesystem
Requires:       python3-notebook = %{version}
Conflicts:      python3-jupyter_notebook < 5.7.8
Provides:       jupyter-notebook-doc = %{version}
Obsoletes:      jupyter-notebook-doc < %{version}

%description -n jupyter-notebook
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package provides the jupyter components.

%package     -n jupyter-notebook-lang
# FIXME: consider using %%lang_package macro
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

%prep
%setup -q -n notebook-%{version}

# We don't want to run selenium tests
rm -rf notebook/tests/selenium

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp docs/resources/icon_512x512.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/JupyterNotebook.svg

for x in 16 24 32 48 64 128 256 512 ; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/
    cp docs/resources/ipynb.iconset/icon_${x}x${x}.png %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/JupyterNotebook.png
done

%{python_expand # the structure is not compatible with (python_)find_lang. Roll our own.
find %{buildroot}%{$python_sitelib}/notebook/i18n -type f -o -type l | grep -v '__init__' > lang-files
sed -E '
    s:%{buildroot}::
    s:(.*/notebook/i18n/)([^/_]+)(.*(mo|po|json)$):%lang(\2) \1\2\3:
' > %{$python_prefix}-notebook.lang < lang-files
sed -E '
    s:%{buildroot}::
    s:(.*/notebook/i18n/)([^/_]+)(.*(mo|po|json)$):%exclude \1\2\3:
' > %{$python_prefix}-notebook.lang-exclude < lang-files
find %{buildroot}%{$python_sitelib}/notebook/i18n -type d -mindepth 1 | grep -v '__pycache__' > lang-dirs
sed -E '
    s:%{buildroot}::
    s:(.*):%dir \1:
' >> %{$python_prefix}-notebook.lang < lang-dirs
sed -E '
    s:%{buildroot}::
    s:(.*):%exclude %dir \1:
' >> %{$python_prefix}-notebook.lang-exclude < lang-dirs
}

%python_clone -a %{buildroot}%{_bindir}/jupyter-bundlerextension
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbextension
%python_clone -a %{buildroot}%{_bindir}/jupyter-notebook
%python_clone -a %{buildroot}%{_bindir}/jupyter-serverextension

%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
# test_launch_socket_collision: fails because there are still servers listening
pythonall_donttest="test_launch_socket_collision"
%{python_expand # these tests call the wrong interpreter somewhere deep in the stack
if [ "$python_" != "python3_" -a "%{$python_provides}" != "python3" ]; then
  python_$python_donttest+=" or (test_kernels_api and (test_connection or test_culling))"
fi
}
%pytest -v -k "not (${pythonall_donttest} ${python_$python_donttest})"
%endif

%if !%{with test}
%post
%python_install_alternative jupyter-notebook jupyter-bundlerextension jupyter-nbextension jupyter-serverextension

%postun
%python_uninstall_alternative jupyter-notebook

%files %{python_files} -f %{python_prefix}-notebook.lang-exclude
%doc README.md
%license LICENSE
%{python_sitelib}/notebook-*-py*.egg-info
%{python_sitelib}/notebook/
%python_alternative %{_bindir}/jupyter-bundlerextension
%python_alternative %{_bindir}/jupyter-nbextension
%python_alternative %{_bindir}/jupyter-notebook
%python_alternative %{_bindir}/jupyter-serverextension

%files %{python_files lang} -f %{python_prefix}-notebook.lang
%license LICENSE

%files -n jupyter-notebook
%license LICENSE
%{_datadir}/icons/hicolor/*/apps/JupyterNotebook.*

%files -n jupyter-notebook-lang
%license LICENSE

%files -n jupyter-notebook-latex
%license LICENSE
%endif

%changelog
