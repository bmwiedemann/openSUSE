#
# spec file for package python-PyKMIP
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
Name:           python-PyKMIP
Version:        0.9.1
Release:        0
Summary:        KMIP v11 library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/OpenKMIP/PyKMIP
Source:         https://files.pythonhosted.org/packages/source/P/PyKMIP/PyKMIP-%{version}.tar.gz
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
Requires:       python-SQLAlchemy
Requires:       python-cryptography
Requires:       python-requests
Requires:       python-six
%ifpython2
Requires:       python-enum34
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The standard
is governed by the `Organization for the Advancement of Structured Information
Standards`_ (OASIS). PyKMIP supports a subset of features in versions
1.0 - 1.2 of the KMIP specification.

%prep
%setup -q -n PyKMIP-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pykmip-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest kmip/tests/unit

%post
%python_install_alternative pykmip-server

%postun
%python_uninstall_alternative pykmip-server

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/pykmip-server

%changelog
