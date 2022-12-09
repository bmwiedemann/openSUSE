#
# spec file for package python-copr
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-copr
Version:        1.124
Release:        0
Summary:        Python client for copr service
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-copr/copr
Source:         https://files.pythonhosted.org/packages/source/c/copr/copr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-marshmallow
Requires:       python-munch
Requires:       python-requests
Requires:       python-requests-toolbelt
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module marshmallow}
BuildRequires:  %{python_module munch}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-gssapi}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Python client for copr service.

%prep
%setup -q -n copr-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/copr
%{python_sitelib}/copr-%{version}*-info

%changelog
