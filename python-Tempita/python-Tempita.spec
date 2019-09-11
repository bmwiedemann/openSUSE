#
# spec file for package python-Tempita
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
Name:           python-Tempita
Version:        0.5.2
Release:        0
Url:            http://pythonpaste.org/tempita/
Summary:        A very small text templating language
License:        MIT
Group:          Development/Languages/Python
Source:         https://pypi.io/packages/source/T/Tempita/Tempita-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%ifpython2
Provides:       python-tempita = %{version}
Obsoletes:      python-tempita < %{version}
%endif
BuildArch:      noarch

%python_subpackages

%description
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
string.Template or % substitution.  It's small, it embeds
Python in strings, and it doesn't do much else.

%prep
%setup -q -n Tempita-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
