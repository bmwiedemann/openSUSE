#
# spec file for package python-translitcodec
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-translitcodec
Version:        0.6.0
Release:        0
Summary:        Unicode to 8-bit charset transliteration codec
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/claudep/translitcodec
Source:         https://files.pythonhosted.org/packages/source/t/translitcodec/translitcodec-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
This package contains codecs for transliterating ISO 10646 texts into
best-effort representations using smaller coded character sets (ASCII,
ISO 8859, etc.).  The translation tables used by the codecs are from
the ``transtab`` collection by Markus Kuhn.

%prep
%setup -q -n translitcodec-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGES README
%license LICENSE
%{python_sitelib}/*

%changelog
