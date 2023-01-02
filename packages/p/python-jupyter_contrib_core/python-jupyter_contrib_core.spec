#
# spec file for package python-jupyter_contrib_core
#
# Copyright (c) 2023 SUSE LLC
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


%define         skip_python2 1
Name:           python-jupyter_contrib_core
Version:        0.4.2
Release:        0
Summary:        Common utilities for jupyter-contrib projects
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-contrib/jupyter_contrib_core
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_contrib_core/jupyter_contrib_core-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module notebook >= 4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module traitlets}
# /SECTION
Requires:       python-jupyter-core
Requires:       python-notebook >= 4.0
Requires:       python-setuptools
Requires:       python-tornado
Requires:       python-traitlets
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-jupyter-contrib-core = %{version}-%{release}
Obsoletes:      python-jupyter-contrib-core < %{version}-%{release}
%if "%python_provides" == "python3" || "%python_flavor" == "python3"
Provides:       jupyter-jupyter_contrib_core = %{version}-%{release}
Obsoletes:      jupyter-jupyter_contrib_core < %{version}-%{release}
%else
Conflicts:      jupyter-jupyter_contrib_core < 0.4
%endif
BuildArch:      noarch

%python_subpackages

%description
Common utilities for jupyter-contrib projects. Includes:

-   providing a notebook-4.2-compatible nbextension API in order to
    smooth over differences in versions 4.0 and 4.1
-   common application components and cli scripts
-   utility classes and functions for use in tests

%prep
%setup -q -n jupyter_contrib_core-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-contrib
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative jupyter-contrib

%postun
%python_uninstall_alternative jupyter-contrib

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/jupyter-contrib
%{python_sitelib}/jupyter_contrib_core/
%{python_sitelib}/jupyter_contrib_core-%{version}*-info

%changelog
