#
# spec file for package python-setuptools-gettext
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


Name:           python-setuptools-gettext
Version:        0.1.1
Release:        0
Summary:        Setuptools gettext extension plugin
License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/setuptools-gettext
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-gettext/setuptools-gettext-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 46.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools >= 46.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module setuptools >= 46.1}
# /SECTION
%python_subpackages

%description
Setuptools gettext extension plugin

%prep
%autosetup -p1 -n setuptools-gettext-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# There doesn't seem to be any tests.

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitelib}/setuptools_gettext
%{python_sitelib}/setuptools_gettext-%{version}*-info

%changelog
