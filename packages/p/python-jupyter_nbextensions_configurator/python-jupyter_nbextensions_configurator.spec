#
# spec file for package python-jupyter_nbextensions_configurator
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


# geckodriver not available
%bcond_with tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-jupyter_nbextensions_configurator
Version:        0.4.1
Release:        0
Summary:        Configuration interfaces for nbextensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/jupyter-contrib/jupyter_nbextensions_configurator
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_nbextensions_configurator/jupyter_nbextensions_configurator-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with tests}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module jupyter_contrib_core >= 0.3.3}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module jupyter_notebook >= 4.0}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module tornado}
BuildRequires:  geckodriver
BuildRequires:  python-mock
%endif
Requires:       python-PyYAML
Requires:       python-jupyter_contrib_core >= 0.3.3
Requires:       python-jupyter_core
Requires:       python-notebook >= 4.0
Requires:       python-tornado
Requires:       python-traitlets
Requires:       jupyter-jupyter_nbextensions_configurator = %{version}
BuildArch:      noarch

%python_subpackages

%description
The jupyter_nbextensions_configurator jupyter server extension provides
graphical user interfaces for configuring which nbextensions are enabled (load
automatically for every notebook), and display their readme files.
In addition, for extensions which include an appropriate yaml descriptor file,
the interface also provides controls to configure the extensions' options.

This package provides the python interface.

%package     -n jupyter-jupyter_nbextensions_configurator
Summary:        Configuration interfaces for nbextensions
Group:          Development/Languages/Python
Requires:       jupyter-jupyter_contrib_core >= 0.3.3
Requires:       jupyter-jupyter_core
Requires:       jupyter-notebook >= 4.0
Requires:       python3-jupyter_nbextensions_configurator = %{version}
Requires(post):   python3-PyYAML
Requires(preun):  python3-PyYAML
Requires(post):   jupyter-jupyter_contrib_core >= 0.3.3
Requires(preun):  jupyter-jupyter_contrib_core >= 0.3.3
Requires(post):   jupyter-jupyter_core
Requires(preun):  jupyter-jupyter_core
Requires(post):   jupyter-notebook >= 4.0
Requires(preun):  jupyter-notebook >= 4.0
Requires(post):   python3-tornado
Requires(preun):  python3-tornado
Requires(post):   python3-traitlets
Requires(preun):  python3-traitlets
Requires(post):   python3-jupyter_nbextensions_configurator = %{version}
Requires(preun):  python3-jupyter_nbextensions_configurator = %{version}

%description -n jupyter-jupyter_nbextensions_configurator
The jupyter_nbextensions_configurator jupyter server extension provides
graphical user interfaces for configuring which nbextensions are enabled (load
automatically for every notebook), and display their readme files.
In addition, for extensions which include an appropriate yaml descriptor file,
the interface also provides controls to configure the extensions' options.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_nbextensions_configurator-%{version}
sed -i 's/\r$//' LICENSE.txt
sed -i 's/\r$//' README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post -n jupyter-jupyter_nbextensions_configurator
%{_bindir}/jupyter-nbextensions_configurator enable --system || true

%preun -n jupyter-jupyter_nbextensions_configurator
if [ $1 = 0 ] && [ -f %{_bindir}/jupyter-nbextensions_configurator ] ; then
    %{_bindir}/jupyter-nbextensions_configurator disable --system || true
fi

%if %{with tests}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
nosetests-%{$python_bin_suffix}
}
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jupyter_nbextensions_configurator-%{version}-py*.egg-info
%{python_sitelib}/jupyter_nbextensions_configurator/

%files -n jupyter-jupyter_nbextensions_configurator
%license LICENSE.txt
%{_bindir}/jupyter-nbextensions_configurator

%changelog
