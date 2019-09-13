#
# spec file for package python-logilab-astng
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  test
Name:           python-logilab-astng
Version:        0.24.3
Release:        0
Summary:        Python Python Abstract Syntax Tree (New Generation)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            http://www.logilab.org/projects/astng
Source:         https://files.pythonhosted.org/packages/source/l/logilab-astng/logilab-astng-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
Requires:       python-logilab-common
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module nose}
%endif
%python_subpackages

%description
The aim of this module is to provide a common base representation of
python source code for projects such as pychecker, pyreverse, pylint...
Well, actually the development of this library is essentially governed
by pylint's needs.

It extends class defined in the compiler.ast [1] module with some
additional methods and attributes. Instance attributes are added by a
builder object, which can either generate extended ast (let's call them
astng ;) by visiting an existant ast tree or by inspecting living
object. Methods are added by monkey patching ast classes.

Please send any comment, patch or question to the python-projects
mailing-list. Before asking a question, please first search the
archives in case it would have already been answered. You may want to
use google and add "site:lists.logilab.org" to your keywords to narrow
your search. We will soon provide our own search engine.

%prep
%setup -q -n logilab-astng-%{version}

%build
%python_build

%install
%python_install

# Avoid conflict with python-logilab-common
%python_expand rm -f %{buildroot}/%{$python_sitelib}/logilab/__init__.py*
%python_expand rm -f %{buildroot}/%{$python_sitelib}/logilab/__pycache__/__init__*.py*

# Do not package testsuite
%python_expand rm -rf %{buildroot}/%{$python_sitelib}/logilab/astng/test

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_expand cp -r test test-%{$python_bin_suffix}
%if %{have_python3} && ! 0%{?skip_python3}
2to3 -wn test-%{python3_bin_suffix}
%endif
%python_expand nosetests-%{$python_bin_suffix} test-%{$python_bin_suffix}
%endif

%files %{python_files}
%license COPYING*
%doc README* ChangeLog
%dir %{python_sitelib}/logilab/
%{python_sitelib}/logilab/astng/
%{python_sitelib}/logilab_astng-%{version}-py*.egg-info
%{python_sitelib}/logilab_astng-%{version}-py*-nspkg.pth

%changelog
