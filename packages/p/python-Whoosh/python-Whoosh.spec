#
# spec file for package python-Whoosh
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        2.7.5
Release:        0
Summary:        Pure-Python full text indexing, search, and spell checking library
License:        BSD-2-Clause
URL:            https://github.com/Sygil-Dev/whoosh-reloaded
Source0:        https://github.com/Sygil-Dev/whoosh-reloaded/archive/refs/tags/v%{version}.tar.gz
Source99:       python-Whoosh.rpmlintrc
# PATCH-FIX-UPSTREAM NullMatcherClass-hashable.patch gh#whoosh-community/whoosh#570 mcepl@suse.com
# NullMatcherClass needs __hash__ method as well for Sphinx4 compatiblity.
Patch0:         NullMatcherClass-hashable.patch
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx-jsonschema
BuildRequires:  python3-sphinx_rtd_theme
Requires:       python-cached-property
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
%autosetup -p1 -n whoosh-reloaded-%{version}

# Fix CRLF->LF
sed -i -e 's/\r$//' docs/source/api/filedb/{filestore,filetables,structfile}.rst

%build
%pyproject_wheel
sphinx-build -b html -d docs/build/doctrees docs/source docs/build/html

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/whoosh
%{python_sitelib}/[Ww]hoosh_[Rr]eloaded-%{version}.dist-info

%if 0%{?suse_version} > 1500
%files -n python-Whoosh-doc
%license LICENSE.txt
%endif
%doc docs/build/html

%changelog
