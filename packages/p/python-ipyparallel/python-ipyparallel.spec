#
# spec file for package python-ipyparallel
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


Name:           python-ipyparallel
Version:        8.4.1
Release:        0
Summary:        Interactive parallel computing library for IPython
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython/ipyparallel
Source:         https://files.pythonhosted.org/packages/source/i/ipyparallel/ipyparallel-%{version}.tar.gz
Source99:       python-ipyparallel-rpmlintrc
# PATCH-FIX-UPSTREAM ipyparallel-pr729+pr753-deprecationfilters.patch gh#ipython/ipyparallel#729, gh#ipython/ipyparallel#753
Patch1:         ipyparallel-pr729+pr753-deprecationfilters.patch
# SECTION build-system requirements
BuildRequires:  %{python_module hatchling >= 0.25}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module jupyterlab >= 3}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
# /SECTION
# SECTION runtime requirements
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module ipykernel >= 4.4}
BuildRequires:  %{python_module ipython >= 4}
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module pyzmq >= 18}
BuildRequires:  %{python_module tornado >= 5.1}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module traitlets >= 4.3}
Requires:       python-decorator
Requires:       python-entrypoints
Requires:       python-ipykernel >= 4.4
Requires:       python-ipython >= 4
Requires:       python-jupyter-client
Requires:       python-psutil
Requires:       python-python-dateutil >= 2.1
Requires:       python-pyzmq >= 18
Requires:       python-tornado >= 5.1
Requires:       python-tqdm
Requires:       python-traitlets >= 4.3
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     jupyter-ipyparallel = %{version}
Provides:       python-jupyter_ipyparallel = %{version}-%{release}
Obsoletes:      python-jupyter_ipyparallel < %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements, including ipython[test]
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
# /SECTION
%python_subpackages

%description
Use multiple instances of IPython in parallel, interactively.

This package provides the python interface.

%package     -n jupyter-ipyparallel
Summary:        Interactive parallel computing library for IPython
Group:          Development/Languages/Python
Requires:       jupyter-jupyter-core
Requires:       jupyter-jupyter-server
Requires:       jupyter-jupyterlab >= 3
Requires:       jupyter-notebook
Requires:       python3-ipyparallel = %{version}
Provides:       jupyter-ipyparallel-l = %{version}-%{release}
Provides:       jupyter-ipyparallel-nbext = %{version}-%{release}
Provides:       jupyter-ipyparallel-serverextension = %{version}-%{release}
# the last pythonX-jupyter_ipyparallel-nbextension package was 2019 before the multiflavor era
Obsoletes:      python-jupyter_ipyparallel-nbextension <= 6.2.3
Obsoletes:      python2-jupyter_ipyparallel-nbextension <= 6.2.3
Obsoletes:      python3-jupyter_ipyparallel-nbextension <= 6.2.3

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
%autosetup -p1 -n ipyparallel-%{version}
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install

# Prepare for update-alternatives
%python_clone -a %{buildroot}%{_bindir}/ipcluster
%python_clone -a %{buildroot}%{_bindir}/ipcontroller
%python_clone -a %{buildroot}%{_bindir}/ipengine

%{python_expand # These files are meant to be runnable stand-alone, so they should be executable
pushd %{buildroot}%{$python_sitelib}/ipyparallel
for f in apps/iploggerapp.py cluster/app.py engine/app.py controller/app.py controller/heartmonitor.py; do
  chmod a+x $f
  # Fix wrong-script-interpreter
  sed -i "s|#!%{_bindir}/env python.*|#!%__$python|" $f
  $python -m compileall $f
  $python -O -m compileall $f
done
popd
%fdupes %{buildroot}%{$python_sitelib}
}

%fdupes %{buildroot}%{_jupyter_prefix}

%check
# can't get a public IP
donttest="test_disambiguate_ip"
# flaky tests
donttest+=" or test_imap_infinite"
donttest+=" or test_execute_raises"
donttest+=" or test_cellpx_keyboard_interrupt_signal_9"
donttest+=" or test_cellpx_keyboard_interrupt_SIGKILL"
donttest+=" or test_compositeerror_render_exception"
donttest+=" or test_local_ip_true_doesnt_trigger_warning"
%pytest -k "not ($donttest)"

%post
%python_install_alternative ipcluster ipcontroller ipengine

%postun
%python_uninstall_alternative ipcluster

%files %{python_files}
%license COPYING.md
%python_alternative %{_bindir}/ipcluster
%python_alternative %{_bindir}/ipcontroller
%python_alternative %{_bindir}/ipengine
%{python_sitelib}/ipyparallel-%{version}*-info
%{python_sitelib}/ipyparallel/

%files -n jupyter-ipyparallel
%license COPYING.md
%doc README.md
%{_jupyter_nbextension_dir}/ipyparallel/
%{_jupyter_labextensions_dir3}/ipyparallel-labextension
%{_jupyter_config} %{_jupyter_server_confdir}/ipyparallel.json
%{_jupyter_config} %{_jupyter_servextension_confdir}/ipyparallel.json
%{_jupyter_config} %{_jupyter_nb_tree_confdir}/ipyparallel.json

%changelog
