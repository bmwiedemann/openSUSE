#
# spec file for package python-afdko
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-afdko%{psuffix}
Version:        3.4.0
Release:        0
Summary:        Adobe Font Development Kit for OpenType
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/adobe-type-tools/afdko
Source:         https://files.pythonhosted.org/packages/source/a/afdko/afdko-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-FontTools >= 4.10.2
Requires:       python-booleanOperations >= 0.9.0
Requires:       python-cu2qu >= 1.6.7
Requires:       python-defcon >= 0.6.0
Requires:       python-fontMath >= 0.6.0
Requires:       python-lxml >= 4.5.1
Requires:       python-mutatorMath >= 3.0.1
Requires:       python-psautohint >= 2.0.1
Requires:       python-ufoProcessor >= 1.9.0
Requires:       python-ufonormalizer >= 0.4.1
Requires:       python-zopfli >= 0.1.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       adobe-afdko
%if %{with test}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Brotli >= 1.0.1}
BuildRequires:  %{python_module FontTools >= 4.8.1}
BuildRequires:  %{python_module afdko}
BuildRequires:  %{python_module booleanOperations >= 0.9.0}
BuildRequires:  %{python_module cu2qu >= 1.6.7}
BuildRequires:  %{python_module defcon >= 0.6.0}
BuildRequires:  %{python_module fontMath >= 0.6.0}
BuildRequires:  %{python_module lxml >= 4.5.1}
BuildRequires:  %{python_module mutatorMath >= 3.0.1}
BuildRequires:  %{python_module psautohint >= 2.0.1}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ufoProcessor >= 1.9.0}
BuildRequires:  %{python_module ufonormalizer >= 0.4.1}
BuildRequires:  %{python_module zopfli >= 0.1.4}
# /SECTION
%endif
%python_subpackages

%description
Adobe Font Development Kit for OpenType

%prep
%setup -q -n afdko-%{version}

%if %{with test}
%check
mkdir tmp
export TMPDIR=tmp
%pytest
#-n auto

%else
%build
%python_build

%install
%python_install

for binary in detype1 makeotfexe mergefonts rotatefont sfntdiff sfntedit \
              spot tx type1 autohint buildcff2vf buildmasterotfs \
              comparefamily checkoutlinesufo makeotf makeinstancesufo \
              otc2otf otf2otc otf2ttf stemhist ttfcomponentizer \
              ttfdecomponentizer ttxn charplot digiplot fontplot \
              fontplot2 fontsetplot hintplot waterfallplot ; do
   %python_clone -a %{buildroot}%{_bindir}/$binary
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%{python_install_alternative makeotf detype1 makeotfexe mergefonts rotatefont
  sfntdiff sfntedit spot tx type1 autohint buildcff2vf buildmasterotfs
  comparefamily checkoutlinesufo makeinstancesufo otc2otf otf2otc otf2ttf
  stemhist ttfcomponentizer ttfdecomponentizer ttxn charplot digiplot
  fontplot fontplot2 fontsetplot hintplot waterfallplot}

%postun
%{python_uninstall_alternative makeotf detype1 makeotfexe mergefonts rotatefont
  sfntdiff sfntedit spot tx type1 autohint buildcff2vf buildmasterotfs
  comparefamily checkoutlinesufo makeinstancesufo otc2otf otf2otc otf2ttf
  stemhist ttfcomponentizer ttfdecomponentizer ttxn charplot digiplot
  fontplot fontplot2 fontsetplot hintplot waterfallplot}

%files %{python_files}
%doc NEWS.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/detype1
%python_alternative %{_bindir}/makeotfexe
%python_alternative %{_bindir}/mergefonts
%python_alternative %{_bindir}/rotatefont
%python_alternative %{_bindir}/sfntdiff
%python_alternative %{_bindir}/sfntedit
%python_alternative %{_bindir}/spot
%python_alternative %{_bindir}/tx
%python_alternative %{_bindir}/type1
%python_alternative %{_bindir}/autohint
%python_alternative %{_bindir}/buildcff2vf
%python_alternative %{_bindir}/buildmasterotfs
%python_alternative %{_bindir}/comparefamily
%python_alternative %{_bindir}/checkoutlinesufo
%python_alternative %{_bindir}/makeotf
%python_alternative %{_bindir}/makeinstancesufo
%python_alternative %{_bindir}/otc2otf
%python_alternative %{_bindir}/otf2otc
%python_alternative %{_bindir}/otf2ttf
%python_alternative %{_bindir}/stemhist
%python_alternative %{_bindir}/ttfcomponentizer
%python_alternative %{_bindir}/ttfdecomponentizer
%python_alternative %{_bindir}/ttxn
%python_alternative %{_bindir}/charplot
%python_alternative %{_bindir}/digiplot
%python_alternative %{_bindir}/fontplot
%python_alternative %{_bindir}/fontplot2
%python_alternative %{_bindir}/fontsetplot
%python_alternative %{_bindir}/hintplot
%python_alternative %{_bindir}/waterfallplot
%{python_sitearch}/*
%endif

%changelog
