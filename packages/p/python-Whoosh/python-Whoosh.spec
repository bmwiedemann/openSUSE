#
# spec file for package python-Whoosh
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


%{?sle15_python_module_pythons}
Name:           python-Whoosh
Version:        2.7.4
Release:        0
Summary:        Pure-Python full text indexing, search, and spell checking library
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/whoosh-community/whoosh/
Source:         https://files.pythonhosted.org/packages/source/W/Whoosh/Whoosh-%{version}.tar.gz
# upstream in completely unrelated https://github.com/whoosh-community/whoosh/commit/b43e5a432109
Patch0:         pytest4.patch
# upstream in https://github.com/whoosh-community/whoosh/commit/f5a777572fb9
Patch1:         py2encoding.patch
# PATCH-FIX-UPSTREAM NullMatcherClass-hashable.patch gh#whoosh-community/whoosh#570 mcepl@suse.com
# NullMatcherClass needs __hash__ method as well for Sphinx4 compatiblity.
Patch2:         NullMatcherClass-hashable.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildArch:      noarch
# SECTION the testing dependencies
BuildRequires:  %{python_module pytest}
# /SECTION
%ifpython2
Provides:       python-whoosh = %{version}
Obsoletes:      python-whoosh < %{version}
%endif
%python_subpackages

%description
Whoosh is a pure-Python indexing and search library. It can be used
to add search functionality to applications and websites. Every part
of how Whoosh works can be extended or replaced to meet specific
needs.

%if 0%{?suse_version} > 1500
%package -n python-Whoosh-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module Whoosh-doc = %{version}}

%description -n python-Whoosh-doc
Whoosh is a pure-Python indexing and search library. It can be used
to add search functionality to applications and websites. Every part
of how Whoosh works can be extended or replaced to meet specific
needs.

This package contains the documentation.
%endif

%prep
%autosetup -p1 -n Whoosh-%{version}

# Fix CRLF->LF
sed -i -e 's/\r$//' docs/source/api/filedb/{filestore,filetables,structfile}.rst

%build
%python_build
sphinx-build -b html -d docs/build/doctrees docs/source docs/build/html

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
# test_list_corrector - depends on dict sorting thats in py3+ only
%pytest -k 'not test_list_corrector'

%files %{python_files}
%license LICENSE.txt
%doc README.txt
%{python_sitelib}/*

%if 0%{?suse_version} > 1500
%files -n python-Whoosh-doc
%license LICENSE.txt
%endif
%doc docs/build/html

%changelog
