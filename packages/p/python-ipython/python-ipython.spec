#
# spec file
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
# Python 3.6 was officiallay supported with IPython up to 7.15
%define         skip_python36 1
%bcond_without  iptest
Name:           python-ipython%{psuffix}
Version:        7.30.1
Release:        0
Summary:        Rich architecture for interactive computing with Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython/ipython
Source:         https://files.pythonhosted.org/packages/source/i/ipython/ipython-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jupyter/qtconsole/4.0.0/qtconsole/resources/icon/JupyterConsole.svg
# PATCH-FIX-UPSTREAM ipython-pr13282-py310-inspect.patch -- gh#ipython/ipython#13282, gh#ipython/ipython#13412
Patch0:         ipython-pr13282-py310-inspect.patch
# PATCH-FIX-UPSTREAM ipython-pr13371-py310-oserror.patch -- gh#ipython/ipython#13371
Patch1:         ipython-pr13371-py310-oserror.patch
BuildRequires:  %{python_module backcall}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools >= 18.5}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-Pygments
Requires:       python-backcall
Requires:       python-base >= 3.7
Requires:       python-decorator
Requires:       python-jedi >= 0.16
Requires:       python-matplotlib-inline
Requires:       python-pexpect >= 4.3
Requires:       python-pickleshare
Requires:       python-prompt_toolkit < 3.1
Requires:       python-prompt_toolkit >= 2.0
Requires:       python-traitlets >= 4.2
Recommends:     jupyter
Recommends:     python-ipykernel
Recommends:     python-ipyparallel
Recommends:     python-ipywidgets
Provides:       IPython3 = %{version}
Obsoletes:      IPython3 < %{version}
Provides:       python-IPython = %{version}
Obsoletes:      python-IPython < %{version}
Provides:       python-jupyter_ipython = %{version}
Obsoletes:      python-jupyter_ipython < %{version}
Provides:       jupyter-ipython = %{version}
Provides:       python-ipython-doc = %{version}
Obsoletes:      python-ipython-doc < %{version}
Provides:       python-jupyter_ipython-doc = %{version}
Obsoletes:      python-jupyter_ipython-doc < %{version}
Provides:       python-jupyter_ipython-doc-html = %{version}
Obsoletes:      python-jupyter_ipython-doc-html < %{version}
Provides:       python-jupyter_ipython-doc-pdf = %{version}
Obsoletes:      python-jupyter_ipython-doc-pdf < %{version}
BuildArch:      noarch
%if %{with test}
# test requirements are specified in the iptest subpackage below
BuildRequires:  %{python_module ipython-iptest = %{version}}
BuildRequires:  %{python_module testsuite}
%endif
%if !%{with test}
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%if %{with ico}
BuildRequires:  icoutils
%endif
%endif
%python_subpackages

%description
IPython provides a rich toolkit to help you make the
most out of using Python interactively. Its main
components are:

 * A powerful interactive Python shell
 * A Jupyter kernel to work with Python code in
   Jupyter notebooks and other interactive frontends.

The enhanced interactive Python shells have the
following main features:

 * Comprehensive object introspection.
 * Input history, persistent across sessions.
 * Caching of output results during a session with automatically
   generated references.
 * Extensible tab completion, with support by default for completion
   of python variables and keywords, filenames and function keywords.
 * Extensible system of ‘magic’ commands for controlling the
   environment and performing many tasks related either to IPython or
   the operating system.
 * A rich configuration system with easy switching between different
   setups (simpler than changing $PYTHONSTARTUP environment variables
   every time).
 * Session logging and reloading.
 * Extensible syntax processing for special purpose situations.
 * Access to the system shell with user-extensible alias system.
 * Easily embeddable in other Python programs and GUIs.
 * Integrated access to the pdb debugger and the Python profiler.

%package iptest
Summary:        Tools for testing packages that rely in %{name}
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-Pygments
Requires:       python-ipykernel
Requires:       python-nbformat
Requires:       python-nose >= 0.10.1
Requires:       python-numpy >= 1.17
Requires:       python-requests
Requires:       python-testpath
%if %{with libalternatives}
Requires:       alts
%endif
Provides:       python-jupyter_ipython-iptest = %{version}
Obsoletes:      python-jupyter_ipython-iptest < %{version}

%description iptest
This package provides the iptest command, which is used for
testing software that uses %{name}.

%prep
%autosetup -p1 -n ipython-%{version}

%build
%python_build

%if !%{with test}
%if %{with ico}
pushd scripts
icotool -x ipython.ico
icotool -x ipython_nb.ico
popd
%endif
%endif

%install
%if !%{with test}
%python_install

%python_clone -a %{buildroot}%{_bindir}/ipython
%python_clone -a %{buildroot}%{_bindir}/ipython3

%if %{with iptest}
%python_clone -a %{buildroot}%{_bindir}/iptest
%python_clone -a %{buildroot}%{_bindir}/iptest3
%else
rm %{buildroot}%{_bindir}/iptest*
%endif

# must clone after copy
cp %{buildroot}%{_mandir}/man1/ipython{,3}.1
%python_clone -a %{buildroot}%{_mandir}/man1/ipython.1
%python_clone -a %{buildroot}%{_mandir}/man1/ipython3.1

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
%python_expand cp %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/IPython-%{$python_bin_suffix}.svg
%if %{with ico}
# Install the icons
for x in 16 24 32 48 256 ; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/
    ipyf=(scripts/ipython_*_${x}x${x}x32.png)
    ipynbf=(scripts/ipython_nb_*_${x}x${x}x32.png)
    %python_expand cp ${ipyf[0]}   %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/IPython-%{$python_bin_suffix}.png
    %python_expand cp ${ipynbf[0]} %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/IPythonNotebook-%{$python_bin_suffix}.png
done
%endif

# Modify and install .desktop file
%{python_expand cp examples/IPython\ Kernel/ipython.desktop ipython-%{$python_bin_suffix}.desktop
desktop-file-edit --set-comment="Enhanced interactive Python %{$python_bin_suffix} shell" --set-name="ipython %{$python_bin_suffix}" --set-generic-name="IPython %{$python_bin_suffix}" --set-key="Exec" --set-value="ipython-%{$python_bin_suffix}" --set-icon="IPython-%{$python_bin_suffix}" ipython-%{$python_bin_suffix}.desktop
%suse_update_desktop_file -i -r ipython-%{$python_bin_suffix} "System;TerminalEmulator;"
}

%{python_expand # These can be run stand-alone, so make them executable rather than removing shebang
find %{buildroot}%{$python_sitelib} -type f -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" {} \;
find %{buildroot}%{$python_sitelib} -type f -name "*.py" -exec sed -i "s|^#!%{_bindir}/python$|#!%{__$python}|" {} \;
find %{buildroot}%{$python_sitelib} -type f -name "*.py" -exec grep -q "#!%{__$python}" {} \; -exec chmod a+x {} \;

$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/IPython
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/IPython

%fdupes %{buildroot}%{$python_sitelib}
}
%fdupes %{buildroot}%{_bindir}
%fdupes %{buildroot}%{_mandir}

%endif

%if %{with test}
%check
export LANG="en_US.UTF-8"
mkdir tester
pushd tester
%python_expand iptest-%{$python_bin_suffix}
popd
%endif

%if !%{with test}

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative ipython

%pre iptest
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative iptest

%post
%python_install_alternative ipython ipython3 ipython.1.gz ipython3.1.gz
%desktop_database_post
%icon_theme_cache_post

%post iptest
%python_install_alternative iptest iptest3

%postun
%python_uninstall_alternative ipython
%desktop_database_postun
%icon_theme_cache_postun

%postun iptest
%python_uninstall_alternative iptest
%endif

%if !%{with test}
%files %{python_files}
%license COPYING.rst
%doc README.rst docs/source/about/license_and_copyright.rst
%python_alternative %{_bindir}/ipython
%python_alternative %{_bindir}/ipython3
%python_alternative %{_mandir}/man1/ipython.1.gz
%python_alternative %{_mandir}/man1/ipython3.1.gz
%{python_sitelib}/IPython/
%{python_sitelib}/ipython-%{version}-py*.egg-info
%{_datadir}/applications/ipython-%{python_bin_suffix}.desktop
%{_datadir}/icons/hicolor/scalable/apps/IPython-%{python_bin_suffix}.svg
%if %{with ico}
%{_datadir}/icons/hicolor/*x*/apps/IPython-%{python_bin_suffix}.png
%{_datadir}/icons/hicolor/*x*/apps/IPythonNotebook-%{python_bin_suffix}.png
%endif

%if %{with iptest}
%files %{python_files iptest}
%python_alternative %{_bindir}/iptest
%python_alternative %{_bindir}/iptest3
%endif
%endif

%changelog
