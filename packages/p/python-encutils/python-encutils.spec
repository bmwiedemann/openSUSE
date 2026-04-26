#
# spec file for package python-encutils
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-encutils
Version:        1.0.0
Release:        0
Summary:        encoding detection collection for Python
License:        LGPL-3.0-or-later
URL:            https://github.com/coherent-oss/encutils
Source:         https://files.pythonhosted.org/packages/source/e/encutils/encutils-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-chardet
BuildArch:      noarch
%python_subpackages

%description
A collection of helper functions to detect encodings of text files
(like HTML, XHTML, XML, CSS, etc.) retrieved via HTTP, file or string.

:func:`getEncodingInfo` is probably the main function of interest which uses
other supplied functions itself and gathers all information together and
supplies an :class:`EncodingInfo` object.

%prep
%autosetup -p1 -n encutils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not test_tryEncodings"

%files %{python_files}
%doc README.md
%license LICENSE LICENSE
%{python_sitelib}/encutils
%{python_sitelib}/encutils-%{version}.dist-info

%changelog
