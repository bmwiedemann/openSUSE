#
# spec file for package python-jupyter_core-doc
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
%bcond_without tests
Name:           python-jupyter_core-doc
Version:        4.5.0
Release:        0
Summary:        Documentation for the Jupyter base package
License:        BSD-3-Clause
Group:          Documentation/Other
URL:            https://github.com/jupyter/jupyter_core
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_core/jupyter_core-%{version}.tar.gz
Source1:        https://buildmedia.readthedocs.org/media/pdf/jupyter-core/stable/jupyter-core.pdf
Source2:        https://buildmedia.readthedocs.org/media/htmlzip/jupyter-core/stable/jupyter-core.zip
# PATCH-FIX-OPENSUSE -- use_rpms_paths.patch -- change paths so they are easy to replace at build time
Patch0:         use_rpms_paths.patch
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%if %{with tests}
# Test requirements
BuildRequires:  %{python_module pytest}
# Python 2.7 test requirements
BuildRequires:  python-mock
%endif

%description
Documentation and help files for the Jupyter base package.

%package     -n jupyter-jupyter_core-doc
Summary:        Documentation for the Jupyter base package
Group:          Documentation/Other
Provides:       python-jupyter_core-doc = %{version}
Obsoletes:      python-jupyter_core-doc < %{version}
Provides:       python-jupyter_core-html = %{version}
Provides:       python-jupyter_core-pdf = %{version}
Obsoletes:      python-jupyter_core-html < %{version}
Obsoletes:      python-jupyter_core-pdf < %{version}
Provides:       %{python_module jupyter_core-doc = %{version}}
Obsoletes:      %{python_module jupyter_core-doc < %{version}}
Provides:       %{python_module jupyter_core-doc-pdf = %{version}}
Obsoletes:      %{python_module jupyter_core-doc-pdf < %{version}}
Provides:       %{python_module jupyter_core-doc-html = %{version}}
Obsoletes:      %{python_module jupyter_core-doc-html < %{version}}

%description -n jupyter-jupyter_core-doc
Documentation and help files for the Jupyter base package.

%prep
%setup -q -n jupyter_core-%{version}
%patch0 -p1
unzip %{SOURCE2} -d docs
mv docs/jupyter-core-* docs/html
rm docs/html/.buildinfo

echo %{_jupyter_prefix}
echo %{_jupyter_confdir}

# Set the appropriate paths dynamically
sed -i "s|\"%{_datadir}/jupyter\"|\"%{_datadir}/jupyter\"|" jupyter_core/paths.py
sed -i "s|\"%{_sysconfdir}/jupyter\"|\"%{_sysconfdir}/jupyter\"|" jupyter_core/paths.py
sed -i "s|(sys\.prefix, 'share', 'jupyter')|('%{_datadir}', 'jupyter')|" jupyter_core/paths.py
sed -i "s|(sys\.prefix, 'etc', 'jupyter')|('%{_sysconfdir}', 'jupyter')|" jupyter_core/paths.py

%build
# Not needed

%install
mkdir -p %{buildroot}%{_docdir}/jupyter-jupyter_core/

cp %{SOURCE1} %{buildroot}%{_docdir}/jupyter-jupyter_core/
cp -r docs/html %{buildroot}%{_docdir}/jupyter-jupyter_core/

%fdupes %{buildroot}%{_docdir}/jupyter-jupyter_core/

%if %{with tests}
%check
# test_migrate requires files not found in the package
pushd jupyter_core/tests
rm test_migrate.py
%pytest
popd
%endif

%files -n jupyter-jupyter_core-doc
%license COPYING.md
%{_docdir}/jupyter-jupyter_core/

%changelog
