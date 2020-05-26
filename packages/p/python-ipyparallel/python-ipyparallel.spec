#
# spec file for package python-ipyparallel
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-ipyparallel
Version:        6.3.0
Release:        0
Summary:        Interactive parallel computing library for IPython
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython/ipyparallel
Source:         https://files.pythonhosted.org/packages/source/i/ipyparallel/ipyparallel-%{version}.tar.gz
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module ipykernel >= 4.4}
BuildRequires:  %{python_module ipython >= 4}
BuildRequires:  %{python_module ipython-iptest >= 4}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module pyzmq >= 13}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module tornado >= 4}
BuildRequires:  %{python_module traitlets >= 4.3}
# /SECTION
Requires:       python-decorator
Requires:       python-ipykernel >= 4.4
Requires:       python-ipython >= 4
Requires:       python-ipython_genutils
Requires:       python-jupyter-client
Requires:       python-python-dateutil >= 2.1
Requires:       python-pyzmq >= 13
Requires:       python-tornado >= 4
Requires:       python-traitlets >= 4.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     jupyter-ipyparallel = %{version}
Recommends:     python-mpi4py
Recommends:     python-pymongo
Provides:       python-jupyter_ipyparallel = %{version}
Obsoletes:      python-jupyter_ipyparallel < %{version}
BuildArch:      noarch
%python_subpackages

%description
Use multiple instances of IPython in parallel, interactively.

This package provides the python interface.

%package     -n jupyter-ipyparallel
Summary:        Interactive parallel computing library for IPython
Group:          Development/Languages/Python
Requires:       jupyter-jupyter-core
Requires:       jupyter-notebook
Requires:       python3-ipyparallel = %{version}
Provides:       python-jupyter_ipyparallel-nbextension = %{version}
Obsoletes:      python-jupyter_ipyparallel-nbextension < %{version}

%description -n jupyter-ipyparallel
Use multiple instances of IPython in parallel, interactively.

This package provides the jupyter notebook extension.

%package     -n jupyter-ipyparallel-doc
Summary:        Documentation for ipyparallel
Group:          Documentation/Other
Provides:       %{python_module ipyparallel-doc = %{version}}
Provides:       %{python_module jupyter_ipyparallel-doc = %{version}}
Obsoletes:      %{python_module jupyter_ipyparallel-doc < %{version}}

%description -n jupyter-ipyparallel-doc
Documentation and help files for ipyparallel.

%prep
%setup -q -n ipyparallel-%{version}
rm -f docs/html/.buildinfo

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{jupyter_move_config}

# Prepare for update-alternatives
%python_clone -a %{buildroot}%{_bindir}/ipcluster
%python_clone -a %{buildroot}%{_bindir}/ipcontroller
%python_clone -a %{buildroot}%{_bindir}/ipengine

echo pass4
# These files are meant to be runnable stand-alone, so they should be executable
%{python_expand pushd %{buildroot}%{$python_sitelib}
chmod a+x ipyparallel/apps/*app.py
chmod a-x ipyparallel/apps/baseapp.py
chmod a+x ipyparallel/controller/heartmonitor.py
# Fix wrong-script-interpreter
sed -i "s|#!%{_bindir}/env python|#!%__$python|" ipyparallel/apps/*app.py
sed -i "s|#!%{_bindir}/env python|#!%__$python|" ipyparallel/controller/heartmonitor.py
# Deduplicating files can generate a RPMLINT warning for pyc mtime
$python -m compileall -d %{$python_sitearch} ipyparallel/apps/
$python -O -m compileall -d %{$python_sitearch} ipyparallel/apps/
$python -m compileall -d %{$python_sitearch} ipyparallel/controller/heartmonitor.py
$python -O -m compileall -d %{$python_sitearch} ipyparallel/controller/heartmonitor.py
%fdupes .
popd
}

%fdupes %{buildroot}%{_jupyter_prefix}

%check
%pytest -k 'not test_disambiguate_ip'

%post
%{python_install_alternative ipcluster ipcontroller ipengine}

%postun
%python_uninstall_alternative ipcluster

%files %{python_files}
%license COPYING.md
%python_alternative %{_bindir}/ipcluster
%python_alternative %{_bindir}/ipcontroller
%python_alternative %{_bindir}/ipengine
%{python_sitelib}/ipyparallel-%{version}-py*.egg-info
%{python_sitelib}/ipyparallel/

%files -n jupyter-ipyparallel
%license COPYING.md
%doc README.md
%{_jupyter_nbextension_dir}/ipyparallel/
%config %{_jupyter_servextension_confdir}/ipyparallel-serverextension.json
%config %{_jupyter_nb_tree_confdir}/ipyparallel-nbextension.json

%changelog
