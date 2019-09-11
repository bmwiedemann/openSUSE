#
# spec file for package python2-ipython
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
%define         skip_python3 1
%define         oldpython python
%bcond_without  iptest
Name:           python2-ipython
Version:        5.8.0
Release:        0
Summary:        Rich architecture for interactive computing with Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython/ipython
Source:         https://files.pythonhosted.org/packages/source/i/ipython/ipython-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jupyter/qtconsole/4.0.0/qtconsole/resources/icon/JupyterConsole.svg
BuildRequires:  %{python_module setuptools}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       python-Pygments
Requires:       python-backports.shutil_get_terminal_size
Requires:       python-decorator
Requires:       python-jedi >= 0.10
Requires:       python-pathlib2
Requires:       python-pexpect
Requires:       python-pickleshare
Requires:       python-prompt_toolkit1 >= 1.0.4
Requires:       python-simplegeneric > 0.8
Requires:       python-traitlets >= 4.2
Requires:       python-typing
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-docrepr
Recommends:     python-ipykernel
Recommends:     python-ipyparallel
Recommends:     python-ipywidgets
Recommends:     python-jupyter_qtconsole
Recommends:     python-nbconvert
Recommends:     python-nbformat
Recommends:     python-notebook
Provides:       IPython = %{version}
Obsoletes:      IPython < %{version}
Provides:       %{oldpython}-IPython = %{version}
Obsoletes:      %{oldpython}-IPython < %{version}
Provides:       python-IPython = %{version}
Obsoletes:      python-IPython < %{version}
Provides:       python2-IPython = %{version}
Obsoletes:      python2-IPython < %{version}
Provides:       %{oldpython}-jupyter_ipython = %{version}
Obsoletes:      %{oldpython}-jupyter_ipython <= %{version}
Provides:       python-jupyter_ipython = %{version}
Obsoletes:      python-jupyter_ipython <= %{version}
Provides:       python2-jupyter_ipython = %{version}
Obsoletes:      python2-jupyter_ipython <= %{version}
Provides:       %{oldpython}-ipython = %{version}
BuildArch:      noarch
%if %{with iptest}
BuildRequires:  %{python_module backports.shutil_get_terminal_size}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pathlib2}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pickleshare}
BuildRequires:  %{python_module prompt_toolkit1 >= 1.0.4}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module simplegeneric > 0.8}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module traitlets}
%else
Provides:       python-jupyter_ipython-iptest = %{version}
Obsoletes:      python-jupyter_ipython-iptest <= %{version}
Obsoletes:      python2-jupyter_ipython-iptest <= %{version}
%endif
%if %{with ico}
BuildRequires:  icoutils
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

IMPORTANT: The Python 2 version of IPython is in long-term support
mode. It will not be receiving major new features. Starting with
IPython 6, only Python 3.3 and later is supported.

%package iptest
Summary:        Tools for testing packages that rely on %{name}
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-matplotlib
# Python 2 Test Requirements
Requires:       python-mock
Requires:       python-nose
Requires:       python-requests
Requires:       python-testpath
Provides:       %{oldpython}-jupyter_ipython-iptest = %{version}
Obsoletes:      %{oldpython}-jupyter_ipython-iptest <= %{version}
Provides:       python-jupyter_ipython-iptest = %{version}
Obsoletes:      python-jupyter_ipython-iptest <= %{version}
Provides:       python2-jupyter_ipython-iptest = %{version}
Obsoletes:      python2-jupyter_ipython-iptest <= %{version}

%description iptest
This package provides the iptest command, which is used for
testing software that uses %{name}.

IMPORTANT: The Python 2 version of IPython is in long-term support
mode. It will not be receiving major new features. Starting with
IPython 6, only Python 3.3 and later is supported.

%prep
%setup -q -n ipython-%{version}

sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python|" IPython/testing/plugin/iptest.py
sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python|" IPython/testing/plugin/setup.py
sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python|" IPython/terminal/ipapp.py

find . -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/python|#!%{_bindir}/python2|" {} \;

%build
%python_build

%if %{with ico}
pushd scripts
icotool -x ipython.ico
icotool -x ipython_nb.ico
popd
%endif

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ipython
%python_clone -a %{buildroot}%{_mandir}/man1/ipython.1

%if %{with iptest}
%python_clone -a %{buildroot}%{_bindir}/iptest
%else
rm %{buildroot}%{_bindir}/iptest*
%endif

ln -s %{_mandir}/man1/ipython-%{python2_bin_suffix}.1.gz %{buildroot}%{_mandir}/man1/ipython2.1.gz

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

# These can be run stand-alone, so make them executable rather than removing shebang
%{python_expand find %{buildroot}%{$python_sitelib} -type f -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" {} \;
find %{buildroot}%{$python_sitelib} -type f -name "*.py" -exec sed -i "s|^#!%{_bindir}/python$|#!%{__$python}|" {} \;
find %{buildroot}%{$python_sitelib} -type f -name "*.py" -exec grep -q "#!%{__$python}" {} \; -exec chmod a+x {} \;

$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/IPython
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/IPython

%fdupes %{buildroot}%{$python_sitelib}
}

rm %{buildroot}%{_bindir}/ipython2
ln -s %{_bindir}/ipython-%{python2_bin_suffix} %{buildroot}%{_bindir}/ipython2

%if %{with iptest}
rm %{buildroot}%{_bindir}/iptest2
ln -s %{_bindir}/iptest-%{python2_bin_suffix} %{buildroot}%{_bindir}/iptest2
%endif

%post
%{python_install_alternative ipython ipython.1.gz}
%desktop_database_post
%icon_theme_cache_post

%post iptest
%python_install_alternative iptest

%postun
%python_uninstall_alternative ipython
%desktop_database_postun
%icon_theme_cache_postun

%postun iptest
%python_uninstall_alternative iptest

%files %{python_files}
%doc README.rst
%license COPYING.rst docs/source/about/license_and_copyright.rst
%python_alternative %{_bindir}/ipython
%python_alternative %{_mandir}/man1/ipython.1.gz
%python2_only %{_bindir}/ipython2
%python2_only %{_mandir}/man1/ipython2.1.gz
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
%doc README.rst
%license COPYING.rst docs/source/about/license_and_copyright.rst
%python_alternative %{_bindir}/iptest
%python2_only %{_bindir}/iptest2
%endif

%changelog
