#
# spec file for package python-xsge_gui
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
%define skip_python2 1
Name:           python-xsge_gui
Version:        1.2.1
Release:        0
Summary:        xSGE GUI Toolkit
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://xsge.nongnu.org
Source:         https://files.pythonhosted.org/packages/source/x/xsge_gui/xsge_gui-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sge-pygame >= 1.0
Requires:       python-six >= 1.4.0
BuildArch:      noarch
%python_subpackages

%description
xSGE is a collection of extensions for SGE.
xSGE extensions are not dependent on any particular SGE implementation.
They should work with any implementation that follows the specification.

This extension provides a toolkit for adding GUIs to a SGE game
as well as support for modal dialog boxes.

%prep
%setup -q -n xsge_gui-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README WHATSNEW
%license xsge_gui/COPYING
%{python_sitelib}/*

%changelog
