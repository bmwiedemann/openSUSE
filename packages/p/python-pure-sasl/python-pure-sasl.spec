#
# spec file for package python-pure-sasl
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
%bcond_without test
Name:           python-pure-sasl
Version:        0.6.1
Release:        0
Summary:        Pure Python client SASL implementation
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/thobbs/pure-sasl
Source:         https://files.pythonhosted.org/packages/source/p/pure-sasl/pure-sasl-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-kerberos
BuildArch:      noarch
%python_subpackages

%description
This package provides a reasonably high-level SASL client written
in pure Python.  New mechanisms may be integrated easily, but by default,
support for PLAIN, ANONYMOUS, CRAM-MD5, DIGEST-MD5, and GSSAPI are
provided.

%prep
%setup -q -n pure-sasl-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
