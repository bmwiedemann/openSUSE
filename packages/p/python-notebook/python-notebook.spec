#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
BuildArch:      noarch
%endif

%define         plainpython python
#
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-notebook%{psuffix}
Version:        6.5.2
Release:        0
Summary:        Jupyter Notebook interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/notebook
Source0:        https://files.pythonhosted.org/packages/source/n/notebook/notebook-%{version}.tar.gz
Source100:      python-notebook-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module jupyter-packaging >= 0.9}
BuildRequires:  %{python_module nbclassic >= 0.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros >= 20210929
Requires:       jupyter-notebook = %{version}
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-argon2-cffi
Requires:       python-ipykernel
Requires:       python-ipython_genutils
Requires:       python-jupyter-client >= 5.3.4
Requires:       python-jupyter-core >= 4.6.1
Requires:       python-nbclassic >= 0.4.7
Requires:       python-nbconvert >= 5
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
BuildRequires:  update-desktop-files
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%endif
%if %{with test}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module notebook = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-unixsocket}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module testpath}
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
Requires:       %{plainpython}(abi) = %{python_version}
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
%autosetup -p1 -n notebook-%{version}
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
# https://github.com/jupyter/notebook/issues/6501, use the same grouping as nbclassic
%python_group_libalternatives jupyter-notebook jupyter-bundlerextension jupyter-nbextension jupyter-serverextension
%suse_update_desktop_file jupyter-notebook

%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
# required when testing with jupyter_core 4.9.1
export PYTHONNOUSERSITE=1
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
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter-notebook

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
%{_datadir}/icons/hicolor/*/apps/notebook.svg
%{_datadir}/applications/jupyter-notebook.desktop

%files -n jupyter-notebook-lang
%license LICENSE

%files -n jupyter-notebook-latex
%license LICENSE
%endif

%changelog
