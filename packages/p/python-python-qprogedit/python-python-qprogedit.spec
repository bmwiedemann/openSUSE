#
# spec file for package python-python-qprogedit
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
Name:           python-python-qprogedit
Version:        4.1.2
Release:        0
Summary:        A QScintilla-based text-editor component
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://github.com/smathot/QProgEdit
Source:         https://files.pythonhosted.org/packages/source/p/python-qprogedit/python-qprogedit-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/smathot/QProgEdit/master/copyright
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module qscintilla-qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-QtPy
Requires:       python-qscintilla-qt5
BuildArch:      noarch

%python_subpackages

%description
QProgEdit is a PyQt widget that implements a text editor
component. Its primary target at the moment is OpenSesame, a graphical
experiment builder.

%prep
%setup -q -n python-qprogedit-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license copyright
%{python_sitelib}/*

%changelog
