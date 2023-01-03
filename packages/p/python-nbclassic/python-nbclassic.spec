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
%endif
# this conditional is used in the python-rpm-macros, but `osc build --without libalternatives` won't work
%bcond_without libalternatives
Name:           python-nbclassic%{psuffix}
Version:        0.4.8
Release:        0
Summary:        Jupyter Notebook as a Jupyter Server Extension
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/nbclassic
# The github archive has the nbclassic tests
Source0:        https://github.com/jupyterlab/nbclassic/archive/v%{version}.tar.gz#/nbclassic-%{version}-gh.tar.gz
# The wheel has the notebook 6 JS stuff
Source1:        https://files.pythonhosted.org/packages/py3/n/nbclassic/nbclassic-%{version}-py3-none-any.whl
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros >= 20210929
BuildRequires:  update-desktop-files
Requires:       jupyter-nbclassic = %{version}
Requires:       python-Jinja2
Requires:       python-Send2Trash >= 1.8.0
Requires:       python-argon2-cffi
Requires:       python-ipykernel
Requires:       python-ipython_genutils
Requires:       python-jupyter-client >= 6.1.1
Requires:       python-jupyter-core >= 4.6.1
Requires:       python-jupyter-server >= 1.17.0
Requires:       python-nbconvert >= 5
Requires:       python-nbformat
Requires:       python-nest-asyncio >= 1.5
Requires:       python-notebook-shim >= 0.1.0
Requires:       python-prometheus-client
Requires:       python-pyzmq >= 17
Requires:       python-terminado >= 0.8.3
Requires:       python-tornado >= 6.1
Requires:       python-traitlets >= 4.2.1
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
BuildRequires:  this-specfile-is-not-functional-without-libalternatives
%endif
%if %{with test}
BuildRequires:  %{python_module nbclassic = %{version}}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-jupyter}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
NBClassic runs the Jupyter Notebook frontend on the Jupyter Server backend.

This project prepares for a future where JupyterLab and other frontends switch
to Jupyter Server for their Python Web application backend. Using this package,
users can launch Jupyter Notebook, JupyterLab and other frontends side-by-side
on top of the new Python server backend.

%package -n jupyter-nbclassic
Summary:        Jupyter Notebook as a Jupyter Server Extension
Requires:       python3-nbclassic = %{version}

%description -n jupyter-nbclassic
NBClassic runs the Jupyter Notebook frontend on the Jupyter Server backend.

This project prepares for a future where JupyterLab and other frontends switch
to Jupyter Server for their Python Web application backend. Using this package,
users can launch Jupyter Notebook, JupyterLab and other frontends side-by-side
on top of the new Python server backend.

This package contains the jupyterlab server configuration and desktop files

%prep
%setup -q -n nbclassic-%{version}

%build
:

%if !%{with test}
%install
%pyproject_install %{SOURCE1}
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbclassic
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbclassic-bundlerextension
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbclassic-extension
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbclassic-serverextension
%{python_expand #
rm %{buildroot}%{$python_sitelib}/nbclassic/bundler/tests/resources/subdir/subsubdir/.gitkeep

%fdupes %{buildroot}%{$python_sitelib}

# the locale structure is not compatible with (python_)find_lang. Roll our own.
echo '%%dir %{$python_sitelib}/nbclassic' > %{$python_prefix}-nbclassic.files
find %{buildroot}%{$python_sitelib}/nbclassic -mindepth 1 -maxdepth 1 -not -name i18n > non-lang-files
sed 's:%{buildroot}::' >> %{$python_prefix}-nbclassic.files < non-lang-files
find %{buildroot}%{$python_sitelib}/nbclassic/i18n -type f -o -type l > lang-files
sed -E '
    s:%{buildroot}::
    s:(.*/nbclassic/i18n/)([^/_]+)(.*(mo|po|json)$):%lang(\2) \1\2\3:
' >> %{$python_prefix}-nbclassic.files < lang-files
find %{buildroot}%{$python_sitelib}/nbclassic/i18n -type d > lang-dirs
sed -E '
    s:%{buildroot}::
    s:(.*):%%dir \1:
' >> %{$python_prefix}-nbclassic.files < lang-dirs
}

%suse_update_desktop_file jupyter-nbclassic
%endif

%pre
# Remove old update-alternatives entry for transition to libalternatives
%python_libalternatives_reset_alternative jupyter-nbclassic

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files} -f %{python_prefix}-nbclassic.files
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/jupyter-nbclassic
%python_alternative %{_bindir}/jupyter-nbclassic-bundlerextension
%python_alternative %{_bindir}/jupyter-nbclassic-extension
%python_alternative %{_bindir}/jupyter-nbclassic-serverextension
%{python_sitelib}/nbclassic-%{version}*-info

%files -n jupyter-nbclassic
%license LICENSE
%{_jupyter_config} %{_jupyter_server_confdir}/nbclassic.json
%{_datadir}/icons/hicolor/*/apps/nbclassic.svg
%{_datadir}/applications/jupyter-nbclassic.desktop
%endif

%changelog
