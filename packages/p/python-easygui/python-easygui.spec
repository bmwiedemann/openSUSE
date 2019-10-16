#
# spec file for package python-easygui
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
%define py_name easygui
Name:           python-easygui
Version:        0.98.1
Release:        0
Summary:        Function-driven python GUI programming
License:        BSD-3-Clause
URL:            https://github.com/robertlugg/easygui
Source0:        https://files.pythonhosted.org/packages/source/e/easygui/easygui-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
EasyGui provides an interface for simple GUI interaction with a user.
It's not event-driven and it does not require the programmer to know
anything about tkinter, frames, widgets, callbacks or lambda.

%prep
%setup -q -n %{py_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.txt
%{python_sitelib}/*

%changelog
