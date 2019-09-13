#
# spec file for package python-ipython-doc
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


# This package has to be kept separate from the main package to avoid
# dependency loops with most of the core jupyter packages.
%define         oldpython python
%define doc_ver 7.7.0
Name:           python-ipython-doc
Version:        7.7.0
Release:        0
Summary:        Documentation for python3-jupyter_ipython
License:        BSD-3-Clause
Group:          Documentation/Other
URL:            https://github.com/ipython/ipython
Source0:        https://files.pythonhosted.org/packages/source/i/ipython/ipython-%{version}.tar.gz
# Please make sure you update the documentation files at every release
Source1:        https://buildmedia.readthedocs.org/media/pdf/ipython/%{doc_ver}/ipython.pdf
Source2:        https://buildmedia.readthedocs.org/media/htmlzip/ipython/%{doc_ver}/ipython.zip
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Provides:       python-ipython-doc = %{version}
Provides:       %{python_module ipython-doc = %{version}}
Provides:       %{oldpython}-jupyter_ipython-doc = %{version}
Obsoletes:      %{oldpython}-jupyter_ipython-doc < %{version}
Provides:       %{oldpython}-jupyter_ipython-doc-html = %{version}
Obsoletes:      %{oldpython}-jupyter_ipython-doc-html < %{version}
Provides:       %{oldpython}-jupyter_ipython-doc-pdf = %{version}
Obsoletes:      %{oldpython}-jupyter_ipython-doc-pdf < %{version}
Provides:       %{python_module jupyter_ipython-doc = %{version}}
Obsoletes:      %{python_module jupyter_ipython-doc < %{version}}
Provides:       %{python_module jupyter_ipython-doc-html = %{version}}
Obsoletes:      %{python_module jupyter_ipython-doc-html < %{version}}
Provides:       %{python_module jupyter_ipython-doc-pdf = %{version}}
Obsoletes:      %{python_module jupyter_ipython-doc-pdf < %{version}}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-ipython-iptest = %{version}
# /SECTION
%ifpython3
Provides:       jupyter-ipython-doc = %{version}
%endif

%description
Documentation and help files for python3-jupyter_ipython.

%prep
%setup -q -n ipython-%{version}
unzip %{SOURCE2} -d docs
mv docs/ipython-* docs/html
rm docs/html/.buildinfo

find examples -type f -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%{_bindir}/python3|" {} \;

%build
# Not needed

%install
mkdir -p %{buildroot}%{_docdir}/python-ipython

cp %{SOURCE1} %{buildroot}%{_docdir}/python-ipython/
cp -r docs/html %{buildroot}%{_docdir}/python-ipython/
cp -r examples %{buildroot}%{_docdir}/python-ipython/

%fdupes %{buildroot}%{_docdir}/python-ipython/

%check
export LANG="en_US.UTF-8"
mkdir tester
pushd tester
iptest
popd

%files
%license COPYING.rst docs/source/about/license_and_copyright.rst
%dir %{_docdir}/python-ipython/
%doc %{_docdir}/python-ipython/ipython.pdf
%doc %{_docdir}/python-ipython/html/
%doc %{_docdir}/python-ipython/examples/

%changelog
