#
# spec file for package python-kovidgoyal-langtool
#
# Copyright (c) 2026 SUSE LLC
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


%define srcname kovidgoyal_langtool
Name:           python-kovidgoyal-langtool
Version:        1.3.0
Release:        0
Summary:        Grammar and style checking based on the LanguageTool rules
License:        LGPL-2.1-or-later
URL:            https://pypi.org/project/kovidgoyal-langtool/
Source:         https://files.pythonhosted.org/packages/source/k/kovidgoyal-langtool/kovidgoyal_langtool-%{version}.tar.gz
BuildRequires:  update-alternatives
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module lxml >= 4.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module regex >= 2022.1.18}
BuildRequires:  %{python_module setuptools >= 69}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
BuildRequires:  fdupes
Requires(post):   update-alternatives
Requires(postun): update-alternatives
Requires:       python-lxml >= 4.6
Requires:       python-regex >= 2022.1.18
%python_subpackages

%description
Grammar and style checking based on the LanguageTool rules: a port of the LanguageTool core to Python with a C extension

%package devel
Summary:        Headers for the %{name} library
Requires:       %{name} = %{version}-%{release}

%description devel
This subpackage contains development files like headers and cmake
scripts.

%prep
%autosetup -p1 -n %{srcname}-%{version}
# rpmlint
rm src/langtool/data/resource/ar/.gitignore
chmod -x src/langtool/data/resource/pt/brazilian_municipalities/*.tsv
chmod -x src/langtool/data/rules/sl/grammar.xml

%build
export CFLAGS="%{optflags}"

export LANGTOOL_STATIC_RULES=1
export LANGTOOL_NO_RULE_TABLES=0

%pyproject_wheel

%python_expand python%{$python_bin_suffix} setup.py build_ext --inplace

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/langtool
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Can not disable with -k
rm tests/test_jregex.py
rm tests/test_disambiguation_rules.py
# disable tests
skiptests="test_api"
skiptests+=" or test_demo_pattern_rules"
skiptests+=" or test_diskcache"
skiptests+=" or test_extensions"
skiptests+=" or test_jlanguagetool"
skiptests+=" or test_regex_rule"
skiptests+=" or test_regex_rule"
skiptests+=" or test_rule_loader"
skiptests+=" or test_string_matcher"
%pytest_arch -k "not ($skiptests)"

%post
%python_install_alternative langtool

%postun
%python_uninstall_alternative langtool

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/langtool
%{python_sitearch}/langtool
%{python_sitearch}/%{srcname}-%{version}.dist-info
%exclude %{python_sitearch}/langtool/_hunspell.c
%exclude %{python_sitearch}/langtool/_rule_engine.h
%exclude %{python_sitearch}/langtool/_rule_tables.h
%exclude %{python_sitearch}/langtool/_speedups.c

%files %{python_files devel}
%{python_sitearch}/langtool/_hunspell.c
%{python_sitearch}/langtool/_rule_engine.h
%{python_sitearch}/langtool/_rule_tables.h
%{python_sitearch}/langtool/_speedups.c

%changelog
