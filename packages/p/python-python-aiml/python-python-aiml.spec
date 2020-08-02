#
# spec file for package python-python-aiml
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
Name:           python-python-aiml
Version:        0.9.3
Release:        0
Summary:        An interpreter package for AIML, the Artificial Intelligence Markup Language
License:        BSD-2-Clause
URL:            https://github.com/paulovn/python-aiml
Source:         https://files.pythonhosted.org/packages/source/p/python-aiml/python-aiml-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      python-aiml < 0.9.0
BuildArch:      noarch
%python_subpackages

%description
python-aiml implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.

This package was forked from PyAIML 0.8.6 which seems to have been abandoned
for a long time.

%prep
%setup -q -n python-aiml-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/aiml-bot
%python_clone -a %{buildroot}%{_bindir}/aiml-validate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative aiml-bot
%python_install_alternative aiml-validate

%postun
%python_uninstall_alternative aiml-bot
%python_uninstall_alternative aiml-validate

%files %{python_files}
%doc CHANGES.txt README.rst
%license COPYING.txt
%python_alternative %{_bindir}/aiml-validate
%python_alternative %{_bindir}/aiml-bot
%{python_sitelib}/*

%changelog
