#
# spec file for package python-jupyter_client-doc
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
%define doc_ver 5.2.3
# PDF documentation currently broken
%bcond_with pdf
%bcond_without html
%bcond_without tests
Name:           python-jupyter_client-doc
Version:        5.3.1
Release:        0
Summary:        Documentation for the Jupyter client libraries
License:        BSD-3-Clause
Group:          Documentation/Other
URL:            https://github.com/jupyter/jupyter_client
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_client/jupyter_client-%{version}.tar.gz
Source1:        https://buildmedia.readthedocs.org/media/pdf/jupyter-client/%{doc_ver}/jupyter-client.pdf
Source2:        https://buildmedia.readthedocs.org/media/htmlzip/jupyter-client/%{doc_ver}/jupyter-client.zip
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Provides:       %{name}-html = %{version}
Provides:       %{name}-pdf = %{version}
Obsoletes:      %{name}-html < %{version}
Obsoletes:      %{name}-pdf < %{version}
BuildArch:      noarch
%if %{with tests}
# Test Requirements
BuildRequires:  %{python_module backcall}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
# Python 2.7 test requirements
BuildRequires:  python-mock
%endif
# Documentation requirements
%if %{with pdf} || %{with html}
BuildRequires:  %{python_module sphinxcontrib-github-alt}
BuildRequires:  python3-Sphinx
%endif
%if %{with pdf}
BuildRequires:  python3-Sphinx-latex
%endif

%description
This package contains documentation and help files for the Jupyter
client libraries.

%package     -n jupyter-jupyter_client-doc
Summary:        Documentation for the Jupyter client libraries
Group:          Documentation/Other
Requires:       jupyter-jupyter_client = %{version}
Provides:       python-jupyter_client-doc = %{version}
Obsoletes:      python-jupyter_client-doc <= %{version}
Provides:       %{python_module jupyter_client-doc = %{version}}
Obsoletes:      %{python_module jupyter_client-doc <= %{version}}

%description -n jupyter-jupyter_client-doc
This package contains documentation and help files for the Jupyter
client libraries.

%prep
%setup -q -n jupyter_client-%{version}
unzip %{SOURCE2} -d docs
mv docs/jupyter-client-* docs/html
rm docs/html/.buildinfo

%build
# Not needed

%install
mkdir -p %{buildroot}%{_docdir}/jupyter-jupyter_client

cp %{SOURCE1} %{buildroot}%{_docdir}/jupyter-jupyter_client/
cp -r docs/html %{buildroot}%{_docdir}/jupyter-jupyter_client/

%fdupes %{buildroot}%{_docdir}/jupyter-jupyter_client/

%if %{with tests}
%check
pushd jupyter_client/tests
%pytest
popd
%endif

%files -n jupyter-jupyter_client-doc
%license COPYING.md
%{_docdir}/jupyter-jupyter_client/jupyter-client.pdf
%{_docdir}/jupyter-jupyter_client/html/

%changelog
